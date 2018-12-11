#! /usr/bin/python3.6

"""

    Example 1:

    Shows how to access the CATIA COM object with a .CATPart open and get the center
    of gravity for the part body 'PartBody'.

"""

from pycatia import create_reference, create_measurable
from pycatia import CATIAApplication
from pycatia import CATIAMeasurable
from pycatia import create_spa_workbench
from pycatia import Document

catia = CATIAApplication()
document = Document(catia.catia)
part = document.part
spa_workbench = create_spa_workbench(document.document)

bodies = part.get_bodies()
body_names = part.get_bodies_names()
# body_names = ['PartBody', 'EmptyPartBody']

# gets first body in bodies list.
body = bodies[0]

# or get the body by name
body_by_name = part.get_body_by_name('PartBody')

# equivalent to VB CreateReferenceFromObject()
reference = create_reference(part.part, body)

# equivalent to VB GetMeasurable()
measurable = create_measurable(spa_workbench, reference)

# the measurable object
catia_measurable = CATIAMeasurable(measurable)

# run the VB function Measurable.GetCOG()
center_of_gravity = catia_measurable.get_cog()
# center_of_gravity = (86.06520158074527, 81.36458658122612, 10.0)
print(center_of_gravity)
