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
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCylinder(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCylinder
                | 
                | Represents the hybrid shape Cylinder feature object.
                | Role: To access the data of the hybrid shape Cylinder feature object. This data
                | includes:
                | 
                |     The center of the Cylinder
                |     The Radius of the Cylinder
                |     Length of Cylinder in the given extrusion direction
                |     Length of Cylinder opposite to extrusion direction
                |     Direction of extrusion for cylinder.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCylinder
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_cylinder = com_object

    @property
    def center(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Center() As Reference
                | 
                |     Returns or sets the center of the cylinder object.
                | 
                |     Example:
                |         This example retrieves in CylinderCenter the center of the Cylinder,
                |         for the Cylinder hybrid shape feature.
                | 
                |          Dim CylinderCenter As Reference 
                |          Set CylinderCenter = Cylinder.Center

        :return: Reference
        """

        return Reference(self.hybrid_shape_cylinder.Center)

    @center.setter
    def center(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_cylinder.Center = value

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the direction of the cylinder object.
                | 
                |     Example:
                |         This example retrieves in CylinderDirection the direction of extrusion
                |         of the Cylinder, for the Cylinder hybrid shape
                |         feature.
                | 
                |          Dim CylinderDirection As HybridShapeDirection 
                |          Set CylinderDirection = Cylinder.Direction

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_cylinder.Direction)

    @direction.setter
    def direction(self, value):
        """
        :param HybridShapeDirection value:
        """

        self.hybrid_shape_cylinder.Direction = value

    @property
    def length1(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Length1() As Length
                | 
                |     Returns or sets the length of the cylinder object in the given extrusion
                |     direction.
                | 
                |     Example:
                |         This example retrieves in CylinderLength1 the length of the Cylinder in
                |         the given extrusion direction, for the Cylinder hybrid shape
                |         feature.
                | 
                |          Dim CylinderLength1 As Length
                |          Set CylinderLength1 = Cylinder.Length1

        :return: Length
        """

        return Length(self.hybrid_shape_cylinder.Length1)

    @length1.setter
    def length1(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_cylinder.Length1 = value

    @property
    def length2(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Length2() As Length
                | 
                |     Returns or sets the length of the cylinder object in the opposite direction
                |     of given extrusion direction.
                | 
                |     Example:
                |         This example retrieves in CylinderLength2 the length of the Cylinder in
                |         the opposite direction of the given extrusion direction, for the Cylinder
                |         hybrid shape feature.
                | 
                |          Dim CylinderLength2 As Length
                |          Set CylinderLength2 = Cylinder.Length2

        :return: Length
        """

        return Length(self.hybrid_shape_cylinder.Length2)

    @length2.setter
    def length2(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_cylinder.Length2 = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Orientation(boolean iOrientation)
                | 
                |     Returns or sets the the inversion of extrusion direction.
                | 
                |     Example:
                |         This example retrieves in IsInverted the inversion status of extrusion
                |         direction for the Cylinder hybrid shape feature.
                | 
                |          Dim IsInverted As boolean
                |          Set IsInverted = Cylinder.Orientation

        :return: False
        """

        return None

    @orientation.setter
    def orientation(self, value):
        """
        :param False value:
        """

        self.hybrid_shape_cylinder.Orientation = value

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Radius() As Length
                | 
                |     Returns or sets the radius of the cylinder object.
                | 
                |     Example:
                |         This example retrieves in CylinderRadius the radius of the Cylinder,
                |         for the Cylinder hybrid shape feature.
                | 
                |          Dim CylinderRadius As Length
                |          Set CylinderRadius = Cylinder.Radius

        :return: Length
        """

        return Length(self.hybrid_shape_cylinder.Radius)

    @radius.setter
    def radius(self, value):
        """
        :param Length value:
        """

        self.hybrid_shape_cylinder.Radius = value

    @property
    def symmetrical_extension(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SymmetricalExtension() As boolean
                | 
                |     Gets or Sets the symmetrical extension of Cylinder (Length 2 = -Length 1).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :return: bool
        """

        return self.hybrid_shape_cylinder.SymmetricalExtension

    @symmetrical_extension.setter
    def symmetrical_extension(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_cylinder.SymmetricalExtension = value

    def invert_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InvertOrientation()
                | 
                |     Inverts the Orientation of Cylinder object.
                | 
                |     Example:
                |         This example inverts the orientation for the Cylinder hybrid shape
                |         feature.
                | 
                |          Cylinder.InvertOrientation

        :return: None
        """
        return self.hybrid_shape_cylinder.InvertOrientation()

    def __repr__(self):
        return f'HybridShapeCylinder(name="{ self.name }")'
