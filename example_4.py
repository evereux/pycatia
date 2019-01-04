#! /usr/bin/python3.6

"""

    Example 4:

    Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

"""

from pycatia import CATIAApplication

catia = CATIAApplication()
document = catia.document()
part = document.part
product = document.product


products = product.get_products()

if len(products) == 0:
    print("Active document has no children or is not a CATProduct.")

for item in product.get_products():

    if item.is_catpart():
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
