from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part import Part


def get_ref_origin_elements(part: Part) -> tuple[Reference, Reference, Reference]:
    """

    :param Part part:
    :return: tuple[Reference, Reference, Reference]
    """

    origin_elements = part.origin_elements
    plane_xy = origin_elements.plane_xy
    plane_yz = origin_elements.plane_yz
    plane_zx = origin_elements.plane_zx
    ref_plane_xy = part.create_reference_from_object(plane_xy)
    ref_plane_yz = part.create_reference_from_object(plane_yz)
    ref_plane_zx = part.create_reference_from_object(plane_zx)

    return (ref_plane_xy, ref_plane_yz, ref_plane_zx)
