import logging

logger = logging.getLogger(__name__)

file_h = logging.FileHandler('./Logging/FileHandler/file.log')
file_h.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)s-%(message)s-%(asctime)s')
file_h.setFormatter(formatter)
logger.addHandler(file_h)

logger.debug("This is a debug message!")
logger.info("This is a info message!")
logger.error("This is a error message!")
logger.warning("This is a warning message!")
logger.critical("This is a critical message!")
