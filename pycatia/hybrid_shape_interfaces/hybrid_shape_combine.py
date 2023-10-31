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


class HybridShapeCombine(HybridShape):
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
                |                         HybridShapeCombine
                | 
                | Represents the hybrid shape combined curve object.
                | Role: To access the data of the hybrid shape combined curve object. This data
                | includes:
                | 
                |     The three curves to which the circle is tangent
                |     The surface that supports the circle
                |     The orientation of each curve.
                | 
                | Use the HybridShapeFactory object to create a HybridShapeCombine
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_combine = com_object

    @property
    def direction1(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction1() As HybridShapeDirection
                | 
                |     Returns or sets the first direction used to create the combined curve. The
                |     first direction is the direction along which the first curve is
                |     extruded.
                | 
                |     Example:
                | 
                |           This example sets firstDir as the first direction to create the
                |           combined curve
                |          hybCombCurve.
                |          
                | 
                |          hybCombCurve.Direction1 = firstDir

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_combine.Direction1)

    @direction1.setter
    def direction1(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_combine.Direction1 = direction.com_object

    @property
    def direction2(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction2() As HybridShapeDirection
                | 
                |     Returns or sets the second direction used to create the combined
                |     curve.
                | 
                |     Example:
                | 
                |           This example retrieves in secondDir the second direction
                |           used
                |          to create the combined curve hybCombCurve.
                |          
                | 
                |          Dim secondDir As CATIAHybridShapeDirection
                |          Set secondDir = hybCombCurve.Direction2

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_combine.Direction2)

    @direction2.setter
    def direction2(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_combine.Direction2 = direction.com_object

    @property
    def elem1(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Elem1() As Reference
                | 
                |     Returns or sets the first curve used to create the combined
                |     curve.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                | 
                |           This example sets firstCurve as the first curve to create the
                |           combined curve
                |          hybCombCurve.
                |          
                | 
                |          hybCombCurve.Elem1 = firstCurve

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_combine.Elem1)

    @elem1.setter
    def elem1(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_combine.Elem1 = reference_element.com_object

    @property
    def elem2(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Elem2() As Reference
                | 
                |     Returns or sets the second curve used to create the combined
                |     curve.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                | 
                |           This example retrieves in secondCurve the second curve used to
                |           create
                |          the combined curve hybCombCurve.
                |          
                | 
                |          Dim secondCurve As CATIAReference
                |          Set secondCurve = hybCombCurve.Elem2

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_combine.Elem2)

    @elem2.setter
    def elem2(self, reference_element: Reference):
        """
        :param Reference reference_element:
        """

        self.hybrid_shape_combine.Elem2 = reference_element.com_object

    @property
    def nearest_solution(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NearestSolution() As long
                | 
                |     Returns or sets whether the combined curve is or should be created as the
                |     curve closest to the first curve.
                |     Role: The nearest solution indicates whether the created combined curve is
                |     the one closest to the first curve if there are several possible combined
                |     curves, or if all these possible combined curves are
                |     created..
                |     Legal values: 0 for the nearest solution and 1 for all possible
                |     solutions.
                | 
                |     Example:
                | 
                |           This example sets the nearest solution mode to create the combined
                |           curve
                |          hybCombCurve closest to the first curve.
                |          
                | 
                |          hybCombCurve.NearestSolution = 1

        :rtype: int
        """

        return self.hybrid_shape_combine.NearestSolution

    @nearest_solution.setter
    def nearest_solution(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_combine.NearestSolution = value

    @property
    def solution_type_combine(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SolutionTypeCombine() As long
                | 
                |     Returns or sets whether the curves that create the combined curve are or
                |     should be extruded along normals to the curve planes or along given
                |     directions.
                |     Role: The curves that make up the combined curve are each extruded along a
                |     direction. This direction can be the normal to the curve plane, or can be set
                |     to a given direction. This is valid for the two curves
                |     altogether.
                |     Legal values: 0 for the normal to the curve planes (default mode), 1 for
                |     given directions
                | 
                |     Example:
                | 
                |           This example sets that the combined curve hybCombCurve should be
                |           created
                |          by extruding the two curves along the normals to their
                |          planes.
                |          
                | 
                |          hybCombCurve.SolutionTypeCombine = 0

        :rtype: int
        """

        return self.hybrid_shape_combine.SolutionTypeCombine

    @solution_type_combine.setter
    def solution_type_combine(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_combine.SolutionTypeCombine = value

    def __repr__(self):
        return f'HybridShapeCombine(name="{self.name}")'
