#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .face import Face


class PlanarFace(Face):
    """
        .. note::
            CAA V5 Visual Basic help

                | 2-D boundary with a planar geometry.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the face of a cube. You will create a PlanarFace object using
                | theactivateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary'),act
                | ivateLinkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBoundary
                | '),activateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoundary')
                | oractivateLinkAnchor('Selection','SelectElement2','Selection.SelectEle
                | ment2')method. Then, you pass it to the operator (such asactivateLinkA
                | nchor('ShapeFactory','AddNewDraft','ShapeFactory.AddNewDraft')).  The
                | lifetime of a PlanarFace object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.planar_face = com_object

    def get_first_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFirstAxis
                | o Sub GetFirstAxis(        oFirstAxis)
                | 
                | Returns the planar face first axis
                |
                | Parameters:
                | oFirstAxis[0]
                |    The X Coordinate of the planar face first axis
                |    
                |  oFirstAxis[1]
                |    The Y Coordinate of the planar face first axis
                |    
                |  oFirstAxis[2]
                |    The Z Coordinate of the planar face first axis


        :return:
        """
        return self.planar_face.GetFirstAxis()

    def get_origin(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(        oOrigin)
                | 
                | Returns the origin of the planar face.
                |
                | Parameters:
                | oOrigin[0]
                |    The X Coordinate of the planar face origin
                |    
                |  oOrigin[1]
                |    The Y Coordinate of the planar face origin
                |    
                |  oOrigin[2]
                |    The Z Coordinate of the planar face origin


        :return:
        """
        return self.planar_face.GetOrigin()

    def get_second_axis(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSecondAxis
                | o Sub GetSecondAxis(        oSecondAxis)
                | 
                | Returns the planar face second axis.
                |
                | Parameters:
                | oSecondAxis[0]
                |     The X Coordinate of the planar face second axis
                |    
                |  oSecondAxis[1]
                |    The Y Coordinate of the planar face second axis
                |    
                |  oSecondAxis[2]
                |    The Z Coordinate of the planar face second axis


        :return:
        """
        return self.planar_face.GetSecondAxis()

    def __repr__(self):
        return f'PlanarFace(name="{self.name}")'
