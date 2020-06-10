#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .tri_dim_feat_edge import TriDimFeatEdge


# todo: add catscript.

class RectilinearTriDimFeatEdge(TriDimFeatEdge):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary belonging to a feature whose topological result is three
                | dimensional, the boundary having a rectilinear geometry.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the edge of a Pad resulting from the extrusion of a square.
                | You will create a RectilinearTriDimFeatEdge object using theactivateLi
                | nkAnchor('Shapes','GetBoundary','Shapes.GetBoundary'),activateLinkAnch
                | or('HybridShapes','GetBoundary','HybridShapes.GetBoundary'),activateLi
                | nkAnchor('Sketches','GetBoundary','Sketches.GetBoundary')oractivateLin
                | kAnchor('Selection','SelectElement2','Selection.SelectElement2')method
                | . Then, you pass it to the operator (such
                | asactivateLinkAnchor('Hole','SetDirection','Hole.SetDirection')).  The
                | lifetime of a RectilinearTriDimFeatEdge object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_tri_dim_feat_edge = com_object

    def get_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDirection
                | o Sub GetDirection(        oDirection)
                | 
                | Returns the direction of the rectilinear edge
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

        :return: tuple
        """
        return self.rectilinear_tri_dim_feat_edge.GetDirection()

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

        :return: tuple
        """
        return self.rectilinear_tri_dim_feat_edge.GetOrigin()

    def __repr__(self):
        return f'RectilinearTriDimFeatEdge(name="{self.name}")'
