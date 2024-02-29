from fastapi import FastAPI

from presentation.handler.create_sopt_hadler import \
    router as create_spot_router
from presentation.handler.get_spot_by_spot_id_collection_handler import \
    router as get_spot_by_spot_id_collection_router

app = FastAPI()

app.include_router(get_spot_by_spot_id_collection_router)
app.include_router(create_spot_router)
