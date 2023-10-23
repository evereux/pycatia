#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_ergo_carry import SWKErgoCarry
from pycatia.dnb_human_modeling_interfaces.swk_ergo_lift_lower import SWKErgoLiftLower
from pycatia.dnb_human_modeling_interfaces.swk_ergo_push_pull import SWKErgoPushPull
from pycatia.dnb_human_modeling_interfaces.swk_ergo_rula import SWKErgoRULA
from pycatia.system_interfaces.any_object import AnyObject


class SWKErgo(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SWKErgo
                | 
                | This interface groups the properties giving access to all the ergonomic studies
                | that can be performed on a manikin.
                | 
                | Its main purpose is to provide bridges to the specific ergonomic analysis
                | interfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_ergo = com_object

    @property
    def carry(self) -> SWKErgoCarry:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Carry() As SWKErgoCarry (Read Only)
                | 
                |     Returns the object for a carry analysis. The Carry can also be obtained by
                |     invoking method GetItem (from AnyObject) with the character string "Carry" as
                |     an argument.

        :rtype: SWKErgoCarry
        """

        return SWKErgoCarry(self.swk_ergo.Carry)

    @property
    def lift_lower(self) -> SWKErgoLiftLower:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LiftLower() As SWKErgoLiftLower (Read Only)
                | 
                |     Returns the object for a lift/lower analysis. The Lift/Lower can also be
                |     obtained by invoking method GetItem (from AnyObject) with the character string
                |     "LiftLower" as an argument.

        :rtype: SWKErgoLiftLower
        """

        return SWKErgoLiftLower(self.swk_ergo.LiftLower)

    @property
    def push_pull(self) -> SWKErgoPushPull:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PushPull() As SWKErgoPushPull (Read Only)
                | 
                |     Returns the object for a push/pull analysis. The Push/Pull can also be
                |     obtained by invoking method GetItem (from AnyObject) with the character string
                |     "PushPull" as an argument.

        :rtype: SWKErgoPushPull
        """

        return SWKErgoPushPull(self.swk_ergo.PushPull)

    @property
    def rula(self) -> SWKErgoRULA:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RULA() As SWKErgoRULA (Read Only)
                | 
                |     Returns the object for a RULA analysis. The RULA object can also be
                |     obtained by invoking method GetItem (from AnyObject) with the character string
                |     "RULA" as an argument.

        :rtype: SWKErgoRULA
        """

        return SWKErgoRULA(self.swk_ergo.RULA)

    def __repr__(self):
        return f'SWKErgo(name="{self.name}")'
