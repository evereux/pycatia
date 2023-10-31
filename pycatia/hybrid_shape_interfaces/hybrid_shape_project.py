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


class HybridShapeProject(HybridShape):
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
                |                         HybridShapeProject
                | 
                | Represents the hybrid shape project feature object.
                | Role: To access data of the hybrid shape project feature. The data
                | includes:
                | 
                |     The element to project which is a point or a curve
                |     The support element which is a curve or a surface
                |     The projection type ( normal or along a direction)
                |     The projection direction if needed
                |     The option to have either the nearest solution or all
                |     solutions
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeatures
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_project = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the projection direction.
                | 
                |     Example: This example retrieves in Dir the direction for the Project hybrid
                |     shape feature.
                | 
                |      Dim Dir As Reference
                |      Set Dir = Project.Direction

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_project.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_project.Direction = direction.com_object

    @property
    def elem_to_project(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ElemToProject() As Reference
                | 
                |     Returns or sets the element to project.This element can be a point or a
                |     curve.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example: This example retrieves in Elem the element to project for the
                |     Project hybrid shape feature.
                | 
                |      Dim Elem As Reference
                |      Set Elem = Project.ElemToProject

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_project.ElemToProject)

    @elem_to_project.setter
    def elem_to_project(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_project.ElemToProject = reference_element.com_object

    @property
    def extrapolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExtrapolationMode() As long
                | 
                |     Returns or sets the extrapolation mode. The extrapolation mode is overriden
                |     when the solution type is 'Nearest solution' (0) or when the extrapolation mode
                |     being set is 'None' (0), otherwise the method fails. Role: None (0), Tangency
                |     (1) or Curvature (2).
                | 
                |     Example: This example retrieves in ExtrapolMode the solution type for the
                |     Project hybrid shape feature.
                | 
                |      Dim ExtrapolMode As long
                |      Set ExtrapolMode = Project.ExtrapolationMode

        :rtype: int
        """

        return self.hybrid_shape_project.ExtrapolationMode

    @extrapolation_mode.setter
    def extrapolation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_project.ExtrapolationMode = value

    @property
    def maximum_deviation_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaximumDeviationValue() As double
                | 
                |     Sets or Gets the maximum deviation allowed for smoothing
                |     operation.
                |     Sets in distance unit, it corresponds to the radius of a pipe around the
                |     input curve in which the result is allowed to be. This value must be set in SI
                |     unit (m).
                | 
                |     Example: This example retrieves in DeviationValue the maximum deviation
                |     value for the Project hybrid shape feature.
                | 
                |      Dim DeviationValue As CATIALength
                |      Set DeviationValue = Project.MaximumDeviationValue

        :rtype: float
        """

        return self.hybrid_shape_project.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_project.MaximumDeviationValue = value

    @property
    def normal(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Normal() As boolean
                | 
                |     Returns or sets the direction option. Role: To define the type of
                |     projection. Normal is set to TRUE if the projection is a normal
                |     projection.Otherwise, the projection is defined along a specified
                |     direction.
                | 
                |     Example: This example retrieves in NormalOption the support for the Project
                |     hybrid shape feature.
                | 
                |      Dim NormalOption As boolean
                |      Set NormalOption = Project.Normal

        :rtype: bool
        """

        return self.hybrid_shape_project.Normal

    @normal.setter
    def normal(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_project.Normal = value

    @property
    def smoothing_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothingType() As long
                | 
                |     Sets or Gets Smoothing Type.
                |     Role: Smoothing type
                |     : 0 -> No Smoothing
                |     : 2 -> G1 Smoothing : Enhance current continuity to tangent continuity
                |     : 3 -> G2 Smoothing : Enhance current continuity to curvature continuity
                | 
                |     Example: This example retrieves in SType the smoothing type for the Project
                |     hybrid shape feature.
                | 
                |      Dim SType As long
                |      Set SType = Project.SmoothingType

        :rtype: int
        """

        return self.hybrid_shape_project.SmoothingType

    @smoothing_type.setter
    def smoothing_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_project.SmoothingType = value

    @property
    def solution_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SolutionType() As long
                | 
                |     Returns or sets the solution type. When the solution type being set is 'All
                |     solutions' (1), the extrapolation mode gets overriden to 'None' (0). Role: All
                |     solutions (1) or Nearest solution (0) (only nearest projection is kept when
                |     more than one solution is possible).
                | 
                |     Example: This example retrieves in SolType the solution type for the
                |     Project hybrid shape feature.
                | 
                |      Dim SolType As long
                |      Set SolType = Project.SolutionType

        :rtype: int
        """

        return self.hybrid_shape_project.SolutionType

    @solution_type.setter
    def solution_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_project.SolutionType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support element.This element can be a plane or a
                |     surface.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example: This example retrieves in SupportElem the support for the Project
                |     hybrid shape feature.
                | 
                |      Dim SupportElem As Reference
                |      Set SupportElem = Project.Support

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_project.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_project.Support = reference_support.com_object

    @property
    def p_3d_smoothing(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property p3DSmoothing() As boolean
                | 
                |     Returns or sets the '3D Smoothing' option.
                |     Role: To activate or not the 3D smoothing option Available only for tangent or curvature
                |     smoothing type TRUE : Smoothing performed without specifying support FALSE : Smoothing performed
                |     with specific support
                | 
                |     Example: This example retrieves in 3DSmoothingOption the support for the
                |     Project hybrid shape feature.
                | 
                |      Dim 3DSmoothingOption As boolean
                |      Set 3DSmoothingOption = Project.p3DSmoothing

        :rtype: bool
        """

        return self.hybrid_shape_project.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_project.p3DSmoothing = value

    def __repr__(self):
        return f'HybridShapeProject(name="{self.name}")'
