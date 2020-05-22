#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeExtrapol(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape extrapolation feature object.Role:  To
                | access the data of the hybrid shape affinity feature object. The
                | hybrid shape extrapolation feature object is created by using an
                | element (a curve or a surface), a boundary of this element (a point in
                | case of curve extrapolation or a curve in case of surface
                | extrapolation), and a limit  (which can be specified by a length or a
                | limit element).The continuity between the extrapolated element and the
                | extrapolation can be  either tangent continuity or curvature
                | continuity.The extrapolation can be assembled or not with the
                | extrapolated curve or surface. In case of surface extrapolation,
                | extrapolation borders can be:Use the  CATIAHybridShapeFactory to
                | create a HybridShapeExtrapol object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extrapol = com_object     

    @property
    def border_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BorderType
                | o Property BorderType(    ) As
                | 
                | Returns or sets the border type of extrapolation. This
                | applies for surface extrapolation only. Legal values: the
                | border type is either normal to the boundary of the
                | extrapolated surface (CATGSMNormalBorder(=0)), or tangent to
                | the edges of the extrapolated surface that are adjacent to
                | the boundary CATGSMTangentBorder(=1)).

        :return:
        """
        return self.hybrid_shape_extrapol.BorderType

    @border_type.setter
    def border_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.BorderType = value 

    @property
    def boundary(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Boundary
                | o Property Boundary(    ) As
                | 
                | Returns or sets the boundary of an extrapolated curve or
                | surface from which extrapolation begins. The boudary is a
                | point for an extrapolated curve, or a curve for an
                | extrapolated surface. Sub-element(s) supported (see object):
                | see , or .

        :return:
        """
        return self.hybrid_shape_extrapol.Boundary

    @boundary.setter
    def boundary(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.Boundary = value 

    @property
    def constant_length_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConstantLengthMode
                | o Property ConstantLengthMode(    ) As
                | 
                | Returns or sets the constant distance mode in case of Length
                | extrapolation limit. This applies in case of Length
                | extrapolation limit.

        :return:
        """
        return self.hybrid_shape_extrapol.ConstantLengthMode

    @constant_length_mode.setter
    def constant_length_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.ConstantLengthMode = value 

    @property
    def continuity_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ContinuityType
                | o Property ContinuityType(    ) As
                | 
                | Returns or sets the continuity type between extrapolated
                | element and extrapolation. Legal values: the continuity type
                | is either CATGSMTangentContinuity (=0) or
                | CATGSMCurvatureContinuity (=1).

        :return:
        """
        return self.hybrid_shape_extrapol.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.ContinuityType = value 

    @property
    def elem_to_extrapol(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToExtrapol
                | o Property ElemToExtrapol(    ) As
                | 
                | Returns or sets the curve or surface to extrapolate. Sub-
                | element(s) supported (see object): see , or .

        :return:
        """
        return self.hybrid_shape_extrapol.ElemToExtrapol

    @elem_to_extrapol.setter
    def elem_to_extrapol(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.ElemToExtrapol = value 

    @property
    def elem_until(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemUntil
                | o Property ElemUntil(    ) As
                | 
                | Returns or sets the surface or volume specifying the
                | extrapolation limit. This applies when the limit type is
                | CATGSMUpToElementLimit (=1).

        :return:
        """
        return self.hybrid_shape_extrapol.ElemUntil

    @elem_until.setter
    def elem_until(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.ElemUntil = value 

    @property
    def extend_edges_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExtendEdgesMode
                | o Property ExtendEdgesMode(    ) As
                | 
                | Returns or sets the extension of extrapolated edges mode.
                | This applies in case of tangent continuity mode, tangent
                | border mode and assembled result.

        :return:
        """
        return self.hybrid_shape_extrapol.ExtendEdgesMode

    @extend_edges_mode.setter
    def extend_edges_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.ExtendEdgesMode = value 

    @property
    def length(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Length
                | o Property Length(    ) As   (Read Only)
                | 
                | Returns the length specifying the extrapolation limit. This
                | applies when the limit type is CATGSMLengthLimit (=0).

        :return:
        """
        return self.hybrid_shape_extrapol.Length

    @property
    def limit_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LimitType
                | o Property LimitType(    ) As
                | 
                | Returns or sets the limit type of extrapolation. The limit
                | can be a length, a surface, or a volume. Legal values: the
                | limit type is either CATGSMLengthLimit(0) or
                | CATGSMUpToElementLimit(1).

        :return:
        """
        return self.hybrid_shape_extrapol.LimitType

    @limit_type.setter
    def limit_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.LimitType = value 

    @property
    def propagation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PropagationMode
                | o Property PropagationMode(    ) As
                | 
                | Returns or sets the propagation mode. This applies in case
                | of curvature extrapolation of a shell.

        :return:
        """
        return self.hybrid_shape_extrapol.PropagationMode

    @propagation_mode.setter
    def propagation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.PropagationMode = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support surface. This applies in case of
                | tangent extrapolation of a wire. If a support surface is
                | given, the extrapolation will lie on it. Sub-element(s)
                | supported (see object): see .

        :return:
        """
        return self.hybrid_shape_extrapol.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_extrapol.Support = value 

    def get_internal_edges_element(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInternalEdgesElement
                | o Func GetInternalEdgesElement(        iPos) As
                | 
                | Gets an element in the list of internal elements (vertex or
                | edges).
                |
                | Parameters:
                | oInternalElement
                |        internal element
                |    
                |  iPos
                |        position of internal element to be retrieved.


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_extrapol.GetInternalEdgesElement(i_pos)

    def is_assemble(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsAssemble
                | o Func IsAssemble(    ) As
                | 
                | Retrieves whether extrapolation is assembled with
                | extrapolated curve or surface.
                |
                | Parameters:
                | oAssemble
                |     The assemble option
                |    True when the extrapolation is assembled with extrapolated curve or surface,
                |    and False otherwise


        :return:
        """
        return self.hybrid_shape_extrapol.IsAssemble()

    def remove_all_internal_edges_element(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllInternalEdgesElement
                | o Sub RemoveAllInternalEdgesElement(    )
                | 
                | Removes all internal elements.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_extrapol.RemoveAllInternalEdgesElement()

    def set_assemble(self, i_assemble):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAssemble
                | o Sub SetAssemble(        iAssemble)
                | 
                | Sets whether extrapolation is to be assembled with
                | extrapolated curve or surface.
                |
                | Parameters:
                | iAssemble
                |     The assemble option
                |    True when the extrapolation is to be assembled with extrapolated curve or surface,
                |    and False otherwise.


        :param i_assemble:
        :return:
        """
        return self.hybrid_shape_extrapol.SetAssemble(i_assemble)

    def __repr__(self):
        return f'HybridShapeExtrapol()'
