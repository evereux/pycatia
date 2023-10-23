#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class PrintArea(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PrintArea
                | 
                | Manages print area of drawing sheet.
                | 
                | This interface is obtained from DrawingSheet.PrintArea method.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.print_area = com_object

    @property
    def activation_state(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ActivationState(boolean iActivated)
                | 
                |     Activates or deactivates the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             boolean iActivated [in] The activation state of the print area
                |             (TRUE means activated, FALSE means deactivated). 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |             The activation state could be valuated. 
                |         E_FAIL
                |             No activation or deactivation possible.

        :rtype: bool
        """

        return self.print_area.ActivationState

    @activation_state.setter
    def activation_state(self, value: bool):
        """
        :param bool value:
        """

        self.print_area.ActivationState = value

    @property
    def area_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AreaHeigth(double iHeigth)
                | 
                |     Valuates the height of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iHeigth [in] The height of the print area. The value must be
                |             strictly positive. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :rtype: float
        """

        return self.print_area.Area_Height

    @area_height.setter
    def area_height(self, value: float):
        """
        :param float value:
        """

        self.print_area.AreaHeigth = value

    @property
    def area_low_x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AreaLowX(double iX)
                | 
                |     Valuates the low x coordinate of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iX [in] The low x coordinate. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :rtype: float
        """

        return self.print_area.AreaLowX

    @area_low_x.setter
    def area_low_x(self, value: float):
        """
        :param float value:
        """

        self.print_area.AreaLowX = value

    @property
    def area_low_y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AreaLowY(double iY)
                | 
                |     Valuates the low y coordinate of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iY [in] The low y coordinate. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :rtype: float
        """

        return self.print_area.AreaLowY

    @area_low_y.setter
    def area_low_y(self, value: float):
        """
        :param float value:
        """

        self.print_area.AreaLowY = value

    @property
    def area_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AreaWidth(double iWidth)
                | 
                |     Valuates the width of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iWidth [in] The width of the print area. The value must be
                |             strictly positive. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :rtype: float
        """

        return self.print_area.AreaWidth

    @area_width.setter
    def area_width(self, value: float):
        """
        :param float value:
        """

        self.print_area.AreaWidth = float

    def get_area(self, o_x: float, o_y: float, o_width: float, o_height: float, o_activated: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetArea(double oX,
                | double oY,
                | double oWidth,
                | double oHeigth,
                | boolean oActivated)
                | 
                |     Gets the printing area defined on an object. Also communicates the
                |     activation state of the printing area. 
                | All the values are given in mm.
                | 
                | Parameters:
                | 
                |     out
                |         double oX [out] The low x coordinate of the area. 
                |     out
                |         double oY [out] The low y coordinate of the area. 
                |     out
                |         double oWidth [out] The width of the area. 
                |     out
                |         double oHeigth [out] The height of the area.
                |     out
                |         boolean oActivated [out] The activation state of the print area (TRUE
                |         means activated, FALSE means deactivated). 
                | 
                | Returns:
                |     Un HRESULT
                | 
                |     S_OK
                |         The print area was succesfully retrieved. 
                |     E_FAIL
                |         No print area could be retrived.


        :rtype: None
        """

        vba_function_name = 'get_area'
        vba_code = """
        Public Function get_area(print_area)
            Dim area (5)
            print_area.GetArea area
            get_area = area
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_area(self, i_x: float, i_y: float, i_width: float, i_height: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetArea(double iX,
                | double iY,
                | double iWidth,
                | double iHeigth)
                | 
                |     Sets a set of coordinates to define a rectangle print area.
                |     
                | All the values are given in mm.
                | 
                | Parameters:
                | 
                |     in
                |         double iX [in] The low x coordinate of the area. 
                |     in
                |         double iY [in] The low y coordinate of the area. 
                |     in
                |         double iWidth [in] The width of the area. The value must be strictly
                |         positive. 
                |     in
                |         double iHeigth [in] The height of the area. The value must be strictly
                |         positive. 
                | 
                | Returns:
                |     Un HRESULT
                | 
                |     S_OK
                |         The print area was successfully defined. 
                |     E_FAIL
                |         No print area could be defined.

        :param float i_x:
        :param float i_y:
        :param float i_width:
        :param float i_height:
        :rtype: None
        """
        return self.print_area.SetArea(i_x, i_y, i_width, i_height)

    def __repr__(self):
        return f'PrintArea(name="{ self.name }")'
