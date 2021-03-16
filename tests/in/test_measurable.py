#! /usr/bin/python3.6

"""
    This file is named test_measurable.py so these tests are run first. Othwerise the tests would fail for
    test_document.py. I've no idea why at the moment.
"""

from pycatia import CATIADocHandler
from pycatia.enumeration.enumeration_types import cat_measurable_name
from tests.source_files import cat_part_measurable
from tests.create_source_parts import geom_set_lines
from tests.create_source_parts import geom_set_surfaces
from tests.create_source_parts import geom_set_arcs
from tests.create_source_parts import geom_set_points
from tests.create_source_parts import geom_set_planes
from tests.create_source_parts import geom_set_cylinders


def round_tuple(tuple_object, decimal_places=6):
    rounded_list = list()

    for item in tuple_object:
        if isinstance(item, int) or isinstance(item, float):
            rounded = round(item, decimal_places)
            rounded_list.append(rounded)
        else:
            rounded_list.append(item)

    return tuple(rounded_list)


def test_area():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        bodies = part.bodies
        body = bodies.item(1)

        reference = part.create_reference_from_object(body)
        measurable = spa_workbench.get_measurable(reference)
        area_m = measurable.area

        area = 0.04

        assert area == round(area_m, 6)


def test_geometry_name():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        bodies = part.bodies
        body = bodies.item(1)

        reference = part.create_reference_from_object(body)
        measurable = spa_workbench.get_measurable(reference)

        assert measurable.geometry_name == cat_measurable_name.index('CatMeasurableVolume')


def test_length():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_lines)
        line1 = hybrid_body.hybrid_shapes.item(1)
        line1_reference = part.create_reference_from_object(line1)
        line1_measurable = spa_workbench.get_measurable(line1_reference)

        length = 141.421356
        catia_length = line1_measurable.length

        assert length == round(catia_length, 6)


def test_perimeter():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()
        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_surfaces)
        surface = hybrid_body.hybrid_shapes.item(1)
        surface_reference = part.create_reference_from_object(surface)
        surface_measurable = spa_workbench.get_measurable(surface_reference)

        perimeter = 400
        catia_perimeter = surface_measurable.perimeter

        assert perimeter == round(catia_perimeter, 6)


def test_radius():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_arcs)
        arc = hybrid_body.hybrid_shapes.item(1)
        arc_reference = part.create_reference_from_object(arc)
        arc_measurable = spa_workbench.get_measurable(arc_reference)
        radius = 25.0
        catia_radius = arc_measurable.radius

        assert radius == round(catia_radius, 6)


def test_angle_between():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_lines)
        line1 = hybrid_body.hybrid_shapes.item(1)
        line1_reference = part.create_reference_from_object(line1)
        line1_measurable = spa_workbench.get_measurable(line1_reference)
        line2 = hybrid_body.hybrid_shapes.item(2)
        line2_reference = part.create_reference_from_object(line2)
        angle = 45.0
        catia_angle = line1_measurable.get_angle_between(line2_reference)

        assert angle == round(catia_angle, 6)


def test_get_axis():
    """
    # I've really no idea what the axis for an arc/circle/cylinder is.
    # I can't reproduce these figures in CATIA.
    :return:
    """

    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_arcs)
        arc = hybrid_body.hybrid_shapes.item(1)
        arc_reference = part.create_reference_from_object(arc)
        arc_measurable = spa_workbench.get_measurable(arc_reference)

        axis = (0.0, 0.0, 441.941738)
        catia_axis = arc_measurable.get_axis()

        assert axis == (round(catia_axis[0], 6), round(catia_axis[1], 6), round(catia_axis[2], 6))


def test_get_axis_system():
    """
    :return:
    """
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document

        part = document.part
        spa_workbench = document.spa_workbench()

        axis_systems = part.axis_systems
        axis = axis_systems.item(1)
        axis_reference = part.create_reference_from_object(axis)
        axis_measurable = spa_workbench.get_measurable(axis_reference)

        axis_system = (
            0.000,
            0.000,
            0.000,
            1.000,
            0.000,
            0.000,
            0.000,
            1.000,
            0.000000,
            0.000000,
            0.000000,
            1.000000)
        catia_axis = axis_measurable.get_axis_system()

        assert axis_system == (
            round(catia_axis[0], 6),
            round(catia_axis[1], 6),
            round(catia_axis[2], 6),
            round(catia_axis[3], 6),
            round(catia_axis[4], 6),
            round(catia_axis[5], 6),
            round(catia_axis[6], 6),
            round(catia_axis[7], 6),
            round(catia_axis[8], 6),
            round(catia_axis[9], 6),
            round(catia_axis[10], 6),
            round(catia_axis[11], 6),
        )


def test_get_direction():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document

        part = document.part
        spa_workbench = document.spa_workbench()
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_lines)
        line1 = hybrid_body.hybrid_shapes.item(1)
        line1_reference = part.create_reference_from_object(line1)
        line1_measurable = spa_workbench.get_measurable(line1_reference)

        direction_vector = (0.707107, 0.707107, 0)
        catia_direction = line1_measurable.get_direction()

        assert direction_vector == (
            round(catia_direction[0], 6),
            round(catia_direction[1], 6),
            round(catia_direction[2], 6),
        )


def test_get_minimum_distance():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document

        part = document.part
        spa_workbench = document.spa_workbench()

        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_lines)
        line1 = hybrid_body.hybrid_shapes.item(1)
        line1_reference = part.create_reference_from_object(line1)
        line1_measurable = spa_workbench.get_measurable(line1_reference)

        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_points)
        point = hybrid_body.hybrid_shapes.item(2)
        point_reference = part.create_reference_from_object(point)

        minimum_distance = 70.710678
        catia_minimum_distance = line1_measurable.get_minimum_distance(point_reference)

        assert minimum_distance == round(catia_minimum_distance, 6)


def test_get_minimum_distance_points():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document

        part = document.part
        spa_workbench = document.spa_workbench()
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_points)
        point1 = hybrid_body.hybrid_shapes.item(1)
        point1_reference = part.create_reference_from_object(point1)
        point1_measurable = spa_workbench.get_measurable(point1_reference)

        point2 = hybrid_body.hybrid_shapes.item(3)
        point2_reference = part.create_reference_from_object(point2)

        minimum_distance_points = (
            0.000000,
            0.000000,
            0.000000,
            100.000000,
            100.000000,
            0.000000,
            None,
            None,
            None
        )
        catia_minimum_distance_points = point1_measurable.get_minimum_distance_points(point2_reference)

        assert minimum_distance_points == round_tuple(catia_minimum_distance_points, 6)


def test_get_plane():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document

        spa_workbench = document.spa_workbench()
        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_planes)
        plane = hybrid_body.hybrid_shapes.item(1)
        plane_reference = part.create_reference_from_object(plane)
        plane_measurable = spa_workbench.get_measurable(plane_reference)

        plane = (
            0.0,
            0.0,
            -200.0,
            1.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0
        )
        catia_plane = plane_measurable.get_plane()
        catia_plane = round_tuple(catia_plane, 6)

        assert plane == catia_plane


def test_get_point():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_points)
        point1 = hybrid_body.hybrid_shapes.item(3)
        point1_reference = part.create_reference_from_object(point1)
        point1_measurable = spa_workbench.get_measurable(point1_reference)

        point = (
            100,
            100,
            0,
        )
        catia_point = point1_measurable.get_point()
        catia_point = round_tuple(catia_point, 6)

        assert point == catia_point


def test_get_points_on_axis():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_cylinders)
        cylinder = hybrid_body.hybrid_shapes.item(1)
        cylinder_reference = part.create_reference_from_object(cylinder)
        cylinder_measurable = spa_workbench.get_measurable(cylinder_reference)

        cylinder = (
            100,
            100,
            50,
            100,
            100,
            100,
            100,
            100,
            0,
        )
        catia_cylinder = cylinder_measurable.get_points_on_axis()
        catia_cylinder = round_tuple(catia_cylinder, 6)

        assert cylinder == catia_cylinder


def test_get_points_on_curve():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_lines)
        line1 = hybrid_body.hybrid_shapes.item(1)
        line1_reference = part.create_reference_from_object(line1)
        line1_measurable = spa_workbench.get_measurable(line1_reference)

        points_on_curve = (
            0.0,
            0.0,
            0.0,
            50.0,
            50.0,
            0,
            100.0,
            100.0,
            0,
        )
        catia_points_on_curve = line1_measurable.get_points_on_curve()
        catia_points_on_curve = round_tuple(catia_points_on_curve, 6)

        assert points_on_curve == catia_points_on_curve


def test_volume():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        bodies = part.bodies
        body = bodies.item(1)

        reference = part.create_reference_from_object(body)
        measurable = spa_workbench.get_measurable(reference)

        volume = 0.0005
        catia_volume = measurable.volume

        assert volume == round(catia_volume, 6)


def test_centre_of_gravity():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        bodies = part.bodies
        body = bodies.item(1)

        reference = part.create_reference_from_object(body)
        measurable = spa_workbench.get_measurable(reference)

        gx = 50
        gy = 50
        gz = 25

        centre_of_gravity = measurable.get_cog()

        assert (gx, gy, gz) == (
            round(centre_of_gravity[0], 6),
            round(centre_of_gravity[1], 6),
            round(centre_of_gravity[2], 6))


def test_angle():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document
        spa_workbench = document.spa_workbench()

        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_arcs)
        arc = hybrid_body.hybrid_shapes.item(1)
        arc_reference = part.create_reference_from_object(arc)
        arc_measurable = spa_workbench.get_measurable(arc_reference)

        angle = 360
        catia_angle = arc_measurable.angle

        assert angle == catia_angle


def test_center():
    with CATIADocHandler(cat_part_measurable) as caa:
        document = caa.document

        spa_workbench = document.spa_workbench()
        part = document.part
        hybrid_bodies = part.hybrid_bodies
        hybrid_body = hybrid_bodies.get_item_by_name(geom_set_arcs)
        arc = hybrid_body.hybrid_shapes.item(1)

        arc_reference = part.create_reference_from_object(arc)
        arc_measurable = spa_workbench.get_measurable(arc_reference)
        catia_center = arc_measurable.get_center()

        center = (0, 100, 0)
        assert center == catia_center
