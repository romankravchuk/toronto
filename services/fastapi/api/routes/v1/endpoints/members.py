from fastapi import APIRouter


router = APIRouter(prefix='/members')


@router.get('/')
async def read_members():
    return {"members": []}
