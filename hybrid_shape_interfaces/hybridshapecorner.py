#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCorner(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape corner feature.Role: To access the data of
                | the hybrid shape corner object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_corner = com_object     

    @property
    def begin_of_corner(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginOfCorner
                | o Property BeginOfCorner(    ) As
                | 
                | Return or Set the number of the beginning curve of the
                | corner. This parameter is used to stabilize the resulting
                | corner 
                |
                | Example:
                | This example set the beginning wire index of
                | the hybShpCorner hybrid shape corner
                | hybShpCorner.BeginOfCorner = 1

        :return:
        """
        return self.hybrid_shape_corner.BeginOfCorner

    @property
    def corner_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CornerType
                | o Property CornerType(    ) As
                | 
                | Returns or sets the Corner Type. 
                |
                | Example:
                | This example
                | retrieves the Corner Type the hybShpCorner hybrid shape
                | corner in CornerType. Dim lCornerType As long lCornerType =
                | hybShpCorner.CornerType

        :return:
        """
        return self.hybrid_shape_corner.CornerType

    @corner_type.setter
    def corner_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.CornerType = value 

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the 3D corner direction. Legal values: This
                | can be a CATIAHybridShapeDirection. See also: 
                |
                | Example:
                | This
                | example sets the direction of the hybShpCorner hybrid shape
                | 3D corner as the existing direction hybShpDirection.
                | hybShpCorner.Direction = hybShpDirection

        :return:
        """
        return self.hybrid_shape_corner.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.Direction = value 

    @property
    def discrimination_index(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DiscriminationIndex
                | o Property DiscriminationIndex(    ) As
                | 
                | Returns or set the discrimination index of the current
                | corner. Several resulting solutions produced by the operator
                | can be same oriented regarding to the input wire bodies. In
                | such a case, they are sorted in order to distinguish them.
                | The Sequence FirstOrientation - SecondOrientation -
                | DiscriminationIndex allows you to identifie a unique one-
                | domain solution. 
                |
                | Example:
                | This example set the
                | discrimination index of the hybShpCorner hybrid shape corner
                | hybShpCorner.DiscriminationIndex = 2

        :return:
        """
        return self.hybrid_shape_corner.DiscriminationIndex

    @property
    def first_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstElem
                | o Property FirstElem(    ) As
                | 
                | Returns or sets the corner first reference element. Legal
                | values: This can be a curve or a point. Sub-element(s)
                | supported (see object): , or . 
                |
                | Example:
                | This example
                | retrieves the first reference element of the hybShpCorner
                | hybrid shape corner in firstElt. Dim fisrtElt As
                | CATIAReference fisrtElt = hybShpCorner.FirstElem

        :return:
        """
        return self.hybrid_shape_corner.FirstElem

    @first_elem.setter
    def first_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.FirstElem = value 

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstOrientation
                | o Property FirstOrientation(    ) As
                | 
                | Returns or sets the orientation of the corner first
                | reference element. The orientation specifies the corner
                | center position. It is either the same of the inverse
                | orientation than those of the cross product: Normal(Support)
                | ^ Tangent(FirstElem) Legal values: 1 if the orientation of
                | the corner first reference element is the same than the
                | cross product: Normal(Support) ^ Tangent(FirstElem), and -1
                | if it is the inverse. 
                |
                | Example:
                | This example retrieves the
                | orientation of first reference element of the hybShpCorner
                | hybrid shape corner in firstOrient. Dim firstOrient As long
                | firstOrient = hybShpCorner.FirstOrientation

        :return:
        """
        return self.hybrid_shape_corner.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.FirstOrientation = value 

    @property
    def first_tangent_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstTangentOrientation
                | o Property FirstTangentOrientation(    ) As
                | 
                | Returns or sets the tangent orientation of the corner first
                | reference element. compared to the corner itself Example:
                | This example retrieves the tangent orientation of first
                | reference element of the hybShpCorner hybrid shape corner in
                | firstOrient. Dim firstOrient As long firstOrient =
                | hybShpCorner.FirstTangentOrientation

        :return:
        """
        return self.hybrid_shape_corner.FirstTangentOrientation

    @first_tangent_orientation.setter
    def first_tangent_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.FirstTangentOrientation = value 

    @property
    def on_vertex(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OnVertex
                | o Property OnVertex(    ) As
                | 
                | Returns or sets the On Vertex mode off/on. 
                |
                | Example:
                | This
                | example retrieves the OnVertex the hybShpCorner hybrid shape
                | corner in OnVertex. Dim bOnVertex As boolean bOnVertex =
                | hybShpCorner.OnVertex

        :return:
        """
        return self.hybrid_shape_corner.OnVertex

    @on_vertex.setter
    def on_vertex(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.OnVertex = value 

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Returns the corner radius. 
                |
                | Example:
                | This example retrieves
                | the radius of the hybShpCorner hybrid shape corner in
                | radius. Dim radius As CATIALength radius =
                | hybShpCorner.Radius

        :return:
        """
        return self.hybrid_shape_corner.Radius

    @property
    def second_elem(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondElem
                | o Property SecondElem(    ) As
                | 
                | Returns or sets the corner second reference element. Legal
                | values: This is always a curve. Sub-element(s) supported
                | (see object): , or . 
                |
                | Example:
                | This example retrieves the
                | second reference element of the hybShpCorner hybrid shape
                | corner in secondElt. Dim secondElt As CATIAReference
                | secondElt = hybShpCorner.SecondElem

        :return:
        """
        return self.hybrid_shape_corner.SecondElem

    @second_elem.setter
    def second_elem(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.SecondElem = value 

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondOrientation
                | o Property SecondOrientation(    ) As
                | 
                | Returns or sets the orientation of the corner second
                | reference element. The orientation specifies the corner
                | center position. It is either the same of the inverse
                | orientation than those of the cross product: Normal(Support)
                | ^ Tangent(SecondElem) Legal values: 1 if the orientation of
                | the corner second reference element is the same than the
                | cross product: Normal(Support) ^ Tangent(SecondElem), and -1
                | if it is the inverse. 
                |
                | Example:
                | This example sets the
                | orientation of second reference element of the hybShpCorner
                | hybrid shape corner to the inverse of the cross porduct
                | Normal(Support) ^ Tangent(SecondElem).
                | hybShpCorner.SecondOrientation = -1

        :return:
        """
        return self.hybrid_shape_corner.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.SecondOrientation = value 

    @property
    def second_tangent_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondTangentOrientation
                | o Property SecondTangentOrientation(    ) As
                | 
                | Returns or sets the tangent orientation of the corner second
                | reference element. compared to the corner itself Example:
                | This example retrieves the tangent orientation of second
                | reference element of the hybShpCorner hybrid shape corner in
                | secondOrient. Dim secondOrient As long firstOrient =
                | hybShpCorner.SecondTangentOrientation

        :return:
        """
        return self.hybrid_shape_corner.SecondTangentOrientation

    @second_tangent_orientation.setter
    def second_tangent_orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.SecondTangentOrientation = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the corner support. Legal values: This can
                | be a plane or a surface. Sub-element(s) supported (see
                | object): . 
                |
                | Example:
                | This example sets the support of the
                | hybShpCorner hybrid shape corner as the exisiting surgace
                | supportSurf. hybShpCorner.Support = supportSurf

        :return:
        """
        return self.hybrid_shape_corner.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.Support = value 

    @property
    def trim(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Trim
                | o Property Trim(    ) As
                | 
                | Returns or sets whether the corner reference curves are or
                | should be trimmed. Legal values: True if the corner
                | reference curves are or should be trimmed, and False
                | otherwise. 
                |
                | Example:
                | This example sets that the corner
                | reference curves of the hybShpCorner hybrid shape corner
                | should be trimmed. hybShpCorner.Trim = True

        :return:
        """
        return self.hybrid_shape_corner.Trim

    @trim.setter
    def trim(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.Trim = value 

    @property
    def trim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TrimMode
                | o Property TrimMode(    ) As
                | 
                | Returns or sets whether the corner reference curves are or
                | should be trimmed. Legal values: 1 if the corner reference
                | curves are or should be trimmed, 0 if the corner reference
                | curves are not or should not be trimmed, 2 if only the first
                | corner reference curve is or should be trimmed, 3 if only
                | the second corner reference curve is or should be trimmed,
                | 
                |
                | Example:
                | This example sets that the corner reference curves
                | of the hybShpCorner hybrid shape corner should be trimmed.
                | hybShpCorner.TrimMode = 1

        :return:
        """
        return self.hybrid_shape_corner.TrimMode

    @trim_mode.setter
    def trim_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_corner.TrimMode = value 

    def invert_first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertFirstOrientation
                | o Sub InvertFirstOrientation(    )
                | 
                | Inverts the first reference element orientation used to
                | compute the corner. 
                |
                | Example:
                | This example inverts the first
                | corner reference element orientation of the hybShpCorner.
                | hybShpCorner.InvertFirstOrientation
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_corner.InvertFirstOrientation()

    def invert_second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InvertSecondOrientation
                | o Sub InvertSecondOrientation(    )
                | 
                | Inverts the second reference element orientation used to
                | compute the corner. 
                |
                | Example:
                | This example inverts the second
                | corner reference element orientation of the hybShpCorner.
                | hybShpCorner.InvertSecondOrientation
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_corner.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeCorner()'
