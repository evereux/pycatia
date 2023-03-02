
"""
    Example - Measure interia in Part:
    Catia must be running and Part documetn is open
    Part must be consider a some solid geometry in MainBody(default is PartBody)
    example is not measure interia all part,only main body.
    options for measure main body is not use
    granularity_mode sets to 1 for all bodies
    and interia=spa_i.add(body) change to interia=spa_i.add(part)
    in this case u can granularity_mode sets to 1 for all bodies
    or granularity_mode sets to 0 for main body
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia

# initialise the catia automation application
caa = catia()
documents = caa.documents

# get the active document
document = caa.active_document
# >>> print(document.path())
# >>> C:\Users\evereux\python\projects\pycatia\tests\CF_catia_measurable_part.CATPart

# get the Part() object.
part = document.part
part.update()

# get the Bodies() collection
bodies = part.bodies

# gets first Body()
body =part.main_body
# >>> print(body)
# >>> Body(name="PartBody")

# or get the body by name
# >>> body_by_name = bodies.get_item_by_name('AnotherPartBody')
# >>> print(body)
# >>> Body(name="AnotherPartBody")

# initialise the spa workbench
spa_workbench = document.spa_workbench()
# create a reference to measure.
reference = part.create_reference_from_object(part)

measurable = spa_workbench.get_measurable(reference)
spa_i=spa_workbench.inertias
interia=spa_i.add(body)

density=interia.density
print(f"old density={density}")
# set new density to this interia
# interia.density=7800
# print(f"New density=7800")
# print(f"Density={interia.density}")

print(f"Mass={interia.mass}")


interia_matrix=interia.get_inertia_matrix()
print("Interia matrix")
print(f"Ixx={interia_matrix[0]}")
print(f"Ixy={interia_matrix[1]}")
print(f"Ixz={interia_matrix[2]}")
print(f"Iyx={interia_matrix[3]}")
print(f"Iyy={interia_matrix[4]}")
print(f"Iyz={interia_matrix[5]}")
print(f"Izx={interia_matrix[6]}")
print(f"Izy={interia_matrix[7]}")
print(f"Izz={interia_matrix[8]}")

principal_axis=interia.get_principal_axes()
print("Principal axis")
print(f"A1x={principal_axis[0]}")
print(f"A2x={principal_axis[1]}")
print(f"A3x={principal_axis[2]}")
print(f"A1y={principal_axis[3]}")
print(f"A2y={principal_axis[4]}")
print(f"A3y={principal_axis[5]}")
print(f"A1z={principal_axis[6]}")
print(f"A2z={principal_axis[7]}")
print(f"A3z={principal_axis[8]}")

principal_moments=interia.get_principal_moments()
print("Principal moments")
print(f"M1={principal_moments[0]}")
print(f"M2={principal_moments[1]}")
print(f"M3={principal_moments[2]}")

GOC=interia.get_cog_position()
print("center of gravity")
print(f"X={GOC[0]}")
print(f"Y={GOC[1]}")
print(f"Z={GOC[2]}")
# close current document
# document.close()
# catia close
# caa.quit()