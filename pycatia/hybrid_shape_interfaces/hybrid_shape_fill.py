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


class HybridShapeFill(HybridShape):
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
                |                         HybridShapeFill
                | 
                | The Fill feature : an Fill is made up of a face to process and one Fill parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fill = com_object

    @property
    def advanced_tolerant_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AdvancedTolerantMode() As long
                | 
                |     Returns or sets the tolerant mode taken into account during fill
                |     construction.
                |     Legal values:
                | 
                |     0
                |         Unknown tolerant mode.
                |     1
                |         None tolerant mode. Error thrown if maximum deviation exceeds CATIA
                |         resolution.
                |     2
                |         Automatic tolerant mode. Error thrown if maximum deviation exceeds 100
                |         times CATIA resolution.
                |     3
                |         Manual tolerant mode. Error thrown if maximum deviation exceeds input
                |         user deviation.
                | 
                |     Example:
                |         This example retrieves in oMode the tolerant mode for the Fill hybrid
                |         shape feature.
                | 
                |          Dim oMode
                |          Set oMode = Fill.AdvancedTolerantMode

        :rtype: int
        """

        return self.hybrid_shape_fill.AdvancedTolerantMode

    @advanced_tolerant_mode.setter
    def advanced_tolerant_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fill.AdvancedTolerantMode = value

    @property
    def constraint(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Constraint() As Reference
                | 
                |     Returns or sets the passing point for the Fill.
                | 
                |     Example:
                |         This example retrieves in Element the passing point for the Fill hybrid
                |         shape feature.
                | 
                |          Dim Element As Reference 
                |          Set Element = Fill.Constraint

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_fill.Constraint)

    @constraint.setter
    def constraint(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_fill.Constraint = reference.com_object

    @property
    def continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Continuity() As long
                | 
                |     Returns or sets the continuity between the support and
                |     fill.
                |     Legal values:
                | 
                |     0
                |         Continuity in point (C0)
                |     1
                |         Continuity in tangency (C1)
                |     2
                |         Continuity in curvature (C2)
                | 
                |     Example:
                |         This example retrieves in oContinuity the continuity type for the Fill
                |         hybrid shape feature.
                | 
                |          Dim oContinuity
                |          Set oContinuity = Fill.Continuity

        :rtype: int
        """

        return self.hybrid_shape_fill.Continuity

    @continuity.setter
    def continuity(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fill.Continuity = value

    @property
    def detection(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Detection() As short
                | 
                |     Returns or sets the Canonical portion detection option.
                |     Legal values:
                | 
                |     0
                |         No detection of canonical surface
                |     2
                |         Detection of canonical surfaces

        :rtype: int
        """

        return self.hybrid_shape_fill.Detection

    @detection.setter
    def detection(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_fill.Detection = value

    @property
    def maximum_deviation_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaximumDeviationValue() As double
                | 
                |     Sets or Gets the maximum deviation allowed for smoothing operation in fill
                |     commnd. This value must be set in SI unit (m).
                | 
                |     Example: This example retrieves in DeviationValue the maximum deviation
                |     value for the Fill hybrid shape feature.
                | 
                |      Dim DeviationValue As double
                |      Set DeviationValue = Fill.MaximumDeviationValue

        :rtype: float
        """

        return self.hybrid_shape_fill.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_fill.MaximumDeviationValue = value

    @property
    def plane_only_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PlaneOnlyMode() As boolean
                | 
                |     Returns or sets whether Planar Boundaries only should be considered during
                |     fill operation.
                |     Legal values:
                | 
                |     TRUE
                |         Planar boundaries are only considered during Fill
                |         operation
                |     FALSE
                |         Non-Planar boundaries are also considered during Fill
                |         operation

        :rtype: bool
        """

        return self.hybrid_shape_fill.PlaneOnlyMode

    @plane_only_mode.setter
    def plane_only_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_fill.PlaneOnlyMode = value

    @property
    def tolerant_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TolerantMode() As boolean
                | 
                |     Deprecated:
                |         V5R26 Use HybridShapeFill.AdvancedTolerantMode Returns or sets the Tolerant mode option.
                |         Role: To activate or not the tolerant mode option TRUE : Tolerant mode is active.
                |         Uses deviation parameter to do tolerant fill. FALSE : Tolerant mode is not active.
                | 
                |         Example: This example retrieves in tolMode the tolerant mode for the
                |         Fill hybrid shape feature.
                | 
                |          Dim tolMode As boolean
                |          Set tolMode = Fill.TolerantMode

        :rtype: bool
        """

        return self.hybrid_shape_fill.TolerantMode

    @tolerant_mode.setter
    def tolerant_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_fill.TolerantMode = value

    def add_bound(self, i_boundary: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddBound(Reference iBoundary)
                | 
                |     Adds an boundary to the hybrid shape fill feature object.
                | 
                |     Parameters:
                | 
                |         iBoundary
                |             The boundary(curve) to be added to the hybrid shape fill feature
                |             object. 
                | 
                |     Example:
                |         The following example adds the iBoundary curve to the Fill
                |         object.
                | 
                |          Fill.AddBound iBoundary

        :param Reference i_boundary:
        :rtype: None
        """
        return self.hybrid_shape_fill.AddBound(i_boundary.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_bound'
        # # vba_code = """
        # # Public Function add_bound(hybrid_shape_fill)
        # #     Dim iBoundary (2)
        # #     hybrid_shape_fill.AddBound iBoundary
        # #     add_bound = iBoundary
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_at_bound(self, i_boundary: Reference, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddSupportAtBound(Reference iBoundary,
                | Reference iSupport)
                | 
                |     Inserts the support at specified boundary in the Fill.
                | 
                |     Parameters:
                | 
                |         iBoundary
                |             Reference of the boundary object to which support has to be added.
                |             
                |         iSupport
                |             Reference of the support object to be added.
                | 
                |             Example:
                |                 This example adds supports in the Fill feature Fill to
                |                 specified iBoundary boundary
                | 
                |                  Fill.AddSupportAtBound iBoundary,iSupport

        :param Reference i_boundary:
        :param Reference i_support:
        :rtype: None
        """
        return self.hybrid_shape_fill.AddSupportAtBound(i_boundary.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_at_bound'
        # # vba_code = """
        # # Public Function add_support_at_bound(hybrid_shape_fill)
        # #     Dim iBoundary (2)
        # #     hybrid_shape_fill.AddSupportAtBound iBoundary
        # #     add_support_at_bound = iBoundary
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def append_constraint(self, i_constraint: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AppendConstraint(Reference iConstraint)
                | 
                |     Appends an constraint to the hybrid shape fill feature object. ========
                |     ONLY USE IN FSS ==============
                | 
                |     Parameters:
                | 
                |         iConstraint
                |             The constraint to be appended. 
                | 
                |     Example:
                |         The following example appends the iConstraint constraint to the Fill
                |         object.
                | 
                |          Fill.AppendConstraint iConstraint

        :param Reference i_constraint:
        :rtype: None
        """
        return self.hybrid_shape_fill.AppendConstraint(i_constraint.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'append_constraint'
        # # vba_code = """
        # # Public Function append_constraint(hybrid_shape_fill)
        # #     Dim iConstraint (2)
        # #     hybrid_shape_fill.AppendConstraint iConstraint
        # #     append_constraint = iConstraint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_bound_at_position(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoundAtPosition(long iPos) As Reference
                | 
                |     Retrieves the boundary at specified position in the hybrid shape fill
                |     feature object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the boundary to retrieve. 
                | 
                |     Example:
                |         The following example gets the oBoundary boundary of the Fill object at
                |         the position iPos.
                | 
                |          Dim oBoundary As Reference
                |          Set oBoundary = Fill.GetBoundAtPosition (iPos).

        :param int i_pos:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_fill.GetBoundAtPosition(i_pos))

    def get_bound_position(self, i_boundary: Reference) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoundPosition(Reference iBoundary) As long
                | 
                |     Retrieves the position of a boundary used by the hybrid shape fill feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iBoundary
                |             The boundary whose position has to be retrieved. 
                | 
                |     Example:
                |         The following example gets the oPos position of the iBoundary boundary
                |         in the Fill object.
                | 
                |          Dim oPos As  long
                |          oPos = Fill.GetBoundPosition (iBoundary).

        :param Reference i_boundary:
        :rtype: int
        """
        return self.hybrid_shape_fill.GetBoundPosition(i_boundary.com_object)

    def get_bound_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoundSize() As long
                | 
                |     Returns the number of boundaries in the Fill object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of boundaries in the Fill.
                | 
                |             Example:
                |                 This example retrieves the number of boundaries in the Fill
                |                 hybrid shape fill.
                | 
                |                  Dim oSize As  long
                |                  oSize = Fill.GetBoundSize

        :rtype: int
        """
        return self.hybrid_shape_fill.GetBoundSize()

    def get_boundary_continuity(self, i_pos: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoundaryContinuity(long iPos) As long
                | 
                |     Returns the continuity mode for a boundary at specified position in the
                |     Fill.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position at which the continuity should be retrieved.
                |             
                |         oContinuity
                |             Continuity retrieved between the support and the
                |             fill.
                |             Legal values:
                | 
                |             0
                |                 Continuity in point (C0)
                |             1
                |                 Continuity in tangency (C1)
                |             2
                |                 Continuity in curvature (C2)
                | 
                |     Example:
                |         This example retrieves in oContinuity the continuity at the specified
                |         position of Fill hybrid shape fill feature.
                | 
                |          oContinuity = Fill.GetBoundaryContinuity iPos

        :param int i_pos:
        :rtype: int
        """
        return self.hybrid_shape_fill.GetBoundaryContinuity(i_pos)

    def get_constraint_at_position(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetConstraintAtPosition(long iPos) As Reference
                | 
                |     Retrieves the constraint at specified position in the hybrid shape fill
                |     feature object. ======== ONLY USE IN FSS ==============
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the constraint to retrieve. 
                | 
                |     Example:
                |         The following example gets the oConstraint constraint of the Fill
                |         object at the position iPos.
                | 
                |          Dim oConstraint As Reference
                |          Set oConstraint = Fill.GetConstraintAtPosition (iPos).

        :param int i_pos:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_fill.GetConstraintAtPosition(i_pos))

    def get_constraints_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetConstraintsSize() As long
                | 
                |     Returns the number of constraints in the Fill object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of constraints in the Fill.
                | 
                |             Example:
                |                 This example retrieves the number of constraints in the Fill
                |                 hybrid shape fill.
                | 
                |                  Dim oSize As  long
                |                  oSize = Fill.GetConstraintsSize

        :rtype: int
        """
        return self.hybrid_shape_fill.GetConstraintsSize()

    def get_support_at_position(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSupportAtPosition(long iPos) As Reference
                | 
                |     Retrieves the support at specified position in the hybrid shape fill
                |     feature object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the support to retrieve. 
                | 
                |     Example:
                |         The following example gets the oSupport support of the Fill object at
                |         the position iPos.
                | 
                |          Dim oSupport As Reference
                |          Set oSupport = Fill.GetSupportAtPosition (iPos).

        :param int i_pos:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_fill.GetSupportAtPosition(i_pos))

    def insert_bound_after_position(self, i_boundary: Reference, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertBoundAfterPosition(Reference iBoundary,
                | long iPos)
                | 
                |     Inserts the boundary after specified position in the Fill.
                | 
                |     Parameters:
                | 
                |         iBoundary
                |             Reference of the boundary object to be inserted. 
                |         iPos
                |             Position after which the element should be
                |             inserted.
                | 
                |             Example:
                |                 This example inserts the boundary in the Fill feature Fill
                |                 after position iPos
                | 
                |                  Fill.InsertBoundAfterPosition iBoundary,iPos

        :param Reference i_boundary:
        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.InsertBoundAfterPosition(i_boundary.com_object, i_pos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_bound_after_position'
        # # vba_code = """
        # # Public Function insert_bound_after_position(hybrid_shape_fill)
        # #     Dim iBoundary (2)
        # #     hybrid_shape_fill.InsertBoundAfterPosition iBoundary
        # #     insert_bound_after_position = iBoundary
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_all_bound(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAllBound()
                | 
                |     Removes all boundaries of the hybrid shape fill feature object.
                |     
                | 
                | Example:
                |     The following example removes all boundaries of the Fill
                |     object.
                | 
                |      Fill.RemoveAllBound

        :rtype: None
        """
        return self.hybrid_shape_fill.RemoveAllBound()

    def remove_all_constraints(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAllConstraints()
                | 
                |     Removes all constraints.

        :rtype: None
        """
        return self.hybrid_shape_fill.RemoveAllConstraints()

    def remove_bound_at_position(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveBoundAtPosition(long iPos)
                | 
                |     Removes boundary at specified position in hybrid shape fill feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the boundary to remove. 
                | 
                |     Example:
                |         The following example removes the boundary object from the Fill object
                |         at the position iPos.
                | 
                |          Fill.RemoveBoundAtPosition iPos.

        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.RemoveBoundAtPosition(i_pos)

    def remove_constraint(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveConstraint(long iPos)
                | 
                |     Removes constraint at specified position in hybrid shape fill feature
                |     object. ======== ONLY USE IN FSS ==============
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the constraint to remove. 
                | 
                |     Example:
                |         The following example removes the constraint object from the Fill
                |         object at the position iPos.
                | 
                |          Fill.RemoveConstraint iPos.

        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.RemoveConstraint(i_pos)

    def remove_support_at_position(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSupportAtPosition(long iPos)
                | 
                |     Removes support at specified position in hybrid shape fill feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the support to remove. 
                | 
                |     Example:
                |         The following example removes the support object from the Fill object
                |         at the position iPos.
                | 
                |          Fill.RemoveSupportAtPosition iPos.

        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.RemoveSupportAtPosition(i_pos)

    def replace_bound_at_position(self, i_boundary: Reference, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReplaceBoundAtPosition(Reference iBoundary,
                | long iPos)
                | 
                |     Replaces the boundary at specified position in the Fill.
                | 
                |     Parameters:
                | 
                |         iBoundary
                |             Reference of the boundary object to be replaced. 
                |         iPos
                |             Position at which the boundary should be replaced.
                | 
                |             Example:
                |                 This example replaces the boundary in the Fill feature Fill at
                |                 specified position iPos
                | 
                |                  Fill.ReplaceBoundAtPosition iBoundary,iPos

        :param Reference i_boundary:
        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.ReplaceBoundAtPosition(i_boundary.com_object, i_pos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_bound_at_position'
        # # vba_code = """
        # # Public Function replace_bound_at_position(hybrid_shape_fill)
        # #     Dim iBoundary (2)
        # #     hybrid_shape_fill.ReplaceBoundAtPosition iBoundary
        # #     replace_bound_at_position = iBoundary
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def replace_constraint(self, i_pos: int, i_constraint: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReplaceConstraint(long iPos,
                | Reference iConstraint)
                | 
                |     Replaces the constraint at specified position in the Fill.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position at which the constraint should be replaced.
                |             
                |         iConstraint
                |             Reference of the constraint object to be replaced.
                | 
                |             Example:
                |                 This example replaces the constraint in the Fill feature Fill
                |                 at specified position iPos
                | 
                |                  Fill.ReplaceConstraint iPos,iConstraint

        :param int i_pos:
        :param Reference i_constraint:
        :rtype: None
        """
        return self.hybrid_shape_fill.ReplaceConstraint(i_pos, i_constraint.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_constraint'
        # # vba_code = """
        # # Public Function replace_constraint(hybrid_shape_fill)
        # #     Dim iPos (2)
        # #     hybrid_shape_fill.ReplaceConstraint iPos
        # #     replace_constraint = iPos
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def replace_support_at_position(self, i_support: Reference, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReplaceSupportAtPosition(Reference iSupport,
                | long iPos)
                | 
                |     Replaces the support at specified position in the Fill.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             Reference of the support object to be replaced. 
                |         iPos
                |             Position at which the support should be replaced.
                | 
                |             Example:
                |                 This example replaces the support in the Fill feature Fill at
                |                 specified position iPos
                | 
                |                  Fill.ReplaceSupportAtPosition iSupport,iPos

        :param Reference i_support:
        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.ReplaceSupportAtPosition(i_support.com_object, i_pos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_support_at_position'
        # # vba_code = """
        # # Public Function replace_support_at_position(hybrid_shape_fill)
        # #     Dim iSupport (2)
        # #     hybrid_shape_fill.ReplaceSupportAtPosition iSupport
        # #     replace_support_at_position = iSupport
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_boundary_continuity(self, i_continuity: int, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBoundaryContinuity(long iContinuity,
                | long iPos)
                | 
                |     Sets the continuity mode for a boundary at specified position in the
                |     Fill.
                | 
                |     Parameters:
                | 
                |         iContinuity
                |             Continuity between the support and the fill.
                |             Legal values:
                | 
                |             0
                |                 Continuity in point (C0)
                |             1
                |                 Continuity in tangency (C1)
                |             2
                |                 Continuity in curvature (C2)
                | 
                |         iPos
                |             Position at which the continuity should be set.
                | 
                |             Example:
                |                 This example sets the continuity in the Fill feature Fill at
                |                 specified position iPos
                | 
                |                  Fill.SetBoundaryContinuity iContinuity,iPos

        :param int i_continuity:
        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_fill.SetBoundaryContinuity(i_continuity, i_pos)

    def __repr__(self):
        return f'HybridShapeFill(name="{self.name}")'
