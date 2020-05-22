#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039


from .boundary import Boundary


class Face(Boundary):
    """
        .. note::
            CAA V5 Visual Basic help

                | 2-D boundary.Role:
                | ThisactivateLinkAnchor('Boundary','','Boundary')object may be, for
                | example, the lateral face of cylinder. You will create a Face object
                | using theactivateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary
                | '),activateLinkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBo
                | undary'),activateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoun
                | dary')oractivateLinkAnchor('Selection','SelectElement2','Selection.Sel
                | ectElement2')method. Then, you pass it to the operator (such asactivat
                | eLinkAnchor('ShapeFactory','AddNewFaceFillet','ShapeFactory.AddNewFace
                | Fillet')).  The lifetime of a Face object is limited,
                | seeactivateLinkAnchor('Boundary','','Boundary').See also:activateLinkA
                | nchor('PlanarFace','','PlanarFace'),activateLinkAnchor('CylindricalFac
                | e','','CylindricalFace').

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.face = com_object     

    def __repr__(self):
        return f'Face(name="{self.name}")'
