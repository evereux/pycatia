#! /usr/bin/python3.6

"""

    Example 3:

    Find all points in the CATPart and print it's co-ordinate.

"""

from pycatia import CATIAApplication
from pycatia import CATIAMeasurable
from pycatia import create_measurable
from pycatia import create_reference
from pycatia import create_spa_workbench

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_catia_measurable_part.CATPart')

document = catia.document()


spa_workbench = create_spa_workbench(document.document)
part = document.part

selected = document.search_for_items(document, ['Point'])

for selection in selected:
    reference = create_reference(part.part, selection)
    selection_measurable = create_measurable(spa_workbench, reference)
    measurable = CATIAMeasurable(selection_measurable)
    print(measurable.get_point(catia))
