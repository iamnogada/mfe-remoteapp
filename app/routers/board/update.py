from fastapi import APIRouter

router = APIRouter()

@router.put('/')
async def udpate_default():
    return {'message': 'Hello from the board update router!'}
@router.put('/{id}')
async def update_board_id(id: str):
    return {'message': 'Hello from the board update router!'}