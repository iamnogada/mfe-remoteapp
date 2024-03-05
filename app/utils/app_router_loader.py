from .app_log import Logger
from importlib import import_module
import os
from fastapi import APIRouter
logger = Logger()

def RouterLoader(app, root="app/routers"):
    logger.debug(f"===Loading routers from {root}")
    for root, dirs, files in os.walk(root):
        for file in files:
            logger.warn(f'Loading file {file}')
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