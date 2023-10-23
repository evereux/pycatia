#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.functional_element import FunctionalElement


class FunctionalPosition(FunctionalElement):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATFunctSystemItf.FunctionalElement
                |                         FunctionalPosition
                | 
                | Represents a Functional Position.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_position = com_object

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property X() As double (Read Only)
                | 
                |     Returns the X coordinate.

        :rtype: float
        """

        return self.functional_position.X

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Y() As double (Read Only)
                | 
                |     Returns the Y coordinate.

        :rtype: float
        """

        return self.functional_position.Y

    def set_coords(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCoords(double iX,
                | double iY)
                | 
                |     Sets the coordinates.
                | 
                |     Parameters:
                | 
                |         iX
                |             the x coordinate. 
                |         iY
                |             the y coordinate

        :param float i_x:
        :param float i_y:
        :rtype: None
        """
        return self.functional_position.SetCoords(i_x, i_y)

    def __repr__(self):
        return f'FunctionalPosition(name="{self.name}")'
