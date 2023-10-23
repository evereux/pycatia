#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCorner(HybridShape):

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
                |                         HybridShapeCorner
                | 
                | Represents the hybrid shape corner feature.
                | Role: To access the data of the hybrid shape corner object. This data
                | includes:
                | 
                |     Two elements
                |     Their orientations (same or inverse than the underlying
                |     curve)
                |     A support for the hybrid shape corner on support feature
                |     A direction for the hybrid shape 3D corner feature
                |     A radius.
                | 
                | Use the HybridShapeFactory to create a HybridShapeCorner
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_corner = com_object

    @property
    def begin_of_corner(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BeginOfCorner() As long
                | 
                |     Return or Set the number of the beginning curve of the corner. This
                |     parameter is used to stabilize the resulting corner
                | 
                |     Example:
                | 
                |           This example set the beginning wire index of
                |          the hybShpCorner hybrid shape corner 
                |          
                | 
                |          hybShpCorner.BeginOfCorner = 1

        :rtype: int
        """

        return self.hybrid_shape_corner.BeginOfCorner

    @begin_of_corner.setter
    def begin_of_corner(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.BeginOfCorner = value

    @property
    def corner_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CornerType() As long
                | 
                |     Returns or sets the Corner Type.
                | 
                |     Example:
                | 
                |           This example retrieves the Corner Type 
                |          the hybShpCorner hybrid shape corner in CornerType.
                |          
                | 
                |          Dim lCornerType As long
                |          lCornerType = hybShpCorner.CornerType

        :rtype: int
        """

        return self.hybrid_shape_corner.CornerType

    @corner_type.setter
    def corner_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.CornerType = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the 3D corner direction.
                |     Legal values: This can be a CATIAHybridShapeDirection.
                | 
                |     See also:
                |         HybridShapeDirection 
                |     Example:
                | 
                |           This example sets the direction of
                |          the hybShpCorner hybrid shape 3D corner as
                |          the existing direction hybShpDirection.
                |          
                | 
                |          hybShpCorner.Direction = hybShpDirection

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_corner.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_corner.Direction = direction.com_object

    @property
    def discrimination_index(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DiscriminationIndex() As long
                | 
                |     Returns or set the discrimination index of the current corner. Several
                |     resulting solutions produced by the operator can be same oriented regarding to
                |     the input wire bodies. In such a case, they are sorted in order to distinguish
                |     them. The Sequence FirstOrientation - SecondOrientation - DiscriminationIndex
                |     allows you to identify a unique one-domain solution.
                | 
                |     Example:
                | 
                |           This example set the discrimination index of
                |          the hybShpCorner hybrid shape corner 
                |          
                | 
                |          hybShpCorner.DiscriminationIndex = 2

        :rtype: int
        """

        return self.hybrid_shape_corner.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.DiscriminationIndex = value

    @property
    def first_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstElem() As Reference
                | 
                |     Returns or sets the corner first reference element.
                |     Legal values: This can be a curve or a point.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example:
                | 
                |           This example retrieves the first reference element
                |           of
                |          the hybShpCorner hybrid shape corner in firstElt.
                |          
                | 
                |          Dim fisrtElt As CATIAReference
                |          fisrtElt = hybShpCorner.FirstElem

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_corner.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_corner.FirstElem = reference_element.com_object

    @property
    def first_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstOrientation() As long
                | 
                |     Returns or sets the orientation of the corner first reference element. The
                |     orientation specifies the corner center position. It is either the same of the
                |     inverse orientation than those of the cross product: Normal(Support) ^
                |     Tangent(FirstElem)
                |     Legal values: 1 if the orientation of the corner first reference element is
                |     the same than the cross product: Normal(Support) ^ Tangent(FirstElem), and -1
                |     if it is the inverse.
                | 
                |     Example:
                | 
                |           This example retrieves the orientation of first reference element
                |           of
                |          the hybShpCorner hybrid shape corner in firstOrient.
                |          
                | 
                |          Dim firstOrient As long
                |          firstOrient = hybShpCorner.FirstOrientation

        :rtype: int
        """

        return self.hybrid_shape_corner.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.FirstOrientation = value

    @property
    def first_tangent_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstTangentOrientation() As long
                | 
                |     Returns or sets the tangent orientation of the corner first reference
                |     element. compared to the corner itself
                | 
                |     Example:
                | 
                |           This example retrieves the tangent orientation of first reference
                |           element of
                |          the hybShpCorner hybrid shape corner in firstOrient.
                |          
                | 
                |          Dim firstOrient As long
                |          firstOrient = hybShpCorner.FirstTangentOrientation

        :rtype: int
        """

        return self.hybrid_shape_corner.FirstTangentOrientation

    @first_tangent_orientation.setter
    def first_tangent_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.FirstTangentOrientation = value

    @property
    def on_vertex(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OnVertex() As boolean
                | 
                |     Returns or sets the On Vertex mode off/on.
                | 
                |     Example:
                | 
                |           This example retrieves the OnVertex
                |          the hybShpCorner hybrid shape corner in OnVertex.
                |          
                | 
                |          Dim bOnVertex As boolean
                |          bOnVertex = hybShpCorner.OnVertex

        :rtype: bool
        """

        return self.hybrid_shape_corner.OnVertex

    @on_vertex.setter
    def on_vertex(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_corner.OnVertex = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns the corner radius.
                | 
                |     Example:
                | 
                |           This example retrieves the radius of
                |          the hybShpCorner hybrid shape corner in radius.
                |          
                | 
                |          Dim radius As CATIALength
                |          radius = hybShpCorner.Radius

        :rtype: Length
        """

        return Length(self.hybrid_shape_corner.Radius)

    @property
    def second_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondElem() As Reference
                | 
                |     Returns or sets the corner second reference element.
                |     Legal values: This is always a curve.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example:
                | 
                |           This example retrieves the second reference element
                |           of
                |          the hybShpCorner hybrid shape corner in secondElt.
                |          
                | 
                |          Dim secondElt As CATIAReference
                |          secondElt = hybShpCorner.SecondElem

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_corner.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_corner.SecondElem = reference_element.com_object

    @property
    def second_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondOrientation() As long
                | 
                |     Returns or sets the orientation of the corner second reference element. The
                |     orientation specifies the corner center position. It is either the same of the
                |     inverse orientation than those of the cross product: Normal(Support) ^
                |     Tangent(SecondElem)
                |     Legal values: 1 if the orientation of the corner second reference element
                |     is the same than the cross product: Normal(Support) ^ Tangent(SecondElem), and
                |     -1 if it is the inverse.
                | 
                |     Example:
                | 
                |           This example sets the orientation of second reference element
                |           of
                |          the hybShpCorner hybrid shape corner to the inverse of the cross
                |          porduct
                |          Normal(Support) ^ Tangent(SecondElem).
                |          
                | 
                |          hybShpCorner.SecondOrientation = -1

        :rtype: int
        """

        return self.hybrid_shape_corner.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.SecondOrientation = value

    @property
    def second_tangent_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondTangentOrientation() As long
                | 
                |     Returns or sets the tangent orientation of the corner second reference
                |     element. compared to the corner itself
                | 
                |     Example:
                | 
                |           This example retrieves the tangent orientation of second reference
                |           element of
                |          the hybShpCorner hybrid shape corner in secondOrient.
                |          
                | 
                |          Dim secondOrient As long
                |          firstOrient = hybShpCorner.SecondTangentOrientation

        :rtype: int
        """

        return self.hybrid_shape_corner.SecondTangentOrientation

    @second_tangent_orientation.setter
    def second_tangent_orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.SecondTangentOrientation = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the corner support.
                |     Legal values: This can be a plane or a surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                | 
                |           This example sets the support of
                |          the hybShpCorner hybrid shape corner as
                |          the existing surface supportSurf.
                |          
                | 
                |          hybShpCorner.Support = supportSurf

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_corner.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_corner.Support = reference_support.com_object

    @property
    def trim(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Trim() As boolean
                | 
                |     Returns or sets whether the corner reference curves are or should be
                |     trimmed.
                |     Legal values: True if the corner reference curves are or should be trimmed,
                |     and False otherwise.
                | 
                |     Example:
                | 
                |           This example sets that the corner reference curves
                |           of
                |          the hybShpCorner hybrid shape corner should be
                |          trimmed.
                |          
                | 
                |          hybShpCorner.Trim = True

        :rtype: bool
        """

        return self.hybrid_shape_corner.Trim

    @trim.setter
    def trim(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_corner.Trim = value

    @property
    def trim_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TrimMode() As long
                | 
                |     Returns or sets whether the corner reference curves are or should be
                |     trimmed.
                |     Legal values: 1 if the corner reference curves are or should be trimmed, 0
                |     if the corner reference curves are not or should not be trimmed, 2 if only the
                |     first corner reference curve is or should be trimmed, 3 if only the second
                |     corner reference curve is or should be trimmed,
                | 
                |     Example:
                | 
                |           This example sets that the corner reference curves
                |           of
                |          the hybShpCorner hybrid shape corner should be
                |          trimmed.
                |          
                | 
                |          hybShpCorner.TrimMode = 1

        :rtype: int
        """

        return self.hybrid_shape_corner.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_corner.TrimMode = value

    def invert_first_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertFirstOrientation()
                | 
                |     Inverts the first reference element orientation used to compute the
                |     corner.
                | 
                |     Example:
                | 
                |           This example inverts the first corner reference element orientation
                |           of
                |          the hybShpCorner.
                |          
                | 
                |          hybShpCorner.InvertFirstOrientation

        :rtype: None
        """
        return self.hybrid_shape_corner.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertSecondOrientation()
                | 
                |     Inverts the second reference element orientation used to compute the
                |     corner.
                | 
                |     Example:
                | 
                |           This example inverts the second corner reference element orientation
                |           of
                |          the hybShpCorner.
                |          
                | 
                |          hybShpCorner.InvertSecondOrientation

        :rtype: None
        """
        return self.hybrid_shape_corner.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeCorner(name="{ self.name }")'
