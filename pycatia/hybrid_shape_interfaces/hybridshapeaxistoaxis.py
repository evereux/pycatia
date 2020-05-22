#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeAxisToAxis(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape axis to axis tranformation feature
                | object.Role: To access the data of the axis to axis tranformation
                | shape feature object. The data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_axis_to_axis = com_object

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
                | example sets that the mode of the hybShpAxisToAxis hybrid
                | shape axis to axis to creation hybShpAxisToAxis.CreationMode
                | = True

        :return:
        """
        return self.hybrid_shape_axis_to_axis.CreationMode

    @creation_mode.setter
    def creation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_to_axis.CreationMode = value

    @property
    def elem_to_transform(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToTransform
                | o Property ElemToTransform(    ) As
                | 
                | Returns or sets the element to transform. 
                |
                | Example:
                | This
                | example retrieves in Elem the element to transform for the
                | AxisToAxis hybrid shape feature. Dim Elem As Reference Set
                | Elem = AxisToAxis.ElemToTransform

        :return:
        """
        return self.hybrid_shape_axis_to_axis.ElemToTransform

    @elem_to_transform.setter
    def elem_to_transform(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_to_axis.ElemToTransform = value

    @property
    def reference_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReferenceAxis
                | o Property ReferenceAxis(    ) As
                | 
                | Returns or sets the reference axis. 
                |
                | Example:
                | This example
                | retrieves in Ref the reference axis for the AxisToAxis
                | hybrid shape feature. Dim Ref As Reference Set Ref =
                | AxisToAxis.ReferenceAxis

        :return:
        """
        return self.hybrid_shape_axis_to_axis.ReferenceAxis

    @reference_axis.setter
    def reference_axis(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_to_axis.ReferenceAxis = value

    @property
    def target_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TargetAxis
                | o Property TargetAxis(    ) As
                | 
                | Returns or sets the target axis. 
                |
                | Example:
                | This example
                | retrieves in Ref the target axis for the AxisToAxis hybrid
                | shape feature. Dim Ref As Reference Set Ref =
                | AxisToAxis.ReferenceAxis

        :return:
        """
        return self.hybrid_shape_axis_to_axis.TargetAxis

    @target_axis.setter
    def target_axis(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_to_axis.TargetAxis = value

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VolumeResult
                | o Property VolumeResult(    ) As
                | 
                | Returns or sets the volume result. Legal values: True if the
                | result of axis to axis transformation is required as volume
                | (option is effective only in case of volumes,requires GSO
                | License)) and False if it is needed as surface . Example:
                | This example sets that the result of the hybShpAxisToAxis
                | hybrid shape AxisToAxis is volume.
                | hybShpAxisToAxis.VolumeResult = True

        :return:
        """
        return self.hybrid_shape_axis_to_axis.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_axis_to_axis.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeAxisToAxis()'
