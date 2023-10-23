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
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeWrapCurve(HybridShape):
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
                |                         HybridShapeWrapCurve
                | 
                | Represents the hybrid shape wrap curve surface object.
                | Role: To access the data of the hybrid shape wrap curve surface
                | object.
                | 
                | This data includes:
                | 
                |     Two support surfaces, one at each limit of the wrap curve
                |     surface
                |     Two curves, one for each support surface
                |     The curve closing points
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeWrapCurve
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_wrap_curve = com_object

    @property
    def first_curves_constraint(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstCurvesConstraint() As long
                | 
                |     Returns or sets constraint at first curves of the
                |     WrapCurve.
                |     Legal values:
                |     1 = no constraint
                |     2 = Deformed surface will have the same tangency and the same curvature as the original surface
                |         at first curves.
                | 
                | Example:
                |     This example retrieves in FirstCurvesConstraint the constraint at first
                |     curves of the ShpWrapCurve hybrid shape WrapCurve feature.
                | 
                |      Dim FirstCurvesConstraint As long
                |      Set FirstCurvesConstraint = ShpWrapCurve.FirstCurvesConstraint

        :rtype: int
        """

        return self.hybrid_shape_wrap_curve.FirstCurvesConstraint

    @first_curves_constraint.setter
    def first_curves_constraint(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_wrap_curve.FirstCurvesConstraint = value

    @property
    def last_curves_constraint(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LastCurvesConstraint() As long
                | 
                |     Returns or sets constraint at last curves of the
                |     WrapCurve.
                |     Legal values:
                |     1 = no constraint,
                |     2 = Deformed surface will have the same tangency and the the same curvatureas the original
                |         surface at last curves.
                | 
                | Example:
                |     This example retrieves in LastCurvesConstraint the constraint at last
                |     curves of the ShpWrapCurve hybrid shape WrapCurve feature.
                | 
                |      Dim LastCurvesConstraint As long
                |      Set LastCurvesConstraint = ShpWrapCurve.LastCurvesConstraint

        :rtype: int
        """

        return self.hybrid_shape_wrap_curve.LastCurvesConstraint

    @last_curves_constraint.setter
    def last_curves_constraint(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_wrap_curve.LastCurvesConstraint = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Surface() As Reference
                | 
                |     Returns or sets the surface to deform of the WrapCurve.
                |     Sub-element(s) supported (see Boundary object): Face. 
                | 
                | Example:
                |     This example retrieves in SurfaceToDeform the surface to deform of the
                |     ShpWrapCurve hybrid shape WrapCurve feature.
                | 
                |      SurfaceToDeform = ShpWrapCurve.Surface

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_wrap_curve.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_wrap_curve.Surface = reference_surface.com_object

    def get_curves(self, i_position: int, o_reference_curve: Reference, o_target_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCurves(long iPosition,
                | Reference oReferenceCurve,
                | Reference oTargetCurve)
                | 
                |     Returns a curve from the WrapCurve.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the curves in the list of curves. 
                |         oReferenceCurve
                |             the reference curve. 
                |         oTargetCurve
                |             the target curve.
                |             Legal values: can be egal to Nothing. In this case, the associated
                |             ref curve will be fixed.
                | 
                |             Example:
                |                 This example retrieves in WrapCurveRefCurve the first reference
                |                 curve of the ShpWrapCurve hybrid shape WrapCurve feature and retrieves in
                |                 WrapCurveTargCurve the first target curve of the ShpWrapCurve hybrid shape
                |                 WrapCurve feature.
                | 
                |                  Dim WrapCurveRefCurve As Reference
                |                  Dim WrapCurveTargCurve As Reference
                |                  ShpWrapCurve.GetCurve(2)

        :param int i_position:
        :param Reference o_reference_curve:
        :param Reference o_target_curve:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.GetCurves(i_position, o_reference_curve.com_object,
                                                      o_target_curve.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_curves'
        # # vba_code = """
        # # Public Function get_curves(hybrid_shape_wrap_curve)
        # #     Dim iPosition (2)
        # #     hybrid_shape_wrap_curve.GetCurves iPosition
        # #     get_curves = iPosition
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_number_of_curves(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNumberOfCurves() As long
                | 
                |     Returns the number of couples of curves of the WrapCurve.
                | 
                |     Returns:
                |         The number of couples of curves
                |         Legal values: positive or null. 
                | 
                | Example:
                |     This example retrieves in NumberOfCurves the number of couples of curves of
                |     the ShpWrapCurve hybrid shape WrapCurve feature.
                | 
                |      NumberOfCurves = ShpWrapCurve.GetNumberOfCurves(2)

        :rtype: int
        """
        return self.hybrid_shape_wrap_curve.GetNumberOfCurves()

    def get_reference_direction(self, o_direction_type: int, o_direction: HybridShapeDirection) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetReferenceDirection(long oDirectionType,
                | HybridShapeDirection oDirection)
                | 
                |     Gets the reference direction projection of the wrap curve
                |     feature.
                | 
                |     Parameters:
                | 
                |         oDirectionType
                |             type of direction.
                |             Legal values: 1 = reference direction is computed, and 2 = user direction. 
                |         oDirection
                |             curve to be added as a direction, if oDirectionType = 2. 
                |         Example:
                |             This example retrieves in RefDirection the reference direction of
                |             the ShpWrapCurve hybrid shape WrapCurve feature and in RefDirectionType the
                |             reference direction of the ShpWrapCurve hybrid shape
                |             WrapCurve
                | 
                |              Dim RefDirectionType As long 
                |              Dim RefDirection As CATIAHybridShapeDirection 
                |              ShpWrapCurve.SetReferenceDirection (RefDirectionType,
                |              RefDirection)

        :param int o_direction_type:
        :param HybridShapeDirection o_direction:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.GetReferenceDirection(o_direction_type, o_direction.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_reference_direction'
        # # vba_code = """
        # # Public Function get_reference_direction(hybrid_shape_wrap_curve)
        # #     Dim oDirectionType (2)
        # #     hybrid_shape_wrap_curve.GetReferenceDirection oDirectionType
        # #     get_reference_direction = oDirectionType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_reference_spine(self, o_spine_type: int, o_spine: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetReferenceSpine(long oSpineType,
                | Reference oSpine)
                | 
                |     Returns the reference spine of the wrap curve feature.
                | 
                |     Parameters:
                | 
                |         oSpineType
                |             type of spine.
                |             Legal values: 1 = Reference Spine is equal to the first reference curve, and
                |                           2 = user spine.
                |         oSpine
                |             curve to be added as a spine, if iSpineType = 2. 
                | 
                |     Example:
                |         This example retrieves in RefSpine the reference spine of the
                |         ShpWrapCurve hybrid shape WrapCurve feature and in RefSpineType the reference
                |         spine type.
                | 
                |          Dim RefSpineType As long 
                |          Dim RefSpine As Reference 
                |          ShpWrapCurve.GetReferenceSpine (RefSpineType,
                |          RefSpine)

        :param int o_spine_type:
        :param Reference o_spine:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.GetReferenceSpine(o_spine_type, o_spine.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_reference_spine'
        # # vba_code = """
        # # Public Function get_reference_spine(hybrid_shape_wrap_curve)
        # #     Dim oSpineType (2)
        # #     hybrid_shape_wrap_curve.GetReferenceSpine oSpineType
        # #     get_reference_spine = oSpineType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def insert_curves(self, i_position: int, i_reference_curve: Reference, i_target_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertCurves(long iPosition,
                | Reference iReferenceCurve,
                | Reference iTargetCurve)
                | 
                |     Inserts a couple of reference curve and target curve to the wrap
                |     curve.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the curves in the list of curves.
                |             Legal values: 0 for the end of the list, or positive and not null.
                |             
                |         iReferenceCurve
                |             the reference curve.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge. 
                |     iTargetCurve
                |         the target curve.
                |         Sub-element(s) supported (see Boundary object): TriDimFeatEdge and
                |         BiDimFeatEdge.
                | 
                | Example:
                |     This example sets the RefCurveForWrapCurve curve and the
                |     TargCurveForWrapCurve curve at the end of the list to the ShpWrapCurve hybrid
                |     shape WrapCurve feature.
                | 
                |      ShpWrapCurve.InsertCurves (0, RefCurveForWrapCurve,
                |      TargCurveForWrapCurve)

        :param int i_position:
        :param Reference i_reference_curve:
        :param Reference i_target_curve:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.InsertCurves(i_position, i_reference_curve.com_object,
                                                         i_target_curve.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_curves'
        # # vba_code = """
        # # Public Function insert_curves(hybrid_shape_wrap_curve)
        # #     Dim iPosition (2)
        # #     hybrid_shape_wrap_curve.InsertCurves iPosition
        # #     insert_curves = iPosition
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def insert_reference_curve(self, i_position: int, i_reference_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertReferenceCurve(long iPosition,
                | Reference iReferenceCurve)
                | 
                |     Inserts a of reference curve to the wrap curve.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the curves in the list of curves.
                |             Legal values: 0 for the end of the list, or positive and not null.
                |             
                |         iReferenceCurve
                |             the reference curve.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge. 
                |     Example:
                |         This example sets the RefCurveForWrapCurve curve at the end of the list
                |         to the ShpWrapCurve hybrid shape WrapCurve feature.
                | 
                |          ShpWrapCurve.InsertCurves (0, RefCurveForWrapCurve)

        :param int i_position:
        :param Reference i_reference_curve:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.InsertReferenceCurve(i_position, i_reference_curve.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_reference_curve'
        # # vba_code = """
        # # Public Function insert_reference_curve(hybrid_shape_wrap_curve)
        # #     Dim iPosition (2)
        # #     hybrid_shape_wrap_curve.InsertReferenceCurve iPosition
        # #     insert_reference_curve = iPosition
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_curves(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveCurves(long iPosition)
                | 
                |     Removes a couple of reference curve and target curve from the
                |     WrapCurve.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the curves in the list of curves.
                |             Legal values: positive, not null and lower to numberOfCurves
                |             
                | 
                |     Example:
                |         This example removes the first couple of reference curve and target
                |         curve of the ShpWrapCurve hybrid shape WrapCurve
                |         feature.
                | 
                |          ShpWrapCurve.RemoveCurves (1)

        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.RemoveCurves(i_position)

    def set_reference_direction(self, i_direction: HybridShapeDirection) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReferenceDirection(HybridShapeDirection iDirection)
                | 
                |     Sets the reference direction projection to the wrap curve
                |     feature.
                | 
                |     Parameters:
                | 
                |         iDirection
                |             curve to be added as a direction, if iDirectionType = 2. 
                |         Example:
                |             This example sets the RefDirection curve as the reference direction
                |             of the ShpWrapCurve hybrid shape WrapCurve
                |             feature.
                | 
                |              ShpWrapCurve.SetReferenceDirection RefDirection

        :param HybridShapeDirection i_direction:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.SetReferenceDirection(i_direction.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_reference_direction'
        # # vba_code = """
        # # Public Function set_reference_direction(hybrid_shape_wrap_curve)
        # #     Dim iDirection (2)
        # #     hybrid_shape_wrap_curve.SetReferenceDirection iDirection
        # #     set_reference_direction = iDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_reference_spine(self, i_spine: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReferenceSpine(Reference iSpine)
                | 
                |     Sets the reference spine to the wrap curve feature.
                | 
                |     Parameters:
                | 
                |         iSpine
                |             curve to be added as a spine.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge, BiDimFeatEdge. 
                | 
                | Example:
                |     This example sets the Curve10 curve as the reference Spine of the
                |     ShpWrapCurve hybrid shape WrapCurve feature.
                | 
                |      ShpWrapCurve.SetReferenceSpine Curve10

        :param Reference i_spine:
        :rtype: None
        """
        return self.hybrid_shape_wrap_curve.SetReferenceSpine(i_spine.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_reference_spine'
        # # vba_code = """
        # # Public Function set_reference_spine(hybrid_shape_wrap_curve)
        # #     Dim iSpine (2)
        # #     hybrid_shape_wrap_curve.SetReferenceSpine iSpine
        # #     set_reference_spine = iSpine
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeWrapCurve(name="{self.name}")'
