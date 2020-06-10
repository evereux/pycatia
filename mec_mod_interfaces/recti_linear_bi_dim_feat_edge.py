#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .bi_dim_featedge import BiDimFeatEdge


# todo: add catscript.


class RectilinearBiDimFeatEdge(BiDimFeatEdge):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary belonging to a feature whose topological result is two
                | dimensional, the boundary having a rectilinear geometry.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the edge of a surface obtained through the extrusion of a
                | line.  You will create a RectilinearBiDimFeatEdge object using theacti
                | vateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary'),activateLi
                | nkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBoundary'),acti
                | vateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoundary')oractiv
                | ateLinkAnchor('Selection','SelectElement2','Selection.SelectElement2')
                | method. Then, you pass it to the operator (such
                | asactivateLinkAnchor('Hole','SetDirection','Hole.SetDirection')).  The
                | lifetime of a RectilinearBiDimFeatEdge object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_bi_dim_feat_edge = com_object

    def get_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDirection
                | o Sub GetDirection(        oDirection)
                | 
                | Returns the direction of the rectilinear edge.
                |
                | Parameters:
                | oDirection[0]
                |    The X Coordinate of the direction
                |    
                |  oDirection[1]
                |    The Y Coordinate of the direction
                |    
                |  oDirection[2]
                |    The Z Coordinate of the direction

        :return:
        """
        return self.rectilinear_bi_dim_feat_edge.GetDirection()

    def get_origin(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(        oOrigin)
                | 
                | Returns the origin of the the rectilinear edge.
                |
                | Parameters:
                | oOrigin[0]
                |    The X Coordinate of the rectilinear edge origin
                |    
                |  oOrigin[1]
                |    The Y Coordinate of the rectilinear edge origin
                |    
                |  oOrigin[2]
                |    The Z Coordinate of the rectilinear edge origin

        :return:
        """
        return self.rectilinear_bi_dim_feat_edge.GetOrigin()

    def __repr__(self):
        return f'RectilinearBiDimFeatEdge(name="{self.name}")'
