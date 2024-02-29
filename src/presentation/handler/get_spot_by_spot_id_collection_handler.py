from typing import List

from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel

from application.service.get_spot_by_spot_id_collection_service import \
    GetSpotBySpotIdCollectionService
from domain.model.raw_data.aggregate import RawDataAggregateFactory
from domain.model.spot_collection.aggregate import \
    SpotCollectionAggregateFactory
from infrastructure.repository.fp_model_repository import FpModelRepository
from infrastructure.repository.spot_repository import SpotRepository
from infrastructure.repository.transmitter_repository import \
    TransmitterRepository

router = APIRouter()

get_spot_by_spot_id_collection_service = GetSpotBySpotIdCollectionService(
    spot_repository=SpotRepository(),
    fp_model_repository=FpModelRepository(),
    transmitter_repository=TransmitterRepository(),
)


class GetSpotBySpotIdCollectionRequest(BaseModel):
    spotIds: List[str]
    rawDataFile: UploadFile


class GetSpotBySpotIdCollectionResponse(BaseModel):
    id: str
    name: str
    floors: int
    locationType: str
    latitude: float
    longitude: float


router = APIRouter()


@router.post("/api/spot/search", response_model=GetSpotBySpotIdCollectionResponse)
async def get_spot_by_spot_id_collection(request: GetSpotBySpotIdCollectionRequest):
    try:
        spot_collection = SpotCollectionAggregateFactory().create(
            spot_id_collection=request.spotIds
        )
        raw_data_file = await request.rawDataFile.read()
        raw_data = RawDataAggregateFactory().create(
            raw_data_file=raw_data_file,
        )

        spot = get_spot_by_spot_id_collection_service.run(
            raw_data=raw_data,
            spot_collection=spot_collection,
        )
        if spot is None:
            raise HTTPException(status_code=404, detail="spot not found")

        return GetSpotBySpotIdCollectionResponse(
            id=str(spot),
            name=spot.get_name_of_private_value(),
            floors=spot.get_floors_of_private_value(),
            locationType=str(spot.get_location_type_of_private_value()),
            latitude=spot.get_coordinate_of_private_value().get_latitude_of_private_value(),
            longitude=spot.get_coordinate_of_private_value().get_longitude_of_private_value(),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
