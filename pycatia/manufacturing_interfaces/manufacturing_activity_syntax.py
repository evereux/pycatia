#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingActivitySyntax(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivitySyntax
                | 
                | This interface offers services to manage PP words of activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_activity_syntax = com_object

    def reset_pp_word_syntax(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetPPWORDSyntax()
                | 
                |     Resets the PP words syntax.
                | 
                |     Returns:
                |         S_OK when the method succeeds, and E_FAIL otherwise

        :rtype: None
        """
        return self.manufacturing_activity_syntax.ResetPPWORDSyntax()

    def set_pp_word_syntax(self, i_ppwords: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPPWORDSyntax(CATBSTR iPPWORDs)
                | 
                |     Sets the PP words syntax.
                | 
                |     Returns:
                |         S_OK when the method succeeds, and E_FAIL otherwise 
                |     Parameters:
                | 
                |         iPPWORDs
                |             The user PP words syntax to set

        :param str i_ppwords:
        :rtype: None
        """
        return self.manufacturing_activity_syntax.SetPPWORDSyntax(i_ppwords)

    def __repr__(self):
        return f'ManufacturingActivitySyntax(name="{self.name}")'
