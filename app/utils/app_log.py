import logging
import logging.config



def Logger(name: str="app") -> logging.Logger:
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger