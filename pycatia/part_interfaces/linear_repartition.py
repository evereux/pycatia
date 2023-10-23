#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.repartition import Repartition


class LinearRepartition(Repartition):

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
                |                         LinearRepartition
                | 
                | Represents the linear repartition.
                | It is used by the rectangular and circular patterns. It is made up of a number
                | of times the shape is copied and of a spacing distance between two consecutive
                | copies of this shape along a direction. The number of times the shape is copied
                | is accessible using the Repartition.InstancesCount property.
                | 
                | See also:
                |     RectPattern, CircPattern
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.linear_repartition = com_object

    @property
    def spacing(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Spacing() As Length (Read Only)
                | 
                |     Returns the distance between two consecutive shapes along the repartition
                |     direction.
                | 
                |     Example:
                |         The following example returns in space1 the spacing distance of the
                |         linear repartition firstRepartition:
                | 
                |          Set space1 = firstRepartition.Spacing

        :rtype: Length
        """

        return Length(self.linear_repartition.Spacing)

    def __repr__(self):
        return f'LinearRepartition(name="{ self.name }")'
