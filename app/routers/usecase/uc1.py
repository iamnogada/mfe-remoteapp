"""Doc String"""
from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.utils import Template, logger

router = APIRouter()

template = Template()
logger.info("usecase/uc1.py")

# http://127.0.0.1:8000/mfe/usecase/uc1
# http://{server url}/{root_path}/{directory_name}/{endpoint}
@router.get("/uc1", response_class=HTMLResponse)
async def search_event(request: Request) -> HTMLResponse:
    """search_event"""
    # business logic
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # request to render html to tempate engine
    return template.TemplateResponse(
        request=request, name="usecase/uc1.html", context={"datetime": formatted_time}
    )
