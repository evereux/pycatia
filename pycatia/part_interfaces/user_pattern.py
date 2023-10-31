#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.pattern import Pattern
from pycatia.system_interfaces.any_object import AnyObject


class UserPattern(Pattern):

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
                |                         PartInterfaces.TransformationShape
                |                             PartInterfaces.Pattern
                |                                 UserPattern
                | 
                | Represents the user pattern.
                | The shape is copied along user's positions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_pattern = com_object

    @property
    def anchor_point(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnchorPoint() As AnyObject
                | 
                |     Returns the anchor point of the user pattern.
                | 
                |     Example:
                |         The following example returns in anchor the anchor point of the Pattern
                |         firstPattern:
                | 
                |          Set anchor = firstPattern.AnchorPoint

        :rtype: AnyObject
        """

        return AnyObject(self.user_pattern.AnchorPoint)

    @anchor_point.setter
    def anchor_point(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.user_pattern.AnchorPoint = value

    @property
    def feature_to_locate_positions(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FeatureToLocatePositions() As AnyObject (Read
                | Only)
                | 
                |     Returns the collection of feature to locate instances.
                | 
                |     Example:
                |         The following example returns in list the list of feature to locate
                |         instances of the Pattern firstPattern:
                | 
                |          Set list = firstPattern.FeatureToLocatePositions

        :rtype: AnyObject
        """

        return AnyObject(self.user_pattern.FeatureToLocatePositions)

    def add_feature_to_locate_positions(self, i_feature_to_locate_positions: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFeatureToLocatePositions(AnyObject
                | iFeatureToLocatePositions)
                | 
                |     Adds a new feature to locate instances.
                | 
                |     Parameters:
                | 
                |         iFeatureToLocatePositions
                |             The new object containing points of positioning 
                | 
                |     Example:
                |         The following example adds the new feature feature to locate instances
                |         of the Pattern firstPattern:
                | 
                |          call firstPattern.AddFeatureToLocatePositions(object)

        :param AnyObject i_feature_to_locate_positions:
        :rtype: None
        """
        return self.user_pattern.AddFeatureToLocatePositions(i_feature_to_locate_positions.com_object)

    def __repr__(self):
        return f'UserPattern(name="{ self.name }")'
