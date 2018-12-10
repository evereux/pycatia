#! /usr/bin/python3.6

from pycatia import CATIAApplication
from pycatia import Document


catia = CATIAApplication()
document = Document(catia.catia)
product = document.part

print(product.name)

for prod in product.get_products():
    print(prod)
