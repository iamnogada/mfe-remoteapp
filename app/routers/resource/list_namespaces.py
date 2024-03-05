from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils import logger

router = APIRouter()
# logging = Logger(__name__)

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

@router.get('/namespaces', response_class=JSONResponse)
async def search_event(clusters: int = 1):
    logger.info(f"clusters: {clusters}")
    filtered_data = [item for item in namespaces if item["cluster_id"] == str(clusters)]
    return {'namespaces': filtered_data}