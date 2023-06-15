#! /usr/bin/python3.9

"""

    Example - Logging - 001

    Description:
        Logging.

    Requirements:
        - CATIA running.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia

caa = catia()

caa.logger.info("Hello world!")
caa.logger.warning("Stay alert, stay safe, bee kind!")

# [2020-06-13 11:12:09,096] INFO in example_14: Hello world!
# [2020-06-13 11:12:09,096] WARNING in example_14: Stay alert, stay safe, bee kind!
