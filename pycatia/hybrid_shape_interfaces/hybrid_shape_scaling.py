#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeScaling(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeScaling
                | 
                | Represents the hybrid shape scaling feature object.
                | Role: To access the data of the hybrid shape feature object. This data
                | includes:
                | 
                |     The element to be transformed using the scaling
                |     The reference element for the scaling which is a point or a
                |     plane
                |     The ratio and its value
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_scaling = com_object

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Center() As Reference
                | 
                |     Returns or sets the reference element.This element can be a point or a
                |     plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace or
                |     Vertex.
                | 
                |     Example:
                |         This example retrieves in RefElem the reference element for the Scaling
                |         hybrid shape feature.
                | 
                |          Dim RefElem As Reference
                |          Set RefElem = Scaling.Center

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_scaling.Center)

    @center.setter
    def center(self, reference_center: Reference):
        """
        :param Reference reference_center:
        """

        self.hybrid_shape_scaling.Center = reference_center.com_object

    @property
    def creation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CreationMode() As boolean
                | 
                |     Returns or sets the creation mode(creation or
                |     modification).
                |     Legal values: True if the result is a creation feature and False if the
                |     result is a modification feature.
                | 
                |     Example:
                | 
                |           This example sets that the mode of
                |          the hybShpScaling hybrid shape scaling to creation
                |          
                | 
                |          hybShpScaling.CreationMode = True

        :rtype: bool
        """

        return self.hybrid_shape_scaling.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_scaling.CreationMode = value

    @property
    def elem_to_scale(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ElemToScale() As Reference
                | 
                |     Returns or sets the element to scale.
                | 
                |     Example:
                |         This example retrieves in Elem the element to scale for the Scaling
                |         hybrid shape feature.
                | 
                |          Dim Elem As Reference
                |          Set Elem = Scaling.ElemToScale

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_scaling.ElemToScale)

    @elem_to_scale.setter
    def elem_to_scale(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_scaling.ElemToScale = reference_element.com_object

    @property
    def ratio(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Ratio() As RealParam (Read Only)
                | 
                |     Returns the scaling ratio.

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_scaling.Ratio)

    @property
    def ratio_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RatioValue() As double
                | 
                |     Returns or sets the scaling ratio value.
                | 
                |     Example:
                |         This example retrieves in Value the ratio value for the Scaling hybrid
                |         shape feature.
                | 
                |          Dim Value As double
                |          Set Value = Scaling.RatioValue

        :rtype: float
        """

        return self.hybrid_shape_scaling.RatioValue

    @ratio_value.setter
    def ratio_value(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_scaling.RatioValue = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property VolumeResult() As boolean
                | 
                |     Returns or sets the volume result.
                |     Legal values: True if the result of Scaling is required as volume (option
                |     is effective only in case of volumes,requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |           This example sets that the result of
                |          the hybShpScaling hybrid shape scaling is volume.
                |          
                | 
                |          hybShpScaling.VolumeResult = True

        :rtype: bool
        """

        return self.hybrid_shape_scaling.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_scaling.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeScaling(name="{self.name}")'
