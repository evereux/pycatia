#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .mono_dim_feat_edge import MonoDimFeatEdge


# todo: add catscript.

class RectilinearMonoDimFeatEdge(MonoDimFeatEdge):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary belonging to a feature whose topological result is one
                | dimensional, the boundary having a rectilinear geometry.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, in a part containing a Sketch which is made up of a line
                | segment and a spline, the line segment.  You will create a
                | RectilinearMonoDimFeatEdge object using theactivateLinkAnchor('Shapes'
                | ,'GetBoundary','Shapes.GetBoundary'),activateLinkAnchor('HybridShapes'
                | ,'GetBoundary','HybridShapes.GetBoundary'),activateLinkAnchor('Sketche
                | s','GetBoundary','Sketches.GetBoundary')oractivateLinkAnchor('Selectio
                | n','SelectElement2','Selection.SelectElement2')method. Then, you pass
                | it to the operator (such
                | asactivateLinkAnchor('Hole','SetDirection','Hole.SetDirection')).  The
                | lifetime of a RectilinearMonoDimFeatEdge object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_mono_dim_feat_edge = com_object

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
        return self.rectilinear_mono_dim_feat_edge.GetDirection()

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
        return self.rectilinear_mono_dim_feat_edge.GetOrigin()

    def __repr__(self):
        return f'RectilinearMonoDimFeatEdge(name="{self.name}")'
