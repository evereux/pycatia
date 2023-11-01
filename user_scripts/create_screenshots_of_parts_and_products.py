#! /usr/bin/python3.9
# author: evereux
# contact: evereux@gmail.com

"""
    Create Screenshots Of Parts And Products

    Description
    ===========
    Loops through all the files (.CATPart and .CATProduct) of a given directory
    takes a screenshot and saves the image as BMP using the documents
    part_number and revision.

    The background is set to white. View is changed to isometric view mode,
    reframed and then zoomed in prior to screenshot being taken.

    The views modes are then reset back to normal.

    Other examples in VB / CATScript I have seen online claim to save to PNG
    but that doesn't seem possible using CATIA. In this script the image library
    Pillow is used to convert the BMP to PNG.

    Warning
    =======
    Products with broken links will currently cause the application to crash.
    Should be easy enough to mitigate this if need be though.

    Requirements
    ============
    python >= 3.9
    pycatia >= 0.6.4
    pillow (used for compressing to png)
    CATIA V5 running
    A network accessible folder with your CATIA parts and products in.

    Documentation
    =============
    https://pycatia.readthedocs.io

    More examples and user scripts can be found at:
    https://github.com/evereux/pycatia/tree/master/examples
    https://github.com/evereux/pycatia/tree/master/user_scripts
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################
import collections
from pathlib import Path
import time

from PIL import Image

from pycatia import CATIADocHandler
from pycatia.cat_logger import create_logger
from pycatia.enumeration.enumeration_types import cat_capture_format
from pycatia.enumeration.enumeration_types import cat_specs_and_geom_window_layout
from pycatia.in_interfaces.camera_3d import Camera3D
from pycatia.in_interfaces.specs_and_geom_window import SpecsAndGeomWindow
from pycatia.in_interfaces.viewer_3d import Viewer3D
from pycatia.product_structure_interfaces.product import Product

# change this to the location of where your catia files are stored.
source_cat_files = Path(Path.home(), 'catia_parts')
# location of where the images will be saved for example C:/Users/<username>/Pictures/catia_screenshots
image_save_path = Path(Path.home(), 'Pictures', 'catia_screenshots')
existing_files_warning = []

logger = create_logger()

img_files = []
# get a list of all CATParts and CATProducts in source_cat_files directory
files = (f for f in source_cat_files.glob('**/*') if f.suffix in ['.CATProduct', '.CATPart'])
for f in files:
    with CATIADocHandler(file_name=f) as handler:

        time.sleep(0.1)
        caah = handler.catia
        caah.display_file_alerts = False
        document = handler.document
        product = Product(document.product.com_object)
        Product.activate_terminal_node(product.products)

        selection = document.selection
        part_number = product.part_number
        revision = product.revision
        if revision == '':
            revision = 'NA'
        if part_number == '':
            part_number = document.name
        img_name = f'{part_number} - {revision}.bmp'
        img_save_name = Path(image_save_path, img_name)

        active_window = caah.active_window
        viewer_3d = Viewer3D(active_window.active_viewer.com_object)
        camera_3d = Camera3D(document.cameras.item(1).com_object)
        viewpoint_3d = viewer_3d.viewpoint_3d

        # turn off the specification tree
        specs_window = SpecsAndGeomWindow(active_window.com_object)

        specs_window.layout = cat_specs_and_geom_window_layout.index('catWindowGeomOnly')

        # toggle off the compass (if already off will turn it back on).
        caah.start_command('Compass')

        # set background colour to white
        default_background_colour = viewer_3d.get_background_color()
        white = (1, 1, 1)
        viewer_3d.put_background_color(white)

        # Change to ISO view mode, reframe and then zoom in.
        sight = (-1, -1, -1)
        viewpoint_3d.put_sight_direction(sight)
        viewer_3d.reframe()
        viewer_3d.zoom_in()

        # make the catia window fullscreen
        selection.clear()
        viewer_3d.full_screen = True

        # save the image file.
        # logger.info(f'Saving image file {img_save_name}.')
        if img_save_name.is_file():
            logger.warning(f'Image file: "{img_save_name}" already exists! Image will be replaced.')
            existing_files_warning.append(img_save_name)
        viewer_3d.capture_to_file(cat_capture_format.index('catCaptureFormatBMP'), str(img_save_name))
        img_files.append(img_save_name)

        # reset the catia view window settings
        viewer_3d.full_screen = False
        viewer_3d.put_background_color(default_background_colour)
        specs_window.layout = cat_specs_and_geom_window_layout.index('catWindowSpecsAndGeom')
        caah.start_command('Compass')

duplicates = [item for item, count in collections.Counter(img_files).items() if count > 1]
if len(duplicates) > 0:
    logger.warning(f'There are duplicate image file names: {duplicates}. Duplicates will be removed.')
    img_files = set(img_files)

logger.info('Compressing image files...')
for f in img_files:
    oi = Image.open(f)
    png_name = f.with_suffix('.png')
    # logger.info(f'Compressing image "{f}" to png.')
    oi.save(png_name)
    # logger.info(f'Deleting image: "{f}".')
    f.unlink()

print('The following files were over-written:')
for f in existing_files_warning:
    print(f)
