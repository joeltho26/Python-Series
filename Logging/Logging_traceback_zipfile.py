import logging
from logging.handlers import TimedRotatingFileHandler
import traceback
import zipfile
import os

def rotator(source,dest):
    zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED).write(source, os.path.basename(source))
    os.remove(source)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(filename="./Logging/TRF-zip.log", interval=1, backupCount=5, encoding="utf-8", when="m")
formatter = logging.Formatter('%(name)s-%(asctime)s-%(message)s')
handler.setFormatter(formatter)
handler.namer = lambda name: name.replace(".log","") + ".zip"
handler.rotator = rotator
logger.addHandler(handler)

try:
    a = 10/0
except Exception as e:
    logger.debug("The error is %s",traceback.format_exc() )