#! usr/bin/python3.6
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


class HybridShapeExtremumPolar(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtremumPolar
                | 
                | Represents the hybrid shape extremum polar feature.
                | Role: To access the data of the extremum polar feature . This data
                | includes:
                | 
                |     The contour
                |     The support (if exist )
                |     The direction of evaluation
                |     The extermum type
                | 
                | Use the HybridShapeFactory.AddNewExtremumPolarto create a
                | HybridShapeExtremumPolar object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extremum_polar = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Angle() As Angle (Read Only)
                | 
                |     returns the resulting angle of extremum.

        :return: Angle
        :rtype: Angle
        """

        return Angle(self.hybrid_shape_extremum_polar.Angle)

    @property
    def contour(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Contour() As Reference
                | 
                |     returns or sets the input contour.

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extremum_polar.Contour)

    @contour.setter
    def contour(self, reference_contour: Reference):
        """
        :param Reference reference_contour:
        """

        self.hybrid_shape_extremum_polar.Contour = reference_contour.com_object

    @property
    def dir(self) -> HybridShapeDirection:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Dir() As HybridShapeDirection
                | 
                |     returns or sets the direction of computation.

        :return: HybridShapeDirection
        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_extremum_polar.Dir)

    @dir.setter
    def dir(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_extremum_polar.Dir = direction.com_object

    @property
    def extremum_type(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExtremumType() As short
                | 
                |     returns or sets the type of extremum.

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_extremum_polar.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_extremum_polar.ExtremumType = value

    @property
    def origin(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Origin() As Reference
                | 
                |     returns or sets the origin of the polar axis.

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extremum_polar.Origin)

    @origin.setter
    def origin(self, reference_origin: Reference):
        """
        :param Reference reference_origin:
        """

        self.hybrid_shape_extremum_polar.Origin = reference_origin.com_object

    @property
    def radius(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     returns the resulting radius of extremum.

        :return: Length
        :rtype: Length
        """

        return Length(self.hybrid_shape_extremum_polar.Radius)

    @property
    def support(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     returns or sets the support (if exist).

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_extremum_polar.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_extremum_polar.Support = reference_support.com_object

    def __repr__(self):
        return f'HybridShapeExtremumPolar(name="{ self.name }")'
