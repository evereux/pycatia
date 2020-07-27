#! /usr/bin/python3.6

"""

    Example 20:

    Creating a message box.

    This creates a message box with the buttons abort, retry ignore and displays the Warning Query icon.

"""

from pycatia import catia

caa = catia()
buttons = 2 + 32
result = caa.message_box('Hello World!?', buttons=buttons, title='Asking a question.')
# result = 3 if the user presses Abort.
