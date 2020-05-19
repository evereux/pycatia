#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.system_interfaces.base_object import AnyObject


class PrintArea(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Manages print area of drawing sheet.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.printarea = com_object

    @property
    def activation_state(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ActivationState
                | o Property ActivationState(        iActivated)
                | 
                | Activates or deactivates the print area.
                |
                | Parameters:
                | in
                | boolean iActivated [in] The activation state of the
                | print area (TRUE means activated, FALSE means deactivated).
                |  
                | 
                | Returns:
                | Un HRESULT
                | S_OK  The activation state could be valuated.
                | E_FAIL  No activation or deactivation possible.



        :return:
        """
        return self.printarea.ActivationState

    @activation_state.setter
    def activation_state(self, i_activated):
        """
        :param i_activated: bool
        """
        self.printarea.ActivationState = i_activated

    @property
    def area_height(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AreaHeigth
                | o Property AreaHeigth(        iHeigth)
                | 
                | Valuates the height of the print area.
                |
                | Parameters:
                | in
                |  double iHeigth [in] The height of the print area. The value must be strictly positive.
                |  
                |  Returns:
                |   Un HRESULT
                |  S_OK
                |  E_FAIL


        :return:
        """
        return self.printarea.AreaHeigth

    @area_height.setter
    def area_height(self, height):
        """
        :param height:
        """
        self.printarea.AreaHeigth = height

    @property
    def area_low_x(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AreaLowX
                | o Property AreaLowX(        iX)
                | 
                | Valuates the low x coordinate of the print area.
                |
                | Parameters:
                | in
                | double iX [in] The low x coordinate.
                |
                | Returns:
                |   Un HRESULT
                |  S_OK
                |  E_FAIL


        :return:
        """
        return self.printarea.AreaLowX

    @area_low_x.setter
    def area_low_x(self, value):
        """
        :param float value:
        """
        self.printarea.AreaLowX = value

    @property
    def area_low_y(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AreaLowY
                | o Property AreaLowY(        iY)
                | 
                | Valuates the low y coordinate of the print area.
                |
                | Parameters:
                | in
                | double iY [in] The low y coordinate.
                | 
                | Returns:
                | Un HRESULT
                | S_OK
                | E_FAIL

        :return:
        """
        return self.printarea.AreaLowY

    @area_low_y.setter
    def area_low_y(self, value):
        """
        :param float value:
        """
        self.printarea.AreaLowY = value

    @property
    def area_width(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AreaWidth
                | o Property AreaWidth(        iWidth)
                | 
                | Valuates the width of the print area.
                |
                | Parameters:
                | in
                |  double iWidth [in] The width of the print area.  The value must be strictly positive.
                |  
                | Returns:
                | Un HRESULT
                | S_OK
                | E_FAIL

        :return:
        """
        return self.printarea.AreaWidth

    @area_width.setter
    def area_width(self, value):
        """
        :param float value:
        """
        self.printarea.AreaWidth = value

    def get_area(self, o_x, o_y, o_width, o_height, o_activated):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetArea
                | o Sub GetArea(oX,
                |               oY,
                |               oWidth,
                |               oHeight,
                |               oActivated)
                | 
                | Gets the printing area defined on an object. Also
                | communicates the activation state of the printing area. All
                | the values are given in mm.
                |
                | Parameters:
                | out
                | double oX [out] The low x coordinate of the area.
                | out
                | double oY [out] The low y coordinate of the area.
                | out
                | double oWidth [out] The width of the area.
                | out
                | double oHeight [out] The height of the area.
                | out
                | boolean oActivated [out] The activation state of the print area
                | (TRUE means activated, FALSE means deactivated).
                | 
                | Returns:
                | Un HRESULT
                | 
                | S_OK  The print area was successfully retrieved.
                | E_FAIL  No print area could be retried.

        :param o_x:
        :param o_y:
        :param o_width:
        :param o_height:
        :param o_activated:
        :return:
        """
        return self.printarea.GetArea(o_x, o_y, o_width, o_height, o_activated)

    def set_area(self, i_x, i_y, i_width, i_height):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetArea
                | o Sub SetArea(iX,
                |               iY,
                |               iWidth,
                |               iHeigth)
                | 
                | Sets a set of coordinates to define a rectangle print area.
                | All the values are given in mm.
                |
                | Parameters:
                | in
                | double iX [in] The low x coordinate of the area.
                | in
                | double iY [in] The low y coordinate of the area.
                | in
                | double iWidth [in] The width of the area. The value must be strictly positive.
                | in
                | double iHeigth [in] The height of the area. The value must be strictly positive.
                |
                | Returns:
                | Un HRESULT
                | S_OK  The print area was successfully defined.
                | E_FAIL  No print area could be defined.

        :param i_x:
        :param i_y:
        :param i_width:
        :param i_height:
        :return:
        """
        return self.printarea.SetArea(i_x, i_y, i_width, i_height)

    def __repr__(self):
        return f'PrintArea()'
