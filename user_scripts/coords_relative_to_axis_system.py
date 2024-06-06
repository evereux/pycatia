#! /usr/bin/python3.9
# author: Mithro86
# contact: mikael@rslnd.se

"""
    Measure point relative to axis system.

    Description
    ===========
    Measures point relative to axis system.

    Requirements
    ============
    python >= 3.9
    pycatia
    CATIA V5 is running with an open part that includes an axis system and a
    geometrical set named "Inputs" containing a point named "Point.1". The first
    axis in the axis collection will be selected.
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
part_document: PartDocument = caa.active_document
part = part_document.part
hybrid_bodies = part.hybrid_bodies
spa_workbench = part_document.spa_workbench()


def coords_relative_to_axis(axis_system, point, precision=6):
    a_origin = axis_system.get_origin()
    a_xaxis = axis_system.get_x_axis()
    a_yaxis = axis_system.get_y_axis()
    a_zaxis = axis_system.get_z_axis()

    n_x = normalize_vector(a_xaxis)
    n_y = normalize_vector(a_yaxis)
    n_z = normalize_vector(a_zaxis)

    reference = part.create_reference_from_object(point)
    measurable = spa_workbench.get_measurable(reference)
    coordinates = measurable.get_point()

    diff = [0] * 3
    diff[0] = coordinates[0] - a_origin[0]
    diff[1] = coordinates[1] - a_origin[1]
    diff[2] = coordinates[2] - a_origin[2]

    x = round(dot_product(diff, n_x), precision)
    y = round(dot_product(diff, n_y), precision)
    z = round(dot_product(diff, n_z), precision)

    return x, y, z


def normalize_vector(vec):
    magnitude = (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2) ** 0.5
    if magnitude != 0:
        x = vec[0] / magnitude
        y = vec[1] / magnitude
        z = vec[2] / magnitude

        return x, y, z


def dot_product(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]


# Get first axis system in collection
axis_system = part.axis_systems.item(2)

# Get point to measure
hb = hybrid_bodies.item("Inputs")
hs = hb.hybrid_shapes
point = hs.item("Point.4")

# Measure point to axis system and print
coords = coords_relative_to_axis(axis_system, point)

print(coords)
