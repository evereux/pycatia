#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.repartition import Repartition
from pycatia.system_interfaces.any_object import AnyObject


class UserRepartition(Repartition):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PartInterfaces.Repartition
                |                         UserRepartition
                | 
                | Represents the User Pattern repartition.
                | It is made up of a number of times the shape is copied and the location of
                | instances. The number of times the shape is copied is accessible using the
                | Repartition.InstancesCount property.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_repartition = com_object

    @property
    def feature_to_locate_positions(self) -> AnyObject:
        """
        .. note::
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

        :return: AnyObject
        :rtype: AnyObject
        """

        return AnyObject(self.user_repartition.FeatureToLocatePositions)

    def add_feature_to_locate_positions(self, i_feature_to_locate_positions: AnyObject) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFeatureToLocatePositions(AnyObject
                | iFeatureToLocatePositions)
                | 
                |     Adds a new feature to locate instances.
                | 
                |     Parameters:
                | 
                |         iFeatureToLocatePositions
                |             The new face to process 
                | 
                |     Example:
                |         The following example adds the new feature feature to locate instances
                |         of the Pattern firstPattern:
                | 
                |          call firstPattern.AddFeatureToLocatePositions(face)

        :param AnyObject i_feature_to_locate_positions:
        :return: None
        :rtype: None
        """
        return self.user_repartition.AddFeatureToLocatePositions(i_feature_to_locate_positions.com_object)

    def __repr__(self):
        return f'UserRepartition(name="{ self.name }")'
