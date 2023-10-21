#! /usr/bin/python3.9
# author: evereux
# contact: evereux@gmail.com

"""
    Create Lines Normal To Surface

    Description
    ===========
    Creates lines normal to the selected surface using all the points in the
    selected Geometrical Set (Hybrid Body).

    Lines are added to the newly created Geometrical Set "Lines".

    Requirements
    ============
    python >= 3.9
    pycatia
    CATIA V5 runnin with a part open that has a Surface and a HybridBody
    containing the Points.

    Documentation
    =============
    https://pycatia.readthedocs.io
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.cat_logger import create_logger
from pycatia.enumeration.enumeration_types import geometrical_feature_type
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.mec_mod_interfaces.part import Part

LINE_LENGTH = 20

logger = create_logger()

caa = catia()
document = caa.active_document
part = Part(document.part.com_object)
hybrid_bodies = part.hybrid_bodies
hsf = part.hybrid_shape_factory
gs_lines = hybrid_bodies.add()
gs_lines.name = ("Lines")

selection = document.selection
selection.clear()

mb = caa.message_box(
    'Please select Surface then the Geometrical Set containing the Points.',
    buttons=1,
    title='Make your selection',
)
if mb == 2:
    logger.info('You have cancelled the script. Exiting ...')
    sys.exit()

message = 'Please select Surface.'
logger.info(message)

selection.select_element2(('BiDim',), message, True)
selected = selection.item2(1)

value = selected.value
ref_surface = HybridShape(value.com_object)
selection.clear()

message = 'Please select Geometrical Set.'
selection.select_element2(('HybridBody',), message, True)
selected = selection.item2(1)

value = selected.value
ref_hybrid_body = HybridBody(value.com_object)
hybrid_shapes = ref_hybrid_body.hybrid_shapes

for shape in hybrid_shapes:
    ref_shape = part.create_reference_from_object(shape)
    type_: int = hsf.get_geometrical_feature_type(ref_shape)
    type_: str = geometrical_feature_type[type_]
    if type_ == 'Point':
        new_line = hsf.add_new_line_normal(ref_surface, ref_shape, -LINE_LENGTH, LINE_LENGTH, False)
        gs_lines.append_hybrid_shape(new_line)

part.update()
