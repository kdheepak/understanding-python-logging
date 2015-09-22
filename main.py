import sys
import logging

#logger = logging.getLogger("module.module")
#logger.setLevel(logging.DEBUG)
#
##stream_handler = logging.StreamHandler(sys.stdout)
##stream_handler.setLevel(logging.INFO)
## 
##formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
##stream_handler.setFormatter(formatter)
## 
##logger.addHandler(stream_handler)
#
## create a file handler
#handler = logging.FileHandler('module.log', 'w')
#handler.setLevel(logging.DEBUG)
#
## create a logging format
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#
## add the handlers to the logger
#logger.addHandler(handler)
#
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#
##stream_handler = logging.StreamHandler(sys.stdout)
##stream_handler.setLevel(logging.DEBUG)
##
##formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
##stream_handler.setFormatter(formatter)
##
##logger.addHandler(stream_handler)
#
#
## create a file handler
#handler = logging.FileHandler("main.log", 'w')
#handler.setLevel(logging.INFO)
#
## create a logging format
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#
## add the handlers to the logger
#logger.addHandler(handler)
#
#
ch = logging.getLogger()
ch.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

ch.addHandler(stream_handler)

# Testing

import module


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info("Inside main")

module.module.MOD()

logger.info("End")
