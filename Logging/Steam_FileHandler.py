import logging

logger = logging.getLogger(__name__)

steam_h = logging.StreamHandler()
file_h = logging.FileHandler('./Logging/file.log')

steam_h.setLevel(logging.INFO)
file_h.setLevel(logging.WARNING)

formatter = logging.Formatter('%(name)s-%(message)s-%(asctime)s')
steam_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(steam_h)
logger.addHandler(file_h)

logger.debug("This is a debug message!")
logger.info("This is a info message!")
logger.error("This is a error message!")
logger.warning("This is a warning message!")
logger.critical("This is a critical message!")
