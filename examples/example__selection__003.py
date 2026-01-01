"""
    Example - Selection - 003

    Description:
        Prompts user to select geometry.

        Returns type of geometry using SPAworkbench get_measurable
        and hybrid shape factory get_geometrical_feature_type

    Requirements:
        - CATPart open with geometry available to select.
"""
##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia
from pycatia import CatMeasurableName
from pycatia import CatSelectionFilter
from pycatia import GeometricalFeatureType
from pycatia.mec_mod_interfaces.part_document import PartDocument

__author__ = '[ptm] by plm-forum.ru'
__status__ = 'alpha'

application = catia()
documents = application.documents
# if the active document is a CATPart this will return a PartDocument
part_document: PartDocument = application.active_document
part = part_document.part

selection = part_document.selection
selection.clear()

hsf = part.hybrid_shape_factory

spa = part_document.spa_workbench()

# promt user select any object
mb = application.message_box('Select any HybridShape, or PartBody.\n'
                             'You can select in tree or graphical area.\n'
                             'If you select in graphical area script has some error',
                             buttons=1, title='Selection prompt')
if mb == 2:
    sys.exit('HybridShape or PartBody not selected.')

selected = selection.select_element2(tuple([csf.value for csf in CatSelectionFilter]),
                                     'Select a HybridShape or PartBody.', True)

sel_name = selection.item2(1).value.name
parent_name = selection.item2(1).value.parent.name
type_sel = selection.item2(1).type

ref_hb = selection.item2(1).reference

# I'm not sure this try / except clause is neccessary? Are there cases where
# CATIA will not report an int? :evereux
try:
    geom_add_type: int = spa.get_measurable(ref_hb).geometry_name
    add_geom_type: str = CatMeasurableName(geom_add_type).name
except:
    add_geom_type: str = CatMeasurableName(0).name

# I'm not sure this try / except clause is neccessary? Are there cases where
# CATIA will not report an int? :evereux
try:
    geom_base_type: int = hsf.get_geometrical_feature_type(ref_hb)
    base_geom_type: str = GeometricalFeatureType(geom_base_type).name
except:
    base_geom_type = GeometricalFeatureType(0).name

text = f'selection_name={sel_name}\n' \
       f'parent={parent_name}\n' \
       f'base_geom_type={base_geom_type}\n' \
       f'addition_geom_type={add_geom_type}'
application.message_box(text)
print(text)
