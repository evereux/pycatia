#! /usr/bin/python3.9

from pycatia import CATIADocHandler
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part_document import PartDocument


def test_circle2_points_rad():
    # todo: add test fixture
    pass


def test_circle3_points():
    cord_1 = (40, 40, 0)
    cord_2 = (130, 70, 0)
    cord_3 = (210, 50, 0)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        assert document is not None

        part = PartDocument(document.com_object).part
        hsf = part.hybrid_shape_factory

        hbs = part.hybrid_bodies
        gs_new = hbs.add()

        points = hsf.add_new_point_coords([cord_1, cord_2, cord_3])
        gs_new.append_hybrid_shapes(points)

        circle = hsf.add_new_circle3_points(points[0], points[1], points[2])
        gs_new.append_hybrid_shape(circle)

        part.update()

        spa = document.spa_workbench()
        measurable = spa.get_measurable(Reference(circle.com_object))

        assert 158.597 == round(measurable.radius, 3)


def test_circle_bitangent_point():
    # todo: add test fixture
    pass


def test_circle_bitangent_radius():
    # todo: add test fixture
    pass


def test_circle_center_axis():
    # todo: add test fixture
    pass


def test_circle_center_axis_with_angles():
    # todo: add test fixture
    pass


def test_circle_center_tangent():
    # todo: add test fixture
    pass


def test_circle_ctr_pt():
    # todo: add test fixture
    pass


def test_circle_ctr_pt_with_angles():
    # todo: add test fixture
    pass


def test_circle_ctr_rad():
    # todo: add test fixture
    pass


def test_circle_ctr_rad_with_angles():
    # todo: add test fixture
    pass


def test_circle_datum():
    # todo: add test fixture
    pass


def test_circle_tritangent():
    # todo: add test fixture
    pass
