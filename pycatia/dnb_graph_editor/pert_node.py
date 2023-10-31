#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PertNode(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PertNode
                | 
                | This Interface represents a PertNode in the PERT Chart.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pert_node = com_object

    def get_location(self, xx: float, yy: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLocation(double xx,
                | double yy)
                | 
                |     This method gets the Location of the PertNode in the PERT
                |     Chart
                | 
                |     Parameters:
                | 
                |         xx
                |             X Coordinate of the Location in the Pert Chart 
                |         yy
                |             Y Coordinate of the Location in the Pert Chart

        :param float xx:
        :param float yy:
        :rtype: None
        """
        return self.pert_node.GetLocation(xx, yy)

    def set_icon(self, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIcon(CATBSTR iFileName)
                | 
                |     This method sets Icon for the PertNode in the PERT Chart
                | 
                |     Parameters:
                | 
                |         iFileName
                |             FileName of the Icon which includes full path

        :param str i_file_name:
        :rtype: None
        """
        return self.pert_node.SetIcon(i_file_name)

    def set_location(self, xx: float, yy: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLocation(double xx,
                | double yy)
                | 
                |     This method place the PertNode in the PERT Chart at any location by
                |     specifying the X and Y Coordinates in the Grid.
                | 
                |     Parameters:
                | 
                |         xx
                |             X Coordinate of the Location in the Pert Chart 
                |         yy
                |             Y Coordinate of the Location in the Pert Chart

        :param float xx:
        :param float yy:
        :rtype: None
        """
        return self.pert_node.SetLocation(xx, yy)

    def __repr__(self):
        return f'PertNode(name="{self.name}")'
