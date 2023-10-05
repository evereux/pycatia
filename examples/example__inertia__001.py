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
from pycatia.mec_mod_interfaces.part import Part
from pycatia.space_analyses_interfaces.inertia import Inertia

__author__ = '[ptm] by plm-forum.ru'
__status__ = 'alpha'

# initialise the catia automation application
caa = catia()
documents = caa.documents
# get the active document
document = caa.active_document
# for IDE autocompletition
part = Part(document.part.com_object)
part.update()

# get the Bodies() collection
bodies = part.bodies

body = part.main_body

# or get the body by name
# body_by_name = bodies.get_item_by_name('AnotherPartBody')

# initialise the spa workbench
spa_workbench = document.spa_workbench()

# create a reference to measure.
reference = part.create_reference_from_object(part)
measurable = spa_workbench.get_measurable(reference)
spa_i = spa_workbench.inertias

#interia = spa_i.add(body)
# for IDE autocompletition
interia=Inertia(spa_i.add(body).com_object)

density = interia.density
print(f'old density={density}')
# set new density to this interia
# interia.density=7800
# print(f'New density=7800\n'
#       f'Density={interia.density}')

print(f'Mass={interia.mass}')


interia_matrix = interia.get_inertia_matrix()
print('Interia matrix\n'
      f'Ixx={interia_matrix[0]}\n'
      f'Ixy={interia_matrix[1]}\n'
      f'Ixz={interia_matrix[2]}\n'
      f'Iyx={interia_matrix[3]}\n'
      f'Iyy={interia_matrix[4]}\n'
      f'Iyz={interia_matrix[5]}\n'
      f'Izx={interia_matrix[6]}\n'
      f'Izy={interia_matrix[7]}\n'
      f'Izz={interia_matrix[8]}')

principal_axis = interia.get_principal_axes()
print('Principal axis\n'
      f'A1x={principal_axis[0]}\n'
      f'A2x={principal_axis[1]}\n'
      f'A3x={principal_axis[2]}\n'
      f'A1y={principal_axis[3]}\n'
      f'A2y={principal_axis[4]}\n'
      f'A3y={principal_axis[5]}\n'
      f'A1z={principal_axis[6]}\n'
      f'A2z={principal_axis[7]}\n'
      f'A3z={principal_axis[8]}')

principal_moments = interia.get_principal_moments()
print('Principal moments\n'
      f'M1={principal_moments[0]}\n'
      f'M2={principal_moments[1]}\n'
      f'M3={principal_moments[2]}')

GOC = interia.get_cog_position()
print('center of gravity\n'
      f'X={GOC[0]}\n'
      f'Y={GOC[1]}\n'
      f'Z={GOC[2]}')
