from pycatia.in_interfaces.selection import Selection
from pycatia.system_interfaces.any_object import AnyObject


def set_colour(selection: Selection, element: AnyObject, colour: tuple[int, int, int, int]) -> None:
    """

    :param Selection selection:
    :param AnyObject element:
    :param tuple[int, int, int, int] colour:
    :return:
    """
    selection.clear()
    selection.add(element)
    visual_properties = selection.vis_properties
    visual_properties.set_real_color(*colour)
    selection.clear()
