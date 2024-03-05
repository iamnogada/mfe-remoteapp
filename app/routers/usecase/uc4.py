from fastapi import APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from app.utils import Template, logger
from datetime import datetime

router = APIRouter()

template = Template()

clusters = [
    {"name": "aws-eks", "id": "1"},
    {
        "name": "azure-aks",
        "id": "2",
    },
    {
        "name": "gcp-gks",
        "id": "3",
    },
]


@router.get("/uc4", response_class=HTMLResponse)
async def search_event(request: Request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(
        request=request,
        name="usecase/uc4.html",
        context={"datetime": formatted_time, "clusters": clusters}
    )


@router.delete("/uc4/section/{item_id}")
async def delete_item(request: Request, item_id:str):
    logger.info(f"Delete item {item_id}")
    return Response(status_code=status.HTTP_200_OK)


@router.get("/uc4/section1", response_class=HTMLResponse)
async def get_section1(request: Request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(
        request=request,
        name="usecase/uc4_section.html",
        context={"datetime": formatted_time, 'title': 'Section 1'}
    )
@router.get("/uc4/section2", response_class=HTMLResponse)
async def get_section2(request: Request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(
        request=request,
        name="usecase/uc4_section.html",
        context={"datetime": formatted_time, 'title': 'Section 2'}
    )
