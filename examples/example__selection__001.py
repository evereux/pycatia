#! /usr/bin/python3.9

"""

    Example - Selection - 001

    Description:
        Prompt the user to select a product and get it's bounding box parameters

    Requirements:
        - An open product document with selectable children.        

    Warnings:
        Currently there must be NO other existing Measure Inertias saved
        ANYWHERE in your product tree as these may be returned and not
        product you have selected.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

import win32con
import win32gui

from pycatia import catia
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument

# Keep in mind, that almost all CATIA commands and windows are dependent on the UI language.
# In order for this example to work you need to set your CATIA to english, or use the correct
# translation of the command or window text.
inertia_cmd_name = "Measure Inertia"
# inertia_cmd_name = "Trägheit messen"
inertia_window_name = "Measure Inertia"
# inertia_window_name = "Trägheit messen"


def close_inertia_window():
    # for future debugging from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    # def winEnumHandler(hwnd, ctx):
    #     if win32gui.IsWindowVisible(hwnd):
    #         print(hex(hwnd), win32gui.GetWindowText(hwnd))
    #
    # win32gui.EnumWindows(winEnumHandler, None)

    handle = win32gui.FindWindow(None, inertia_window_name)
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


caa = catia()
product_document: ProductDocument = caa.active_document
product = product_document.product

selection = product_document.selection
selection.clear()

c = True
while c is True:
    input("Selection product to measure.\nPress <ENTER> when selection made.")
    selection = product_document.selection

    caa.start_command(inertia_cmd_name)
    parameters = product.parameters
    print(f"BBOx = {parameters.item('BBOx').value_as_string()}.")
    print(f"BBOy = {parameters.item('BBOy').value_as_string()}.")
    print(f"BBOz = {parameters.item('BBOz').value_as_string()}.")
    print(f"BBLx = {parameters.item('BBLx').value_as_string()}.")
    print(f"BBLy = {parameters.item('BBLy').value_as_string()}.")
    print(f"BBLz = {parameters.item('BBLz').value_as_string()}.")
    selection.clear()
    close_inertia_window()

    prompt = input("Continue? (Y/N):")

    if prompt.lower()[0] == "n":
        c = False
    else:
        c = True
