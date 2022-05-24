from fastapi import APIRouter

from .endpoints import members


router = APIRouter()
router.include_router(members.router)


@router.get('/')
async def home():
    return {"message": "Welcome!", "github_url": "https://github.com/romankravchuk"}