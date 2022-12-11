#! /usr/bin/python3.6

from pycatia import CATIADocHandler


def test_point_between():
    co_ord_1 = (0, 0, 0)
    co_ord_2 = (100, 0, 0)
    r = (50, 0, 0)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        cg_points = hybrid_bodies.add()

        point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
        point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])

        cg_points.append_hybrid_shape(point_1)
        cg_points.append_hybrid_shape(point_2)

        point_between = hsf.add_new_point_between(point_1, point_2, 0.5, 0)

        cg_points.append_hybrid_shape(point_between)

        part.update()

        assert point_between.get_coordinates() == r


def test_point_center():
    length = 100
    co_ord_1 = (0, 0, 0)
    co_ord_2 = (length, 0, 0)
    center = (length / 2, 0, 0)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        gs_new = hybrid_bodies.add()

        point = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])

        gs_new.append_hybrid_shape(point)

        xy_plane = part.origin_elements.plane_xy

        circle = hsf.add_new_circle_ctr_rad(point, xy_plane, True, 50)

        gs_new.append_hybrid_shape(circle)

        point_center = hsf.add_new_point_center(circle)
        gs_new.append_hybrid_shape(point_center)

        part.update()

        assert point_center.get_coordinates() == point.get_coordinates()


def test_point_coord():
    co_ord = (0, 10, 100)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        cg_points = hybrid_bodies.add()

        point_1 = hsf.add_new_point_coord(co_ord[0], co_ord[1], co_ord[2])
        cg_points.append_hybrid_shape(point_1)

        part.update()

        assert point_1.get_coordinates() == co_ord


def test_point_coord_reference():
    co_ord = (0.0, 10.0, 100.0)
    r = tuple([i + i for i in co_ord])

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        cg_points = hybrid_bodies.add()

        org_point = hsf.add_new_point_coord(co_ord[0], co_ord[1], co_ord[2])
        cg_points.append_hybrid_shape(org_point)
        point_1 = hsf.add_new_point_coord_with_reference(co_ord[0], co_ord[1], co_ord[2], org_point)
        cg_points.append_hybrid_shape(point_1)

        part.update()

        assert point_1.get_coordinates() == r


def test_point_datum():
    # todo: write this test.
    pass


def test_point_explicit():
    # todo: write this test.
    pass


def test_point_on_curve():
    length = 100
    co_ord_1 = (0, 0, 0)
    co_ord_2 = (length, 0, 0)
    center = (length / 2, 0, 0)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        gs_new = hybrid_bodies.add()

        point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
        point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])

        gs_new.append_hybrid_shape(point_1)
        gs_new.append_hybrid_shape(point_2)

        line = hsf.add_new_line_pt_pt(point_1, point_2)

        gs_new.append_hybrid_shape(line)

        part.update()

        line_ref = part.create_reference_from_object(line)
        direction = hsf.add_new_direction(line_ref)

        point_center = hsf.add_new_point_on_curve_along_direction(line, length / 2, 0, direction)

        gs_new.append_hybrid_shape(point_center)

        part.update()

        assert point_center.get_coordinates() == center


def test_point_curve_along_direction():
    # todo: write this test.
    pass


def test_point_curve_from_distance():
    # todo: write this test.
    pass


def test_point_curve_from_percent():
    # todo: write this test.
    pass


def test_point_on_plane():
    co_ord_1 = (250.0, 100.0)

    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        gs_new = hybrid_bodies.add()

        xy_plane = part.origin_elements.plane_xy
        point = hsf.add_new_point_on_plane(xy_plane, co_ord_1[0], co_ord_1[1])

        gs_new.append_hybrid_shape(point)

        part.update()

        assert point.get_coordinates() == (co_ord_1[0], co_ord_1[1], 0.0)


def test_point_on_plane_reference():
    co_ord_1 = (250, 100, 0)
    co_ord_2 = (100, 200)
    r = (co_ord_1[0] + co_ord_2[0], co_ord_1[1] + co_ord_2[1], co_ord_1[2])
    with CATIADocHandler(new_document="Part") as caa:
        document = caa.document
        part = document.part
        hsf = part.hybrid_shape_factory

        hybrid_bodies = part.hybrid_bodies
        gs_new = hybrid_bodies.add()

        xy_plane = part.origin_elements.plane_xy
        org_point = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])

        gs_new.append_hybrid_shape(org_point)

        point = hsf.add_new_point_on_plane_with_reference(xy_plane, org_point, co_ord_2[0], co_ord_2[1])

        gs_new.append_hybrid_shape(point)

        part.update()

        assert point.get_coordinates() == r


def test_point_on_surface():
    # todo: write this test.
    pass


def test_point_on_surface_reference():
    # todo: write this test.
    pass


def test_point_tangent():
    # todo: write this test.
    pass
