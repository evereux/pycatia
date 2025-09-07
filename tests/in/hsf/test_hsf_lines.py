#! /usr/bin/python3.9
import pytest

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part_document import PartDocument
from tests.conftest import application
from tests.source_files import cat_part_measurable


def test_line_angle():
    pass


def test_line_bi_tangent():
    pass


def test_line_bisecting():
    pass


def test_line_explicit():
    pass


def test_line_normal():
    pass


def test_line_point_direction():
    pass


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_line_point_point(document_open_test_close):
    length = 100
    co_ord_1 = (0, 0, 0)
    co_ord_2 = (length, 0, 0)

    part_document: PartDocument = application.active_document
    part = part_document.part
    hsf = part.hybrid_shape_factory

    hybrid_bodies = part.hybrid_bodies
    gs_new = hybrid_bodies.add()

    point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
    point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])

    gs_new.append_hybrid_shape(point_1)
    gs_new.append_hybrid_shape(point_2)

    line = hsf.add_new_line_pt_pt(Reference(point_1.com_object), Reference(point_2.com_object))

    gs_new.append_hybrid_shape(line)

    part.update()

    line_ref = part.create_reference_from_object(line)
    spa_wb = part_document.spa_workbench()
    measurable = spa_wb.get_measurable(line_ref)

    assert measurable.length == length
