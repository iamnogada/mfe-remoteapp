import os
from fastapi import FastAPI, APIRouter,Request, Response, Path
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from importlib import import_module
import logging
from app.utils import getlogger
import time

# logging.basicConfig(
#     level=logging.INFO,
#     format="[%(asctime)s] [%(levelname)s] - %(name)s : %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )
# logger = logging.getLogger(__name__)
logger = getlogger(__name__)
app = FastAPI(title="Remote App", version="0.1.0")


def load_routers(app, root="app/routers"):
    logger.debug(f"===Loading routers from {root}")
    for root, dirs, files in os.walk(root):
        for file in files:
            # logger.warn(f'Loading file {file}')
            if file.endswith(
                ".py"
            ):  # Adjust this if your router files are named differently
                module_path = (
                    os.path.join(root, file).replace("/", ".").replace("\\", ".")[:-3]
                )
                mod = import_module(module_path)
                if hasattr(mod, "router") and isinstance(mod.router, APIRouter):
                    prefix = os.path.relpath(root, "app/routers").replace(os.sep, "/")
                    app.include_router(mod.router, prefix=f"/{prefix}", tags=[prefix])
                else:
                    logger.info(f"Module {module_path} does not have a FastAPI router.")
                logger.info(f"Loading router {module_path} with prefix {prefix}")

app.mount(f"/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount(f"/js", StaticFiles(directory="public/js"), name="js")
app.mount(f"/css", StaticFiles(directory="public/css"), name="css")

templates = Jinja2Templates(directory=f"app/routers")

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

load_routers(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}
