from pycatia import catia
from pycatia.product_structure_interfaces.product import Product

caa = catia()
document = caa.active_document
product = Product(document.product.com_object)
user_def_properties = product.user_ref_properties

for property in user_def_properties:
    print(property.name)
    print(property.value_as_string())
