#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_rectangle import ArrangementRectangle
from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementRectangles(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementRectangles
                | 
                | A Collection object for ArrangementRectangle objects.
                | Role: Use this object to manage (create, retrieve and remove)
                | ArrangementRectangle objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementRectangle)
        self.arrangement_rectangles = com_object

    def add_rectangle(
            self,
            i_rel_axis: Move,
            i_position: tuple,
            i_width: float,
            i_length: float
    ) -> ArrangementRectangle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddRectangle(Move iRelAxis,
                | CATSafeArrayVariant iPosition,
                | double iWidth,
                | double iLength) As ArrangementRectangle
                | 
                |     Creates an ArrangementRectangle and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             Relative Axis to be considered. 
                |         iPosition
                |             Position information for the Rectangle (rotation and location).
                |             
                |         iWidth
                |             Width of the Rectangle. 
                |         iLength
                |             Length of the Rectangle. 
                | 
                |     Returns:
                |         Returns the newly created ArrangementRectangle and adds it to the
                |         collection.

        :param Move i_rel_axis:
        :param tuple i_position:
        :param float i_width:
        :param float i_length:
        :rtype: ArrangementRectangle
        """
        return ArrangementRectangle(
            self.arrangement_rectangles.AddRectangle(i_rel_axis.com_object, i_position, i_width, i_length))

    def item(self, i_index: cat_variant) -> ArrangementRectangle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementRectangle
                | 
                |     Returns the specified ArrangementRectangle item of the collection
                |     object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementRectangle to retrieve from
                |             this collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementRectangle in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementRectangle by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ArrangementRectangle object.

        :param cat_variant i_index:
        :rtype: ArrangementRectangle
        """
        return ArrangementRectangle(self.arrangement_rectangles.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes the specified ArrangementRectangle object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementRectangle to remove from
                |             this collection.
                | 
                |             To remove a specific object by number, use the rank of the
                |             ArrangementRectangle in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To remove a specific
                |                 ArrangementRectangle by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.arrangement_rectangles.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(arrangement_rectangles)
        # #     Dim iIndex (2)
        # #     arrangement_rectangles.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementRectangles(name="{self.name}")'
