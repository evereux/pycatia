#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.in_interfaces.reference import Reference


class Boundary(Reference):
    """
        .. note::
            CAA V5 Visual Basic help

                | Topological cell, such as a face, an edge or a vertex.Role:  The
                | Boundary objects are basic topological objects, such as the edge of a
                | Pad. Some of them posess  a geometrical feature
                | (planarface,rectilinearedge). You will create a Boundary object (such
                | as theactivateLinkAnchor('TriDimFeatEdge','','TriDimFeatEdge')object,
                | which is derived, indirectly,  from the Boundary object) using theacti
                | vateLinkAnchor('Shapes','GetBoundary','Shapes.GetBoundary'),activateLi
                | nkAnchor('HybridShapes','GetBoundary','HybridShapes.GetBoundary'),acti
                | vateLinkAnchor('Sketches','GetBoundary','Sketches.GetBoundary')oractiv
                | ateLinkAnchor('Selection','SelectElement2','Selection.SelectElement2')
                | method. Then, you pass it to the operator (such asactivateLinkAnchor('
                | ShapeFactory','AddNewEdgeFilletWithConstantRadius','ShapeFactory.AddNe
                | wEdgeFilletWithConstantRadius')). Note that, regarding V4 sub-
                | elements, once the data of a CATIA Version 4 Model has been copied to
                | a .CATPart, the sub-elements of the resulting .CATPart are supported
                | by theactivateLinkAnchor('Boundary','','Boundary')object.  The
                | lifetime of a Boundary object is limited. In particular, after having
                | callactivateLinkAnchor('Part','Update','Part.Update'), the Boundary
                | objects are usually no more valid.See
                | also:Note:activateLinkAnchor('Boundary','','Boundary')objects cannot
                | be selected into the specification tree.Note:For
                | aactivateLinkAnchor('Boundary','','Boundary')object, the object
                | returned by
                | theactivateLinkAnchor('AnyObject','Parent','AnyObject.Parent')property
                | is the master shape. For example, if we have:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.boundary = com_object

    def __repr__(self):
        return f'Boudary()'


