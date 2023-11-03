#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.navigator_interfaces.annotated_views import AnnotatedViews
from pycatia.navigator_interfaces.group import Group
from pycatia.navigator_interfaces.marker_3Ds import Marker3Ds
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.system_service import SystemService


class Distance(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Distance
                | 
                | Represents the Distance object.
                | The Distance object is a specification of a distance computation between
                | products or groups of products.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.distance = com_object

    @property
    def accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Accuracy() As double
                | 
                |     Returns or sets the accuracy value for the computation.
                | 
                |     The accuracy value must be greater than 0.
                | 
                |     Example:
                | 
                |              The first example retrieves the accuracy value of NewDistance
                |              Distance.
                |
                |             Dim AccuracyValue As double
                |             AccuracyValue = NewDistance.Accuracy
                |
                |                 The second example sets the accuracy value of NewDistance
                |                 Distance.
                |
                |                 NewDistance.Accuracy = 10.

        :rtype: float
        """

        return self.distance.Accuracy

    @accuracy.setter
    def accuracy(self, value: float):
        """
        :param float value:
        """

        self.distance.Accuracy = value

    @property
    def annotated_views(self) -> AnnotatedViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnnotatedViews() As AnnotatedViews (Read Only)
                | 
                |     Returns the AnnotatedViews collection of the distance.
                | 
                |     Example:
                | 
                |              This example retrieves the AnnotatedViews collection of
                |              NewDistance Distance.
                |
                |             Dim TheAnnotatedViewsList As AnnotatedViews
                |             Set TheAnnotatedViewsList = NewDistance.AnnotatedViews

        :rtype: AnnotatedViews
        """

        return AnnotatedViews(self.distance.AnnotatedViews)

    @property
    def computation_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ComputationType() As CatDistanceComputationType
                | 
                |     Returns or sets the computation type for the computation.
                | 
                |     Example:
                | 
                |              The first example retrieves the computation type of NewDistance
                |              Distance.
                |
                |             Dim ComputationType As CatDistanceComputationType
                |             ComputationType = NewDistance.ComputationType
                |
                |                 The second example sets the computation type of NewDistance
                |                 Distance.
                |
                |                 NewDistance.ComputationType = CatDistanceComputationTypeInsideOne

        :rtype: int
        """

        return self.distance.ComputationType

    @computation_type.setter
    def computation_type(self, value: int):
        """
        :param int value:
        """

        self.distance.ComputationType = value

    @property
    def first_group(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstGroup() As Group
                | 
                |     Returns or sets the first group used by the computation.
                | 
                |     Example:
                | 
                |              The first example retrieves the first group of NewDistance
                |              Distance.
                |
                |             Dim FirstGroup As Group
                |             Set FirstGroup = NewDistance.FirstGroup
                |
                |                 The second example sets the first  group of NewDistance
                |                 Distance.
                |
                |                 Dim FirstGroup As Group
                |                 NewDistance.FirstGroup = FirstGroup

        :rtype: Group
        """

        return Group(self.distance.FirstGroup)

    @first_group.setter
    def first_group(self, value: Group):
        """
        :param Group value:
        """

        self.distance.FirstGroup = value

    @property
    def first_product(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstProduct() As Product (Read Only)
                | 
                |     Returns the product belonging to the first group that realizes the minimum
                |     distance.
                | 
                |     Example:
                | 
                |              This example retrieves the first product involved in the
                |              NewDistance Distance.
                |
                |             Dim AProduct As Product
                |             Set AProduct = NewDistance.FirstProduct

        :rtype: Product
        """

        return Product(self.distance.FirstProduct)

    @property
    def is_defined(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsDefined() As long (Read Only)
                | 
                |     Returns a diagnosis on the distance.
                | 
                |     The diagnosis can take two values:
                | 
                |         = 0: the distance is undefined (for example only one product) and the results are invalid.
                |         = 1: the distance is defined and all results are valid. 
                | 
                |     Example:
                | 
                |              This example retrieves the diagnosis on NewDistance
                |              Distance.
                |
                |             If NewDistance.IsDefined = 1 Then

        :rtype: int
        """

        return self.distance.IsDefined

    @property
    def marker_3ds(self) -> Marker3Ds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker3Ds() As Marker3Ds (Read Only)
                | 
                |     Returns the Marker3Ds collection of the distance.
                | 
                |     Example:
                | 
                |              This example retrieves the Marker3Ds collection of NewDistance
                |              Distance.
                |
                |             Dim TheMarker3DsList As Marker3Ds
                |             Set TheMarker3DsList = NewDistance.Marker3Ds

        :rtype: Marker3Ds
        """

        return Marker3Ds(self.distance.Marker3Ds)

    @property
    def maximum_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaximumDistance() As double
                | 
                |     Returns or sets the maximum distance value for the computation (valid only
                |     for band analysis).
                | 
                |     The maximum distance value must be greater than 0.
                | 
                |     Example:
                | 
                |              The first example retrieves the maximum distance value of
                |              NewDistance Distance.
                |
                |             Dim MaximumValue As double
                |             MaximumValue = NewDistance.MaximumDistance
                |
                |                 The second example sets the maximum distance value of
                |                 NewDistance Distance.
                |
                |                 NewDistance.MaximumDistance = 10.

        :rtype: float
        """

        return self.distance.MaximumDistance

    @maximum_distance.setter
    def maximum_distance(self, value: float):
        """
        :param float value:
        """

        self.distance.MaximumDistance = value

    @property
    def measure_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MeasureType() As CatDistanceMeasureType
                | 
                |     Returns or sets the type of distance that will be
                |     calculated.
                | 
                |     Example:
                | 
                |             The first example retrieves the type of NewDistance
                |             Distance.
                |
                |             Dim MeasureType As CatDistanceMeasureType
                |             MeasureType = NewDistance.MeasureType
                |
                |             The second example sets the Type of NewDistance
                |             Distance.
                |
                |             NewDistance.MeasureType = CatDistanceMeasureTypeMinimum

        :return: enum cat_distance_measure_type
        :rtype: int
        """

        return self.distance.MeasureType

    @measure_type.setter
    def measure_type(self, value: int):
        """
        :param int value: enum cat_distance_measure_type
        """

        self.distance.MeasureType = value

    @property
    def minimum_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MinimumDistance() As double
                | 
                |     Returns or sets the minimum distance value for the computation (valid only
                |     for band analysis).
                | 
                |     The minimum distance value must be greater than 0.
                | 
                |     Example:
                | 
                |              The first example retrieves the minimum distance value of
                |              NewDistance Distance.
                |
                |             Dim MinimumValue As double
                |             MinimumValue = NewDistance.MinimumDistance
                |
                |                 The second example sets the minimum distance value of
                |                 NewDistance Distance.
                |
                |                 NewDistance.MinimumDistance = 10.

        :rtype: float
        """

        return self.distance.MinimumDistance

    @minimum_distance.setter
    def minimum_distance(self, value: float):
        """
        :param float value:
        """

        self.distance.MinimumDistance = value

    @property
    def second_group(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondGroup() As Group
                | 
                |     Returns or sets the second group used by the computation.
                | 
                |     Example:
                | 
                |              The first example retrieves the second group of NewDistance
                |              Distance.
                |
                |             Dim SecondGroup As Group
                |             Set SecondGroup = NewDistance.SecondGroup
                |
                |                 The second example sets the second group of NewDistance
                |                 Distance.
                |
                |                 Dim SecondGroup As Group
                |                 NewDistance.SecondGroup = SecondGroup

        :rtype: Group
        """

        return Group(self.distance.SecondGroup)

    @second_group.setter
    def second_group(self, value: Group):
        """
        :param Group value:
        """

        self.distance.SecondGroup = value

    @property
    def second_product(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondProduct() As Product (Read Only)
                | 
                |     Returns the product belonging to the second group that realizes the minimum
                |     distance.
                | 
                |     Example:
                | 
                |              This example retrieves the coordinates in the NewDistance
                |              Distance.
                |
                |             Dim AProduct As Product
                |             Set AProduct = NewDistance.SecondProduct

        :rtype: Product
        """

        return Product(self.distance.SecondProduct)

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Value() As double (Read Only)
                | 
                |     Returns the distance value.
                | 
                |     Example:
                | 
                |              This example retrieves the value of NewDistance
                |              Distance.
                |
                |             Dim MinimumValue As double
                |             MinimumValue = NewDistance.Value

        :rtype: float
        """

        return self.distance.Value

    def compute(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Compute()
                | 
                |     Computes the distance.
                | 
                |     Example:
                | 
                |              This example computes the distance of NewDistance
                |              Distance.
                |
                |             NewDistance.Compute

        :rtype: None
        """
        return self.distance.Compute()

    def get_first_point_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFirstPointCoordinates(CATSafeArrayVariant
                | oCoordinates)
                | 
                |     Retrieves the coordinates of the point belonging to the first product,
                |     which realizes the distance.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinates of the point
                | 
                |                 oCoordinates(0) is the X coordinate
                |                 oCoordinates(1) is the Y coordinate
                |                 oCoordinates(2) is the Z coordinate 
                | 
                |     Example:
                | 
                |              This example retrieves the coordinates of the first point in
                |              NewDistance Distance.
                |
                |             Dim Coordinates (2)
                |             NewDistance.GetFirstPointCoordinates Coordinates

        :rtype: tuple
        """

        vba_function_name = 'get_first_point_coordinates'
        vba_code = """
        Public Function get_first_point_coordinates(distance)
            Dim oCoordinates (2)
            distance.GetFirstPointCoordinates oCoordinates
            get_first_point_coordinates = oCoordinates
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_second_point_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSecondPointCoordinates(CATSafeArrayVariant
                | oCoordinates)
                | 
                |     Retrieves the coordinates of the point belonging to the second product,
                |     which realizes the distance.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinates of the point
                | 
                |                 oCoordinates(0) is the X coordinate
                |                 oCoordinates(1) is the Y coordinate
                |                 oCoordinates(2) is the Z coordinate 
                | 
                |     Example:
                | 
                |              This example retrieves the coordinates of the first point in
                |              NewDistance Distance.
                |
                |             Dim Coordinates (2)
                |             NewDistance.GetSecondPointCoordinates Coordinates

        :rtype: None
        """

        vba_function_name = 'get_second_point_coordinates'
        vba_code = """
        Public Function get_second_point_coordinates(distance)
            Dim oCoordinates (2)
            distance.GetSecondPointCoordinates oCoordinates
            get_second_point_coordinates = oCoordinates
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Distance(name="{self.name}")'
