#! /usr/bin/python3.9
"""
Tests the RenderingMaterial object.

Warning: This tests requires that the test_material_document test passed from the test_material.py file.
"""
import os
from pathlib import Path

from pycatia import CATIADocHandler
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from tests.common_vars import test_files
from tests.source_files import cat_material

icon_folder = Path(os.getcwd(), test_files)


def test_ambient_color():
    with CATIADocHandler(cat_material) as caa:
        document = caa.document
        assert document is not None
        material_document = MaterialDocument(document.com_object)
        material_families = material_document.families
        materials = material_families.item(1).materials
        material = materials.item(1)

        # Test PUT method
        material.rendering_material.put_ambient_color((20, 30, 40))

        # Test GET method
        rgb = material.rendering_material.get_ambient_color()
        assert isinstance(rgb, tuple)
        assert rgb == (20, 30, 40)
