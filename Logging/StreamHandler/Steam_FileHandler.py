import logging

#streamhandler will only print messages from level warning and higher only (warning, error, critical)

logger = logging.getLogger(__name__)
steam_h = logging.StreamHandler()
steam_h.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)s-%(message)s-%(asctime)s')
steam_h.setFormatter(formatter)
logger.addHandler(steam_h)

logger.debug("This is a debug message!")
logger.info("This is a info message!")
logger.error("This is a error message!")
logger.warning("This is a warning message!")
logger.critical("This is a critical message!")
