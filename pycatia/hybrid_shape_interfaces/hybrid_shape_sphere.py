#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSphere(HybridShape):
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
                |                         HybridShapeSphere
                | 
                | Represents the hybrid shape sphere feature object.
                | Role: To access the data of the hybrid shape sphere explicit feature
                | object.
                | The Sphere feature : a Sphere is made up of 4 angles parameters.
                | 
                | See also:
                |     HybridShapeFactory

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sphere = com_object

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Axis() As Reference
                | 
                |     Returns or sets axis on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sphere.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        """
        :param Reference reference_axis:
        """

        self.hybrid_shape_sphere.Axis = reference_axis.com_object

    @property
    def begin_meridian_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginMeridianAngle() As Angle (Read Only)
                | 
                |     Returns BeginMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sphere.BeginMeridianAngle)

    @property
    def begin_parallel_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginParallelAngle() As Angle (Read Only)
                | 
                |     Returns BeginParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sphere.BeginParallelAngle)

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Center() As Reference
                | 
                |     Returns or sets the sphere center.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in HybShpSphereCenter the center of the
                |         HybShpSphere hybrid shape sphere.
                | 
                |          Dim HybShpSphereCenter As Reference
                |          HybShpSphereCenter = HybShpSphere.Center

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sphere.Center)

    @center.setter
    def center(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_sphere.Center = reference.com_object

    @property
    def end_meridian_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndMeridianAngle() As Angle (Read Only)
                | 
                |     Returns EndMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sphere.EndMeridianAngle)

    @property
    def end_parallel_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndParallelAngle() As Angle (Read Only)
                | 
                |     Returns EndParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sphere.EndParallelAngle)

    @property
    def limitation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Limitation(long iLimitationType)
                | 
                |     Returns whether the sphere is created as a whole sphere or
                |     not.
                |     Legal values: 0 for a sphere with angles and 1 for a whole
                |     sphere.
                | 
                |     Example:

        :rtype: int
        """

        return self.hybrid_shape_sphere.Limitation

    @limitation.setter
    def limitation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sphere.Limitation = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     Role: Get sphere radius.
                | 
                |     Parameters:
                | 
                |         oRadius
                |             Sphere radius return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Length 
                |     See also:
                |         HybridShapeFactory

        :rtype: Length
        """

        return Length(self.hybrid_shape_sphere.Radius)

    def set_begin_meridian_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBeginMeridianAngle(double iAngle)
                | 
                |     Sets BeginMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sphere.SetBeginMeridianAngle(i_angle)

    def set_begin_parallel_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBeginParallelAngle(double iAngle)
                | 
                |     Sets BeginParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sphere.SetBeginParallelAngle(i_angle)

    def set_end_meridian_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetEndMeridianAngle(double iAngle)
                | 
                |     Sets EndMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sphere.SetEndMeridianAngle(i_angle)

    def set_end_parallel_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetEndParallelAngle(double iAngle)
                | 
                |     Sets EndParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sphere.SetEndParallelAngle(i_angle)

    def set_radius(self, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRadius(double iRadius)
                | 
                |     Sets Radius on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param float i_radius:
        :rtype: None
        """
        return self.hybrid_shape_sphere.SetRadius(i_radius)

    def __repr__(self):
        return f'HybridShapeSphere(name="{self.name}")'
