from fastapi import APIRouter

router = APIRouter()

@router.get('/form')
async def form_view():
    return {'message': 'Hello from the board form router!'}