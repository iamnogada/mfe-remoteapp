from fastapi import APIRouter

router = APIRouter()

@router.get('/{id}')
async def view_item(id: str):
    return {'message': 'Hello from the board view:id router!'}