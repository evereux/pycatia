#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

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
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

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
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As Angle (Read Only)
                | 
                |     returns the resulting angle of extremum.

        :return: Angle
        """

        return Angle(self.hybrid_shape_extremum_polar.Angle)

    @property
    def contour(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Contour() As Reference
                | 
                |     returns or sets the input contour.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extremum_polar.Contour)

    @contour.setter
    def contour(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extremum_polar.Contour = value

    @property
    def dir(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Dir() As HybridShapeDirection
                | 
                |     returns or sets the direction of computation.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_extremum_polar.Dir)

    @dir.setter
    def dir(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_extremum_polar.Dir = value

    @property
    def extremum_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtremumType() As short
                | 
                |     returns or sets the type of extremum.

        :return: enum
        """

        return self.hybrid_shape_extremum_polar.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value):
        """
        :param enum value:
        """

        self.hybrid_shape_extremum_polar.ExtremumType = value

    @property
    def origin(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Origin() As Reference
                | 
                |     returns or sets the origin of the polar axis.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extremum_polar.Origin)

    @origin.setter
    def origin(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extremum_polar.Origin = value

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Radius() As Length (Read Only)
                | 
                |     returns the resulting radius of extremum.

        :return: Length
        """

        return Length(self.hybrid_shape_extremum_polar.Radius)

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Support() As Reference
                | 
                |     returns or sets the support (if exist).

        :return: Reference
        """

        return Reference(self.hybrid_shape_extremum_polar.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extremum_polar.Support = value

    def __repr__(self):
        return f'HybridShapeExtremumPolar(name="{ self.name }")'
