from fastapi import FastAPI, Request, Response, Path
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import Optional, Annotated
import time
from models import MockupData
import logging
logger = logging.getLogger(__name__)

APP_NAME="/mfe"
app = FastAPI(root_path=f"{APP_NAME}")


app.mount(f"/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount(f"/js", StaticFiles(directory="public/js"), name="js")
app.mount(f"/css", StaticFiles(directory="public/css"), name="css")

templates = Jinja2Templates(directory=f"views")


# check HX request if not add basic css and js files for application
# add process time to response header
@app.middleware("http")
async def check_hx_header(request: Request, call_next):
    start_time = time.time()
    if "Hx-Request" in request.headers:
        # add hx_request to state so JINJA2 use this to add css and js files
        request.state.hx_request = True
    request.state.root_path = APP_NAME
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/", response_class=JSONResponse)
def read_root(request: Request):
    return {"message": f"This is '{APP_NAME}' Application"}


@app.get("/items")
async def read_item(request: Request):
    return RedirectResponse(f"{request.state.root_path}/items/0")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int=1):
    return templates.TemplateResponse(
        request=request, name="main.html", context={"items": MockupData.Todos[id:id+1]}
    )

@app.get("/clusters/{slot:path}/name", response_class=HTMLResponse)
async def read_item(request: Request, slot: str):
    logging.warn(f"Slot: {slot}")
    return templates.TemplateResponse(
        request=request, name="main.html", context={"items": MockupData.Todos[0:1]}
    )