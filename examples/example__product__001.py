#! /usr/bin/python3.9

"""

    Example - Product - 001

    Description:
        Assembly Design: Reorder a Product tree alphabetically. The Product
        shall already be loaded.

        Sort a product tree like this:

            Product1
                |- Product2 (Product2.1)
                |- Product3 (Product3.1)
                |- Product4 (Product4.1)
                |- Part1 (Part1.1)
                |- Part3 (Part3.1)
                |- Part2 (Part2.1)
                |- Product2 (Product2.2)
                |- Product2 (Product2.3)
                |- Part3 (Part3.2)
                |- Part3 (Part3.3)

        To this:

            Product1
                |- Part1 (Part1.1)
                |- Part2 (Part2.1)
                |- Part3 (Part3.1)
                |- Part3 (Part3.2)
                |- Part3 (Part3.3)
                |- Product2 (Product2.1)
                |- Product2 (Product2.2)
                |- Product2 (Product2.3)
                |- Product3 (Product3.1)
                |- Product4 (Product4.1)

        Please note the use of sleep = 0.25. This is because the
        caa.start_command('Graph tree reordering') isn't thread locking so the
        script continues to run while the "Graph Tree" is launching. This can
        cause issues for pywinauto finding the windows it needs.

    Requirements:
        - pywinauto installed (pip install pywinauto).
        - An open product document with children that need sorting.
        
    Warnings:
        With regards to pycatia this example only shows how to select the root
        product. The rest is handled by pywinauto. _https://pywinauto.github.io/

        You will need to manually install package pywinauto to run this script.
        Also, the placement of `from pywinauto import Desktop` is important.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

import time
from typing import Optional

from pywinauto import Desktop
from pywinauto.controls.win32_controls import ButtonWrapper
from pywinauto.controls.win32_controls import ListBoxWrapper

from pycatia import catia
from pycatia.product_structure_interfaces.product_document import ProductDocument

lang = 'EN'  # only EN and DE currently supported, more translations welcomed.
sleep = 0.25

text_translations = {
    'OK': {
        'EN': 'OK',
        'DE': 'OK',
    },
    'Apply': {
        'EN': 'Apply',
        'DE': 'Anwenden',
    },
    'Move Up': {
        'EN': 'Move Up',
        'DE': 'Nach oben verschieben',
    },
    'Move Down': {
        'EN': 'Move Down',
        'DE': 'Nach unten verschieben',
    },
    'List box': {
        'EN': 'ListProd',
        'DE': 'ListProd',
    },
    'graph_tree_cmd': {
        'EN': 'Graph tree Reordering',
        'DE': 'Neuordnung des Grafikbaums',
    },
    'graph_tree_window_name': {
        'EN': 'Graph tree reordering',
        'DE': 'Neuordnung des Grafikstrukturbaums'
    }
}


def get_window_text(window_text_translations: dict, lang):
    """

    :param dict window_text_translations:
    :param str lang:
    :return: dict
    """
    _window_text = {}

    for label in window_text_translations:
        translation = window_text_translations[label][lang]
        _window_text[label] = translation

    return _window_text


window_text = get_window_text(text_translations, lang)

caa = catia()
product_document: ProductDocument = caa.active_document
product = product_document.product

selection = product_document.selection
selection.clear()
selection.add(product)
caa.start_command(window_text['graph_tree_cmd'])
# that's it for pycatia.

time.sleep(sleep)

windows = Desktop().windows()

graph_window = None
for window in windows:
    if window_text['graph_tree_window_name'] in window.window_text():
        graph_window = window

if not graph_window:
    raise AttributeError("Could not find Graph tree reordering window.")

btn_move_up: Optional[ButtonWrapper] = None
btn_move_down: Optional[ButtonWrapper] = None
btn_ok: Optional[ButtonWrapper] = None
btn_apply: Optional[ButtonWrapper] = None
list_box: Optional[ListBoxWrapper] = None

# loop through Graph tree reordering window and find the buttons we need and
# the list_box.
for child in graph_window.children():
    if child.window_text() == window_text['OK']:
        btn_ok = child
    if child.window_text() == window_text['Apply']:
        btn_apply = child
    if child.window_text() == window_text['Move Up']:
        btn_move_up = child
    if child.window_text() == window_text['Move Down']:
        btn_move_down = child
    if child.window_text() == window_text['List box']:
        list_box = child

btn_list = [btn_move_up, btn_ok, btn_apply, list_box]
if not any(btn_list):
    raise ValueError(f'One of the buttons has not been found. {btn_list}')

# create a text list of the items in the list box and sort them.
tree_items = []
for text in list_box.item_texts():  # type: ignore
    tree_items.append(text)
tree_items.sort()

# reorder the items in the tree
for i, value in enumerate(tree_items):
    # select the item in list box
    list_box.select(value)  # type: ignore
    # find it's current position in the list_box
    current_position = list_box.item_texts().index(value)  # type: ignore
    target_position = i
    # current_position - target position is the number of times to click the
    # move up button.
    for _ in range(current_position - target_position):
        btn_move_up.click()  # type: ignore

btn_apply.click()  # type: ignore
btn_ok.click()  # type: ignore
