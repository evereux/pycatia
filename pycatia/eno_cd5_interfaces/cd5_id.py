#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class CD5ID(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5ID
                | 
                | Represents the ENOVIA V6 Integration identifier.
                | Role: It identifies an ENOVIA V6 Object thanks to its
                | Type/Name/Revision(/Version). It is managed by CD5Engine.
                | 
                | See also:
                |     CD5Engine, CD5Structure
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_id = com_object

    def get_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetID() As CATBSTR
                | 
                |     Returns the Identifier of the ENOVIA V6 Object associated to the
                |     CD5ID.
                | 
                |     Returns:
                |         The identifier String of the ENOIACD5ID. 
                |     Example:
                | 
                |           The following example returns in oID the identifier corresponding to
                |           the CD5ID oCD5ID.
                |
                |          Dim oCD5Engine As CD5Engine
                |          Set oCD5Engine = CATIA.GetItem("CD5Engine")
                |          Dim oCD5ID As CD5ID
                |          Set oCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "MyProduct", "---")
                |          Dim oID As CATBSTR
                |          oID = oCD5ID.GetID

        :rtype: str
        """
        return self.cd5_id.GetID()

    def __repr__(self):
        return f'CD5ID(name="{self.name}")'
