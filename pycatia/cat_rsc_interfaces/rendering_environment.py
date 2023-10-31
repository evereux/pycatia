#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_rsc_interfaces.rendering_environment_wall import RenderingEnvironmentWall
from pycatia.system_interfaces.any_object import AnyObject


class RenderingEnvironment(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RenderingEnvironment
                | 
                | Represents a Environment object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_environment = com_object

    @property
    def active_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveStatus() As short
                | 
                |     Returns or sets the environment active status.
                |     Only one environment can be active for a product. The active status can
                |     be:
                |     1: environment is activated
                |     0: environment is deactivated

        :rtype: int
        """

        return self.rendering_environment.ActiveStatus

    @active_status.setter
    def active_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment.ActiveStatus = value

    @property
    def face_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FaceNumber() As short
                | 
                |     Returns or sets the spherical environment face number.
                |     The default value for a new spherical environment is 2.
                |     If face number is set to 1, a mapped texture image will covered whole
                |     environment sphere.
                |     If face number is set to 2, two different texture images can be mapped for
                |     upper hemisphere and lower hemisphere.
                |     N.B. This property is useless for cubical and cylindrical environments.

        :rtype: int
        """

        return self.rendering_environment.FaceNumber

    @face_number.setter
    def face_number(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment.FaceNumber = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Height() As double
                | 
                |     Returns or sets the cubic or cylindrical environment height value.

        :rtype: float
        """

        return self.rendering_environment.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment.Height = value

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Length() As double
                | 
                |     Returns or sets the cubic environment length value.

        :rtype: float
        """

        return self.rendering_environment.Length

    @length.setter
    def length(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment.Length = value

    @property
    def radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Radius() As double
                | 
                |     Returns or sets the spherical or cylindrical environment radius value.

        :rtype: float
        """

        return self.rendering_environment.Radius

    @radius.setter
    def radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment.Radius = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Width() As double
                | 
                |     Returns or sets the cubic environment width value.

        :rtype: float
        """

        return self.rendering_environment.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment.Width = value

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns the coordinates of the origin of the environment.
                |     These coordinates are set as an array of 3 Variants (double type).

        :param tuple o_origin:
        :rtype: None
        """
        return self.rendering_environment.GetOrigin(o_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(rendering_environment)
        # #     Dim oOrigin (2)
        # #     rendering_environment.GetOrigin oOrigin
        # #     get_origin = oOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetType() As short
                | 
                |     Returns the environment type.
                | 
                |         Possible environment types are:
                |         1: Cubical environment
                |         2: Spherical environment
                |         3: Cylindrical environment

        :rtype: int
        """
        return self.rendering_environment.GetType()

    def get_vertical_axis(self, o_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetVerticalAxis(CATSafeArrayVariant oAxis)
                | 
                |     Returns the coordinates of the vertical axis vector of the
                |     environment.
                |     These coordinates are set as an array of 3 Variants (double type).

        :param tuple o_axis:
        :rtype: None
        """
        return self.rendering_environment.GetVerticalAxis(o_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_vertical_axis'
        # # vba_code = """
        # # Public Function get_vertical_axis(rendering_environment)
        # #     Dim oAxis (2)
        # #     rendering_environment.GetVerticalAxis oAxis
        # #     get_vertical_axis = oAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_wall(self, i_type: int) -> RenderingEnvironmentWall:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWall(short iType) As RenderingEnvironmentWall
                | 
                |     Returns the environment walls.
                |     The environment wall type can be:
                |     1: North wall (for cubical and cylindrical environments)
                |     2: South wall (for cubical and cylindrical environments)
                |     3: East wall (for cubical environments)
                |     4: West wall (for cubical environments)
                |     5: Top wall (for cubical, cylindrical and shperical
                |     environments)
                |     6: Bottom wall (for cubical, cylindrical and shperical
                |     environments)

        :param int i_type:
        :rtype: RenderingEnvironmentWall
        """
        return RenderingEnvironmentWall(self.rendering_environment.GetWall(i_type))

    def put_origin(self, i_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutOrigin(CATSafeArrayVariant iOrigin)
                | 
                |     Sets the coordinates of the origin of the environment.
                |     These coordinates are set as an array of 3 Variants (double
                |     type).
                | 
                |     Example:
                |         This example sets the origin of the MyEnvironment environment. to the
                |         point with coordinates (10, 25, 15).
                | 
                |          MyEnvironment.PutOrigin Array(10, 25, 15)

        :param tuple i_origin:
        :rtype: None
        """
        return self.rendering_environment.PutOrigin(i_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_origin'
        # # vba_code = """
        # # Public Function put_origin(rendering_environment)
        # #     Dim iOrigin (2)
        # #     rendering_environment.PutOrigin iOrigin
        # #     put_origin = iOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_vertical_axis(self, i_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutVerticalAxis(CATSafeArrayVariant iAxis)
                | 
                |     Sets the coordinates of the vertical axis vector of the
                |     environment.
                |     These coordinates are set as an array of 3 Variants (double type).

        :param tuple i_axis:
        :rtype: None
        """
        return self.rendering_environment.PutVerticalAxis(i_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_vertical_axis'
        # # vba_code = """
        # # Public Function put_vertical_axis(rendering_environment)
        # #     Dim iAxis (2)
        # #     rendering_environment.PutVerticalAxis iAxis
        # #     put_vertical_axis = iAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RenderingEnvironment(name="{self.name}")'
