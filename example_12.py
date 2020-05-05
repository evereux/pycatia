#! /usr/bin/python3.7

"""
    Example 12:
    Access the CATIA COM object with a .CATPart open and and display each parameter along with its name, value and its associated parameter set.
"""

from pycatia.base_interfaces import CATIAApplication
from pycatia.knowledge_interfaces import Parameters
from pycatia.knowledge_interfaces import Relations
# from pycatia.knowledge_interfaces import BoolParam

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_Part_3.CATPart')

document = catia.document()

part = document.part()

# gets part parameters
part_parameters = Parameters(part.part.parameters)

# create parameter to activate pocket
part_parameters.create_boolean("Activate_Pocket", True)
# find and assign parameters
pocket_activity = part_parameters.item("Activate_Pocket")
# or create and assign it in one process with one of this tow methods
## pocket_activity = part_parameters.create_boolean("Activate_Pocket", True)
## pocket_activity = BoolParam("Activate_Pocket", True, parent=part_parameters)

# gets RootParameterSet inside of parameters
root_parameterset = part_parameters.root_parameter_set()

# gets ParameterSets inside of RootParameterSet
root_parametersets = root_parameterset.root_parameter_sets()
# root_parametersets.count() == 2

# gets every item inside of ParameterSets
root_parametersets_items = root_parametersets.get_items()
root_parametersets_items_names = root_parametersets.get_item_names()
# root_parametersets_items_names = ['Parameters_Pad', 'Parameters_Pocket']

for item in root_parametersets_items:
    print("ParameterSet name: {}".format(item.name))
    subitems = item.all_parameters()
    for subitem in subitems.all_parameter():
        print("Parameter name: {} - Value: {}".format(subitem.name, subitem.value))
    print()

# -----------------------------------------------------------------
# Output
# -----------------------------------------------------------------
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
part_relations = Relations(part.part.relations)
# create the parameter to which you want to assign a formula
sketch_pocket_activity = part_parameters.item("Sketches\\Sketch_Pocket\\Activity")
object_pocket_activity = part_parameters.item("PartBody\\Pocket.1\\Activity")

# create the formula to combine the sketch and pocket activity with the parameter <pocket_activity>
part_relations.create_formula("Activity_Sketch_Pocket",
                              "Checks weather the Pocket schould be activated or not", sketch_pocket_activity.parameter,
                              pocket_activity.formula_name)

part_relations.create_formula("Activity_Object_Pocket",
                              "Checks weather the Pocket schould be activated or not", object_pocket_activity.parameter,
                              pocket_activity.formula_name)

part.update()

# remove created formula
# -----------------------------------------------------------------
# part_relations.remove("Activity_Sketch_Pocket")
# part_relations.remove("Activity_Object_Pocket")
