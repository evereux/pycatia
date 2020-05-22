#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePositionTransfo(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape position transformation feature
                | object.Role: To access the data of the hybrid shape position
                | transformation feature object. This data includes:Use the
                | CATIAHybridShapeFactory to create a HybridShapePositionTransfo object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_position_transfo = com_object     

    @property
    def initial_direction_computation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InitialDirectionComputationMode
                | o Property InitialDirectionComputationMode(    ) As
                | 
                | Gets or sets the computation mode of the X axis (or
                | direction) of the initial axis system.

        :return:
        """
        return self.hybrid_shape_position_transfo.InitialDirectionComputationMode

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mode
                | o Property Mode(    ) As
                | 
                | Returns or sets the positioning mode. Legal values:
                | CATGSMPositionMode_NoneOrPositioned No positioning
                | CATGSMPositionMode_ExplicitSweep The explicit profile is to
                | be moved from its initial plane to the first sweep plane
                | CATGSMPositionMode_Develop

        :return:
        """
        return self.hybrid_shape_position_transfo.Mode

    @mode.setter
    def mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_position_transfo.Mode = value 

    @property
    def profile(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Profile
                | o Property Profile(    ) As
                | 
                | Returns or sets the profile to be positioned.

        :return:
        """
        return self.hybrid_shape_position_transfo.Profile

    @profile.setter
    def profile(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_position_transfo.Profile = value 

    def get_nb_pos_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbPosAngle
                | o Func GetNbPosAngle(    ) As
                | 
                | Gets the number of numerical positioning parameters : first
                | axis direction angles.
                |
                | Parameters:
                | oI
                |      Number of parameters


        :return:
        """
        return self.hybrid_shape_position_transfo.GetNbPosAngle()

    def get_nb_pos_coord(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbPosCoord
                | o Func GetNbPosCoord(    ) As
                | 
                | Gets the number of numerical positioning parameters : origin
                | planar coordinates.
                |
                | Parameters:
                | oI
                |       Number of parameters


        :return:
        """
        return self.hybrid_shape_position_transfo.GetNbPosCoord()

    def get_pos_angle(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosAngle
                | o Func GetPosAngle(        iI) As
                | 
                | Returns angles of both initial and target coordinate systems
                | from default positions.
                |
                | Parameters:
                | iI
                |     The index of numerical positioning angles in initial
                |            (value 1) or target (value 2) axis system.
                |  
                |  oAngle
                |     The angle value.


        :param i_i:
        :return:
        """
        return self.hybrid_shape_position_transfo.GetPosAngle(i_i)

    def get_pos_coord(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosCoord
                | o Func GetPosCoord(        ii) As
                | 
                | Returns translation coordinates if both initial and target
                | coordinate systems from default positions.
                |
                | Parameters:
                | iI
                |     The iIndex of numerical positioning coordinates in initial
                |            (value 1 or 2) or target (value 3 or 4) coordinate system.
                |  
                |  oCoordinate
                |     The coordinate value


        :param ii:
        :return:
        """
        return self.hybrid_shape_position_transfo.GetPosCoord(ii)

    def get_pos_point(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosPoint
                | o Func GetPosPoint(        ii) As
                | 
                | Returns the points designated as the origins of the initial
                | and target planes.
                |
                | Parameters:
                | iI
                |     The plane index: 1 for initial one, 2 for target one
                |  
                |  oElem
                |     The origin point


        :param ii:
        :return:
        """
        return self.hybrid_shape_position_transfo.GetPosPoint(ii)

    def get_pos_swap_axes(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosSwapAxes
                | o Func GetPosSwapAxes(        ii) As
                | 
                | Returns axis inversion from previous definitions for both
                | initial and target planes.
                |
                | Parameters:
                | iI
                |     The coordinate system index: 1 for initial one, 2 for target one
                |  
                |  oInversion
                |     The inversion value:
                |    
                | CATGSMAxisInversionMode_None
                | No axis inverted
                | CATGSMAxisInversionMode_X
                | Only the X axis iq inverted
                | CATGSMAxisInversionMode_Y
                | Only the Y axis is inverted
                | CATGSMAxisInversionMode_Both
                | Both axes inverted


        :param ii:
        :return:
        """
        return self.hybrid_shape_position_transfo.GetPosSwapAxes(ii)

    def get_position_direction(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPositionDirection
                | o Func GetPositionDirection(        iI) As
                | 
                | Returns the positioning directions. The positioning
                | direction can be initial or target plane X-axis direction.
                |
                | Parameters:
                | iI
                |     The plane index: 1 for initial one, 2 for target one
                |  
                |  oElem
                |     The direction element


        :param i_i:
        :return:
        """
        return self.hybrid_shape_position_transfo.GetPositionDirection(i_i)

    def remove_all_pos_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllPosAngle
                | o Sub RemoveAllPosAngle(    )
                | 
                | Removes all numerical positioning parameters : first axis
                | direction angles.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_position_transfo.RemoveAllPosAngle()

    def remove_all_pos_coord(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllPosCoord
                | o Sub RemoveAllPosCoord(    )
                | 
                | Removes all numerical positioning parameters : origin planar
                | coordinates.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_position_transfo.RemoveAllPosCoord()

    def set_pos_angle(self, i_i, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosAngle
                | o Sub SetPosAngle(        iI,
                |                           iAngle)
                | 
                | Sets angles of both initial and target coordinate systems.
                |
                | Parameters:
                | iI
                |     The index of numerical positioning angles in initial
                |            (value 1) or target (value 2) axis system.
                |  
                |  iAngle
                |     The angle value.


        :param i_i:
        :param i_angle:
        :return:
        """
        return self.hybrid_shape_position_transfo.SetPosAngle(i_i, i_angle)

    def set_pos_coord(self, i_i, i_coordinate):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosCoord
                | o Sub SetPosCoord(        iI,
                |                           iCoordinate)
                | 
                | Sets translation coordinates of both initial and target
                | coordinate systems.
                |
                | Parameters:
                | iI
                |     The iIndex of numerical positioning coordinates in initial
                |            (value 1 or 2) or target (value 3 or 4) coordinate system.
                |  
                |  iCoordinate
                |     The coordinate value


        :param i_i:
        :param i_coordinate:
        :return:
        """
        return self.hybrid_shape_position_transfo.SetPosCoord(i_i, i_coordinate)

    def set_pos_point(self, i_i, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosPoint
                | o Sub SetPosPoint(        iI,
                |                           iElem)
                | 
                | Sets the points designated as the origins of the initial and
                | target planes.
                |
                | Parameters:
                | iI
                |     The plane index: 1 for initial one, 2 for target one
                |  
                |  iElem
                |     The origin point


        :param i_i:
        :param i_elem:
        :return:
        """
        return self.hybrid_shape_position_transfo.SetPosPoint(i_i, i_elem)

    def set_pos_swap_axes(self, ii, i_inversion):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosSwapAxes
                | o Sub SetPosSwapAxes(        ii,
                |                              iInversion)
                | 
                | Sets axis inversion from previous definitions for both
                | initial and target planes.
                |
                | Parameters:
                | iI
                |     The coordinate system index: 1 for initial one, 2 for target one
                |  
                |  iInversion
                |     The inversion value:
                |    
                | CATGSMAxisInversionMode_None
                | No axis inverted
                | CATGSMAxisInversionMode_X
                | Only the X axis iq inverted
                | CATGSMAxisInversionMode_Y
                | Only the Y axis is inverted
                | CATGSMAxisInversionMode_Both
                | Both axes inverted


        :param ii:
        :param i_inversion:
        :return:
        """
        return self.hybrid_shape_position_transfo.SetPosSwapAxes(ii, i_inversion)

    def set_position_direction(self, i_i, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPositionDirection
                | o Sub SetPositionDirection(        iI,
                |                                    iElem)
                | 
                | Sets the positioning directions. The positioning direction
                | can be initial or target plane X-axis direction.
                |
                | Parameters:
                | iI
                |     The plane index: 1 for initial one, 2 for target one
                |  
                |  iElem
                |     The direction element


        :param i_i:
        :param i_elem:
        :return:
        """
        return self.hybrid_shape_position_transfo.SetPositionDirection(i_i, i_elem)

    def __repr__(self):
        return f'HybridShapePositionTransfo()'
