#! /usr/bin/python3.6

"""

    Example 1:

    Get the center of gravity for the part body 'PartBody'.

"""

from pycatia import catia

# initialise the catia automation application
caa = catia()
documents = caa.documents
documents.open(r'tests/cat_files/part_measurable.CATPart')

# get the active document
document = caa.active_document
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
spa_workbench = document.spa_workbench()
# create a reference to measure.
reference = part.create_reference_from_object(body)

measurable = spa_workbench.get_measurable(reference)

center_of_gravity = measurable.get_cog()
print(center_of_gravity)
