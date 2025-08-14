#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_area import ArrangementArea
from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementAreas(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementAreas
                | 
                | A Collection object for ArrangementArea objects.
                | Role: Use this interface to add, retrieve and remove ArrangementArea objects
                | from this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementArea)
        self.arrangement_areas = com_object

    def add_area(self, i_rel_axis: Move, i_position: tuple, i_height: float) -> ArrangementArea:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddArea(Move iRelAxis,
                | CATSafeArrayVariant iPosition,
                | double iHeight) As ArrangementArea
                | 
                |     Creates a ArrangementArea and adds it to the collection. The Area created
                |     will be without any contour. Hence only the height of the area is
                |     specified.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             Relative Axis to be considered. 
                |         iPosition
                |             Position information for the Area (rotation and location).
                |             
                |         iHeight
                |             Height of the Area. 
                | 
                |     Returns:
                |         The newly created ArrangementArea object that is also added to the
                |         collection.

        :param Move i_rel_axis:
        :param tuple i_position:
        :param float i_height:
        :rtype: ArrangementArea
        """
        return ArrangementArea(self.arrangement_areas.AddArea(i_rel_axis.com_object, i_position, i_height))

    def item(self, i_index: cat_variant) -> ArrangementArea:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementArea
                | 
                |     Returns the specified item of the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementArea to retrieve from this
                |             collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementArea in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementArea by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ArrangementArea object.
                | 
                |         Example:
                |             This example retrieves ArrangementArea, objArea1, of rank 1 under
                |             the Areas collection.
                | 
                |              Dim objArea1 As ArrangementArea
                |              Set objArea1= Areas.Item(1)

        :param cat_variant i_index:
        :rtype: ArrangementArea
        """
        return ArrangementArea(self.arrangement_areas.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes the specified ArrangementArea object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementArea to remove from this
                |             collection.
                | 
                |             To remove a specific object by number, use the rank of the
                |             ArrangementArea in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To remove a specific
                |                 ArrangementArea by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property.
                | 
                |         Example:
                |             This example removes ArrangementArea of rank 1 under the Areas
                |             collection.
                | 
                |              Areas.Remove(1)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.arrangement_areas.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(arrangement_areas)
        # #     Dim iIndex (2)
        # #     arrangement_areas.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementAreas(name="{self.name}")'
