#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_activity import ManufacturingActivity
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingPrecedence(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingPrecedence
                | 
                | Defines a precedence relation between objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_precedence = com_object

    @property
    def precedence_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PrecedenceType() As CatManufacturingPrecedenceType (Read
                | Only)
                | 
                |     Returns the type of the precedence.

        :return: enum cat_manufacturing_precedence_type
        :rtype: int
        """

        return self.manufacturing_precedence.PrecedenceType

    @property
    def target_operation(self) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TargetOperation() As ManufacturingActivity (Read
                | Only)
                | 
                |     Returns the target object of the precedence, but with the Operation
                |     interface if it is.

        :rtype: ManufacturingActivity
        """

        return ManufacturingActivity(self.manufacturing_precedence.TargetOperation)

    def __repr__(self):
        return f'ManufacturingPrecedence(name="{self.name}")'
