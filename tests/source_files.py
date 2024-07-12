#! /usr/bin/python3.6

import os
from pathlib import Path

from tests.create_source_parts import get_cat_part_measurable
from tests.create_source_products import get_cat_product_top
from tests.create_source_drawing import get_cat_drawing
from tests.create_source_material import get_cat_material
from tests.create_source_functional_system import get_cat_functional_system

design_table_1 = Path(os.getcwd(), r"tests/cat_files/design_table_1.txt")

cat_drawing = get_cat_drawing()
cat_part_measurable = get_cat_part_measurable()
cat_product = get_cat_product_top()

cat_material = get_cat_material()
cat_functional_system = get_cat_functional_system()

igs_file = Path(os.getcwd(), r"tests/cat_files/part_measurable.igs")
stp_file = Path(os.getcwd(), r"tests/cat_files/part_measurable.stp")
