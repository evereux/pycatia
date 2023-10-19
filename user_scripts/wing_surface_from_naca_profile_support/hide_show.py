from pycatia.in_interfaces.selection import Selection
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


def hide_the_shape(selection: Selection, hide_elements: list[HybridShape]) -> None:
    """

    :param Selection document:
    :param HybridShape hybrid_shape:
    :return:
    """

    visual_properties = selection.vis_properties
    for hs in hide_elements:
        selection.add(hs)
    visual_properties.set_show(1)
    selection.clear()


def hide_the_shapes(selection: Selection, hybrid_body: HybridBody) -> None:
    """
    Hides all the HybridShapes under HybridBody. Recursively gets all
    HybridShapes to hide.
    :param Selection selection:
    :param HybridBody hybrid_body:
    :return:
    """

    hybrid_bodies = hybrid_body.hybrid_bodies
    hybrid_shapes = hybrid_body.hybrid_shapes

    hide_collection = []

    for hybrid_body in hybrid_bodies:
        hide_the_shapes(selection, hybrid_body)

    for hybrid_shape in hybrid_shapes:
        hide_collection.append(hybrid_shape)

    hide_the_shape(selection, hide_collection)
