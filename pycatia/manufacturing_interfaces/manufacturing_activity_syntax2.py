#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingActivitySyntax2(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivitySyntax2
                | 
                | This interface offers services to manage PP words of activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_activity_syntax2 = com_object

    def get_pp_word_syntax(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPPWORDSyntax() As CATBSTR
                | 
                |     Retrieves the PP words syntax.
                | 
                |     Returns:
                |         the PPWORDS

        :rtype: str
        """
        return self.manufacturing_activity_syntax2.GetPPWORDSyntax()

    def __repr__(self):
        return f'ManufacturingActivitySyntax2(name="{self.name}")'
