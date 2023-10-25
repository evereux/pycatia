#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ArrangementItemReservation(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementItemReservation
                | 
                | Use this object to access the ArrangementItemReservation properties and
                | methods.
                | Role: Use this object to control the visualization mode, dimensions of the
                | ArrangementItemReservation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_item_reservation = com_object

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Height() As double
                | 
                |     Returns or sets the height of the
                |     ArrangementItemReservation.
                | 
                |     Example:
                |         This example retrieves the Height of the objItemRes1
                |         object.
                | 
                |          Dim dblHeight   As Double
                |          dblHeight  = objItemRes1.Height

        :rtype: float
        """

        return self.arrangement_item_reservation.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.arrangement_item_reservation.Height = value

    @property
    def visu_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuMode() As CATArrangementItemResVisuMode
                | 
                |     Returns or set the Visualization Mode for the
                |     ArrangementItemReservation.
                | 
                |     Example:
                |         This example Sets the Visualization Mode of the objItemRes1 object to
                |         CatArrangementItemReservationVisuModeBox .
                | 
                |          objItemRes1.VisuMode = CatArrangementItemReservationVisuModeBox

        :return: enum cat_arrangement_item_res_visu_mode
        :rtype: int
        """

        return self.arrangement_item_reservation.VisuMode

    @visu_mode.setter
    def visu_mode(self, value: int):
        """
        :param int value: enum cat_arrangement_item_res_visu_mode
        """

        self.arrangement_item_reservation.VisuMode = value

    @property
    def x_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property XLength() As double
                | 
                |     Returns or sets the XLength of the
                |     ArrangementItemReservation.
                | 
                |     Example:
                |         This example retrieves the XLength of the objItemRes1
                |         object.
                | 
                |          Dim dblXLength   As Double
                |          dblXLength  = objItemRes1.XLength

        :rtype: float
        """

        return self.arrangement_item_reservation.XLength

    @x_length.setter
    def x_length(self, value: float):
        """
        :param float value:
        """

        self.arrangement_item_reservation.XLength = value

    @property
    def y_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property YLength() As double
                | 
                |     Returns or sets the YLength of the
                |     ArrangementItemReservation.
                | 
                |     Example:
                |         This example retrieves the YLength of the objItemRes1
                |         object.
                | 
                |          Dim dblYLength   As Double
                |          dblYLength  = objItemRes1.YLength

        :rtype: float
        """

        return self.arrangement_item_reservation.YLength

    @y_length.setter
    def y_length(self, value: float):
        """
        :param float value:
        """

        self.arrangement_item_reservation.YLength = value

    def get_dimension(self, io_item_res_dimensions: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDimension(CATSafeArrayVariant ioItemResDimensions)
                | 
                |     Returns the Dimensions of the ArrangementItemReservation.
                | 
                |     Parameters:
                | 
                |         ioItemResDimensions
                |             The output array initialized with the dimensions that make up the
                |             ArrangementItemReservation. The first three components represent the Minimum
                |             XCoord, YCoord and Z Coord while the remaining three components represent the
                |             Maximum XCoord, YCoord and Z Coord respectively.
                | 
                |             Example:
                |                 This example retrieves the coordinate dimensions of the
                |                 objItemRes1 object.
                | 
                |                  Dim dblDimension(6)   As Double
                |                  objItemRes1.GetDimension(dblDimension)

        :param tuple io_item_res_dimensions:
        :rtype: None
        """
        return self.arrangement_item_reservation.GetDimension(io_item_res_dimensions)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_dimension'
        # # vba_code = """
        # # Public Function get_dimension(arrangement_item_reservation)
        # #     Dim ioItemResDimensions (2)
        # #     arrangement_item_reservation.GetDimension ioItemResDimensions
        # #     get_dimension = ioItemResDimensions
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTechnologicalObject(CATBSTR iApplicationType) As
                | CATBaseDispatch
                | 
                |     Returns the applicative data whose type is the given
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iApplicationType
                |             The type of applicative data searched. 
                |         oApplicativeObj
                |             The matched applicative object.
                | 
                |             Example:
                |                 This example retrieves the desired applicative object from the
                |                 objItemRes1 object.
                | 
                |                  Dim objProd   As Product
                |                  objProd  = objItemRes1.GetTechnologicalObject("Product")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.arrangement_item_reservation.GetTechnologicalObject(i_application_type)

    def set_dimension(self, i_item_res_dimensions: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDimension(CATSafeArrayVariant iItemResDimensions)
                | 
                |     Sets the Dimensions of the ArrangementItemReservation.
                | 
                |     Parameters:
                | 
                |         iItemResDimensions
                |             The input array initialized with the dimensions that make up the
                |             ArrangementItemReservation. The first three components represent the Minimum
                |             XCoord, YCoord and Z Coord while the remaining three components represent the
                |             Maximum XCoord, YCoord and Z Coord respectively.
                | 
                |             Example:
                |                 This example sets the coordinate dimensions of the objItemRes1
                |                 object.
                | 
                |                  Dim dblDimension(6)   As Double
                |                  dblDimension(0)       = 300.0 '//XMin
                |                  dblDimension(1)       = 500.0 '//YMin
                |                  dblDimension(2)       = 300.0 '//ZMin
                |                  dblDimension(3)       = 500.0 '//XMax
                |                  dblDimension(4)       = 0.0   '//YMax
                |                  dblDimension(5)       = 300.0 '//ZMax
                |                  objItemRes1.SetDimension(dblDimension)

        :param tuple i_item_res_dimensions:
        :rtype: None
        """
        return self.arrangement_item_reservation.SetDimension(i_item_res_dimensions)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dimension'
        # # vba_code = """
        # # Public Function set_dimension(arrangement_item_reservation)
        # #     Dim iItemResDimensions (2)
        # #     arrangement_item_reservation.SetDimension iItemResDimensions
        # #     set_dimension = iItemResDimensions
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementItemReservation(name="{self.name}")'
