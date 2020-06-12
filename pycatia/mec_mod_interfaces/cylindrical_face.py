#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039


from .face import Face


class CylindricalFace(Face):
    """
        .. note::
            CAA V5 Visual Basic help

                | 2-D boundary with a cylindrical geometry.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the lateral face of a cylinder. You will create a
                | CylindricalFace object using theactivateLinkAnchor('Shapes','GetBounda
                | ry','Shapes.GetBoundary'),activateLinkAnchor('HybridShapes','GetBounda
                | ry','HybridShapes.GetBoundary'),activateLinkAnchor('Sketches','GetBoun
                | dary','Sketches.GetBoundary')oractivateLinkAnchor('Selection','SelectE
                | lement2','Selection.SelectElement2')method. Then, you pass it to the
                | operator (such asactivateLinkAnchor('ShapeFactory','AddNewCircPattern'
                | ,'ShapeFactory.AddNewCircPattern')).  The lifetime of a
                | CylindricalFace object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cylindrical_face = com_object

    def get_direction(self, o_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDirection
                | o Sub GetDirection(        oDirection)
                | 
                | Returns the direction of the cylindrical face axis
                |
                | Parameters:
                | oDirection[0]
                |    The X Coordinate of the axis direction 
                |    
                |  oDirection[1]
                |    The Y Coordinate of the axis direction
                |    
                |  oDirection[2]
                |    The Z Coordinate of the axis direction
                |

        :param o_direction:
        :return:
        """
        return self.cylindrical_face.GetDirection(o_direction)

    def get_origin(self, o_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(        oOrigin)
                | 
                | Returns the origin of the cylindrical face axis.
                |
                | Parameters:
                | oOrigin[0]
                |    The X Coordinate of the axis origin
                |    
                |  oOrigin[1]
                |    The Y Coordinate of the axis origin
                |    
                |  oOrigin[2]
                |    The Z Coordinate of the axis origin
                |

        :param o_origin:
        :return:
        """
        return self.cylindrical_face.GetOrigin(o_origin)

    def __repr__(self):
        return f'CylindricalFace(name="{self.name}")'
