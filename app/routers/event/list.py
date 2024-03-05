from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

data = [
    {
        "title": "Post Title 1",
        "contents": "This is the content of post 1. It's just an example.",
        "datetime": "2023-03-21 04:24:17",
        "writer": "Writer1"
    },
    {
        "title": "Post Title 2",
        "contents": "This is the content of post 2. It's just an example.",
        "datetime": "2023-07-20 04:24:17",
        "writer": "Writer2"
    },
    {
        "title": "Post Title 3",
        "contents": "This is the content of post 3. It's just an example.",
        "datetime": "2023-12-29 04:24:17",
        "writer": "Writer3"
    },
    {
        "title": "Post Title 4",
        "contents": "This is the content of post 4. It's just an example.",
        "datetime": "2023-05-03 04:24:17",
        "writer": "Writer4"
    },
    {
        "title": "Post Title 5",
        "contents": "This is the content of post 5. It's just an example.",
        "datetime": "2023-06-21 04:24:17",
        "writer": "Writer5"
    }
]

person = {
    "name": "John",
    "age": 30
}

@router.get('/', response_class=JSONResponse)
async def search_event():
    return {'data': data}