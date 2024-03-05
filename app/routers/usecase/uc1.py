from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils import Template, logger
from datetime import datetime

router = APIRouter()

template = Template()
# logging = Logger(__name__)

@router.get('/uc1', response_class=HTMLResponse)
async def search_event(request: Request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(request = request, name="usecase/uc1.html",context={'datetime':formatted_time})