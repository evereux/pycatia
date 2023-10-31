#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.sketch_based_shape import SketchBasedShape


class Stiffener(SketchBasedShape):

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
                |                             Stiffener
                | 
                | Represents the stiffener shape.
                | A stiffener is made up of a sketch used as the stiffener profile, that is
                | extruded (offset) and that fills the nearest shape. This is a "positive" shape:
                | it adds material to the body it belongs to.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.stiffener = com_object

    @property
    def is_from_top(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsFromTop() As boolean
                | 
                |     Returns or sets whether the stiffener is From Side or From
                |     Top.
                |     True if the stiffener is From Top stiffener with respect to the base
                |     sketch. False if the stiffener is From Side stiffener with respect to the base
                |     sketch.
                | 
                |     Example:
                |         The following example returns in FromTopFlag whether the firstStiffener
                |         stiffener is From Top, and then sets it as From Top stiffener with respect to
                |         its base sketch:
                | 
                |          Set FromTopFlag = firstStiffener.IsFromTop
                |          firstStiffener.IsFromTop  = True

        :rtype: bool
        """

        return self.stiffener.IsFromTop

    @is_from_top.setter
    def is_from_top(self, value: bool):
        """
        :param bool value:
        """

        self.stiffener.IsFromTop = value

    @property
    def is_symmetric(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsSymmetric() As boolean
                | 
                |     Returns or sets whether the stiffener is symmetric.
                |     True if the stiffener is symmetric with respect to the base
                |     sketch.
                | 
                |     Example:
                |         The following example returns in symFlag whether the firstStiffener
                |         stiffener is symmetric, and then sets it as symmetric with respect to its base
                |         sketch:
                | 
                |          Set symFlag = firstStiffener.IsSymmetric
                |          firstStiffener.IsSymmetric  = True

        :rtype: bool
        """

        return self.stiffener.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        """
        :param bool value:
        """

        self.stiffener.IsSymmetric = value

    @property
    def thickness(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Thickness() As Length (Read Only)
                | 
                |     Returns the stiffener thickness. This is half of the thickness if the
                |     stiffener is symmetrical, and the thickness otherwise.
                | 
                |     Example:
                |         The following example returns in thickness the thickness of the
                |         firstStiffener stiffener:
                | 
                |          Set thickness = firstStiffener.Thickness

        :rtype: Length
        """

        return Length(self.stiffener.Thickness)

    @property
    def thickness_from_top(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThicknessFromTop() As Length (Read Only)
                | 
                |     Returns the stiffener thickness top in case of From Top stiffener. This is
                |     equal to first thickness if the stiffener is symmetrical,
                | 
                |     Example:
                |         The following example returns in thicknessfromtop the thickness of the
                |         firstStiffener stiffener:
                | 
                |          Set thicknessfromtop = firstStiffener.ThicknessFromTop

        :rtype: Length
        """

        return Length(self.stiffener.ThicknessFromTop)

    def reverse_depth(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReverseDepth()
                | 
                |     Reverses the stiffener direction. This is useful for finding the shape to
                |     reach.
                | 
                |     Example:
                |         The following example reverses the current direction of the
                |         firstStiffener stiffener:
                | 
                |          firstStiffener.ReverseDepth

        :rtype: None
        """
        return self.stiffener.ReverseDepth()

    def reverse_thickness(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReverseThickness()
                | 
                |     Reverses the stiffener thickness direction. The stiffener thickness is
                |     swapped with respect to the base sketch.
                | 
                |     Example:
                |         The following example reverses the current direction of the
                |         firstStiffener stiffener:
                | 
                |          firstStiffener.ReverseThickness

        :rtype: None
        """
        return self.stiffener.ReverseThickness()

    def __repr__(self):
        return f'Stiffener(name="{ self.name }")'
