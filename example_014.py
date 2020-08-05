#! /usr/bin/python3.6

"""

    Example 14:

    Logging.

"""
from pycatia import catia

caa = catia()

caa.logger.info('Hello world!')
caa.logger.warning('Stay alert, stay safe, bee kind!')

# [2020-06-13 11:12:09,096] INFO in example_14: Hello world!
# [2020-06-13 11:12:09,096] WARNING in example_14: Stay alert, stay safe, bee kind!
