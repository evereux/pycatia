#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchZone(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchZone
                | 
                | Manage zone boundaries.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_zone = com_object

    def update_bounded_elements(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UpdateBoundedElements()
                | 
                |     Update the zone members based on the current zone
                |     boundaries.
                | 
                |     Parameters:
                | 
                |         iGRRToAdd
                |             The graphical representation to be added to the zone.
                |             
                |     Example:
                |
                |          Dim objThisIntf As SchZone
                |           ...
                |          objThisIntf.UpdateBoundedElements

        :rtype: None
        """
        return self.sch_zone.UpdateBoundedElements()

    def __repr__(self):
        return f'SchZone(name="{self.name}")'
