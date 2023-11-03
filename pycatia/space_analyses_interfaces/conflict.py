#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.system_service import SystemService


class Conflict(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Conflict
                | 
                | Represents the Conflict object.
                | 
                | One Conflict object exists for each couple of products that are
                | colliding.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.conflict = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Comment() As CATBSTR
                | 
                |     Returns or sets a comment on the conflict.
                | 
                |     Example:
                | 
                |              The first example gets the comment of NewConflict
                |              Conflict.
                |
                |             Dim aComment As String
                |             aComment = NewConflict.Comment
                |
                |                 The second example sets a comment on the NewConflict
                |                 Conflict.
                |
                |                 NewConflict.Comment = "OK : plastic part"

        :rtype: str
        """

        return self.conflict.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.conflict.Comment = value

    @property
    def comparison_info(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ComparisonInfo() As CatConflictComparison (Read
                | Only)
                | 
                |     Returns the information on the comparison between the conflict and the
                |     previous one.
                | 
                |     Example:
                | 
                |              This example retrieves the comparison information of the
                |              NewConflict Conflict.
                |
                |             Dim anInfo As CatConflictComparison
                |             anInfo = NewConflict.ComparisonInfo

        :return: enum cat_conflict_comparison
        :rtype: int
        """

        return self.conflict.ComparisonInfo

    @property
    def first_product(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstProduct() As Product (Read Only)
                | 
                |     Returns the first product involved in the conflict.
                | 
                |     Example:
                | 
                |              This example retrieves the first product involved in the
                |              NewConflict Conflict.
                |
                |             Dim aProduct As Product
                |             Set aProduct = NewConflict.FirstProduct

        :rtype: Product
        """

        return Product(self.conflict.FirstProduct)

    @property
    def second_product(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondProduct() As Product (Read Only)
                | 
                |     Returns the second product involved in the conflict.
                | 
                |     Example:
                | 
                |              This example retrieves the second product involved in the
                |              NewConflict Conflict.
                |
                |             Dim aProduct As Product
                |             Set aProduct = NewConflict.SecondProduct

        :rtype: Product
        """

        return Product(self.conflict.SecondProduct)

    @property
    def status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Status() As CatConflictStatus
                | 
                |     Returns or sets the status of the conflict.
                | 
                |     Example:
                | 
                |              The first example gets the status of NewConflict
                |              Conflict.
                |
                |             Dim aStatus As CatConflictStatus
                |             aStatus = NewConflict.Status
                |
                |                 The second example sets the status of NewConflict
                |                 Conflict.
                |
                |                 NewConflict.Status = CatConflictStatusIrrelevant

        :return: enum cat_conflict_status
        :rtype: int
        """

        return self.conflict.Status

    @status.setter
    def status(self, value: int):
        """
        :param int value: enum cat_conflict_status
        """

        self.conflict.Status = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CatConflictType (Read Only)
                | 
                |     Returns the type of the conflict.
                | 
                |     Example:
                | 
                |              This example retrieves the type of the NewConflict
                |              Conflict.
                |
                |             Dim conflictType As CatConflictType
                |             conflictType = NewConflict.Type

        :return: enum cat_conflict_type
        :rtype: int
        """

        return self.conflict.Type

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Value() As double (Read Only)
                | 
                |     Returns the conflict value.
                | 
                |     This value is the penetration lengh in case of a clash or the minimum
                |     distance in case of clearance violation.
                | 
                |     Example:
                | 
                |              This example retrieves the value of the NewConflict
                |              Conflict.
                |
                |             Dim conflictValue As double
                |             conflictValue = NewConflict.Value

        :rtype: float
        """

        return self.conflict.Value

    def get_first_point_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFirstPointCoordinates(CATSafeArrayVariant
                | oCoordinates)
                | 
                |     Retrieves the coordinates of the point on the first product which realizes
                |     the penetration or minimum distance.
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
                |              This example retrieves the first product involved in the
                |              NewConflict Conflict.
                |
                |             Dim Coordinates (2)
                |             NewConflict.GetFirstPointCoordinates Coordinates

        :rtype: tuple
        """

        vba_function_name = 'get_first_point_coordinates'
        vba_code = """
        Public Function get_first_point_coordinates(conflict)
            Dim oCoordinates(2)
            conflict.GetFirstPointCoordinates oCoordinates
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
                |     Retrieves the coordinates of the point on the second product which realizes
                |     the penetration or minimum distance.
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
                |              This example retrieves the coordinates in the NewConflict
                |              Conflict.
                |
                |             Dim Coordinates (2)
                |             NewConflict.GetSecondPointCoordinates Coordinates

        :rtype: tuple
        """

        vba_function_name = 'get_second_point_coordinates'
        vba_code = """
        Public Function get_second_point_coordinates(conflict)
            Dim oCoordinates (2)
            conflict.GetSecondPointCoordinates oCoordinates
            get_second_point_coordinates = oCoordinates
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Conflict(name="{self.name}")'
