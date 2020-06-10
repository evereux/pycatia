#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.real_param import RealParam


class HybridShapePlaneEquation(Plane):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneEquation
                | 
                | Plane define by an equation plane.
                | Role: Allows to access data of the plane feature created by its cartesian equation. Plane equation is Ax+By+Cz = D.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_equation = com_object

    @property
    def a(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property A() As RealParam (Read Only)
                | 
                |     Gets A coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oA
                |             A Coefficient of cartesian plane 
                | 
                |     See also:
                |         RealParam 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_plane_equation.A)

    @property
    def b(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property B() As RealParam (Read Only)
                | 
                |     Gets B coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oB
                |             B Coefficient of cartesian plane 
                | 
                |     See also:
                |         RealParam 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_plane_equation.B)

    @property
    def c(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property C() As RealParam (Read Only)
                | 
                |     Gets C coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oC
                |             C Coefficient of cartesian plane return value for CATScript
                |             applications, with (IDLRETVAL) function type 
                | 
                |     See also:
                |         RealParam 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: RealParam
        """

        return RealParam(self.hybrid_shape_plane_equation.C)

    @property
    def d(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property D() As Length (Read Only)
                | 
                |     Gets D coefficient for plane equation.
                | 
                |     Parameters:
                | 
                |         oD
                |             D Coefficient of cartesian plane 
                | 
                |     See also:
                |         Length 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Length
        """

        return Length(self.hybrid_shape_plane_equation.D)

    @property
    def ref_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RefAxisSystem() As Reference
                | 
                |     Returns or Sets the reference Axis System for PlaneEquation
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis
                |     system.
                |     If reference point is not specified, X,Y and Z are measured from origin of
                |     this axis system.
                | 
                |     Example
                |     :
                |         This example retrieves in oRefAxis the reference Axis System for
                |         PlaneEquation feature.
                | 
                |          Dim oRefAxis As CATIAReference
                |          Set oRefAxis  = PlaneEquation.RefAxisSystem

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane_equation.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane_equation.RefAxisSystem = value

    def get_reference_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetReferencePoint() As Reference
                | 
                |     Gets the reference point.
                | 
                |     Parameters:
                | 
                |         oReferencePoint
                |             reference point

        :return: Reference
        """
        return Reference(self.hybrid_shape_plane_equation.GetReferencePoint())

    def set_reference_point(self, i_reference_point=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetReferencePoint(Reference iReferencePoint)
                | 
                |     Sets the reference point.
                | 
                |     Parameters:
                | 
                |         iReferencePoint
                |             reference point

        :param Reference i_reference_point:
        :return: None
        """
        return self.hybrid_shape_plane_equation.SetReferencePoint(i_reference_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_reference_point'
        # # vba_code = """
        # # Public Function set_reference_point(hybrid_shape_plane_equation)
        # #     Dim iReferencePoint (2)
        # #     hybrid_shape_plane_equation.SetReferencePoint iReferencePoint
        # #     set_reference_point = iReferencePoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapePlaneEquation(name="{ self.name }")'
