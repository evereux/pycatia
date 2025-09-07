#! /usr/bin/python3.9
"""
Tests the RenderingMaterial object.

Warning: This tests requires that the test_material_document test passed from the test_material.py file.
"""
import os
from pathlib import Path

import pytest

from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from tests.common_vars import test_files
from tests.conftest import application
from tests.source_files import cat_material

icon_folder = Path(os.getcwd(), test_files)


@pytest.mark.parametrize('file_name', [cat_material])
def test_ambient_color(document_close_all_open_test_close):
    material_document: MaterialDocument = application.active_document
    material_families = material_document.families
    materials = material_families.item(1).materials
    material = materials.item(1)

    # Test PUT method
    material.rendering_material.put_ambient_color((20, 30, 40))

    # Test GET method
    rgb = material.rendering_material.get_ambient_color()
    assert isinstance(rgb, tuple)
    assert rgb == (20, 30, 40)
