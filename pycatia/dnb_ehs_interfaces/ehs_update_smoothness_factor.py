#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class EhsUpdateSmoothnessFactor(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     EHSUpdateSmoothnessFactor
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIAEHSUpdateSmoothnessFactor are
                | ...
                | 
                | Do not use the DNBIAEHSUpdateSmoothnessFactor interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ehs_update_smoothness_factor = com_object

    def update_bundle_smoothness(self, i_smoothness_factor: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UpdateBundleSmoothness(short iSmoothnessFactor)
                | 
                |     Sets Smoothness Factor for Bundle segment.
                | 
                |     Parameters:
                | 
                |         iSmoothnessFactor
                |             the input smoothness factor. 
                | 
                |     Returns:
                |         An HRESULT
                |         Legal values:
                | 
                |             S_OK if the Property is returned successfully.
                |             E_FAIL otherwise
                |             .

        :param int i_smoothness_factor:
        :rtype: None
        """
        return self.ehs_update_smoothness_factor.UpdateBundleSmoothness(i_smoothness_factor)

    def __repr__(self):
        return f'EhsUpdateSmoothnessFactor(name="{self.name}")'
