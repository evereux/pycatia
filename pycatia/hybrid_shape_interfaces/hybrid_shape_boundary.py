#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

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
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

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
    def from_(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property From() As Reference
                | 
                |     Removes or sets the ending limit(i.e Limit2) of the boundary

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_boundary.From)

    @from_.setter
    def from_(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_boundary.From = reference.com_object

    @property
    def from_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FromOrientation() As long
                | 
                |     Gets or sets the Ending Limit Orientation (i.e same or inverse)

        :rtype: int
        """

        return self.hybrid_shape_boundary.FromOrientation

    @from_orientation.setter
    def from_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_boundary.FromOrientation = value

    @property
    def initial_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_boundary.InitialElement)

    @initial_element.setter
    def initial_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_boundary.InitialElement = value.com_object

    @property
    def propagation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: int
        """

        return self.hybrid_shape_boundary.Propagation

    @propagation.setter
    def propagation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_boundary.Propagation = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
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

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_boundary.Support)

    @support.setter
    def support(self, support_reference: Reference):
        """
        :param Reference support_reference:
        """

        self.hybrid_shape_boundary.Support = support_reference.com_object

    @property
    def to(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property To() As Reference
                | 
                |     Removes or sets the starting limit(i.e Limit1) of the boundary

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_boundary.To)

    @to.setter
    def to(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_boundary.To = value.com_object

    @property
    def to_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ToOrientation() As long
                | 
                |     Gets or sets the Starting Limit Orientation (i.e same or inverse)

        :rtype: int
        """

        return self.hybrid_shape_boundary.ToOrientation

    @to_orientation.setter
    def to_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_boundary.ToOrientation = value

    def __repr__(self):
        return f'HybridShapeBoundary(name="{self.name}")'
