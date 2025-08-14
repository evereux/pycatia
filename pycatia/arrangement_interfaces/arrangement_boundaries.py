#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_boundary import ArrangementBoundary
from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementBoundaries(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementBoundaries
                | 
                | A collection object for ArrangementBoundary objects.
                | Role: This collection object is used to manage (create, retrieve and remove
                | )ArrangementBoundary objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementBoundary)
        self.arrangement_boundaries = com_object

    def add_boundary(
            self,
            i_rel_axis: Move,
            i_listof_math_points: tuple,
            i_math_direction: tuple
    ) -> ArrangementBoundary:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddBoundary(Move iRelAxis,
                | CATSafeArrayVariant iListofMathPoints,
                | CATSafeArrayVariant iMathDirection) As ArrangementBoundary
                | 
                |     Creates an ArrangementBoundary and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             Relative Axis to be considered. 
                |         iListofMathPoints
                |             List of points through which to route. 
                |         iMathDirection
                |             Starting routing direction. 
                | 
                |     Returns:
                |         The newly created ArrangementBoundary object.

        :param Move i_rel_axis:
        :param tuple i_listof_math_points:
        :param tuple i_math_direction:
        :rtype: ArrangementBoundary
        """
        return ArrangementBoundary(
            self.arrangement_boundaries.AddBoundary(
                i_rel_axis.com_object,
                i_listof_math_points,
                i_math_direction))

    def item(self, i_index: cat_variant) -> ArrangementBoundary:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementBoundary
                | 
                |     Returns the specified ArrangementBoundary item of the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementBoundary to retrieve from
                |             this collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementBoundary in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementBoundary by name, use name that you assigned using the
                |                 
                |         AnyObject.Name property.
                |     Returns:
                |         The retrieved ArrangementBoundary object.

        :param cat_variant i_index:
        :rtype: ArrangementBoundary
        """
        return ArrangementBoundary(self.arrangement_boundaries.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes the specified ArrangementBoundary object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementBoundary to remove from
                |             this collection.
                | 
                |             To remove a specific object by number, use the rank of the
                |             ArrangementBoundary in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To remove a specific
                |                 ArrangementBoundary by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.arrangement_boundaries.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(arrangement_boundaries)
        # #     Dim iIndex (2)
        # #     arrangement_boundaries.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementBoundaries(name="{self.name}")'
