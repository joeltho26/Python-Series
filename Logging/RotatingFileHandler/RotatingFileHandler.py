import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = RotatingFileHandler('./Logging/RotatingFileHandler/RFfile.log',backupCount=7,maxBytes=1000,encoding='utf-8')
formatter = '%(asctime)s-%(name)s-%(message)s'
handler.setFormatter(logging.Formatter(formatter))
handler.namer = lambda name: name.replace(".log","") + ".zip"
logger.addHandler(handler)

for i in range(100):
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")