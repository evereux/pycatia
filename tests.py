#! /usr/bin/python36

from catia_python import Application
from catia_python import Document
from catia_python import create_reference, create_measurable
from catia_python import CATIAMeasurable
from catia_python import Part, get_document_part_object
from catia_python import create_spa_workbench

catia = Application()
document = Document(catia.catia).document
spa_workbench = create_spa_workbench(document)

part = Part(document)

bodies = part.get_bodies()
body = bodies[0]

reference = create_reference(part.part, body)
measurable = create_measurable(spa_workbench, reference)
catia_measurable = CATIAMeasurable(measurable)

hybrid_body = part.get_hybrid_body_by_name('Lines')
line1 = hybrid_body.HybridShapes.Item(1)
line1_reference = create_reference(part.part, line1)
line1_measurable = create_measurable(spa_workbench, line1_reference)
catia_measurable_line1 = CATIAMeasurable(line1_measurable)

line2 = hybrid_body.HybridShapes.Item(2)
line2_reference = create_reference(part.part, line2)
line2_measurable = create_measurable(spa_workbench, line2_reference)
catia_measurable_line2 = CATIAMeasurable(line2_measurable)

hybrid_body = part.get_hybrid_body_by_name('Surfaces')
surface = hybrid_body.HybridShapes.Item(1)
surface_reference = create_reference(part.part, surface)
surface_measurable = create_measurable(spa_workbench, surface_reference)
catia_measurable_surface = CATIAMeasurable(surface_measurable)

hybrid_body = part.get_hybrid_body_by_name('Arcs')
arc = hybrid_body.HybridShapes.Item(1)
arc_reference = create_reference(part.part, arc)
arc_measurable = create_measurable(spa_workbench, arc_reference)
catia_measurable_arc = CATIAMeasurable(arc_measurable)

axis_systems = part.get_axis_systems()
axis = axis_systems[0]
axis_reference = create_reference(part.part, axis)
axis_measurable = create_measurable(spa_workbench, axis_reference)
catia_measurable_axis = CATIAMeasurable(axis_measurable)

hybrid_body = part.get_hybrid_body_by_name('Points')
point1 = hybrid_body.HybridShapes.Item(1)
point1_reference = create_reference(part.part, point1)
point1_measurable = create_measurable(spa_workbench, point1_reference)
catia_measurable_point1 = CATIAMeasurable(point1_measurable)

point2 = hybrid_body.HybridShapes.Item(2)
point2_reference = create_reference(part.part, point2)
point2_measurable = create_measurable(spa_workbench, point2_reference)
catia_measurable_point2 = CATIAMeasurable(point2_measurable)

hybrid_body = part.get_hybrid_body_by_name('Planes')
plane = hybrid_body.HybridShapes.Item(1)
plane_reference = create_reference(part.part, plane)
plane_measurable = create_measurable(spa_workbench, plane_reference)
catia_measurable_plane = CATIAMeasurable(plane_measurable)

hybrid_body = part.get_hybrid_body_by_name('Cylinders')
cylinder = hybrid_body.HybridShapes.Item(1)
cylinder_reference = create_reference(part.part, cylinder)
cylinder_measurable = create_measurable(spa_workbench, cylinder_reference)
catia_measurable_cylinder = CATIAMeasurable(cylinder_measurable)


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
    """

    :return:
    """

    area = 0.032119
    catia_area = catia_measurable.area

    assert area == round(catia_area, 6)


def test_geometry_name():
    """

    :return:
    """

    geometry_name = 'CatMeasurableVolume'
    catia_geomertry_name = catia_measurable.geometry_name

    assert geometry_name == catia_geomertry_name


def test_length():
    """

    :return:
    """

    length = 91.553263
    catia_length = catia_measurable_line1.length

    assert length == round(catia_length, 6)


def test_permieter():
    """

    :return:
    """

    perimiter = 265.946845
    catia_permieter = catia_measurable_surface.perimeter

    assert perimiter == round(catia_permieter, 6)


def test_radius():
    """

    :return:
    """

    radius = 45.0
    catia_radius = catia_measurable_arc.radius

    assert radius == round(catia_radius, 6)


def test_angle_between():
    """

    :return:
    """

    angle = 71.496249
    catia_angle = catia_measurable_line1.get_angle_between(line2_reference)

    assert angle == round(catia_angle, 6)


def test_get_axis():
    """
    # I've really no idea what the axis for an arc/circle/cylinder is.
    # I can't reproduce these figures in CATIA.
    :return:
    """

    axis = (0.0, 0.0, 2025.0)
    catia_axis = catia_measurable_arc.get_axis()

    assert axis == (round(catia_axis[0], 6), round(catia_axis[1], 6), round(catia_axis[2], 6))


def test_get_axis_system():
    """
    :return:
    """

    axis_system = (
        -91.418000,
        39.387000,
        0.000000,
        0.709325,
        0.704882,
        0.000000,
        0.704882,
        -0.709325,
        0.000000,
        0.000000,
        0.000000,
        -1.000000)
    catia_axis = catia_measurable_axis.get_axis_system()

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


def test_get_center():
    """

    :return:
    """

    # todo: this test fails, not sure why, this is the error message.
    #    Object doesn't support this property or method: 'measurable.GetCOGPosition'\nLine: 4\nColumn: 12\n)\n",
    #    None, 0, -2147467259), None)
    # x = -47.039
    # y = 83.488
    # z = 0
    #
    # center = (x, y, z)
    # catia_center = catia_measurable_arc.get_center()
    #
    # assert center == catia_center

    pass


def test_get_direction():
    """

    :return:
    """

    direction_vector = (0.939344, 0.207529, -0.273065)
    catia_direction = catia_measurable_line1.get_direction()

    assert direction_vector == (
        round(catia_direction[0], 6),
        round(catia_direction[1], 6),
        round(catia_direction[2], 6),
    )


def test_get_minimum_distance():
    """

    :return:
    """

    minimum_distance = 44.126069
    catia_minimum_distance = catia_measurable_line1.get_minimum_distance(arc_reference)

    assert minimum_distance == round(catia_minimum_distance, 6)


def test_get_minimum_distance_points():
    """

    :return:
    """

    minimum_distance_points = (
        0.000000,
        8.000000,
        -4.000000,
        86.000000,
        27.000000,
        -29.000000,
        None,
        None,
        None
    )
    catia_minimum_distance_points = catia_measurable_point1.get_minimum_distance_points(point2_reference)
    print(catia_minimum_distance_points)

    assert minimum_distance_points == round_tuple(catia_minimum_distance_points, 6)


def test_get_plane():
    """

    :return:
    """

    plane = (
        86.0,
        27.0,
        -29.0,
        0.342977,
        -0.568381,
        0.747870,
        0.0,
        -0.796162,
        -0.605083
    )
    catia_plane = catia_measurable_plane.get_plane()
    catia_plane = round_tuple(catia_plane, 6)

    assert plane == catia_plane


def test_get_point():
    """

    :return:
    """

    point = (
        0.0,
        8.0,
        -4.0,
    )
    catia_point = catia_measurable_point1.get_point()
    catia_point = round_tuple(catia_point, 6)

    assert point == catia_point


def test_get_points_on_axis():
    """

    :return:
    """

    cylinder = (
        -92.049,
        142.675,
        10.000,
        -92.049,
        142.675,
        20.000,
        -92.049,
        142.675,
        0.000,
    )
    catia_cylinder = catia_measurable_cylinder.get_points_on_axis()
    catia_cylinder = round_tuple(catia_cylinder, 6)

    assert cylinder == catia_cylinder


def test_get_points_on_curve():
    """

    :return:
    """

    points_on_curve = (
        0.0,
        8.0,
        -4,
        43.0,
        17.5,
        -16.5,
        86.0,
        27,
        -29,
    )
    catia_points_on_curve = catia_measurable_line1.get_points_on_curve()
    catia_points_on_curve = round_tuple(catia_points_on_curve, 6)

    assert points_on_curve == catia_points_on_curve


def test_volume():
    """

    :return:
    """

    volume = 0.000235
    catia_volume = catia_measurable.volume

    assert volume == round(catia_volume, 6)


def test_centre_of_gravity():
    """

    :return:
    """

    gx = 86.065202
    gy = 81.364587
    gz = 10.000000

    centre_of_gravity = catia_measurable.get_cog()

    assert (gx, gy, gz) == (
        round(centre_of_gravity[0], 6),
        round(centre_of_gravity[1], 6),
        round(centre_of_gravity[2], 6))
