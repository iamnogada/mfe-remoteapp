
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils import RouterLoader, Template
from app.middlewares import MFEMiddleware




#  Context path for the application
APP_NAME="/mfe"

app = FastAPI(root_path=f"{APP_NAME}",title=f"{APP_NAME}", version="0.1.0",debug=True)

app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount("/js", StaticFiles(directory="public/js"), name="js")
app.mount("/css", StaticFiles(directory="public/css"), name="css")
app.mount("/test", StaticFiles(directory="public/css"), name="html")

RouterLoader(app)
# If Reqeust form HTMX, then response only block html, othwerwise return full html including header
# For HTMX, set request.state.hx_request = True so Jinja2 conditionally add css and js files
mfe_middleware = MFEMiddleware(app=app, root_path=f"{APP_NAME}")
app.add_middleware(BaseHTTPMiddleware, dispatch=mfe_middleware.dispatch)

templates = Template()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request = request, name="main.html")
