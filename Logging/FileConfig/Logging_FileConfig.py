import logging
import logging.config

logging.config.fileConfig('./Logging/FileConfig/logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug("This is a debug message")

