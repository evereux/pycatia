#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeDevelop(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeDevelop
                | 
                | Represents the hybrid shape develop feature object.
                | Role: To access the data of the hybrid shape develop feature object. This data
                | includes:
                | 
                |     The developing mode
                |     The positining mode used for the 2D wire
                |     The 2D wire to be developed
                |     The positioning transformation
                |     The support revolution surface on which the development is
                |     operated
                |     The point designated as the origin of the planar 2D wire
                |     The direction corresponding to the first axis of the planar axis system
                |     related to the planar 2D wire
                |     The development origin on the support surface
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeDevelop
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_develop = com_object

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Mode() As long
                | 
                |     Returns or sets the developing mode.
                |     Legal values:
                | 
                |     CATGSMDevelopMethod_DevDev
                |         Develop / develop algorithm
                |     CATGSMDevelopMethod_DevProj
                |         Develop / project algorithm

        :return: int
        """

        return self.hybrid_shape_develop.Mode

    @mode.setter
    def mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_develop.Mode = value

    @property
    def mode_pos(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ModePos() As long
                | 
                |     Returns or sets the positioning mode used for the 2D wire.
                |     Legal values:
                | 
                |     CATGSMPositionMode_NoneOrPositioned
                |         No positioning 
                |     CATGSMPositionMode_ExplicitSweep
                |     CATGSMPositionMode_Develop
                |         The 2D wire is to be moved from its initial position

        :return: int
        """

        return self.hybrid_shape_develop.ModePos

    @mode_pos.setter
    def mode_pos(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_develop.ModePos = value

    @property
    def plane_axis_direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PlaneAxisDirection() As Reference
                | 
                |     Returns or sets the direction corresponding to the first axis of the planar
                |     axis system related to the planar 2D wire.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     BiDimFeatEdge or RectilinearMonoDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_develop.PlaneAxisDirection)

    @plane_axis_direction.setter
    def plane_axis_direction(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_develop.PlaneAxisDirection = value

    @property
    def plane_axis_origin(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PlaneAxisOrigin() As Reference
                | 
                |     Returns or sets the point designated as the origin of the planar 2D
                |     wire.
                |     Sub-element(s) supported (see Boundary object): Vertex.

        :return: Reference
        """

        return Reference(self.hybrid_shape_develop.PlaneAxisOrigin)

    @plane_axis_origin.setter
    def plane_axis_origin(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_develop.PlaneAxisOrigin = value

    @property
    def point_on_support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PointOnSupport() As Reference
                | 
                |     Returns or sets the development origin on the support
                |     surface.
                |     Sub-element(s) supported (see Boundary object): Vertex.

        :return: Reference
        """

        return Reference(self.hybrid_shape_develop.PointOnSupport)

    @point_on_support.setter
    def point_on_support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_develop.PointOnSupport = value

    @property
    def positioned_wire(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PositionedWire() As Reference
                | 
                |     Returns or sets the positioning transformation.
                |     Role: To retrieve or set the positioning transformation associated to the
                |     develop feature and which result corresponds to the positioned 2D wire.

        :return: Reference
        """

        return Reference(self.hybrid_shape_develop.PositionedWire)

    @positioned_wire.setter
    def positioned_wire(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_develop.PositionedWire = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support revolution surface on which the development is
                |     operated.
                |     Sub-element(s) supported (see Boundary object): Face.

        :return: Reference
        """

        return Reference(self.hybrid_shape_develop.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_develop.Support = value

    @property
    def wire_to_develop(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WireToDevelop() As Reference
                | 
                |     Returns or sets the 2D wire to be developed.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_develop.WireToDevelop)

    @wire_to_develop.setter
    def wire_to_develop(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_develop.WireToDevelop = value

    def get_plane_axis_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPlaneAxisAngle() As Angle
                | 
                |     Retrieves the rotation angle.
                |     Role: The rotation angle is expressed in the planar coordinate system
                |     related to the 2D planar wire from its default position.
                | 
                |     Returns:
                |         The rotation value

        :return: Angle
        """
        return Angle(self.hybrid_shape_develop.GetPlaneAxisAngle())

    def get_plane_axis_coord(self, i_coor_idx):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPlaneAxisCoord(long iCoorIdx) As Length
                | 
                |     Retrieves the translation coordinates.
                |     Role: The translation coordinates are expressed with respect to the planar
                |     coordinate system related to the 2D planar wire from its default position.
                |     GetPlaneAxisCoord retrieves one coordinate at a time.
                | 
                |     Parameters:
                | 
                |         iCoorIdx
                |             The coordinate index
                |             Legal values
                |             : 1 for X and 2 for Y 
                | 
                |     Returns:
                |         The coordinate value

        :param int i_coor_idx:
        :return: Length
        """
        return Length(self.hybrid_shape_develop.GetPlaneAxisCoord(i_coor_idx))

    def get_plane_axis_swap_axes(self, ii):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPlaneAxisSwapAxes(long ii) As long
                | 
                |     Retrieves the inversion axes from their previous
                |     definitions.
                | 
                |     Parameters:
                | 
                |         iI
                |             == NOT USED YET == Must always be set to 0 
                | 
                |     Returns:
                |         The inversion value
                |         Legal values:
                | 
                |         CATGSMAxisInversionMode_None
                |             No axis inverted 
                |         CATGSMAxisInversionMode_X
                |             Only the X axis is inverted
                |         CATGSMAxisInversionMode_Y
                |             Only the Y axis is inverted
                |         CATGSMAxisInversionMode_Both
                |             Both axes are inverted

        :param int ii:
        :return: int
        """
        return self.hybrid_shape_develop.GetPlaneAxisSwapAxes(ii)

    def set_plane_axis_angle(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneAxisAngle(double iAngle)
                | 
                |     Sets the rotation angle.
                |     Role: The rotation angle is expressed in the planar coordinate system
                |     related to the 2D planar wire from its default position.
                | 
                |     Parameters:
                | 
                |         iAngle
                |             The rotation angle value.

        :param float i_angle:
        :return: None
        """
        return self.hybrid_shape_develop.SetPlaneAxisAngle(i_angle)

    def set_plane_axis_coord(self, i_coor_idx, i_coord_value):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneAxisCoord(long iCoorIdx,
                | double iCoordValue)
                | 
                |     Sets the translation coordinates.
                |     Role: The translation coordinates are expressed with respect to the planar
                |     coordinate system related to the 2D planar wire from its default position.
                |     SetPlaneAxisCoord sets one coordinate at a time.
                | 
                |     Parameters:
                | 
                |         iCoorIdx
                |             The coordinate index
                |             Legal values
                |             : 1 for X and 2 for Y 
                |         iCoordValue
                |             The coordinate value

        :param int i_coor_idx:
        :param float i_coord_value:
        :return: None
        """
        return self.hybrid_shape_develop.SetPlaneAxisCoord(i_coor_idx, i_coord_value)

    def set_plane_axis_swap_axes(self, i_idx, i_inversion_value):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneAxisSwapAxes(long iIdx,
                | long iInversionValue)
                | 
                |     Sets the inversion axes from their previous definitions.
                | 
                |     Parameters:
                | 
                |         iIdx
                |             == NOT USED YET == Must always be set to 0 
                |         iInversionValue
                |             The inversion value
                |             Legal values:
                | 
                |             CATGSMAxisInversionMode_None
                |                 No axis inverted 
                |             CATGSMAxisInversionMode_X
                |                 Only the X axis is inverted
                |             CATGSMAxisInversionMode_Y
                |                 Only the Y axis is inverted
                |             CATGSMAxisInversionMode_Both
                |                 Both axes are inverted

        :param int i_idx:
        :param int i_inversion_value:
        :return: None
        """
        return self.hybrid_shape_develop.SetPlaneAxisSwapAxes(i_idx, i_inversion_value)

    def __repr__(self):
        return f'HybridShapeDevelop(name="{ self.name }")'
