#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection

from .boundary import Boundary

class Edge(Boundary):
    """
        .. note::
            CAA V5 Visual Basic help

                | 1-D boundary.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the edge of a cylinder. You will create an Edge object using 
                | theactivateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary'),act
                | ivateLinkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBoundary
                | '),activateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoundary')
                | oractivateLinkAnchor('Selection','SelectElement2','Selection.SelectEle
                | ment2')method. Then, you pass it to the operator (such asactivateLinkA
                | nchor('HybridShapeFactory','AddNewPointTangent','HybridShapeFactory.Ad
                | dNewPointTangent')).  The lifetime of an Edge object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').See also:activateLinkA
                | nchor('TriDimFeatEdge','','TriDimFeatEdge'),activateLinkAnchor('Rectil
                | inearTriDimFeatEdge','','RectilinearTriDimFeatEdge'),activateLinkAncho
                | r('BiDimFeatEdge','','BiDimFeatEdge'),activateLinkAnchor('RectilinearB
                | iDimFeatEdge','','RectilinearBiDimFeatEdge'),activateLinkAnchor('MonoD
                | imFeatEdge','','MonoDimFeatEdge'),activateLinkAnchor('RectilinearMonoD
                | imFeatEdge','','RectilinearMonoDimFeatEdge').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.edge = com_object     

    def __repr__(self):
        return f'Edge()'
