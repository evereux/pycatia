#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.angle import Angle
from pycatia.part_interfaces.repartition import Repartition


class AngularRepartition(Repartition):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PartInterfaces.Repartition
                |                         AngularRepartition
                | 
                | Represents the angular repartition.
                | It is used by the circular pattern. It is made up of a number of times the
                | shape is copied and of an angular spacing between two consecutive copies of the
                | shape along a crown. The number of times the shape is copied is accessible
                | using the Repartition.InstancesCount property.
                | 
                | See also:
                |     CircPattern
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.angular_repartition = com_object

    @property
    def angular_spacing(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngularSpacing() As Angle (Read Only)
                | 
                |     Returns the angle between two consecutive copies of a shape along the
                |     repartition crown.
                | 
                |     Example:
                |         The following example returns in AngSpace1 the angular spacing of the
                |         angular repartition firstRepartition:
                | 
                |          Set AngSpace1 = firstRepartition.AngularSpacing

        :rtype: Angle
        """

        return Angle(self.angular_repartition.AngularSpacing)

    @property
    def instance_spacing(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InstanceSpacing() As Angle (Read Only)
                | 
                |     Returns the angle at which the pattern spacing is done for unequal angular
                |     spacing mode.
                | 
                |     Example:
                |         The following example returns in AngSpace1 the angular spacing of the
                |         angular repartition firstRepartition:
                | 
                |          Set AngSpace1 = firstRepartition.AngularSpacing

        :rtype: Angle
        """

        return Angle(self.angular_repartition.InstanceSpacing)

    def __repr__(self):
        return f'AngularRepartition(name="{ self.name }")'
