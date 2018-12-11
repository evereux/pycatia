#! /usr/bin/python3.6

"""

    Example 4:

    Shows how to loop through a CATProduct and find if sub component is
    a CATPart or CATProduct.

"""

from pycatia import CATIAApplication
from pycatia import Document
from pycatia import Part

catia = CATIAApplication()
document = Document(catia.catia)
product = document.product

for item in product.get_products():

    if item.is_catpart():
        part = Part(item.product)
        print(f'This is a part: "{part}"')
        print('')

    if item.is_catproduct():
        product = item
        print(f'This is a product: "{product}"')

        if item.has_children():
            print('This product has children.')
            children = item.get_children()
            print(children)
        print('')
