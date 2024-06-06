"""
    Example - Inertia - 001:

    Catia must be running with a Part open that contains a solid object
        within the MainBody (PartBody).

    This example will only measure the inertia for the MainBody.
        Additional PartBodies will be ignored.


    Options for measure main body is not use:
    If you Granularity_mode sets to 1 for all bodies
    and interia=spa_i.add(body) change to interia=spa_i.add(part) then
    in this case you can granularity_mode sets to 1 for all bodies
    or granularity_mode sets to 0 for main body
    
    Read comment in script to change density or select another body.
    
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.space_analyses_interfaces.inertia import Inertia

__author__ = '[ptm] by plm-forum.ru'
__status__ = 'alpha'

# initialise the catia automation application
caa = catia()
# if the active document is a CATPart this will return a PartDocument
part_document: PartDocument = caa.active_document
part = part_document.part
part.update()

# get the Bodies() collection
bodies = part.bodies

body = part.main_body

# or get the body by name
# body_by_name = bodies.get_item_by_name('AnotherPartBody')

# initialise the spa workbench
spa_workbench = part_document.spa_workbench()

# create a reference to measure.
reference = part.create_reference_from_object(part)
measurable = spa_workbench.get_measurable(reference)
spa_i = spa_workbench.inertias
inertia = Inertia(spa_i.add(body).com_object)

print(f'Density={inertia.density}\n\n')
# set new density to this inertia
# inertia.density=7800
# print(f'New density=7800')
# print(f'Density={inertia.density}')

print(f'Mass={inertia.mass}\n\n')

inertia_matrix = inertia.get_inertia_matrix()
print('--------------\n'
      'Interia Matrix\n'
      '--------------\n'
      f'Ixx={inertia_matrix[0]}\n'
      f'Ixy={inertia_matrix[1]}\n'
      f'Ixz={inertia_matrix[2]}\n'
      f'Iyx={inertia_matrix[3]}\n'
      f'Iyy={inertia_matrix[4]}\n'
      f'Iyz={inertia_matrix[5]}\n'
      f'Izx={inertia_matrix[6]}\n'
      f'Izy={inertia_matrix[7]}\n'
      f'Izz={inertia_matrix[8]}\n')

principal_axis = inertia.get_principal_axes()
print('--------------\n'
      'Principal Axis\n'
      '--------------\n'
      f'A1x={principal_axis[0]}\n'
      f'A2x={principal_axis[1]}\n'
      f'A3x={principal_axis[2]}\n'
      f'A1y={principal_axis[3]}\n'
      f'A2y={principal_axis[4]}\n'
      f'A3y={principal_axis[5]}\n'
      f'A1z={principal_axis[6]}\n'
      f'A2z={principal_axis[7]}\n'
      f'A3z={principal_axis[8]}\n')

principal_moments = inertia.get_principal_moments()
print('-----------------\n'
      'Principal Moments\n'
      '-----------------\n'
      f'M1={principal_moments[0]}\n'
      f'M2={principal_moments[1]}\n'
      f'M3={principal_moments[2]}\n')

cog = inertia.get_cog_position()
print('-----------------\n'
      'Center Of Gravity\n'
      '-----------------\n'
      f'X={cog[0]}\n'
      f'Y={cog[1]}\n'
      f'Z={cog[2]}')
