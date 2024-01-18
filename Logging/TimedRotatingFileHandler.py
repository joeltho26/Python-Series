import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = TimedRotatingFileHandler('./Logging/TRFfile.log',when='m',interval=1,backupCount=5,encoding='utf-8')
formatter = '%(asctime)s-%(name)s-%(message)s'
handler.setFormatter(logging.Formatter(formatter))
handler.namer = lambda name: name.replace(".log","") + ".log"
logger.addHandler(handler)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")