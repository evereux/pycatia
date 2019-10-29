#! /usr/bin/python3.6

"""

    Example 9:

    Get the position matrix of products (CATPart or CATProduct) in product.

"""

from pycatia import CATIAApplication

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_TopLevelAssy.CATProduct')
document = catia.document()

main_product = document.product()
products = main_product.get_products()

for product in products:
    print(product.name, product.position.get_components(catia))

document.close()
