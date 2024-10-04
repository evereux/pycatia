#! /usr/bin/python3.9

"""

    Example - Visual Properties - 001

    Description:
        Searching and changing visual properties. Find all Red points and make them Pink.

    Requirements:
        - CATIA running with an open part document containing some points.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia

caa = catia()
document = caa.active_document
selection = document.selection
selection.search("CATGmoSearch.Point.Color='(255,0,0)',in")

# how many items have been found?
caa.logger.info(f"Found {selection.count2} items.")

# to loop through the items
for i in range(selection.count2):
    index = i + 1
    item = selection.item2(i + index)
    type = item.type
    value = item.value
    reference = item.reference
    print(item, type, value, reference)

# change the colour of all the selection red points to blue.
vis_properties = selection.vis_properties
real_colour = vis_properties.get_real_color()
s, r, g, b = real_colour
# s represents the enum cat_vis_property_status.
# >>> cat_vis_property_status[s]
# catVisPropertyDefined # this means all colours in selection are the same.
# >>> cat_vis_property_status[s]
# catVisPropertyUnDefined # this means all colours in selection are NOT the same.
# r, g, b are the red, green blue values returned by get_real_color since we
# searched for all red points r == 255, g == 0 and b == 0.

# Let's change all the selected red points pink with no inheritance.
vis_properties.set_real_color(255, 128, 255, 0)
