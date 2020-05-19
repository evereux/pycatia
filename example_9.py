#! /usr/bin/python3.6

"""

    Example 9:

    Get the position matrix of products (CATPart or CATProduct) in product.

"""

from pycatia.in_interfaces.application import catia_application as catia
from pycatia.in_interfaces.position import Position

documents = catia.documents
documents.open(r'tests\CF_TopLevelAssy.CATProduct')
document = catia.active_document

product = document.product()
products = product.get_products()

for product in products:
    position = Position(product.com_object)
    print(position.get_components())
    # print(product.name, position.get_components())

document.close()
