#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeScaling(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape scaling feature object.Role: To access the
                | data of the hybrid shape feature object. This data includes:Use the
                | CATIAHybridShapeFactory to create HybridShapeFeature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_scaling = com_object     

    @property
    def center(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Center
                | o Property Center(    ) As
                | 
                | Returns or sets the reference element.This element can be a
                | point or a plane. Sub-element(s) supported (see object): or
                | . 
                |
                | Example:
                | This example retrieves in RefElem the reference
                | element for the Scaling hybrid shape feature. Dim RefElem As
                | Reference Set RefElem = Scaling.Center

        :return:
        """
        return self.hybrid_shape_scaling.Center

    @center.setter
    def center(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_scaling.Center = value 

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
                | example sets that the mode of the hybShpScaling hybrid shape
                | scaling to creation hybShpScaling.CreationMode = True

        :return:
        """
        return self.hybrid_shape_scaling.CreationMode

    @creation_mode.setter
    def creation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_scaling.CreationMode = value 

    @property
    def elem_to_scale(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToScale
                | o Property ElemToScale(    ) As
                | 
                | Returns or sets the element to scale. 
                |
                | Example:
                | This example
                | retrieves in Elem the element to scale for the Scaling
                | hybrid shape feature. Dim Elem As Reference Set Elem =
                | Scaling.ElemToScale

        :return:
        """
        return self.hybrid_shape_scaling.ElemToScale

    @elem_to_scale.setter
    def elem_to_scale(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_scaling.ElemToScale = value 

    @property
    def ratio(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Ratio
                | o Property Ratio(    ) As   (Read Only)
                | 
                | Returns the scaling ratio.

        :return:
        """
        return self.hybrid_shape_scaling.Ratio

    @property
    def ratio_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RatioValue
                | o Property RatioValue(    ) As
                | 
                | Returns or sets the scaling ratio value. 
                |
                | Example:
                | This
                | example retrieves in Value the ratio value for the Scaling
                | hybrid shape feature. Dim Value As double Set Value =
                | Scaling.RatioValue

        :return:
        """
        return self.hybrid_shape_scaling.RatioValue

    @ratio_value.setter
    def ratio_value(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_scaling.RatioValue = value 

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the volume result. Legal values: True if the
                | result of Scaling is required as volume (option is effective
                | only in case of volumes,requires GSO License) and False if
                | it is needed as surface . 
                |
                | Example:
                | This example sets that
                | the result of the hybShpScaling hybrid shape scaling is
                | volume. hybShpScaling.VolumeResult = True

        :return:
        """
        return self.hybrid_shape_scaling.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_scaling.VolumeResult = value 

    def __repr__(self):
        return f'HybridShapeScaling()'
