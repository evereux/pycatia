#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchAppCntrColour(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppCntrColor
                | 
                | Manage graphical representation of schematic connector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_cntr_colour = com_object

    def app_get_connector_colour_by_type(self, o_colour: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetConnectorColorByType(long oColor)
                | 
                |     Specify the connector color of this connector type.
                | 
                |     Parameters:
                | 
                |         oColor
                |             Application connector color for "this" connector type. Please refer
                |             to CATColorName.h of Visualization FW. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppCntrColor
                |          Dim intVar1 As Integer
                |           ...
                |          objThisIntf.AppGetConnectorColorByTypeintVar1

        :param int o_colour:
        :rtype: None
        """
        return self.sch_app_cntr_colour.AppGetConnectorColorByType(o_colour)

    def __repr__(self):
        return f'SchAppCntrColour(name="{self.name}")'
