#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.sketch_based_shape import SketchBasedShape


class SolidCombine(SketchBasedShape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SketchBasedShape
                |                             SolidCombine
                | 
                | The interface to access a CATIASolidCombine.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.solid_combine = com_object

    @property
    def first_component_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstComponentDirection() As Reference
                | 
                |     Returns or sets the direction of first component of
                |     SolidCombine.
                | 
                |     Example:
                |         The following example returns in firstDirection the direction of first
                |         component of firstSolidCombine SolidCombine feature, and then sets it to the
                |         firstDirection2 direction element.
                | 
                |          Set firstDirection = firstSolidCombine.FirstComponentDirection
                |          Set firstSolidCombine.FirstComponentDirection = firstDirection2

        :rtype: Reference
        """

        return Reference(self.solid_combine.FirstComponentDirection)

    @first_component_direction.setter
    def first_component_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.solid_combine.FirstComponentDirection = value.com_object

    @property
    def first_component_profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstComponentProfile() As Reference
                | 
                |     Returns or sets the profile of first component of
                |     SolidCombine.
                | 
                |     Example:
                |         The following example returns in firstProfile the profile of first
                |         component of firstSolidCombine SolidCombine feature, and then sets it to the
                |         firstProfile2 profile element:
                | 
                |          Set firstProfile = firstSolidCombine.FirstComponentProfile
                |          Set firstSolidCombine.FirstComponentProfile = firstProfile2

        :rtype: Reference
        """

        return Reference(self.solid_combine.FirstComponentProfile)

    @first_component_profile.setter
    def first_component_profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.solid_combine.FirstComponentProfile = value.com_object

    @property
    def second_component_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondComponentDirection() As Reference
                | 
                |     Returns or sets the direction of second component of
                |     SolidCombine.
                | 
                |     Example:
                |         The following example returns in secondDirection the direction of
                |         second component of firstSolidCombine SolidCombine feature, and then sets it to
                |         the secondDirection2 direction element.
                | 
                |          Set secondDirection = firstSolidCombine.SecondComponentDirection
                |          Set firstSolidCombine.SecondComponentDirection = secondDirection2

        :rtype: Reference
        """

        return Reference(self.solid_combine.SecondComponentDirection)

    @second_component_direction.setter
    def second_component_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.solid_combine.SecondComponentDirection = value.com_object

    @property
    def second_component_profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondComponentProfile() As Reference
                | 
                |     Returns or sets the profile of second component of
                |     SolidCombine.
                | 
                |     Example:
                |         The following example returns in secondProfile the profile of second
                |         component of firstSolidCombine SolidCombine feature, and then sets it to the
                |         secondProfile2 profile element:
                | 
                |          Set secondProfile = firstSolidCombine.SecondComponentProfile
                |          Set firstSolidCombine.SecondComponentProfile = secondProfile2

        :rtype: Reference
        """

        return Reference(self.solid_combine.SecondComponentProfile)

    @second_component_profile.setter
    def second_component_profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.solid_combine.SecondComponentProfile = value.com_object

    def __repr__(self):
        return f'SolidCombine(name="{ self.name }")'
