from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils import Template, logger
from datetime import datetime

router = APIRouter()

clusters = [
  {
    "name": "aws-eks",
    "id": "1"
  },
  {
    "name": "azure-aks",
    "id": "2",
  },
  {
    "name": "gcp-gks",
    "id": "3",
  }
]

template = Template()
# logging = Logger(__name__)


@router.get('/clusters', response_class=HTMLResponse)
async def search_event(request: Request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(request = request, name="resource/list_clusters.html",context={'clusters':clusters, 'datetime':formatted_time})