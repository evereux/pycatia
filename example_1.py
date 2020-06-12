#! /usr/bin/python3.6

"""

    Example 1:

    Get the center
    of gravity for the part body 'PartBody'.

"""

from pycatia import catia
from pycatia.space_analyses_interfaces.spa_workbench import SPAWorkbench

documents = catia.documents
documents.open(r'tests\CF_catia_measurable_part.CATPart')

# get the active document
document = catia.active_document
# >>> print(document.path())
# >>> C:\Users\evereux\python\projects\pycatia\tests\CF_catia_measurable_part.CATPart

# get the Part() object.
part = document.part()

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
spa_workbench = SPAWorkbench(document.document)
# create a reference to measure.
reference = part.create_reference_from_object(body)

measurable = spa_workbench.get_measurable(reference)

center_of_gravity = measurable.get_cog()
# >>> print(center_of_gravity)
# >>> center_of_gravity = (86.06520158074527, 81.36458658122612, 10.0)
