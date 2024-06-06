#! /usr/bin/python3.9

"""

    Example - Space Analysis - 001

    Description:
        Get the center of gravity for the part body 'PartBody'.

    Requirements:
        - CATIA running.
        - Tests already setup.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################
from pathlib import Path

from pycatia import catia
from pycatia.mec_mod_interfaces.part_document import PartDocument

# initialise the catia automation application
caa = catia()
documents = caa.documents
# if the active document is a CATPart this will return a PartDocument
part_document: PartDocument = documents.open(Path(os.getcwd(), r"tests/cat_files/part_measurable.CATPart"))
part = part_document.part

# get the Bodies() collection
bodies = part.bodies

# gets first Body()
body = bodies.item(1)
# >>> print(body)
# >>> Body(name="PartBody")

# or get the body by name
# >>> body_by_name = bodies.get_item_by_name('AnotherPartBody')
# >>> print(body)
# >>> Body(name="AnotherPartBody")

# initialise the spa workbench
spa_workbench = part_document.spa_workbench()
# create a reference to measure.
reference = part.create_reference_from_object(body)

measurable = spa_workbench.get_measurable(reference)

center_of_gravity = measurable.get_cog()
print(center_of_gravity)
