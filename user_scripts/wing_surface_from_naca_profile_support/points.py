from pycatia.hybrid_shape_interfaces.hybrid_shape_factory import HybridShapeFactory
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody


def add_points(
        hsf: HybridShapeFactory,
        reference_plane: Reference,
        geometrical_set: HybridBody,
        points: list[tuple[int, int]]
):
    """

    :param HybridShapeFactory hsf:
    :param Reference reference_plane:
    :param HybridBody geometrical_set:
    :param list points:
    :return:
    """
    for coordinate in points:
        x: float = coordinate[0]
        y: float = coordinate[1]
        point_on_plane = hsf.add_new_point_on_plane(reference_plane, x, y)
        geometrical_set.append_hybrid_shape(point_on_plane)
