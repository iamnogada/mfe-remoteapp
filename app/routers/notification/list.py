from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def search_board():
    return {'message': 'Hello from the board search_board router!'}