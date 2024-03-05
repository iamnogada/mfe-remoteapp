import logging
import logging.config



# def Logger(name: str="app") -> logging.Logger:
#     # logging.config.fileConfig("logging.conf")
#     logger = logging.getLogger(name)
#     # logger.setLevel(logging.DEBUG)
#     return logger
# Disable uvicorn access logger
uvicorn_access = logging.getLogger("uvicorn.access")
# uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.getLevelName(logging.DEBUG))