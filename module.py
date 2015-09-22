import sys
import logging

logger = logging.getLogger(__name__)

logger.info("initializing mod")

class MOD(object):
    def __init__(self):
        logger.info("Created mod object\nAre you seeing this log in the stream?")
        logger.debug("This should appear in the file")
