#! /usr/bin/python3.9

import os
from pathlib import Path

import pytest

from pycatia import CATIADocHandler
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.cat_mat_interfaces.material_manager import MaterialManager
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument
from tests.common_vars import test_files
from tests.conftest import application
from tests.source_files import cat_material
from tests.source_files import cat_part_measurable
from tests.source_files import cat_product

icon_folder = Path(os.getcwd(), test_files)


@pytest.mark.parametrize('file_name', [cat_material])
def test_material_document(document_close_all_open):
    material_document: MaterialDocument = application.active_document

    material_families = material_document.families
    materials = material_families.item(1).materials
    assert material_families.count > 0
    assert materials.count > 0


@pytest.mark.parametrize('file_name', [cat_material])
def test_material_manager_part(document_open):
    material_document: MaterialDocument = application.active_document
    material_families = material_document.families
    materials = material_families.item(1).materials
    material = materials.item(1)

    with CATIADocHandler(cat_part_measurable) as caap:
        part_document: PartDocument = caap.document
        part = part_document.part
        main_body = part.main_body
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.add()

        material_item = part.get_item("CATMatManagerVBExt")
        material_manager = MaterialManager(material_item.com_object)

        material_manager.apply_material_on_body(i_body=main_body, i_material=None)
        material_manager.apply_material_on_part(i_part=part, i_material=None)
        material_manager.apply_material_on_hybrid_body(i_hybrid_body=hybrid_body, i_material=None)

        material_manager.apply_material_on_body(i_body=main_body, i_material=material)
        material_manager.apply_material_on_part(i_part=part, i_material=material)
        material_manager.apply_material_on_hybrid_body(i_hybrid_body=hybrid_body, i_material=material)

        part_mat = material_manager.get_material_on_part(i_part=part)
        body_mat = material_manager.get_material_on_body(i_body=main_body)
        hybrid_mat = material_manager.get_material_on_hybrid_body(i_hybrid_body=hybrid_body)

        assert part_mat.name == material.name
        assert body_mat.name == material.name
        assert hybrid_mat.name == material.name


@pytest.mark.parametrize('file_name', [cat_material])
def test_material_manager_product(document_open):
    material_document: MaterialDocument = application.active_document
    material_families = material_document.families
    materials = material_families.item(1).materials
    material = materials.item(1)

    with CATIADocHandler(cat_product) as caap:
        product_document: ProductDocument = caap.document  #
        product = product_document.product
        material_item = product.get_item("CATMatManagerVBExt")
        material_manager = MaterialManager(material_item.com_object)

        material_manager.apply_material_on_product(i_product=product, i_material=None)
        material_manager.apply_material_on_product(i_product=product, i_material=material, i_link_mode=True)
        product_mat = material_manager.get_material_on_product(i_product=product)

        assert product_mat.name == material.name


@pytest.mark.parametrize('file_name', [cat_material])
def test_analysis_material(document_open):
    material_document: MaterialDocument = application.active_document
    material_families = material_document.families
    materials = material_families.item(1).materials
    material = materials.item(1)
    assert material.analysis_material.get_type() == "MATERIAL_ISOTROPIC"
    assert float(material.analysis_material.get_value("SAMDensity")) > 0.0


@pytest.mark.parametrize('file_name', [cat_material])
def test_material(document_open_test_close):
    material_document: MaterialDocument = application.active_document
    material_families = material_document.families
    materials = material_families.item(1).materials
    material = materials.item(1)
    material.get_icon(str(icon_folder))
    material.put_icon(str(icon_folder))
    icon_path = f"{icon_folder}\\{material.name}.jpg"

    assert material.exist_analysis_data()
    assert material.exist_rendering_data()
    assert os.path.isfile(icon_path)
    os.remove(icon_path)
