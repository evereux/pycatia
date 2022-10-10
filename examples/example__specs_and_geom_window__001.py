#! /usr/bin/python3.6

"""

    Example - Specs And Geometry Window - 001:

    Loop through all the CATParts in a directory and save PLAN VIEW, SIDE VIEW,
    END VIEW and ISO pngs for each part.

    The tree is turned off and the background turned white for the screen
    capture and then turned back on.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pathlib import Path

from pycatia import CATIADocHandler
from pycatia.enumeration.enumeration_types import cat_capture_format, cat_specs_and_geom_window_layout
from pycatia.in_interfaces.specs_and_geom_window import SpecsAndGeomWindow

source_folder = Path('tests/cat_files')
source_files = source_folder.glob('*.CATPart')

# create a dictionary of views to create.
x_up = (1, 0, 0)
y_up = (0, 1, 0)
z_up = (0, 0, 1)
iso = (0.577, 0.577, 0.577)

views = {'x_up': x_up, 'y_up': y_up, 'z_up': z_up, 'iso': iso}


def save_file_path(prod_part_number, prod_revision, view_type):
    """

    :param str prod_part_number:
    :param str prod_revision:
    :param str view_type:
    :return: Path
    """

    file_name = Path(Path.home(), 'Pictures', f'{prod_part_number}-{prod_revision}-{view_type}.jpg')

    return file_name


for cat_part in source_files:
    with CATIADocHandler(cat_part) as handler:
        caa = handler.catia
        document = caa.active_document
        product = document.product()
        active_window = caa.active_window
        active_viewer = active_window.active_viewer
        cameras = document.cameras

        # get current background colour
        background_colour = active_viewer.get_background_color()
        # set background color to white
        white = (1, 1, 1)
        active_viewer.put_background_color(white)

        # lets turn off the specification tree.
        specs_and_geom = SpecsAndGeomWindow(active_window.com_object)
        specs_and_geom.layout = cat_specs_and_geom_window_layout.index("catWindowGeomOnly")

        view_point_3D = active_viewer.create_viewer_3d().viewpoint_3d

        # loop through each view type.
        for view in views:
            view_point_3D.put_sight_direction(views[view])
            active_viewer.update()
            active_viewer.reframe()
            active_viewer.zoom_in()
            file_name = save_file_path(product.part_number, product.revision, view)
            active_viewer.capture_to_file(cat_capture_format.index("catCaptureFormatJPEG"), file_name)

        # reset background colour.
        active_viewer.put_background_color(background_colour)
        # bring back the specification tree.
        specs_and_geom.layout = cat_specs_and_geom_window_layout.index("catWindowSpecsAndGeom")
