#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

"""
Example - example__selection__003
    Prompt to select geometry
    returns type of geometry using SPAworkbench get_measurable
    and hybrid shape factory get_geometrical_feature_type
"""


from pycatia.mec_mod_interfaces.part import Part
from pycatia import catia
from pycatia.exception_handling.exceptions import CATIAApplicationException

__author__ = '[ptm] by plm-forum.ru'
__status__ = 'alpha'

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

# import headers
try:
    caa = catia()
    documents = caa.documents
    document = caa.active_document
except CATIAApplicationException as e:
    print(e.message)
    print('CATIA not started or document not ' +
          'opened or started several CATIA sessions')
    print('Press any key to exit...')
    sys.exit(e.message)
if document.is_part:
    # need to autocomplete
    part_document = Part(document.part.com_object)
    selection = document.selection

    try:
        part_document.update()
    except CATIAApplicationException as e:
        print(e.message)
        print('Part document must be without errors!')
        print('Press any key to exit...')
        sys.exit('Part document must be without errors!')

hsf = part_document.hybrid_shape_factory

spa = document.spa_workbench()

# promt user select any object
caa.message_box('Select a anyobjects.\n'
                'You can select in tree or graphical area\n'
                'If you select in graphical area script has some error',
                0, title='Selection promt')

# type geom filter
sFilter = ('ZeroDim',
           'MonoDim',
           'MonoDimInfinite',
           'RectilinearMonoDim',
           'RectilinearMonoDimInfinite',
           'BiDim',
           'BiDimInfinite',
           'PlanarBiDim',
           'PlanarBiDimInfinite',
           'CylindricalBiDim',
           'TriDim'
           )

sStatus = selection.select_element2(sFilter, 'select a HybridBody', True)
if sStatus == 'Cancel':
    sys.exit('HybridBodies not select')

sel_name = selection.item2(1).value.name
parent_name = selection.item2(1).value.parent.name
type_sel = selection.item2(1).type


ref_hb = selection.item2(1).reference

try:
    int_geom_add_type = spa.get_measurable(ref_hb).geometry_name
    print(int_geom_add_type)
    match int_geom_add_type:
        case 0:
            ADD_GEOM_TYPE = 'Unknown'
        case 1:
            ADD_GEOM_TYPE = 'Other'
        case 2:
            ADD_GEOM_TYPE = 'Volume'
        case 3:
            ADD_GEOM_TYPE = 'Surface'
        case 4:
            ADD_GEOM_TYPE = 'Cylinder'
        case 5:
            ADD_GEOM_TYPE = 'Sphere'
        case 6:
            ADD_GEOM_TYPE = 'Cone'
        case 7:
            ADD_GEOM_TYPE = 'Plane'
        case 8:
            ADD_GEOM_TYPE = 'Curve'
        case 9:
            ADD_GEOM_TYPE = 'Circle'
        case 10:
            ADD_GEOM_TYPE = 'Line'
        case 11:
            ADD_GEOM_TYPE = 'Point'
        case 12:
            ADD_GEOM_TYPE = 'Axis System'
except:
    ADD_GEOM_TYPE = None
try:
    int_geom_base_type = hsf.get_geometrical_feature_type(ref_hb)

    match int_geom_base_type:
        case 0:
            BASE_GEOM_TYPE = 'Unknown'
        case 1:
            BASE_GEOM_TYPE = 'Point'
        case 2:
            BASE_GEOM_TYPE = 'Curve'
        case 3:
            BASE_GEOM_TYPE = 'Line'
        case 4:
            BASE_GEOM_TYPE = 'Circle'
        case 5:
            BASE_GEOM_TYPE = 'Surface'
        case 6:
            BASE_GEOM_TYPE = 'Plane'
        case 7:
            BASE_GEOM_TYPE = 'Solid or Volume'
except:
    BASE_GEOM_TYPE = None

text = f'selection_name={sel_name}\n'\
    f'parent={parent_name}\n'\
    f'base_geom_type={BASE_GEOM_TYPE}\n'\
    f'addition_geom_type={ADD_GEOM_TYPE}'
caa.message_box(text)
sys.exit(text)
