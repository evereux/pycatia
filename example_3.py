#! /usr/bin/python3.6

"""

    Example 3:

    Find all points in the CATPart and find it's co-ordinate.

"""

from pycatia import CATIA_Application
from pycatia import CATIAMeasurable
from pycatia import create_measurable
from pycatia import create_reference
from pycatia import create_spa_workbench
from pycatia import Document
from pycatia import Part

catia = CATIA_Application()
document = Document(catia.catia)
spa_workbench = create_spa_workbench(document.document)
part = Part(document.document)


selected = document.search_for_items(document, ['Point'])

for selection in selected:
    reference = create_reference(part.part, selection)
    selection_measurable = create_measurable(spa_workbench, reference)
    measurable = CATIAMeasurable(selection_measurable)
    print(measurable.get_point())
