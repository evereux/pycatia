#! /usr/bin/python3.7

"""

    Example 12:

    Access the CATIA COM object with a .CATPart open and and display
    each parameter along with its name, value and its associated parameter set.

"""

from pycatia import catia

# from pycatia.knowledge_interfaces import BoolParam


documents = catia.documents
documents.open(r'tests\CF_Part_3.CATPart')

document = catia.active_document

part = document.part()

# gets part parameters
part_parameters = part.parameters

# create parameter to activate pocket
part_parameters.create_boolean("Activate_Pocket", True)

# find and assign parameters
pocket_activity = part_parameters.item("Activate_Pocket")

# gets RootParameterSet inside of parameters
root_parameter_set = part_parameters.root_parameter_set
# ParameterSet(name="Parameters")

# gets ParameterSets inside of RootParameterSet
parameter_sets = root_parameter_set.parameter_sets

# gets all parameter sets  inside of parameter_sets
sub_parameter_set = parameter_sets.items()
# [ParameterSet(name="Parameters_Pad"), ParameterSet(name="Parameters_Pocket")]

for parm_set in sub_parameter_set:
    print(parm_set.name)
    sub_parms = parm_set.all_parameters
    for sub_item in sub_parms:
        print(sub_item)
        print("Parameter name: {} - Value: {}".format(sub_item.name, sub_item.value))
    print()

# ParameterSet name: Parameters_Pad
# Parameter name: CF_Part_3\Parameters_Pad\Width| value: 120.0
# Parameter name: CF_Part_3\Parameters_Pad\Length| value: 60.0
# Parameter name: CF_Part_3\Parameters_Pad\Height| value: 10.0

# ParameterSet name: Parameters_Pocket
# Parameter name: CF_Part_3\Parameters_Pocket\Width| value: 30.0
# Parameter name: CF_Part_3\Parameters_Pocket\Length| value: 15.0
# Parameter name: CF_Part_3\Parameters_Pocket\Height| value: 10.0
# -----------------------------------------------------------------


# gets part relations
part_relations = part.relations
# create the parameter to which you want to assign a formula
sketch_pocket_activity = part_parameters.item("Sketches\\Sketch_Pocket\\Activity")
object_pocket_activity = part_parameters.item("PartBody\\Pocket.1\\Activity")

# create the formula to combine the sketch and pocket activity with the parameter <pocket_activity>
part_relations.create_formula("Activity_Sketch_Pocket",
                              "Checks weather the Pocket should be activated or not", sketch_pocket_activity,
                              pocket_activity.name)

part_relations.create_formula("Activity_Object_Pocket",
                              "Checks weather the Pocket should be activated or not", object_pocket_activity,
                              pocket_activity.name)

part.update()

# remove created formula
# -----------------------------------------------------------------
# part_relations.remove("Activity_Sketch_Pocket")
# part_relations.remove("Activity_Object_Pocket")
