from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel

from application.service.create_spot_service import CreateSpotService
from domain.model.raw_data.aggregate import RawDataAggregateFactory
from domain.model.spot.aggregate import SpotAggregateFactory
from infrastructure.repository.fp_model_repository import FpModelRepository
from infrastructure.repository.raw_data_repository import RawDataRepository
from infrastructure.repository.spot_repository import SpotRepository
from infrastructure.repository.transmitter_repository import TransmitterRepository

router = APIRouter()

create_spot_service = CreateSpotService(
    spot_repository=SpotRepository(),
    raw_data_repository=RawDataRepository(),
    fp_model_repository=FpModelRepository(),
    transmitter_repository=TransmitterRepository(),
)


class CreateSpotRequest(BaseModel):
    name: str
    floors: int
    locationType: str
    latitude: float
    longitude: float
    rawDataFile: UploadFile


class CreateSpotResponse(BaseModel):
    id: str
    name: str
    floors: int
    location_type: str
    latitude: float
    longitude: float


@router.get("/api/spot/create", response_model=CreateSpotResponse)
async def create_spot(request: CreateSpotRequest):
    try:
        raw_data_file = await request.rawDataFile.read()
        raw_data = RawDataAggregateFactory().create(
            raw_data_file=raw_data_file,
        )
        spot_aggregate = SpotAggregateFactory.create(
            name=request.name,
            floors=request.floors,
            location_type=request.locationType,
            latitude=request.latitude,
            longitude=request.longitude,
        )

        # スポット情報を保存
        create_spot_service.run(
            raw_data=raw_data,
            spot=spot_aggregate,
        )

        return CreateSpotResponse(
            id=str(spot_aggregate.get_id_of_private_value()),
            name=spot_aggregate.get_name_of_private_value(),
            floors=spot_aggregate.get_floors_of_private_value(),
            location_type=str(spot_aggregate.get_location_type_of_private_value()),
            latitude=spot_aggregate.get_coordinate_of_private_value().get_latitude_of_private_value(),
            longitude=spot_aggregate.get_coordinate_of_private_value().get_longitude_of_private_value(),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
