import logging
import logging.config



def getlogger(name: str) -> logging.Logger:
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger(name)
    return logger