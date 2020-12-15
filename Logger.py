#!/usr/bin/env python
from time import sleep
import logging


## Configure Logger
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)