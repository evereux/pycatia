#! /usr/bin/python3.9
import pytest

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part_document import PartDocument
from tests.conftest import application
from tests.source_files import cat_part_measurable


def test_circle2_points_rad():
    # todo: add test fixture
    pass


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_circle3_points(document_open_test_close):
    cord_1 = (40, 40, 0)
    cord_2 = (130, 70, 0)
    cord_3 = (210, 50, 0)

    part_document: PartDocument = application.active_document
    part = part_document.part
    hsf = part.hybrid_shape_factory

    hbs = part.hybrid_bodies
    gs_new = hbs.add()

    points = hsf.add_new_point_coords([cord_1, cord_2, cord_3])
    gs_new.append_hybrid_shapes(points)

    circle = hsf.add_new_circle3_points(points[0], points[1], points[2])
    gs_new.append_hybrid_shape(circle)

    part.update()

    spa = part_document.spa_workbench()
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
