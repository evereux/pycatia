#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.sketcher_interfaces.sketch import Sketch
from pycatia.structure_interfaces.str_object import StrObject


class StrPlate(StrObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProductStructureInterfaces.Product
                |                         StructureInterfaces.StrObject
                |                             StrPlate
                | 
                | Represents a structure plate object.
                | A plate is defined by a thickness and aggregates a support object and a sketch
                | defining its contour.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_plate = com_object

    @property
    def offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Offset() As Parameter (Read Only)
                | 
                |     Returns the offset between the given support and the support of the plate.

        :rtype: Parameter
        """

        return Parameter(self.str_plate.Offset)

    @property
    def sketch(self) -> Sketch:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Sketch() As Sketch (Read Only)
                | 
                |     Returns the sketch object of the plate.

        :rtype: Sketch
        """

        return Sketch(self.str_plate.Sketch)

    @property
    def standard_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StandardThickness() As double
                | 
                |     Returns the standard thickness following the support orientation.

        :rtype: float
        """

        return self.str_plate.StandardThickness

    @standard_thickness.setter
    def standard_thickness(self, value: float):
        """
        :param float value:
        """

        self.str_plate.StandardThickness = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support of the plate.

        :rtype: Reference
        """

        return Reference(self.str_plate.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.str_plate.Support = value.com_object

    def reverse_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ReverseDirection()
                | 
                |     Reverses the material orientation of the plate.
                | 
                |      Plate_1.ReverseDirection

        :rtype: None
        """
        return self.str_plate.ReverseDirection()

    def set_material_and_grade(self, i_material: str, i_grade: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMaterialAndGrade(CATBSTR iMaterial,
                | CATBSTR iGrade)

        :param str i_material:
        :param str i_grade:
        :rtype: None
        """
        return self.str_plate.SetMaterialAndGrade(i_material, i_grade)

    def __repr__(self):
        return f'StrPlate(name="{self.name}")'
