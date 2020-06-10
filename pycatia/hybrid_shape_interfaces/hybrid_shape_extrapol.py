#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtrapol(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeExtrapol
                | 
                | Represents the hybrid shape extrapolation feature object.
                | Role: To access the data of the hybrid shape affinity feature object. The
                | hybrid shape extrapolation feature object is created by using an element (a
                | curve or a surface), a boundary of this element (a point in case of curve
                | extrapolation or a curve in case of surface extrapolation), and a limit (which
                | can be specified by a length or a limit element).
                | The continuity between the extrapolated element and the extrapolation can be
                | either tangent continuity or curvature continuity.
                | The extrapolation can be assembled or not with the extrapolated curve or
                | surface. In case of surface extrapolation, extrapolation borders can
                | be:
                | 
                |     Normal to the boundary of the extrapolated surface
                |     Tangent to the edges of the extrapolated surface, that are adjacent to the
                |     boundary
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtrapol
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extrapol = com_object

    @property
    def border_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property BorderType() As long
                | 
                |     Returns or sets the border type of extrapolation.
                |     This applies for surface extrapolation only.
                |     Legal values: the border type is either normal to the boundary of the
                |     extrapolated surface (CATGSMNormalBorder(=0)), or tangent to the edges of the
                |     extrapolated surface that are adjacent to the boundary
                |     CATGSMTangentBorder(=1)).

        :return: int
        """

        return self.hybrid_shape_extrapol.BorderType

    @border_type.setter
    def border_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extrapol.BorderType = value

    @property
    def boundary(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Boundary() As Reference
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetBoundary method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extrapol.Boundary)

    @boundary.setter
    def boundary(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extrapol.Boundary = value

    @property
    def constant_length_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ConstantLengthMode() As boolean
                | 
                |     Returns or sets the constant distance mode in case of Length extrapolation
                |     limit.
                |     This applies in case of Length extrapolation limit.

        :return: bool
        """

        return self.hybrid_shape_extrapol.ConstantLengthMode

    @constant_length_mode.setter
    def constant_length_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_extrapol.ConstantLengthMode = value

    @property
    def continuity_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ContinuityType() As long
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetContinuityType method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: int
        """

        return self.hybrid_shape_extrapol.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extrapol.ContinuityType = value

    @property
    def elem_to_extrapol(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ElemToExtrapol() As Reference
                | 
                |     Returns or sets the curve or surface to extrapolate.
                |     Sub-element(s) supported (see Boundary object): see Face , TriDimFeatEdge
                |     or BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extrapol.ElemToExtrapol)

    @elem_to_extrapol.setter
    def elem_to_extrapol(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extrapol.ElemToExtrapol = value

    @property
    def elem_until(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ElemUntil() As Reference
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetElemUntil method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extrapol.ElemUntil)

    @elem_until.setter
    def elem_until(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extrapol.ElemUntil = value

    @property
    def extend_edges_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ExtendEdgesMode() As boolean
                | 
                |     Returns or sets the extension of extrapolated edges mode.
                |     This applies in case of tangent continuity mode, tangent border mode and
                |     assembled result.

        :return: bool
        """

        return self.hybrid_shape_extrapol.ExtendEdgesMode

    @extend_edges_mode.setter
    def extend_edges_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_extrapol.ExtendEdgesMode = value

    @property
    def extrapol_both_sides_identically(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ExtrapolBothSidesIdentically() As boolean
                | 
                |     Returns or sets the the boolean telling if the second side is extrapolated
                |     according to the first side's settings or to its own ones.
                |     This applies in case the element to extrapol is a wire.

        :return: bool
        """

        return self.hybrid_shape_extrapol.ExtrapolBothSidesIdentically

    @extrapol_both_sides_identically.setter
    def extrapol_both_sides_identically(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_extrapol.ExtrapolBothSidesIdentically = value

    @property
    def length(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Length() As Length (Read Only)
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetLength method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: Length
        """

        return Length(self.hybrid_shape_extrapol.Length)

    @property
    def limit_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property LimitType() As long
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetLimitType method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: int
        """

        return self.hybrid_shape_extrapol.LimitType

    @limit_type.setter
    def limit_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extrapol.LimitType = value

    @property
    def propagation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property PropagationMode() As long
                | 
                |     Returns or sets the propagation mode.
                |     This applies in case of curvature extrapolation of a shell.

        :return: int
        """

        return self.hybrid_shape_extrapol.PropagationMode

    @propagation_mode.setter
    def propagation_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_extrapol.PropagationMode = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support surface.
                |     This applies in case of tangent extrapolation of a wire. If a support
                |     surface is given, the extrapolation will lie on it.
                |     Sub-element(s) supported (see Boundary object): see Face.

        :return: Reference
        """

        return Reference(self.hybrid_shape_extrapol.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_extrapol.Support = value

    def get_boundary(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetBoundary(long iPos) As Reference
                | 
                |     Returns or sets the iPos-th boundary of an extrapolated curve or surface
                |     from which extrapolation begins. If iPos equals 0 or the number of
                |     extrapolations, SetBoundary appends iBoundary to the list of
                |     boundaries.
                |     The boudary is a point for an extrapolated curve, or a curve for an
                |     extrapolated surface.
                |     Sub-element(s) supported (see Boundary object): see Face , TriDimFeatEdge
                |     or BiDimFeatEdge.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.hybrid_shape_extrapol.GetBoundary(i_pos))

    def get_continuity_type(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetContinuityType(long iPos) As long
                | 
                |     Returns or sets the continuity type between extrapolated element and
                |     extrapolation at the iPos-th boundary. If iPos equals 0 or the number of
                |     extrapolations, SetContinuityType appends iLim to the list of
                |     lengths.
                |     Legal values: the continuity type is either CATGSMTangentContinuity (=0) or
                |     CATGSMCurvatureContinuity (=1).

        :param int i_pos:
        :return: int
        """
        return int(self.hybrid_shape_extrapol.GetContinuityType(i_pos))

    def get_elem_until(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetElemUntil(long iPos) As Reference
                | 
                |     Returns or sets the surface or volume specifying the limit of the
                |     extrapolation that begins from the iPos-th boundary. If iPos equals 0 or the
                |     number of extrapolations, SetElemUntil appends iElemUntil to the list of up-to
                |     elements.
                |     This applies when the limit type is CATGSMUpToElementLimit (=1).

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.hybrid_shape_extrapol.GetElemUntil(i_pos))

    def get_internal_edges_element(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetInternalEdgesElement(long iPos) As Reference
                | 
                |     Gets an element in the list of internal elements (vertex or
                |     edges).
                | 
                |     Parameters:
                | 
                |         oInternalElement
                |             internal element 
                |         iPos
                |             position of internal element to be retrieved.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.hybrid_shape_extrapol.GetInternalEdgesElement(i_pos))

    def get_length(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLength(long iPos) As Length
                | 
                |     Returns or sets the length specifying the limit of the extrapolation that
                |     begins from the iPos-th boundary. If iPos equals 0 or the number of
                |     extrapolations, SetLength appends iLength to the list of
                |     lengths.
                |     This applies when the limit type is CATGSMLengthLimit (=0).

        :param int i_pos:
        :return: Length
        """
        return Length(self.hybrid_shape_extrapol.GetLength(i_pos))

    def get_limit_type(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLimitType(long iPos) As long
                | 
                |     Returns or sets the limit type of the extrapolation that begins from the
                |     iPos-th boundary. If iPos equals 0 or the number of extrapolations,
                |     SetLimitType appends iLim to the list of limit types.
                |     The limit can be a length, a surface, or a volume.
                |     Legal values: the limit type is either CATGSMLengthLimit(0) or
                |     CATGSMUpToElementLimit(1).

        :param int i_pos:
        :return: int
        """
        return int(self.hybrid_shape_extrapol.GetLimitType(i_pos))

    def get_number_of_extrapolations(self, o_number_of_extrapolations=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetNumberOfExtrapolations(long
                | oNumberOfExtrapolations)
                | 
                |     Returns the number of extrapolations set. An extrapolation is specified by
                |     a boundary of the element to extrapolate, a limit type, a limit and a
                |     continuity type.

        :param int o_number_of_extrapolations:
        :return: None
        """
        return self.hybrid_shape_extrapol.GetNumberOfExtrapolations(o_number_of_extrapolations)

    def is_assemble(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func IsAssemble() As boolean
                | 
                |     Retrieves whether extrapolation is assembled with extrapolated curve or
                |     surface.
                | 
                |     Parameters:
                | 
                |         oAssemble
                |             The assemble option
                |             True when the extrapolation is assembled with extrapolated curve or
                |             surface, and False otherwise

        :return: bool
        """
        return bool(self.hybrid_shape_extrapol.IsAssemble())

    def remove_all_extrapolations_except_the_first_one(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveAllExtrapolationsExceptTheFirstOne()
                | 
                |     Removes all extrapolations that may have been set, except the first one.

        :return: None
        """
        return self.hybrid_shape_extrapol.RemoveAllExtrapolationsExceptTheFirstOne()

    def remove_all_internal_edges_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveAllInternalEdgesElement()
                | 
                |     Removes all internal elements.

        :return: None
        """
        return self.hybrid_shape_extrapol.RemoveAllInternalEdgesElement()

    def remove_extrapolation(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveExtrapolation(long iPos)
                | 
                |     Removes the iPos-th extrapolation that has been set.

        :param int i_pos:
        :return: None
        """
        return self.hybrid_shape_extrapol.RemoveExtrapolation(i_pos)

    def set_assemble(self, i_assemble=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetAssemble(boolean iAssemble)
                | 
                |     Sets whether extrapolation is to be assembled with extrapolated curve or
                |     surface.
                | 
                |     Parameters:
                | 
                |         iAssemble
                |             The assemble option
                |             True when the extrapolation is to be assembled with extrapolated
                |             curve or surface, and False otherwise.

        :param bool i_assemble:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetAssemble(i_assemble)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_assemble'
        # # vba_code = """
        # # Public Function set_assemble(hybrid_shape_extrapol)
        # #     Dim iAssemble (2)
        # #     hybrid_shape_extrapol.SetAssemble iAssemble
        # #     set_assemble = iAssemble
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_boundary(self, i_pos=None, i_boundary=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetBoundary(long iPos,
                | Reference iBoundary)

        :param int i_pos:
        :param Reference i_boundary:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetBoundary(i_pos, i_boundary)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_boundary'
        # # vba_code = """
        # # Public Function set_boundary(hybrid_shape_extrapol)
        # #     Dim iPos (2)
        # #     hybrid_shape_extrapol.SetBoundary iPos
        # #     set_boundary = iPos
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_continuity_type(self, i_pos=None, i_lim=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetContinuityType(long iPos,
                | long iLim)

        :param int i_pos:
        :param int i_lim:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetContinuityType(i_pos, i_lim)

    def set_elem_until(self, i_pos=None, i_elem_until=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetElemUntil(long iPos,
                | Reference iElemUntil)

        :param int i_pos:
        :param Reference i_elem_until:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetElemUntil(i_pos, i_elem_until)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_elem_until'
        # # vba_code = """
        # # Public Function set_elem_until(hybrid_shape_extrapol)
        # #     Dim iPos (2)
        # #     hybrid_shape_extrapol.SetElemUntil iPos
        # #     set_elem_until = iPos
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_length(self, i_pos=None, i_length=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLength(long iPos,
                | Length iLength)
                | 
                |     Do not use this method.

        :param int i_pos:
        :param Length i_length:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetLength(i_pos, i_length)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_length'
        # # vba_code = """
        # # Public Function set_length(hybrid_shape_extrapol)
        # #     Dim iPos (2)
        # #     hybrid_shape_extrapol.SetLength iPos
        # #     set_length = iPos
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_length_d(self, i_pos=None, i_length=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLengthD(long iPos,
                | double iLength)

        :param int i_pos:
        :param float i_length:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetLengthD(i_pos, i_length)

    def set_limit_type(self, i_pos=None, i_lim=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLimitType(long iPos,
                | long iLim)

        :param int i_pos:
        :param int i_lim:
        :return: None
        """
        return self.hybrid_shape_extrapol.SetLimitType(i_pos, i_lim)

    def __repr__(self):
        return f'HybridShapeExtrapol(name="{ self.name }")'
