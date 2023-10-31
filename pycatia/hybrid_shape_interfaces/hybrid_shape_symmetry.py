#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSymmetry(HybridShape):
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
                |                         HybridShapeSymmetry
                | 
                | Represents the hybrid shape symmetry feature object.
                | Role: To access the data of the symmetry shape feature object. The data
                | includes:
                | 
                |     The element to be transformed
                |     The reference element which can be a point, a line or a
                |     plane
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_symmetry = com_object

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
                |          the hybShpSymmetry hybrid shape symmetry to creation
                |          
                | 
                |          hybShpSymmetry.CreationMode = True

        :rtype: bool
        """

        return self.hybrid_shape_symmetry.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_symmetry.CreationMode = value

    @property
    def elem_to_symmetry(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ElemToSymmetry() As Reference
                | 
                |     Returns or sets the element to transform.
                | 
                |     Example:
                |         This example retrieves in Elem the element to transform for the
                |         Symmetry hybrid shape feature.
                | 
                |          Dim Elem As Reference
                |          Set Elem = Symmetry.ElemToSymmetry

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_symmetry.ElemToSymmetry)

    @elem_to_symmetry.setter
    def elem_to_symmetry(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_symmetry.ElemToSymmetry = reference_element.com_object

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Reference() As Reference
                | 
                |     Returns or sets the reference element.This element can be a point, a line
                |     or a plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace, Edge or
                |     Vertex.
                | 
                |     Example:
                |         This example retrieves in Ref the reference element for the Symmetry
                |         hybrid shape feature.
                | 
                |          Dim Ref As Reference
                |          Set Ref = Symmetry.Reference

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_symmetry.Reference)

    @reference.setter
    def reference(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_symmetry.Reference = reference.com_object

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property VolumeResult() As boolean
                | 
                |     Returns or sets the volume result.
                |     Legal values: True if the result of symmetry is required as volume (option
                |     is effective only in case of volumes, requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |           This example sets that the result of
                |          the hybShpSymmetry hybrid shape symmetry is volume.
                |          
                | 
                |          hybShpSymmetry.VolumeResult = True

        :rtype: bool
        """

        return self.hybrid_shape_symmetry.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_symmetry.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeSymmetry(name="{self.name}")'
