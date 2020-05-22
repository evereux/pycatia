#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.realparam import RealParam
from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeDirection(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape direction feature object.Role: To access
                | the data of the hybrid shape direction feature object. A direction can
                | be specified using:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeDirection object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_direction = com_object

    @property
    def object(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Object
                | o Property Object(    ) As
                | 
                | Returns or sets the object that specifies the direction.
                | This object can be a line or a plane.

        :return:
        """
        return Reference(self.hybrid_shape_direction.Object)

    @object.setter
    def object(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_direction.Object = value

    @property
    def ref_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RefAxisSystem
                | o Property RefAxisSystem(    ) As
                | 
                | Returns or Sets the reference Axis System for Direction
                | feature. This data is not mandatory, if element is null, the
                | absolute axis system is taken. When an element is given, X,
                | Y and Z are considered in this Axis system. 
                |
                | Example:
                | This
                | example retrieves in oRefAxis the reference Axis System for
                | Direction feature. Dim oRefAxis As CATIAReference Set
                | oRefAxis = Direction.RefAxisSystem

        :return:
        """
        return Reference(self.hybrid_shape_direction.RefAxisSystem)

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Type
                | o Property Type(    ) As   (Read Only)
                | 
                | Returns the direction type. Legal value: The direction type
                | can be: 0 The direction is specified using an object (a line
                | or a plane). In the case of a plane, the direction is the
                | normal to the plane 1 The direction is specified using its
                | components

        :return: float
        """
        return self.hybrid_shape_direction.Type

    def direction_specification(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DirectionSpecification
                | o Func DirectionSpecification(    ) As
                | 
                | Queries the direction specification status.
                |
                | Parameters:
                | oDir
                |        direction specification =  0 : Direction is not specified.
                |                               =  1 : Direction is specified and is valid.
                |                               = -1 : Direction is specified but is not valid.


        :return: float
        """
        return self.hybrid_shape_direction.DirectionSpecification()

    def get_x(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetX
                | o Func GetX(    ) As
                | 
                | Returns the direction X component. This method succeeds only
                | when direction is specified using components. It fails when
                | direction is specified using a geometrical element i.e Line,
                | Plane. In such cases use GetXVal method instead.
                |
                | Parameters:
                | oCoordinates
                |     The direction X component


        :return:
        """
        return RealParam(self.hybrid_shape_direction.GetX())

    def get_x_val(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetXVal
                | o Func GetXVal(    ) As
                | 
                | Returns the direction X component as Double. This method
                | succeeds irrespective of the way direction is specified.
                |
                | Parameters:
                | oX
                |     The direction X component


        :return: float
        """
        return self.hybrid_shape_direction.GetXVal()

    def get_y(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetY
                | o Func GetY(    ) As
                | 
                | Returns the direction Y component. This method succeeds only
                | when direction is specified using components. It fails when
                | direction is specified using a geometrical element i.e Line,
                | Plane. In such cases use GetYVal method instead.
                |
                | Parameters:
                | oCoordinates
                |     The direction Y component


        :return:
        """
        return RealParam(self.hybrid_shape_direction.GetY())

    def get_y_val(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetYVal
                | o Func GetYVal(    ) As
                | 
                | Returns the direction Y component as Double.This method
                | succeeds irrespective of the way direction is specified.
                |
                | Parameters:
                | oY
                |     The direction Y component


        :return: float
        """
        return self.hybrid_shape_direction.GetYVal()

    def get_z(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetZ
                | o Func GetZ(    ) As
                | 
                | Returns the direction Z component. This method succeeds only
                | when direction is specified using components. It fails when
                | direction is specified using a geometrical element i.e Line,
                | Plane. In such cases use GetZVal method instead.
                |
                | Parameters:
                | oCoordinates
                |     The direction Z component


        :return:
        """
        return RealParam(self.hybrid_shape_direction.GetZ())

    def get_z_val(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetZVal
                | o Func GetZVal(    ) As
                | 
                | Returns the direction Z component as Double.This method
                | succeeds irrespective of the way direction is specified.
                |
                | Parameters:
                | oZ
                |    The direction Z component


        :return: float
        """
        return self.hybrid_shape_direction.GetZVal()

    def __repr__(self):
        return f'HybridShapeDirection()'
