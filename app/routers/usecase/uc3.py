from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from app.utils import Template, logger
from datetime import datetime

router = APIRouter()

template = Template()
# logging = Logger(__name__)

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
namespaces = [
  {
    "name": "eks-system",
    "cluster_id": "1",
    "id": "1"
  },
  {
    "name": "zcp-system",
    "cluster_id": "1",
    "id": "2"
  },
  {
    "name": "hr-system",
    "cluster_id": "1",
    "id": "3"
  },
  {
    "name": "aks-system",
    "cluster_id": "2",
    "id": "4"
  },
  {
    "name": "zcp-system",
    "cluster_id": "2",
    "id": "5"
  },
  {
    "name": "erp-system",
    "cluster_id": "2",
    "id": "6"
  },
  {
    "name": "gks-system",
    "cluster_id": "3",
    "id": "7"
  },
  {
    "name": "api-system",
    "cluster_id": "3",
    "id": "8"
  },
  {
    "name": "edu-system",
    "cluster_id": "3",
    "id": "9"
  }
  
]

@router.get('/uc3', response_class=HTMLResponse)
async def search_event(request: Request):
    # logger.info(f"cluster: {clusters}")
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(request = request, name="usecase/uc3.html",context={'datetime':formatted_time, 'clusters':clusters})
  
@router.get('/uc3/namespace', response_class=JSONResponse)
async def search_event(cluster: int = 1):
    # logger.info(f"cluster: {clusters}")
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    filtered_data = [item for item in namespaces if item["cluster_id"] == str(cluster)]
    # logger.info(f"filtered_data: {filtered_data}")
    return {'namespaces': filtered_data}