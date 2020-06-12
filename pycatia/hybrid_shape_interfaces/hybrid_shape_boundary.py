#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeBoundary(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeBoundary
                | 
                | Represents the hybrid shape boundary feature object.
                | Role: To access the data of the hybrid shape boundary feature object. This data
                | includes:
                | 
                |     The boundary propagation
                |     The initial element used for the boundary propagation
                |     The boundary support
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeBoundary
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_boundary = com_object

    @property
    def from_py(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property From() As Reference
                | 
                |     Removes or sets the ending limit(i.e Limit2) of the boundary

        :return: Reference
        """

        return Reference(self.hybrid_shape_boundary.From)

    @from_py.setter
    def from_py(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_boundary.From = value

    @property
    def from_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FromOrientation() As long
                | 
                |     Gets or sets the Ending Limit Orientation (i.e same or inverse)

        :return: int
        """

        return self.hybrid_shape_boundary.FromOrientation

    @from_orientation.setter
    def from_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_boundary.FromOrientation = value

    @property
    def initial_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property InitialElement() As Reference
                | 
                |     Returns or sets the element used to initialize the boundary
                |     propagation.
                |     Sub-element(s) supported (see Boundary object):
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in InitElem the initial element of the
                |         ShpBoundary hybrid shape boundary feature.
                | 
                |          Dim InitElem As Reference
                |          InitElem = ShpBoundary.InitialElement

        :return: Reference
        """

        return Reference(self.hybrid_shape_boundary.InitialElement)

    @initial_element.setter
    def initial_element(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_boundary.InitialElement = value

    @property
    def propagation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Propagation() As long
                | 
                |     Returns or sets the boundary propagation.
                |     Legal values: xxxxxxxxxx
                | 
                |     Example:
                |         This example retrieves in Prop the boundary propagation of the
                |         ShpBoundary hybrid shape boundary feature.
                | 
                |          Prop = ShpBoundary.Propagation

        :return: int
        """

        return self.hybrid_shape_boundary.Propagation

    @propagation.setter
    def propagation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_boundary.Propagation = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support surface around which the boundary is
                |     computed.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in SupSurf the initial element of the
                |         ShpBoundary hybrid shape boundary feature.
                | 
                |          Dim SupSurf As Reference
                |          SupSurf = ShpBoundary.Support

        :return: Reference
        """

        return Reference(self.hybrid_shape_boundary.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_boundary.Support = value

    @property
    def to(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property To() As Reference
                | 
                |     Removes or sets the starting limit(i.e Limit1) of the boundary

        :return: Reference
        """

        return Reference(self.hybrid_shape_boundary.To)

    @to.setter
    def to(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_boundary.To = value

    @property
    def to_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ToOrientation() As long
                | 
                |     Gets or sets the Starting Limit Orientation (i.e same or inverse)

        :return: int
        """

        return self.hybrid_shape_boundary.ToOrientation

    @to_orientation.setter
    def to_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_boundary.ToOrientation = value

    def __repr__(self):
        return f'HybridShapeBoundary(name="{self.name}")'
