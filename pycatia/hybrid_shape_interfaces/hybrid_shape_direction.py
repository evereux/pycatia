#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeDirection(HybridShape):
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
                |                         HybridShapeDirection
                | 
                | Represents the hybrid shape direction feature object.
                | Role: To access the data of the hybrid shape direction feature object. A
                | direction can be specified using:
                | 
                |     A line: the direction is tangent to the line
                |     A plane: the direction is normal to the plane
                |     Its components
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeDirection
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_direction = com_object

    @property
    def object(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Object() As Reference
                | 
                |     Returns or sets the object that specifies the direction.
                |     This object can be a line or a plane.
                | 
                |     Parameters:
                | 
                |         oObject
                |             The object (a line or a plane) that specifies the
                |             direction
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge
                |         or RectilinearMonoDimFeatEdge.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_direction.Object)

    @object.setter
    def object(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_direction.Object = reference.com_object

    @property
    def ref_axis_system(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RefAxisSystem() As Reference
                | 
                |     Returns or Sets the reference Axis System for Direction
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis system.
                |     
                | Example
                | :
                |     This example retrieves in oRefAxis the reference Axis System for Direction
                |     feature.
                | 
                |      Dim oRefAxis As CATIAReference
                |      Set oRefAxis  = Direction.RefAxisSystem

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_direction.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, reference_axis: Reference):
        """
        :param Reference reference_axis:
        """

        self.hybrid_shape_direction.RefAxisSystem = reference_axis.com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As long (Read Only)
                | 
                |     Returns the direction type.
                |     Legal value: The direction type can be:
                | 
                |     0
                |         The direction is specified using an object (a line or a plane). In the
                |         case of a plane, the direction is the normal to the
                |         plane
                |     1
                |         The direction is specified using its components

        :rtype: int
        """

        return self.hybrid_shape_direction.Type

    def direction_specification(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func DirectionSpecification() As long
                | 
                |     Queries the direction specification status.
                | 
                |     Parameters:
                | 
                |         oDir
                |             direction specification = 0 : Direction is not specified. = 1 :
                |            Direction is specified and is valid. = -1 : Direction is specified but is not valid.

        :rtype: int
        """
        return self.hybrid_shape_direction.DirectionSpecification()

    def get_x(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetX() As RealParam
                | 
                |     Returns the direction X component. This method succeeds only when direction
                |     is specified using components. It fails when direction is specified using a
                |     geometrical element i.e Line, Plane. In such cases use GetXVal method
                |     instead.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The direction X component

        :rtype: RealParam
        """
        return RealParam(self.hybrid_shape_direction.GetX())

    def get_x_val(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetXVal() As double
                | 
                |     Returns the direction X component as Double. This method succeeds
                |     irrespective of the way direction is specified.
                | 
                |     Parameters:
                | 
                |         oX
                |             The direction X component

        :rtype: float
        """
        return self.hybrid_shape_direction.GetXVal()

    def get_y(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetY() As RealParam
                | 
                |     Returns the direction Y component. This method succeeds only when direction
                |     is specified using components. It fails when direction is specified using a
                |     geometrical element i.e Line, Plane. In such cases use GetYVal method
                |     instead.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The direction Y component

        :rtype: RealParam
        """
        return RealParam(self.hybrid_shape_direction.GetY())

    def get_y_val(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetYVal() As double
                | 
                |     Returns the direction Y component as Double.This method succeeds
                |     irrespective of the way direction is specified.
                | 
                |     Parameters:
                | 
                |         oY
                |             The direction Y component

        :rtype: float
        """
        return self.hybrid_shape_direction.GetYVal()

    def get_z(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetZ() As RealParam
                | 
                |     Returns the direction Z component. This method succeeds only when direction
                |     is specified using components. It fails when direction is specified using a
                |     geometrical element i.e Line, Plane. In such cases use GetZVal method
                |     instead.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The direction Z component

        :rtype: RealParam
        """
        return RealParam(self.hybrid_shape_direction.GetZ())

    def get_z_val(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetZVal() As double
                | 
                |     Returns the direction Z component as Double.This method succeeds
                |     irrespective of the way direction is specified.
                | 
                |     Parameters:
                | 
                |         oZ
                |             The direction Z component

        :rtype: float
        """
        return self.hybrid_shape_direction.GetZVal()

    def __repr__(self):
        return f'HybridShapeDirection(name="{self.name}")'
