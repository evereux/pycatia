import pytest

from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.hybrid_shape_interfaces.plane import Plane
from tests.conftest import application
from tests.source_files import cat_part_measurable


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_get_first_axis(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes
    plane_1 = Plane(hybrid_shapes.item('Plane.Offset').com_object)
    first_axis = plane_1.get_first_axis()

    assert (first_axis == (1.0, 0.0, 0.0))


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_get_origin(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes
    plane_1 = Plane(hybrid_shapes.item('Plane.TwoLines').com_object)
    origin = plane_1.get_origin()

    assert (origin == (50.000000000000014, 50.000000000000014, 0.0))


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_get_position(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes
    plane_1 = Plane(hybrid_shapes.item('Plane.Offset').com_object)
    position = plane_1.get_position()

    assert (position == (0.0, 0.0, 0.0))


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_get_second_axis(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes
    plane_1 = Plane(hybrid_shapes.item('Plane.Offset').com_object)
    position = plane_1.get_position()

    assert (position == (0.0, 0.0, 0.0))


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_is_a_ref_plane(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes
    plane_1 = Plane(hybrid_shapes.item('Plane.Offset').com_object)
    is_ref_plane = plane_1.is_a_ref_plane()

    assert (is_ref_plane == 1)


# def test_plane_put_first_axis():
#     # todo: write test
#     pass
#
#
# def test_plane_put_origin():
#     # todo: write test
#     pass
#
#
# def test_plane_put_second_axis():
#     # todo: write test
#     pass

@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_remove_position(document_open):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes

    plane_1 = Plane(hybrid_shapes.item('Plane.TwoLines').com_object)

    position = (1.0, 1.0, 0.0)
    plane_1.set_position(*position)
    part.update()
    plane_1.remove_position()

    assert (plane_1.get_position() == (0.0, 0.0, 0.0))


@pytest.mark.parametrize('file_name', [cat_part_measurable])
def test_plane_set_position(document_open_test_close):
    part_document: PartDocument = application.active_document
    part = part_document.part
    hybrid_bodies = part.hybrid_bodies
    hb_construction_planes = hybrid_bodies.item('construction_planes')
    hybrid_shapes = hb_construction_planes.hybrid_shapes
    plane_1 = Plane(hybrid_shapes.item('Plane.TwoLines').com_object)
    position = (1.0, 1.0, 0.0)
    plane_1.set_position(*position)
    location = plane_1.get_position()

    assert (location == (position))
