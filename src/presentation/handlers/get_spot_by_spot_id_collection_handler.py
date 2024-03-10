from typing import List, Tuple

from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from pydantic import BaseModel

from application.services.get_spot_by_spot_id_collection_service import \
    GetSpotBySpotIdCollectionService
from domain.models.raw_data.aggregate import RawDataAggregateFactory
from domain.models.spot_collection.aggregate import \
    SpotCollectionAggregateFactory
from infrastructure.repository.fp_model_repository import FpModelRepository
from infrastructure.repository.spot_repository import SpotRepository
from infrastructure.repository.transmitter_repository import \
    TransmitterRepository
from presentation.middleware.application_middleware import get_credential
from utils.global_variable import APPLICATION


class GetSpotBySpotIdCollectionResponse(BaseModel):
    id: str
    name: str
    floor: int
    locationType: str
    latitude: float
    longitude: float


router = APIRouter()

get_spot_by_spot_id_collection_service = GetSpotBySpotIdCollectionService(
    spot_repository=SpotRepository(),
    fp_model_repository=FpModelRepository(),
    transmitter_repository=TransmitterRepository(),
)


@router.post("/api/spot/search", response_model=GetSpotBySpotIdCollectionResponse)
async def get_spot_by_spot_id_collection(
    spotIds: List[str] = Query(...),
    rawDataFile: UploadFile = File(...),
    credentials: Tuple[str, str] = Depends(get_credential),
):
    try:
        application_id, _ = credentials
        APPLICATION.id = application_id

        spot_collection = SpotCollectionAggregateFactory().create(
            spot_id_collection=spotIds
        )

        raw_data_file = await rawDataFile.read()
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
            id=spot.get_id_of_private_value().get_id_of_private_value(),
            name=spot.get_name_of_private_value(),
            floor=spot.get_floor_of_private_value(),
            locationType=spot.get_location_type_of_private_value().get_location_type_of_private_value(),
            latitude=spot.get_coordinate_of_private_value().get_latitude_of_private_value(),
            longitude=spot.get_coordinate_of_private_value().get_longitude_of_private_value(),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
