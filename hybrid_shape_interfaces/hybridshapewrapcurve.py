#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeWrapCurve(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape wrap curve surface object.Role: To access
                | the data of the hybrid shape wrap curve surface object.This data
                | includes:Use the CATIAHybridShapeFactory to create a
                | HybridShapeWrapCurve object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_wrap_curve = com_object     

    @property
    def first_curves_constraint(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstCurvesConstraint
                | o Property FirstCurvesConstraint(    ) As
                | 
                | Returns or sets constraint at first curves of the WrapCurve.
                | Legal values: 1 = no constraint, 2 = Deformed surface will
                | have the same tangency and the same curvature as the
                | original surface at first curves.

        :return:
        """
        return self.hybrid_shape_wrap_curve.FirstCurvesConstraint

    @first_curves_constraint.setter
    def first_curves_constraint(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_curve.FirstCurvesConstraint = value 

    @property
    def last_curves_constraint(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LastCurvesConstraint
                | o Property LastCurvesConstraint(    ) As
                | 
                | Returns or sets constraint at last curves of the WrapCurve.
                | Legal values: 1 = no constraint, 2 = Deformed surface will
                | have the same tangency and the the same curvatureas the
                | original surface at last curves.

        :return:
        """
        return self.hybrid_shape_wrap_curve.LastCurvesConstraint

    @last_curves_constraint.setter
    def last_curves_constraint(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_curve.LastCurvesConstraint = value 

    @property
    def surface(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Surface
                | o Property Surface(    ) As
                | 
                | Returns or sets the surface to deform of the WrapCurve. Sub-
                | element(s) supported (see object): .

        :return:
        """
        return self.hybrid_shape_wrap_curve.Surface

    @surface.setter
    def surface(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_wrap_curve.Surface = value 

    def get_curves(self, i_position, o_reference_curve, o_target_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCurves
                | o Sub GetCurves(        iPosition,
                |                         oReferenceCurve,
                |                         oTargetCurve)
                | 
                | Returns a curve from the WrapCurve.
                |
                | Parameters:
                | iPosition
                |      The position of the curves in the list of curves. 
                |  
                |  oReferenceCurve
                |     the reference curve. 
                |  
                |  oTargetCurve
                |     the target curve.
                |    Legal values: can be egal to Nothing. In this case, the associated ref curve will be fixed.

                | Examples:
                | This example retrieves in WrapCurveRefCurve the first
                | reference curve of the ShpWrapCurve hybrid shape WrapCurve
                | feature and retrieves in WrapCurveTargCurve the first target
                | curve of the ShpWrapCurve hybrid shape WrapCurve feature.
                | Dim WrapCurveRefCurve As Reference Dim WrapCurveTargCurve As
                | Reference ShpWrapCurve.GetCurve(2)

        :param i_position:
        :param o_reference_curve:
        :param o_target_curve:
        :return:
        """
        return self.hybrid_shape_wrap_curve.GetCurves(i_position, o_reference_curve, o_target_curve)

    def get_number_of_curves(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNumberOfCurves
                | o Func GetNumberOfCurves(    ) As
                | 
                | Returns the number of couples of curves of the WrapCurve.
                | Returns: The number of couples of curves Legal values:
                | positive or null. 
                |
                | Example:
                | This example retrieves in
                | NumberOfCurves the number of couples of curves of the
                | ShpWrapCurve hybrid shape WrapCurve feature. NumberOfCurves
                | = ShpWrapCurve.GetNumberOfCurves(2)
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_wrap_curve.GetNumberOfCurves()

    def get_reference_direction(self, o_direction_type, o_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetReferenceDirection
                | o Sub GetReferenceDirection(        oDirectionType,
                |                                     oDirection)
                | 
                | Gets the reference direction projection of the wrap curve
                | feature.
                |
                | Parameters:
                | oDirectionType
                |      type of direction.
                |      Legal values: 1 = reference direction is computed,
                |        and 2 = user direction.
                |    
                |  oDirection
                |      curve to be added as a direction, if oDirectionType = 2.

                | Examples:
                | This example retrieves in RefDirection the reference
                | direction of the ShpWrapCurve hybrid shape WrapCurve feature
                | and in RefDirectionType the reference direction of the
                | ShpWrapCurve hybrid shape WrapCurve Dim RefDirectionType As
                | long Dim RefDirection As CATIAHybridShapeDirection
                | ShpWrapCurve.SetReferenceDirection (RefDirectionType,
                | RefDirection)

        :param o_direction_type:
        :param o_direction:
        :return:
        """
        return self.hybrid_shape_wrap_curve.GetReferenceDirection(o_direction_type, o_direction)

    def get_reference_spine(self, o_spine_type, o_spine):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetReferenceSpine
                | o Sub GetReferenceSpine(        oSpineType,
                |                                 oSpine)
                | 
                | Returns the reference spine of the wrap curve feature.
                |
                | Parameters:
                | oSpineType
                |      type of spine.
                |      Legal values: 1 = Reference Spine is equal to the first reference curve, 
                |        and 2 = user spine.
                |    
                |  oSpine
                |      curve to be added as a spine, if iSpineType = 2.

                | Examples:
                | This example retrieves in RefSpine the reference spine of
                | the ShpWrapCurve hybrid shape WrapCurve feature and in
                | RefSpineType the reference spine type. Dim RefSpineType As
                | long Dim RefSpine As Reference
                | ShpWrapCurve.GetReferenceSpine (RefSpineType, RefSpine)

        :param o_spine_type:
        :param o_spine:
        :return:
        """
        return self.hybrid_shape_wrap_curve.GetReferenceSpine(o_spine_type, o_spine)

    def insert_curves(self, i_position, i_reference_curve, i_target_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertCurves
                | o Sub InsertCurves(        iPosition,
                |                            iReferenceCurve,
                |                            iTargetCurve)
                | 
                | Inserts a couple of reference curve and target curve to the
                | wrap curve.
                |
                | Parameters:
                | iPosition
                |      The position of the curves in the list of curves. 
                |      Legal values: 0 for the end of the list, or positive and not null.
                |  
                |  iReferenceCurve
                |     the reference curve. 
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .  
                |      iTargetCurve
                |     the target curve.
                |  Sub-element(s) supported (see 
                |  object):  
                |  and 
                | .

                | Examples:
                | This example sets the RefCurveForWrapCurve curve and the
                | TargCurveForWrapCurve curve at the end of the list to the
                | ShpWrapCurve hybrid shape WrapCurve feature.
                | ShpWrapCurve.InsertCurves (0, RefCurveForWrapCurve,
                | TargCurveForWrapCurve)

        :param i_position:
        :param i_reference_curve:
        :param i_target_curve:
        :return:
        """
        return self.hybrid_shape_wrap_curve.InsertCurves(i_position, i_reference_curve, i_target_curve)

    def insert_reference_curve(self, i_position, i_reference_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertReferenceCurve
                | o Sub InsertReferenceCurve(        iPosition,
                |                                    iReferenceCurve)
                | 
                | Inserts a of reference curve to the wrap curve.
                |
                | Parameters:
                | iPosition
                |      The position of the curves in the list of curves. 
                |      Legal values: 0 for the end of the list, or positive and not null.
                |  
                |  iReferenceCurve
                |     the reference curve. 
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                |  and 
                | .

                | Examples:
                | This example sets the RefCurveForWrapCurve curve at the end
                | of the list to the ShpWrapCurve hybrid shape WrapCurve
                | feature. ShpWrapCurve.InsertCurves (0, RefCurveForWrapCurve)

        :param i_position:
        :param i_reference_curve:
        :return:
        """
        return self.hybrid_shape_wrap_curve.InsertReferenceCurve(i_position, i_reference_curve)

    def remove_curves(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveCurves
                | o Sub RemoveCurves(        iPosition)
                | 
                | Removes a couple of reference curve and target curve from
                | the WrapCurve.
                |
                | Parameters:
                | iPosition
                |      The position of the curves in the list of curves. 
                |      Legal values: positive, not null and lower to numberOfCurves

                | Examples:
                | This example removes the first couple of reference curve and
                | target curve of the ShpWrapCurve hybrid shape WrapCurve
                | feature. ShpWrapCurve.RemoveCurves (1)

        :param i_position:
        :return:
        """
        return self.hybrid_shape_wrap_curve.RemoveCurves(i_position)

    def set_reference_direction(self, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetReferenceDirection
                | o Sub SetReferenceDirection(        iDirection)
                | 
                | Sets the reference direction projection to the wrap curve
                | feature.
                |
                | Parameters:
                | iDirection
                |      curve to be added as a direction, if iDirectionType = 2.

                | Examples:
                | This example sets the RefDirection curve as the reference
                | direction of the ShpWrapCurve hybrid shape WrapCurve
                | feature. ShpWrapCurve.SetReferenceDirection RefDirection

        :param i_direction:
        :return:
        """
        return self.hybrid_shape_wrap_curve.SetReferenceDirection(i_direction)

    def set_reference_spine(self, i_spine):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetReferenceSpine
                | o Sub SetReferenceSpine(        iSpine)
                | 
                | Sets the reference spine to the wrap curve feature.
                |
                | Parameters:
                | iSpine
                |      curve to be added as a spine.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | , 
                | .

                | Examples:
                | This example sets the Curve10 curve as the reference Spine
                | of the ShpWrapCurve hybrid shape WrapCurve feature.
                | ShpWrapCurve.SetReferenceSpine Curve10

        :param i_spine:
        :return:
        """
        return self.hybrid_shape_wrap_curve.SetReferenceSpine(i_spine)

    def __repr__(self):
        return f'HybridShapeWrapCurve()'
