#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeFill(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The Fill feature : an Fill is made up of a face to process and one
                | Fill parameter.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fill = com_object     

    @property
    def constraint(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Constraint
                | o Property Constraint(    ) As
                | 
                | Returns or sets the passing point for the Fill. Example:
                | This example retrieves in Element the passing point for the
                | Fill hybrid shape feature. Dim Element As Reference Set
                | Element = Fill.Constraint

        :return:
        """
        return self.hybrid_shape_fill.Constraint

    @constraint.setter
    def constraint(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fill.Constraint = value 

    @property
    def continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Continuity
                | o Property Continuity(    ) As
                | 
                | Returns or sets the continuity between the support and fill.
                | Legal values: 0 Continuity in point (C0) 1 Continuity in
                | tangency (C1) 2 Continuity in curvature (C2) 
                |
                | Example:
                | This
                | example retrieves in oContinuity the continuity type for the
                | Fill hybrid shape feature. Dim oContinuity Set oContinuity =
                | Fill.Continuity

        :return:
        """
        return self.hybrid_shape_fill.Continuity

    @continuity.setter
    def continuity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fill.Continuity = value 

    @property
    def detection(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Detection
                | o Property Detection(    ) As
                | 
                | Returns or sets the Canonical portion detection option.
                | Legal values: 0 No detection of canonical surface 2
                | Detection of canonical surfaces

        :return:
        """
        return self.hybrid_shape_fill.Detection

    @detection.setter
    def detection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fill.Detection = value 

    @property
    def maximum_deviation_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MaximumDeviationValue
                | o Property MaximumDeviationValue(    ) As
                | 
                | Sets or Gets the maximum deviation allowed for smoothing
                | operation in fill commnd. This value must be set in SI unit
                | (m). 
                |
                | Example:
                | This example retrieves in DeviationValue the
                | maximum deviation value for the Fill hybrid shape feature.
                | Dim DeviationValue As double Set DeviationValue =
                | Fill.MaximumDeviationValue

        :return:
        """
        return self.hybrid_shape_fill.MaximumDeviationValue

    @property
    def plane_only_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PlaneOnlyMode
                | o Property PlaneOnlyMode(    ) As
                | 
                | Returns or sets whether Planar Boundaries only should be
                | considered during fill operation. Legal values: TRUE Planar
                | boundaries are only considered during Fill operation FALSE
                | Non-Planar boundaries are also considered during Fill
                | operation

        :return:
        """
        return self.hybrid_shape_fill.PlaneOnlyMode

    @plane_only_mode.setter
    def plane_only_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fill.PlaneOnlyMode = value 

    @property
    def tolerant_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TolerantMode
                | o Property TolerantMode(    ) As
                | 
                | Returns or sets the Tolerant mode option. Role: To activate
                | or not the tolerant mode option TRUE : Tolerant mode is
                | active. Uses deviation parameter to do tolerant fill. FALSE
                | : Tolerant mode is not active. 
                |
                | Example:
                | This example
                | retrieves in tolMode the tolerant mode for the Fill hybrid
                | shape feature. Dim tolMode As boolean Set tolMode =
                | Fill.TolerantMode

        :return:
        """
        return self.hybrid_shape_fill.TolerantMode

    @tolerant_mode.setter
    def tolerant_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_fill.TolerantMode = value 

    def add_bound(self, i_boundary):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddBound
                | o Sub AddBound(        iBoundary)
                | 
                | Adds an boundary to the hybrid shape fill feature object.
                |
                | Parameters:
                | iBoundary
                | 		The boundary(curve) to be added to the hybrid shape fill feature object.

                | Examples:
                | The following example adds the iBoundary curve to the Fill
                | object. Fill.AddBound iBoundary

        :param i_boundary:
        :return:
        """
        return self.hybrid_shape_fill.AddBound(i_boundary)

    def add_support_at_bound(self, i_boundary, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddSupportAtBound
                | o Sub AddSupportAtBound(        iBoundary,
                |                                 iSupport)
                | 
                | Inserts the support at specified boundary in the Fill.
                |
                | Parameters:
                | iBoundary
                |       Reference of the boundary object to which support has to be added.
                |  
                |  iSupport
                | 		Reference of the support object to be added.

                | Examples:
                | This example adds supports in the Fill feature Fill to
                | specified iBoundary boundary Fill.AddSupportAtBound
                | iBoundary,iSupport

        :param i_boundary:
        :param i_support:
        :return:
        """
        return self.hybrid_shape_fill.AddSupportAtBound(i_boundary, i_support)

    def append_constraint(self, i_constraint):
        """
        .. note::
            CAA V5 Visual Basic help

                | AppendConstraint
                | o Sub AppendConstraint(        iConstraint)
                | 
                | Appends an constraint to the hybrid shape fill feature
                | object. ======== ONLY USE IN FSS ==============
                |
                | Parameters:
                | iConstraint
                | 		The constraint to be appended.

                | Examples:
                | The following example appends the iConstraint constraint to
                | the Fill object. Fill.AppendConstraint iConstraint

        :param i_constraint:
        :return:
        """
        return self.hybrid_shape_fill.AppendConstraint(i_constraint)

    def get_bound_at_position(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundAtPosition
                | o Func GetBoundAtPosition(        iPos) As
                | 
                | Retrieves the boundary at specified position in the hybrid
                | shape fill feature object.
                |
                | Parameters:
                | iPos
                | 		The position of the boundary to retrieve.

                | Examples:
                | The following example gets the oBoundary boundary of the
                | Fill object at the position iPos. Dim oBoundary As Reference
                | Set oBoundary = Fill.GetBoundAtPosition (iPos).

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.GetBoundAtPosition(i_pos)

    def get_bound_position(self, i_boundary):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundPosition
                | o Func GetBoundPosition(        iBoundary) As
                | 
                | Retrieves the position of a boundary used by the hybrid
                | shape fill feature object.
                |
                | Parameters:
                | iBoundary
                | 		The boundary whose position has to be retrieved.

                | Examples:
                | The following example gets the oPos position of the
                | iBoundary boundary in the Fill object. Dim oPos As long oPos
                | = Fill.GetBoundPosition (iBoundary).

        :param i_boundary:
        :return:
        """
        return self.hybrid_shape_fill.GetBoundPosition(i_boundary)

    def get_bound_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundSize
                | o Func GetBoundSize(    ) As
                | 
                | Returns the number of boundaries in the Fill object.
                |
                | Parameters:
                | oSize
                |      Number of boundaries in the Fill.

                | Examples:
                | This example retrieves the number of boundaries in the Fill
                | hybrid shape fill. Dim oSize As long oSize =
                | Fill.GetBoundSize

        :return:
        """
        return self.hybrid_shape_fill.GetBoundSize()

    def get_boundary_continuity(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBoundaryContinuity
                | o Func GetBoundaryContinuity(        iPos) As
                | 
                | Returns the continuity mode for a boundary at specified
                | position in the Fill.
                |
                | Parameters:
                | iPos
                |      Position at which the continuity should be retrieved.
                |  
                |  oContinuity
                |       Continuity retrieved between the support and the fill.
                |  Legal values:
                |  
                | 0
                | Continuity in point (C0)
                | 1
                | Continuity in tangency (C1)
                | 2
                | Continuity in curvature (C2)

                | Examples:
                | This example retrieves in oContinuity the continuity at the
                | specified position of Fill hybrid shape fill feature.
                | oContinuity = Fill.GetBoundaryContinuity iPos

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.GetBoundaryContinuity(i_pos)

    def get_constraint_at_position(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintAtPosition
                | o Func GetConstraintAtPosition(        iPos) As
                | 
                | Retrieves the constraint at specified position in the hybrid
                | shape fill feature object. ======== ONLY USE IN FSS
                | ==============
                |
                | Parameters:
                | iPos
                | 		The position of the constraint to retrieve.

                | Examples:
                | The following example gets the oConstraint constraint of the
                | Fill object at the position iPos. Dim oConstraint As
                | Reference Set oConstraint = Fill.GetConstraintAtPosition
                | (iPos).

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.GetConstraintAtPosition(i_pos)

    def get_constraints_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintsSize
                | o Func GetConstraintsSize(    ) As
                | 
                | Returns the number of constraints in the Fill object.
                |
                | Parameters:
                | oSize
                |      Number of constraints in the Fill.

                | Examples:
                | This example retrieves the number of constraints in the Fill
                | hybrid shape fill. Dim oSize As long oSize =
                | Fill.GetConstraintsSize

        :return:
        """
        return self.hybrid_shape_fill.GetConstraintsSize()

    def get_support_at_position(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSupportAtPosition
                | o Func GetSupportAtPosition(        iPos) As
                | 
                | Retrieves the support at specified position in the hybrid
                | shape fill feature object.
                |
                | Parameters:
                | iPos
                | 		The position of the support to retrieve.

                | Examples:
                | The following example gets the oSupport support of the Fill
                | object at the position iPos. Dim oSupport As Reference Set
                | oSupport = Fill.GetSupportAtPosition (iPos).

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.GetSupportAtPosition(i_pos)

    def insert_bound_after_position(self, i_boundary, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertBoundAfterPosition
                | o Sub InsertBoundAfterPosition(        iBoundary,
                |                                        iPos)
                | 
                | Inserts the boundary after specified position in the Fill.
                |
                | Parameters:
                | iBoundary
                |       Reference of the boundary object to be inserted.
                |  
                |  iPos
                |      Position after which the element should be inserted.

                | Examples:
                | This example inserts the boundary in the Fill feature Fill
                | after position iPos Fill.InsertBoundAfterPosition
                | iBoundary,iPos

        :param i_boundary:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.InsertBoundAfterPosition(i_boundary, i_pos)

    def remove_all_bound(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllBound
                | o Sub RemoveAllBound(    )
                | 
                | Removes all boundaries of the hybrid shape fill feature
                | object.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fill.RemoveAllBound()

    def remove_all_constraints(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllConstraints
                | o Sub RemoveAllConstraints(    )
                | 
                | Removes all constraints.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_fill.RemoveAllConstraints()

    def remove_bound_at_position(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveBoundAtPosition
                | o Sub RemoveBoundAtPosition(        iPos)
                | 
                | Removes boundary at specified position in hybrid shape fill
                | feature object.
                |
                | Parameters:
                | iPos
                | 		The position of the boundary to remove.

                | Examples:
                | The following example removes the boundary object from the
                | Fill object at the position iPos. Fill.RemoveBoundAtPosition
                | iPos.

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.RemoveBoundAtPosition(i_pos)

    def remove_constraint(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveConstraint
                | o Sub RemoveConstraint(        iPos)
                | 
                | Removes constraint at specified position in hybrid shape
                | fill feature object. ======== ONLY USE IN FSS ==============
                |
                | Parameters:
                | iPos
                | 		The position of the constraint to remove.

                | Examples:
                | The following example removes the constraint object from the
                | Fill object at the position iPos. Fill.RemoveConstraint
                | iPos.

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.RemoveConstraint(i_pos)

    def remove_support_at_position(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveSupportAtPosition
                | o Sub RemoveSupportAtPosition(        iPos)
                | 
                | Removes support at specified position in hybrid shape fill
                | feature object.
                |
                | Parameters:
                | iPos
                | 		The position of the support to remove.

                | Examples:
                | The following example removes the support object from the
                | Fill object at the position iPos.
                | Fill.RemoveSupportAtPosition iPos.

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.RemoveSupportAtPosition(i_pos)

    def replace_bound_at_position(self, i_boundary, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceBoundAtPosition
                | o Sub ReplaceBoundAtPosition(        iBoundary,
                |                                      iPos)
                | 
                | Replaces the boundary at specified position in the Fill.
                |
                | Parameters:
                | iBoundary
                |       Reference of the boundary object to be replaced.
                |  
                |  iPos
                |      Position at which the boundary should be replaced.

                | Examples:
                | This example replaces the boundary in the Fill feature Fill
                | at specified position iPos Fill.ReplaceBoundAtPosition
                | iBoundary,iPos

        :param i_boundary:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.ReplaceBoundAtPosition(i_boundary, i_pos)

    def replace_constraint(self, i_pos, i_constraint):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceConstraint
                | o Sub ReplaceConstraint(        iPos,
                |                                 iConstraint)
                | 
                | Replaces the constraint at specified position in the Fill.
                |
                | Parameters:
                | iPos
                |      Position at which the constraint should be replaced.
                |  
                |  iConstraint
                |       Reference of the constraint object to be replaced.

                | Examples:
                | This example replaces the constraint in the Fill feature
                | Fill at specified position iPos Fill.ReplaceConstraint
                | iPos,iConstraint

        :param i_pos:
        :param i_constraint:
        :return:
        """
        return self.hybrid_shape_fill.ReplaceConstraint(i_pos, i_constraint)

    def replace_support_at_position(self, i_support, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceSupportAtPosition
                | o Sub ReplaceSupportAtPosition(        iSupport,
                |                                        iPos)
                | 
                | Replaces the support at specified position in the Fill.
                |
                | Parameters:
                | iSupport
                |       Reference of the support object to be replaced.
                |  
                |  iPos
                |      Position at which the support should be replaced.

                | Examples:
                | This example replaces the support in the Fill feature Fill
                | at specified position iPos Fill.ReplaceSupportAtPosition
                | iSupport,iPos

        :param i_support:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.ReplaceSupportAtPosition(i_support, i_pos)

    def set_boundary_continuity(self, i_continuity, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetBoundaryContinuity
                | o Sub SetBoundaryContinuity(        iContinuity,
                |                                     iPos)
                | 
                | Sets the continuity mode for a boundary at specified
                | position in the Fill.
                |
                | Parameters:
                | iContinuity
                |       Continuity between the support and the fill.
                |  Legal values:
                |  
                | 0
                | Continuity in point (C0)
                | 1
                | Continuity in tangency (C1)
                | 2
                | Continuity in curvature (C2)
                | 
                | 
                |  iPos
                |      Position at which the continuity should be set.

                | Examples:
                | This example sets the continuity in the Fill feature Fill at
                | specified position iPos Fill.SetBoundaryContinuity
                | iContinuity,iPos

        :param i_continuity:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_fill.SetBoundaryContinuity(i_continuity, i_pos)

    def __repr__(self):
        return f'HybridShapeFill()'
