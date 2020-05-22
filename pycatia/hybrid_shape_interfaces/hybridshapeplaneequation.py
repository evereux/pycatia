#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePlaneEquation(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Plane define by an equation plane.Role:  Allows to access data of the
                | plane feature created by its cartesian equation. Plane equation is
                | Ax+By+Cz = D.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_equation = com_object     

    @property
    def a(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | A
                | o Property A(    ) As   (Read Only)
                | 
                | Gets A coefficient for plane equation.

        :return:
        """
        return self.hybrid_shape_plane_equation.A

    @property
    def b(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | B
                | o Property B(    ) As   (Read Only)
                | 
                | Gets B coefficient for plane equation.

        :return:
        """
        return self.hybrid_shape_plane_equation.B

    @property
    def c(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | C
                | o Property C(    ) As   (Read Only)
                | 
                | Gets C coefficient for plane equation.

        :return:
        """
        return self.hybrid_shape_plane_equation.C

    @property
    def d(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | D
                | o Property D(    ) As   (Read Only)
                | 
                | Gets D coefficient for plane equation.

        :return:
        """
        return self.hybrid_shape_plane_equation.D

    @property
    def ref_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RefAxisSystem
                | o Property RefAxisSystem(    ) As
                | 
                | Returns or Sets the reference Axis System for PlaneEquation
                | feature. This data is not mandatory, if element is null, the
                | absolute axis system is taken. When an element is given, X,
                | Y and Z are considered in this Axis system. If reference
                | point is not specified, X,Y and Z are measured from origin
                | of this axis system. 
                |
                | Example:
                | This example retrieves in
                | oRefAxis the reference Axis System for PlaneEquation
                | feature. Dim oRefAxis As CATIAReference Set oRefAxis =
                | PlaneEquation.RefAxisSystem

        :return:
        """
        return self.hybrid_shape_plane_equation.RefAxisSystem

    def get_reference_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetReferencePoint
                | o Func GetReferencePoint(    ) As
                | 
                | Gets the reference point.
                |
                | Parameters:
                | oReferencePoint
                |       reference  point


        :return:
        """
        return self.hybrid_shape_plane_equation.GetReferencePoint()

    def set_reference_point(self, i_reference_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetReferencePoint
                | o Sub SetReferencePoint(        iReferencePoint)
                | 
                | Sets the reference point.
                |
                | Parameters:
                | iReferencePoint
                |       reference  point


        :param i_reference_point:
        :return:
        """
        return self.hybrid_shape_plane_equation.SetReferencePoint(i_reference_point)

    def __repr__(self):
        return f'HybridShapePlaneEquation()'
