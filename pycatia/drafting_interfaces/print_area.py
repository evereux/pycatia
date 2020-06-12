#! usr/bin/python3.6
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
    def activation_state(self):
        """
        .. note::
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

        :return: False
        """

        return None

    @activation_state.setter
    def activation_state(self, value):
        """
        :param False value:
        """

        self.print_area.ActivationState = value

    @property
    def area_heigth(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AreaHeigth(double iHeigth)
                | 
                |     Valuates the heigth of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iHeigth [in] The heigth of the print area. The value must be
                |             strictly positive. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :return: False
        """

        return None

    @area_heigth.setter
    def area_heigth(self, value):
        """
        :param False value:
        """

        self.print_area.AreaHeigth = value

    @property
    def area_low_x(self):
        """
        .. note::
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

        :return: False
        """

        return None

    @area_low_x.setter
    def area_low_x(self, value):
        """
        :param False value:
        """

        self.print_area.AreaLowX = value

    @property
    def area_low_y(self):
        """
        .. note::
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

        :return: False
        """

        return None

    @area_low_y.setter
    def area_low_y(self, value):
        """
        :param False value:
        """

        self.print_area.AreaLowY = value

    @property
    def area_width(self):
        """
        .. note::
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

        :return: False
        """

        return None

    @area_width.setter
    def area_width(self, value):
        """
        :param False value:
        """

        self.print_area.AreaWidth = value

    def get_area(self, o_x, o_y, o_width, o_heigth, o_activated):
        """
        .. note::
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
                |         double oHeigth [out] The heigth of the area. 
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

        :param float o_x:
        :param float o_y:
        :param float o_width:
        :param float o_heigth:
        :param bool o_activated:
        :return: None
        """
        return self.print_area.GetArea(o_x, o_y, o_width, o_heigth, o_activated)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_area'
        # # vba_code = """
        # # Public Function get_area(print_area)
        # #     Dim oX (2)
        # #     print_area.GetArea oX
        # #     get_area = oX
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_area(self, i_x, i_y, i_width, i_heigth):
        """
        .. note::
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
                |         double iHeigth [in] The heigth of the area. The value must be strictly
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
        :param float i_heigth:
        :return: None
        """
        return self.print_area.SetArea(i_x, i_y, i_width, i_heigth)

    def __repr__(self):
        return f'PrintArea(name="{ self.name }")'
