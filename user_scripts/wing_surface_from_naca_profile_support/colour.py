from pycatia.in_interfaces.selection import Selection
from pycatia.system_interfaces.any_object import AnyObject


def set_colour(
        selection: Selection,
        element: AnyObject,
        colour: tuple[int, int, int, int]
) -> None:
    """

    :param Selection selection:
    :param AnyObject element:
    :param tuple[int, int, int, int] colour:
    :return:
    """
    red = colour[0]
    green = colour[1]
    blue = colour[2]
    inheritance = colour[3]

    selection.clear()
    selection.add(element)
    visual_properties = selection.vis_properties
    visual_properties.set_real_color(0, 255, 0, 0)
    selection.clear()
