#! /usr/bin/python3.9

"""

    Example - Material - 001

    Description:
        Opens the material catalog and retrieves the first few materials.
        Creates a new part and applies the material to the part, the main
        body and a hybrid body.
        Creates a new product and applies the material to it.

    Requirements:
        - CATIA running.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pathlib import Path

from pycatia import catia
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.cat_mat_interfaces.material_manager import MaterialManager
from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product

caa = catia()

##########################################################
# MATERIAL MANAGER ON MATERIAL CATALOGS
##########################################################
material_document: MaterialDocument = caa.documents.open(Path(os.getcwd(), r"tests/cat_files/Catalog.CATMaterial"))
material_families = material_document.families
materials = material_families.item(1).materials

material_families_list = []
material_list = []

for i in range(len(material_families)):
    index = i + 1
    family = material_families.item(index)
    material_families_list.append(family)

for i in range(len(materials)):
    index = i + 1
    material = materials.item(index)
    material_list.append(material)

print(f"Found {material_families.count} material families: " f"{', '.join([n.name for n in material_families_list])}.")
print(f"Found {materials.count} materials in the first family: " f"{', '.join([n.name for n in material_list])}.")

##########################################################
# MATERIAL MANAGER ON PARTS
##########################################################
caa.documents.add("Part")
part_document = caa.active_document
part = Part(part_document.part.com_object)  # type: ignore
main_body = part.main_body
hybrid_bodies = part.hybrid_bodies
hybrid_body = hybrid_bodies.add()

material_item = part.get_item("CATMatManagerVBExt")
material_manager = MaterialManager(material_item.com_object)

print("Removing all materials ...")
material_manager.apply_material_on_body(i_body=main_body, i_material=None)
material_manager.apply_material_on_part(i_part=part, i_material=None)
material_manager.apply_material_on_hybrid_body(i_hybrid_body=hybrid_body, i_material=None)

print("Adding materials with link ...")
material_manager.apply_material_on_part(i_part=part, i_material=material_list[0], i_link_mode=True)
material_manager.apply_material_on_body(i_body=main_body, i_material=material_list[1], i_link_mode=True)
material_manager.apply_material_on_hybrid_body(i_hybrid_body=hybrid_body, i_material=material_list[2], i_link_mode=True)

material_1 = material_manager.get_material_on_part(i_part=part)
print(
    "Material applied to Part:",
    "None" if material_1 is None else material_1.name,
)

material_2 = material_manager.get_material_on_body(i_body=main_body)
print(
    "Material applied to Main Body:",
    "None" if material_2 is None else material_2.name,
)

material_3 = material_manager.get_material_on_hybrid_body(i_hybrid_body=hybrid_body)
print(
    "Material applied to Hybrid Body:",
    "None" if material_3 is None else material_3.name,
)

##########################################################
# MATERIAL MANAGER ON PRODUCTS
##########################################################
caa.documents.add("Product")
product_document = caa.active_document
product = product_document.product  # type: ignore
product = Product(product.com_object)
material_item = product.get_item("CATMatManagerVBExt")
material_manager = MaterialManager(material_item.com_object)

print("Removing material ...")
material_manager.apply_material_on_product(i_product=product, i_material=None)

print("Adding material with link ...")
material_manager.apply_material_on_product(i_product=product, i_material=material_list[3], i_link_mode=True)

material_4 = material_manager.get_material_on_product(i_product=product)
print(
    "Material applied to Product:",
    "None" if material_4 is None else material_4.name,
)
