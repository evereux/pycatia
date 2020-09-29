#! /usr/bin/python3.6

"""

    Example 26:

    Prompt the user to select a product and get it's bounding box parameters

    .. warning:
        Currently there must be NO other existing Measure Inertias saved
        ANYWHERE in your product tree as these may be returned and not
        product you have selected.

"""

import win32con
import win32gui
from pycatia import catia


def close_inertia_window():
    # for future debugging from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    # def winEnumHandler(hwnd, ctx):
    #     if win32gui.IsWindowVisible(hwnd):
    #         print(hex(hwnd), win32gui.GetWindowText(hwnd))
    #
    # win32gui.EnumWindows(winEnumHandler, None)

    handle = win32gui.FindWindow(None, "Measure Inertia")
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


caa = catia()
document = caa.active_document
product = document.product()
selection = document.selection
selection.clear()

c = True
while c is True:
    input("Selection product to measure.\nPress <ENTER> when selection made.")
    selection = document.selection

    caa.start_command("Measure Inertia")
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

    if prompt.lower()[0] == 'n':
        c = False
    else:
        c = True
