#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class StrCutoutFeature(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrCutoutFeature
                | 
                | Represents a Cutout Feature.
                | CutoutType,Direction,Surface,DeirectionElement can be
                | redefined.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_cutout_feature = com_object

    @property
    def contour(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Contour() As Reference
                | 
                |     Returns or Sets the Contour Sketch for Current Cutout.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim NewContour As Reference
                |          Set NewContour = rootProduct.CreateReferenceFromName("Product1/New/!Sketch.2")
                |          ExistingCutout.Contour =NewContour

        :rtype: Reference
        """

        return Reference(self.str_cutout_feature.Contour)

    @contour.setter
    def contour(self, value: Reference):
        """
        :param Reference value:
        """

        self.str_cutout_feature.Contour = value.com_object

    @property
    def cutout_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CutoutType() As CATBSTR
                | 
                |     Returns or Sets the CutoutType for Current Cutout.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim Type As String
                |          Type = Cutout1.CutoutType

        :rtype: str
        """

        return self.str_cutout_feature.CutoutType

    @cutout_type.setter
    def cutout_type(self, value: str):
        """
        :param str value:
        """

        self.str_cutout_feature.CutoutType = value

    @property
    def direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Direction() As CATSafeArrayVariant
                | 
                |     Returns or Sets the Direction Vector for Current Cutout.If we are in
                |     CATStrBeforeForming mode, it gives NULL.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim GetDir(3)
                |          GetDir(3) = Cutoutctr.Direction
                |          Dim x, y, z As Double
                |          x = GetDir(0)
                |          y = GetDir(1)
                |          z = GetDir(2)
                |          'For Setting Direction
                |          Dim Setdir(3) 
                |          Setdir(0) = 0.5
                |          Setdir(1) = 0.5
                |          Setdir(2) = 0.5
                |          Cutout1.Direction =Setdir

        :rtype: tuple
        """

        return self.str_cutout_feature.Direction

    @direction.setter
    def direction(self, value: tuple):
        """
        :param tuple value:
        """

        self.str_cutout_feature.Direction = value

    @property
    def direction_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DirectionElement() As Reference
                | 
                |     Returns or Sets the Element used for defining for Current Cutout.If we are
                |     in CATStrBeforeForming mode, it gives NULL.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim DirOfCutOut As Reference
                |          Set DirOfCutOut = Cutout2.DirectionElement

        :rtype: Reference
        """

        return Reference(self.str_cutout_feature.DirectionElement)

    @direction_element.setter
    def direction_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.str_cutout_feature.DirectionElement = value.com_object

    @property
    def reference_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceSurface() As Reference
                | 
                |     Returns or Sets the Reference Surface used for defining for Current
                |     Cutout.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim SurForCutout As Reference
                |          Set SurForCutout = Cutout2.ReferenceSurface

        :rtype: Reference
        """

        return Reference(self.str_cutout_feature.ReferenceSurface)

    @reference_surface.setter
    def reference_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.str_cutout_feature.ReferenceSurface = value.com_object

    def get_object(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetObject() As Product
                | 
                |     Retrieves the Structure object on which the cutout is applied
                |     on.
                | 
                |     Parameters:
                | 
                |         oObject
                |             [out] Product 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example
                |         :
                |             This example gives the product on which cutout is
                |             applied.
                | 
                |              Dim Prod As Product
                |              Set Prod = Cutout1.GetObject
                |              
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :rtype: Product
        """
        return Product(self.str_cutout_feature.GetObject())

    def __repr__(self):
        return f'StrCutoutFeature(name="{self.name}")'
