#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchZoneMembership(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchZoneMembership
                | 
                | Manage zone memberships.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_zone_membership = com_object

    def update_zone_membership(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UpdateZoneMembership()
                | 
                |     Check all zones geometric boundaries and put this element into the correct
                |     zone membership lists.
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchZoneMembership
                |           ...
                |          objThisIntf.UpdateZoneMembership

        :rtype: None
        """
        return self.sch_zone_membership.UpdateZoneMembership()

    def __repr__(self):
        return f'SchZoneMembership(name="{self.name}")'
