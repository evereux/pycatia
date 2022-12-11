#! /usr/bin/python3.6

from pycatia.base_interfaces.context import CATIADocHandler
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part_document import PartDocument


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


def test_line_point_point():
    length = 100
    co_ord_1 = (0, 0, 0)
    co_ord_2 = (length, 0, 0)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        assert document is not None

        part = PartDocument(document.com_object).part
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
        spa_wb = document.spa_workbench()
        measurable = spa_wb.get_measurable(line_ref)

        assert measurable.length == length
