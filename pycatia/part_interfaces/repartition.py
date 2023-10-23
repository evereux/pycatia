#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.system_interfaces.any_object import AnyObject


class Repartition(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Repartition
                | 
                | Represents the repartition.
                | A repartition is a set of objects used by the pattern shapes. It is the base
                | object for linear and angular repartitions.
                | 
                | See also:
                |     LinearRepartition, AngularRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.repartition = com_object

    @property
    def instances_count(self) -> IntParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InstancesCount() As IntParam (Read Only)
                | 
                |     Returns the total number of copied shapes.
                | 
                |     Example:
                |         The following example returns in Nb the number of shapes of the
                |         repartition firstRepartition:
                | 
                |          Set Nb = firstRepartition.InstancesCount

        :rtype: IntParam
        """

        return IntParam(self.repartition.InstancesCount)

    def __repr__(self):
        return f'Repartition(name="{ self.name }")'
