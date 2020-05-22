#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCylinder(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Cylinder feature object.Role: To access
                | the data of the hybrid shape Cylinder feature object. This data
                | includes:Use the  CATIAHybridShapeFactory to create a
                | HybridShapeCylinder object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_cylinder = com_object     

    @property
    def center(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Center
                | o Property Center(    ) As
                | 
                | Returns or sets the center of the cylinder object. Example:
                | This example retrieves in CylinderCenter the center of the
                | Cylinder, for the Cylinder hybrid shape feature. Dim
                | CylinderCenter As Reference Set CylinderCenter =
                | Cylinder.Center

        :return:
        """
        return self.hybrid_shape_cylinder.Center

    @center.setter
    def center(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_cylinder.Center = value 

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the direction of the cylinder object.
                | 
                |
                | Example:
                | This example retrieves in CylinderDirection the
                | direction of extrusion of the Cylinder, for the Cylinder
                | hybrid shape feature. Dim CylinderDirection As
                | HybridShapeDirection Set CylinderDirection =
                | Cylinder.Direction

        :return:
        """
        return self.hybrid_shape_cylinder.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_cylinder.Direction = value 

    @property
    def length1(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Length1
                | o Property Length1(    ) As
                | 
                | Returns or sets the length of the cylinder object in the
                | given extrusion direction. 
                |
                | Example:
                | This example retrieves
                | in CylinderLength1 the length of the Cylinder in the given
                | extrusion direction, for the Cylinder hybrid shape feature.
                | Dim CylinderLength1 As Length Set CylinderLength1 =
                | Cylinder.Length1

        :return:
        """
        return self.hybrid_shape_cylinder.Length1

    @length1.setter
    def length1(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_cylinder.Length1 = value 

    @property
    def length2(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Length2
                | o Property Length2(    ) As
                | 
                | Returns or sets the length of the cylinder object in the
                | opposite direction of given extrusion direction. Example:
                | This example retrieves in CylinderLength2 the length of the
                | Cylinder in the opposite direction of the given extrusion
                | direction, for the Cylinder hybrid shape feature. Dim
                | CylinderLength2 As Length Set CylinderLength2 =
                | Cylinder.Length2

        :return:
        """
        return self.hybrid_shape_cylinder.Length2

    @length2.setter
    def length2(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_cylinder.Length2 = value 

    @property
    def orientation(self, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(        iOrientation)
                | 
                | Returns or sets the the inversion of extrusion direction.
                | 
                |
                | Example:
                | This example retrieves in IsInverted the inversion
                | status of extrusion direction for the Cylinder hybrid shape
                | feature. Dim IsInverted As boolean Set IsInverted =
                | Cylinder.Orientation

        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_cylinder.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_cylinder.Orientation = value 

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As
                | 
                | Returns or sets the radius of the cylinder object. Example:
                | This example retrieves in CylinderRadius the radius of the
                | Cylinder, for the Cylinder hybrid shape feature. Dim
                | CylinderRadius As Length Set CylinderRadius =
                | Cylinder.Radius

        :return:
        """
        return self.hybrid_shape_cylinder.Radius

    @radius.setter
    def radius(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_cylinder.Radius = value 

    @property
    def symmetrical_extension(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SymmetricalExtension
                | o Property SymmetricalExtension(    ) As
                | 
                | Gets or Sets the symmetrical extension of Cylinder (Length 2
                | = -Length 1).

        :return:
        """
        return self.hybrid_shape_cylinder.SymmetricalExtension

    def invert_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertOrientation
                | o Sub InvertOrientation(    )
                | 
                | Inverts the Orientation of Cylinder object. 
                |
                | Example:
                | This
                | example inverts the orientation for the Cylinder hybrid
                | shape feature. Cylinder.InvertOrientation
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_cylinder.InvertOrientation()

    def __repr__(self):
        return f'HybridShapeCylinder()'
