#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSymmetry(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape symmetry feature object.Role: To access
                | the data of the symmetry shape feature object. The data includes:Use
                | the CATIAHybridShapeFactory to create HybridShapeFeature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_symmetry = com_object     

    @property
    def creation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreationMode
                | o Property CreationMode(    ) As
                | 
                | Returns or sets the creation mode(creation or modification).
                | Legal values: True if the result is a creation feature and
                | False if the result is a modification feature. 
                |
                | Example:
                | This
                | example sets that the mode of the hybShpSymmetry hybrid
                | shape symmetry to creation hybShpSymmetry.CreationMode =
                | True

        :return:
        """
        return self.hybrid_shape_symmetry.CreationMode

    @creation_mode.setter
    def creation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_symmetry.CreationMode = value 

    @property
    def elem_to_symmetry(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToSymmetry
                | o Property ElemToSymmetry(    ) As
                | 
                | Returns or sets the element to transform. 
                |
                | Example:
                | This
                | example retrieves in Elem the element to transform for the
                | Symmetry hybrid shape feature. Dim Elem As Reference Set
                | Elem = Symmetry.ElemToSymmetry

        :return:
        """
        return self.hybrid_shape_symmetry.ElemToSymmetry

    @elem_to_symmetry.setter
    def elem_to_symmetry(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_symmetry.ElemToSymmetry = value 

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Reference
                | o Property Reference(    ) As
                | 
                | Returns or sets the reference element.This element can be a
                | point, a line or a plane. Sub-element(s) supported (see
                | object): , or . 
                |
                | Example:
                | This example retrieves in Ref the
                | reference element for the Symmetry hybrid shape feature. Dim
                | Ref As Reference Set Ref = Symmetry.Reference

        :return:
        """
        return self.hybrid_shape_symmetry.Reference

    @reference.setter
    def reference(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_symmetry.Reference = value 

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the volume result. Legal values: True if the
                | result of symmetry is required as volume (option is
                | effective only in case of volumes, requires GSO License) and
                | False if it is needed as surface . 
                |
                | Example:
                | This example
                | sets that the result of the hybShpSymmetry hybrid shape
                | symmetry is volume. hybShpSymmetry.VolumeResult = True

        :return:
        """
        return self.hybrid_shape_symmetry.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_symmetry.VolumeResult = value 

    def __repr__(self):
        return f'HybridShapeSymmetry()'
