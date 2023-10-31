#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapePositionTransfo(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapePositionTransfo
                | 
                | Represents the hybrid shape position transformation feature
                | object.
                | Role: To access the data of the hybrid shape position transformation feature
                | object. This data includes:
                | 
                |     The positioning mode
                |     The profile to be positioned
                |     The initila and target planes
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePositionTransfo
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_position_transfo = com_object

    @property
    def initial_direction_computation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InitialDirectionComputationMode() As long
                | 
                |     Gets or sets the computation mode of the X axis (or direction) of the
                |     initial axis system.
                | 
                |     Parameters:
                | 
                |         oDirCompMode
                |             computation mode =
                |             0 : no X axis specified
                |             1 : the X axis is implicitly the tangent
                |                 of the profile at the origin(the origin then HAS to be on the profile).
                |             2 : the X axis is specified by a direction by SetPositionDirection(1,UserInputDirection).

        :rtype: int
        """

        return self.hybrid_shape_position_transfo.InitialDirectionComputationMode

    @initial_direction_computation_mode.setter
    def initial_direction_computation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_position_transfo.InitialDirectionComputationMode = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Mode() As long
                | 
                |     Returns or sets the positioning mode.
                |     Legal values:
                | 
                |     CATGSMPositionMode_NoneOrPositioned
                |         No positioning
                |     CATGSMPositionMode_ExplicitSweep
                |         The explicit profile is to be moved from its initial plane to the first
                |         sweep plane
                |     CATGSMPositionMode_Develop

        :rtype: int
        """

        return self.hybrid_shape_position_transfo.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_position_transfo.Mode = value

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Profile() As Reference
                | 
                |     Returns or sets the profile to be positioned.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_position_transfo.Profile)

    @profile.setter
    def profile(self, reference_profile: Reference):
        """
        :param Reference reference_profile:
        """

        self.hybrid_shape_position_transfo.Profile = reference_profile.com_object

    def get_nb_pos_angle(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbPosAngle() As long
                | 
                |     Gets the number of numerical positioning parameters : first axis direction angles.
                | 
                |     Parameters:
                | 
                |         oI
                |             Number of parameters

        :rtype: int
        """
        return self.hybrid_shape_position_transfo.GetNbPosAngle()

    def get_nb_pos_coord(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbPosCoord() As long
                | 
                |     Gets the number of numerical positioning parameters : origin planar coordinates.
                | 
                |     Parameters:
                | 
                |         oI
                |             Number of parameters

        :rtype: int
        """
        return self.hybrid_shape_position_transfo.GetNbPosCoord()

    def get_pos_angle(self, i_i: int) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosAngle(long iI) As Angle
                | 
                |     Returns angles of both initial and target coordinate systems from default
                |     positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             The index of numerical positioning angles in initial (value 1) or
                |             target (value 2) axis system. 
                |         oAngle
                |             The angle value.

        :param int i_i:
        :rtype: Angle
        """
        return Angle(self.hybrid_shape_position_transfo.GetPosAngle(i_i))

    def get_pos_coord(self, ii: int) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosCoord(long ii) As Length
                | 
                |     Returns translation coordinates if both initial and target coordinate
                |     systems from default positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             The iIndex of numerical positioning coordinates in initial (value 1
                |             or 2) or target (value 3 or 4) coordinate system. 
                |         oCoordinate
                |             The coordinate value

        :param int ii:
        :rtype: Length
        """
        return Length(self.hybrid_shape_position_transfo.GetPosCoord(ii))

    def get_pos_point(self, ii: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosPoint(long ii) As Reference
                | 
                |     Returns the points designated as the origins of the initial and target
                |     planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         oElem
                |             The origin point

        :param int ii:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_position_transfo.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosSwapAxes(long ii) As long
                | 
                |     Returns axis inversion from previous definitions for both initial and
                |     target planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The coordinate system index: 1 for initial one, 2 for target one
                |             
                |         oInversion
                |             The inversion value:
                | 
                |             CATGSMAxisInversionMode_None
                |                 No axis inverted
                |             CATGSMAxisInversionMode_X
                |                 Only the X axis iq inverted
                |             CATGSMAxisInversionMode_Y
                |                 Only the Y axis is inverted
                |             CATGSMAxisInversionMode_Both
                |                 Both axes inverted

        :param int ii:
        :rtype: int
        """
        return self.hybrid_shape_position_transfo.GetPosSwapAxes(ii)

    def get_position_direction(self, i_i: int) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPositionDirection(long iI) As HybridShapeDirection
                | 
                |     Returns the positioning directions.
                |     The positioning direction can be initial or target plane X-axis
                |     direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         oElem
                |             The direction element

        :param int i_i:
        :rtype: HybridShapeDirection
        """
        return HybridShapeDirection(self.hybrid_shape_position_transfo.GetPositionDirection(i_i))

    def remove_all_pos_angle(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAllPosAngle()
                | 
                |     Removes all numerical positioning parameters : first axis direction angles.

        :rtype: None
        """
        return self.hybrid_shape_position_transfo.RemoveAllPosAngle()

    def remove_all_pos_coord(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAllPosCoord()
                | 
                |     Removes all numerical positioning parameters : origin planar coordinates.

        :rtype: None
        """
        return self.hybrid_shape_position_transfo.RemoveAllPosCoord()

    def set_pos_angle(self, i_i: int, i_angle: Angle) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosAngle(long iI,
                | Angle iAngle)
                | 
                |     Sets angles of both initial and target coordinate systems.
                | 
                |     Parameters:
                | 
                |         iI
                |             The index of numerical positioning angles in initial (value 1) or
                |             target (value 2) axis system. 
                |         iAngle
                |             The angle value.

        :param int i_i:
        :param Angle i_angle:
        :rtype: None
        """
        return self.hybrid_shape_position_transfo.SetPosAngle(i_i, i_angle.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pos_angle'
        # # vba_code = """
        # # Public Function set_pos_angle(hybrid_shape_position_transfo)
        # #     Dim iI (2)
        # #     hybrid_shape_position_transfo.SetPosAngle iI
        # #     set_pos_angle = iI
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pos_coord(self, i_i: int, i_coordinate: Length) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosCoord(long iI,
                | Length iCoordinate)
                | 
                |     Sets translation coordinates of both initial and target coordinate
                |     systems.
                | 
                |     Parameters:
                | 
                |         iI
                |             The iIndex of numerical positioning coordinates in initial (value 1
                |             or 2) or target (value 3 or 4) coordinate system. 
                |         iCoordinate
                |             The coordinate value

        :param int i_i:
        :param Length i_coordinate:
        :rtype: None
        """
        return self.hybrid_shape_position_transfo.SetPosCoord(i_i, i_coordinate.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pos_coord'
        # # vba_code = """
        # # Public Function set_pos_coord(hybrid_shape_position_transfo)
        # #     Dim iI (2)
        # #     hybrid_shape_position_transfo.SetPosCoord iI
        # #     set_pos_coord = iI
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pos_point(self, i_i: int, i_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosPoint(long iI,
                | Reference iElem)
                | 
                |     Sets the points designated as the origins of the initial and target
                |     planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         iElem
                |             The origin point

        :param int i_i:
        :param Reference i_elem:
        :rtype: None
        """
        return self.hybrid_shape_position_transfo.SetPosPoint(i_i, i_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pos_point'
        # # vba_code = """
        # # Public Function set_pos_point(hybrid_shape_position_transfo)
        # #     Dim iI (2)
        # #     hybrid_shape_position_transfo.SetPosPoint iI
        # #     set_pos_point = iI
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pos_swap_axes(self, ii: int, i_inversion: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosSwapAxes(long ii,
                | long iInversion)
                | 
                |     Sets axis inversion from previous definitions for both initial and target
                |     planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The coordinate system index: 1 for initial one, 2 for target one
                |             
                |         iInversion
                |             The inversion value:
                | 
                |             CATGSMAxisInversionMode_None
                |                 No axis inverted
                |             CATGSMAxisInversionMode_X
                |                 Only the X axis iq inverted
                |             CATGSMAxisInversionMode_Y
                |                 Only the Y axis is inverted
                |             CATGSMAxisInversionMode_Both
                |                 Both axes inverted

        :param int ii:
        :param int i_inversion:
        :rtype: None
        """
        return self.hybrid_shape_position_transfo.SetPosSwapAxes(ii, i_inversion)

    def set_position_direction(self, i_i: int, i_elem: HybridShapeDirection) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPositionDirection(long iI,
                | HybridShapeDirection iElem)
                | 
                |     Sets the positioning directions.
                |     The positioning direction can be initial or target plane X-axis
                |     direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         iElem
                |             The direction element

        :param int i_i:
        :param HybridShapeDirection i_elem:
        :rtype: None
        """
        return self.hybrid_shape_position_transfo.SetPositionDirection(i_i, i_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_position_direction'
        # # vba_code = """
        # # Public Function set_position_direction(hybrid_shape_position_transfo)
        # #     Dim iI (2)
        # #     hybrid_shape_position_transfo.SetPositionDirection iI
        # #     set_position_direction = iI
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapePositionTransfo(name="{self.name}")'
