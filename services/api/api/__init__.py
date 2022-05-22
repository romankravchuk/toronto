from fastapi import FastAPI


def create_api():
    api = FastAPI()

    from .routes.v1.api import router

    api.include_router(router=router)
    
    return api
