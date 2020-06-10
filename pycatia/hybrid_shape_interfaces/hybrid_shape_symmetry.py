#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

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
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

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
    def creation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: bool
        """

        return self.hybrid_shape_symmetry.CreationMode

    @creation_mode.setter
    def creation_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_symmetry.CreationMode = value

    @property
    def elem_to_symmetry(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_symmetry.ElemToSymmetry)

    @elem_to_symmetry.setter
    def elem_to_symmetry(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_symmetry.ElemToSymmetry = value

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_symmetry.Reference)

    @reference.setter
    def reference(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_symmetry.Reference = value

    @property
    def volume_result(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: bool
        """

        return self.hybrid_shape_symmetry.VolumeResult

    @volume_result.setter
    def volume_result(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_symmetry.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeSymmetry(name="{ self.name }")'
