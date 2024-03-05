from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils import Template, logger

router = APIRouter()

template = Template()
# logging = Logger(__name__)

@router.get('/', response_class=HTMLResponse)
async def search_event(request: Request):
    return template.TemplateResponse(request = request, name="counter/counter.html")