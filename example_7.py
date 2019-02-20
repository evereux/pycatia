#! /usr/bin/python3.6

"""

    Example 7:

    Use the context manager to open CATIA documents and close

"""

import time

from pycatia import CATIADocHandler

catia_part = r'tests\CF_catia_measurable_part.CATPart'

with CATIADocHandler(catia_part) as handler:
    document = handler.document
    # do some stuff.
    time.sleep(5)  # don't do this, no need.
    # document is automatically closed. Lovely.
