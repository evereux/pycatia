#! /usr/bin/python3.9

"""
    Description
    ===========
    A script that uses pycatia to generate a drawing format for all sheets
    in the active drawing.

    Requirements
    ============
    python >= 3.9
    pycatia
    CATIA V5 running with a drawing open.

    Running The Script
    ==================
    > python ./user_scripts/drawing_template.py -draw-existing
"""

import argparse

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia.drafting_interfaces.drawing_view import DrawingView

from drawing_template_support.caa import caa
from drawing_template_support.caa import get_active_drawing
from drawing_template_support.border import create_border
from drawing_template_support.copyright_box import create_copyright_box
from drawing_template_support.drawing import create_drawing
from drawing_template_support.paper_size import get_sheet_size_info
from drawing_template_support.parameters import create_parameters
from drawing_template_support.purge import purge_background_view
from drawing_template_support.settings import sheet_sizes
from drawing_template_support.template_name import create_template_name
from drawing_template_support.title_block import create_title_block

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='pycatia-drawing-template',
        usage='%(prog)s [options]',
        description='Create drawing border templates using pycatia.'
    )

    # optional argument
    parser.add_argument(
        '-create-new',
        nargs='?',
    )

    parser.add_argument(
        '-draw-existing',
        action='store_true'
    )

    args = parser.parse_args()

    if args.create_new:
        if args.create_new not in sheet_sizes:
            raise ValueError('Please supply a valid sheet size.')
        sheet_size = args.create_new
        print(f'Creating new "{sheet_size}" sheet.')
        create_drawing(sheet_size)

    if args.draw_existing is True:
        drawing = get_active_drawing(caa)
        sheets = drawing.sheets
        parameters = create_parameters(drawing)
        sheet_number = 1
        for sheet in sheets:
            size_info = get_sheet_size_info(sheet)

            # !! delete everything in the background view!!
            purge_background_view(drawing, sheet)

            create_border(sheet, size_info)
            create_copyright_box(sheet, parameters)
            create_title_block(sheet, size_info, parameters, sheet_number)
            create_template_name(sheet, size_info)
            # required as colour changes are not otherwise visible.
            sheet.force_update()
            sheet_number += 1

        # activate the first sheet and main view.
        # on border creation the main view is activated after work in the
        # background view is completed yet it seems to have no effect on sheet 1.
        # I even tried looping through the sheets to activate the main view but
        # then this didn't work for sheet.2.
        for sheet in sheets:
            sheet.activate()
            main_view = DrawingView(sheet.views.get_item_by_name('Main View').com_object)
            main_view.activate()
            viewer = caa.active_window
            # fit all in.
            viewer.active_viewer.reframe()
        sheets[0].activate()
