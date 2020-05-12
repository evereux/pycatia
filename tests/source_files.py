#! /usr/bin/python3.6

import os
from pathlib import Path

cat_product = Path(os.getcwd(), r"tests/CF_TopLevelAssy.CATProduct")

cat_part_1 = Path(os.getcwd(), r"tests/CF_Part_1.CATPart")
cat_part_2 = Path(os.getcwd(), r"tests/CF_Part_2.CATPart")
cat_part_3 = Path(os.getcwd(), r"tests/CF_Part_3.CATPart")
cat_part_blank = Path(os.getcwd(), r"tests/CF_Part_Blank.CATPart")
cat_part_temp = Path(os.getcwd(), r"tests/CF_Part_temp.CATPart")
cat_part_measurable = Path(os.getcwd(), r"tests/CF_catia_measurable_part.CATPart")
cat_part_not_updated = Path(os.getcwd(), r"tests/CF_part_not_updated.CATPart")

cat_drawing = Path(os.getcwd(), r"tests/CF_Drawing1.CATDrawing")
