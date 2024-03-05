from fastapi.templating import Jinja2Templates

def Template(directory:str=f"app/routers"):
    templates = Jinja2Templates(directory=f"{directory}")
    return templates