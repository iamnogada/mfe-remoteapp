from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils import Template, logger
from datetime import datetime

router = APIRouter()

template = Template()
# logging = Logger(__name__)

@router.get('/timer', response_class=HTMLResponse)
async def search_event(request: Request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(request = request, name="counter/timer.html",context={'datetime':formatted_time})