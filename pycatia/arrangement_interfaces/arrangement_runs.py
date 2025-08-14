#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_run import ArrangementRun
from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementRuns(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementRuns
                | 
                | A collection object of ArrangementRun objects.
                | Role: Use this collection object to manage ArrangementRun
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementRun)
        self.arrangement_runs = com_object

    def add_run(
            self,
            i_rel_axis: Move,
            i_listof_math_points: tuple,
            i_math_direction: tuple
    ) -> ArrangementRun:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddRun(Move iRelAxis,
                | CATSafeArrayVariant iListofMathPoints,
                | CATSafeArrayVariant iMathDirection) As ArrangementRun
                | 
                |     Creates an ArrangementRun and adds it to the collection.
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
                |         Returns the newly created ArrangementRun object and adds it to the
                |         collection.

        :param Move i_rel_axis:
        :param tuple i_listof_math_points:
        :param tuple i_math_direction:
        :rtype: ArrangementRun
        """
        return ArrangementRun(
            self.arrangement_runs.AddRun(
                i_rel_axis.com_object,
                i_listof_math_points,
                i_math_direction
            )
        )

    def item(self, i_index: cat_variant) -> ArrangementRun:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementRun
                | 
                |     Returns the specified ArrangementRun item of the collection
                |     object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementRun to retrieve from this
                |             collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementRun in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementRun by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ArrangementRun object.

        :param cat_variant i_index:
        :rtype: ArrangementRun
        """
        return ArrangementRun(self.arrangement_runs.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes the specified ArrangementRun object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementRun to remove from this
                |             collection.
                | 
                |             To remove a specific object by number, use the rank of the
                |             ArrangementRun in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To remove a specific
                |                 ArrangementRun by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.arrangement_runs.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(arrangement_runs)
        # #     Dim iIndex (2)
        # #     arrangement_runs.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementRuns(name="{self.name}")'
