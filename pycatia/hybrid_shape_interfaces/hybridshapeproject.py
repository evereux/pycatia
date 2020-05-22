#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeProject(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape project feature object.Role: To access
                | data of the hybrid shape project feature. The data includes:Use the
                | CATIAHybridShapeFactory to create HybridShapeFeatures objects.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_project = com_object     

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the projection direction. 
                |
                | Example:
                | This
                | example retrieves in Dir the direction for the Project
                | hybrid shape feature. Dim Dir As Reference Set Dir =
                | Project.Direction

        :return:
        """
        return self.hybrid_shape_project.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_project.Direction = value 

    @property
    def elem_to_project(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ElemToProject
                | o Property ElemToProject(    ) As
                | 
                | Returns or sets the element to project.This element can be a
                | point or a curve. Sub-element(s) supported (see object): ,
                | or . 
                |
                | Example:
                | This example retrieves in Elem the element to
                | project for the Project hybrid shape feature. Dim Elem As
                | Reference Set Elem = Project.ElemToProject

        :return:
        """
        return self.hybrid_shape_project.ElemToProject

    @elem_to_project.setter
    def elem_to_project(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_project.ElemToProject = value 

    @property
    def maximum_deviation_value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MaximumDeviationValue
                | o Property MaximumDeviationValue(    ) As
                | 
                | Sets or Gets the maximum deviation allowed for smoothing
                | operation. Sets in distance unit, it corresponds to the
                | radius of a pipe around the input curve in which the result
                | is allowed to be. This value must be set in SI unit (m).
                | 
                |
                | Example:
                | This example retrieves in DeviationValue the
                | maximum deviation value for the Project hybrid shape
                | feature. Dim DeviationValue As CATIALength Set
                | DeviationValue = Project.MaximumDeviationValue

        :return:
        """
        return self.hybrid_shape_project.MaximumDeviationValue

    @property
    def normal(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Normal
                | o Property Normal(    ) As
                | 
                | Returns or sets the direction option. Role: To define the
                | type of projection. Normal is set to TRUE if the projection
                | is a normal projection.Otherwise, the projection is defined
                | along a specified direction. 
                |
                | Example:
                | This example retrieves
                | in NormalOption the support for the Project hybrid shape
                | feature. Dim NormalOption As boolean Set NormalOption =
                | Project.Normal

        :return:
        """
        return self.hybrid_shape_project.Normal

    @normal.setter
    def normal(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_project.Normal = value 

    @property
    def smoothing_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothingType
                | o Property SmoothingType(    ) As
                | 
                | Sets or Gets Smoothing Type. Role: Smoothing type : 0 -> No
                | Smoothing : 2 -> G1 Smoothing : Enhance current continuity
                | to tangent continuity : 3 -> G2 Smoothing : Enhance current
                | continuity to curvature continuity 
                |
                | Example:
                | This example
                | retrieves in SType the smoothing type for the Project hybrid
                | shape feature. Dim SType As long Set SType =
                | Project.SmoothingType

        :return:
        """
        return self.hybrid_shape_project.SmoothingType

    @property
    def solution_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SolutionType
                | o Property SolutionType(    ) As
                | 
                | Returns or sets the solution type. Role: All solutions or
                | Nearest solution (only nearest projection is kept when more
                | than one solution is possible). 
                |
                | Example:
                | This example
                | retrieves in SolType the solution type for the Project
                | hybrid shape feature. Dim SolType As long Set SolType =
                | Project.SolutionType

        :return:
        """
        return self.hybrid_shape_project.SolutionType

    @solution_type.setter
    def solution_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_project.SolutionType = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support element.This element can be a
                | plane or a surface. Sub-element(s) supported (see object): ,
                | or . 
                |
                | Example:
                | This example retrieves in SupportElem the
                | support for the Project hybrid shape feature. Dim
                | SupportElem As Reference Set SupportElem = Project.Support

        :return:
        """
        return self.hybrid_shape_project.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_project.Support = value 

    @property
    def p_3d_smoothing(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | p3DSmoothing
                | o Property p3DSmoothing(    ) As
                | 
                | Returns or sets the '3D Smoothing' option. Role: To activate
                | or not the 3D smoothing option Available only for tangent or
                | curvature smoothing type TRUE : Smoothing performed without
                | specifying support FALSE : Smoothing performed with specific
                | support 
                |
                | Example:
                | This example retrieves in 3DSmoothingOption
                | the support for the Project hybrid shape feature. Dim
                | 3DSmoothingOption As boolean Set 3DSmoothingOption =
                | Project.p3DSmoothing

        :return:
        """
        return self.hybrid_shape_project.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_project.p3DSmoothing = value 

    def __repr__(self):
        return f'HybridShapeProject()'
