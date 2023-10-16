from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


def hide_element(document: Document, element: AnyObject):
    """

    :param document:
    :param element:
    :return:
    """

    selection = document.selection

    visual_properties = selection.vis_properties
    selection.add(element)
    visual_properties.set_show(1)
    selection.clear()
