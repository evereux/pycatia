#! /usr/bin/python3.6

"""

    Example 9:

    Get the position matrix of products (CATPart or CATProduct) in product.

"""

from pycatia import catia

caa = catia()
documents = caa.documents
documents.open(r'tests\cat_files\product_top.CATProduct')
document = caa.active_document

product = document.product()
products = product.get_products()

for product in products:
    print(product.position.get_components())
    # print(product.name, position.get_components())

document.close()
