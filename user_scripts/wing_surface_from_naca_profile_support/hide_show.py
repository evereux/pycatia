from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


def hide_the_shape(document: Document, hide_elements: list[HybridShape]) -> None:
    """

    :param Document document:
    :param HybridShape hybrid_shape:
    :return:
    """

    selection = document.selection
    visual_properties = selection.vis_properties
    for hs in hide_elements:
        selection.add(hs)
    visual_properties.set_show(1)
    selection.clear()


def hide_the_shapes(document: Document, hybrid_body: HybridBody) -> None:
    """
    Hides all the HybridShapes under HybridBody. Recursively gets all
    HybridShapes to hide.
    :param document:
    :param hybrid_body:
    :return:
    """

    hybrid_bodies = hybrid_body.hybrid_bodies
    hybrid_shapes = hybrid_body.hybrid_shapes

    hide_collection = []

    for hybrid_body in hybrid_bodies:
        hide_the_shapes(document, hybrid_body)

    for hybrid_shape in hybrid_shapes:
        hide_collection.append(hybrid_shape)

    hide_the_shape(document, hide_collection)
