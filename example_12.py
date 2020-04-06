#! /usr/bin/python3.7

"""
    Example 12:
    Access the CATIA COM object with a .CATPart open and and display each parameter along with its name, value and its associated parameter set.
"""

from pycatia.base_interfaces import CATIAApplication
from pycatia.parameter_interfaces import Parameters

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_Part_3.CATPart')

document = catia.document()

part = document.part()

# gets origin parameters
part_parameters = Parameters(part.part.parameters)

# gets RootParameterSet inside of parameters
root_parameter_set = part_parameters.get_root_parameter_set()

# gets ParameterSets inside of RootParameterSet
root_parametersets = root_parameter_set.get_child_parametersets()
# root_parametersets.count() == 2

# gets every item inside of ParameterSets
root_parametersets_items = root_parametersets.get_items()
root_parametersets_items_names = root_parametersets.get_item_names()
# root_parametersets_items_names = ['Parameters_Pad', 'Parameters_Pocket']

for item in root_parametersets_items:
    print("ParameterSet name: {}".format(item.name))
    all_subitems = item.get_all_parameters()
    for subitems in all_subitems.get_all_parameter():
        print("Parameter name: {}| value: {}".format(subitems.name, subitems.value))
    print()

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
