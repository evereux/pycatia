#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_item_reservation import ArrangementItemReservation
from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementItemReservations(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementItemReservations
                | 
                | A collection object for ArrangementItemReservation objects.
                | Role: Use this collection object to manage (create, retrieve and remove)
                | ArrangementItemReservation objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementItemReservation)
        self.arrangement_item_reservations = com_object

    def add_item_reservation(
            self,
            i_rel_axis: Move,
            i_position: tuple,
            i_x_min: float,
            i_y_min: float,
            i_z_min: float,
            i_x_max: float,
            i_y_max: float,
            i_z_max: float
    ) -> ArrangementItemReservation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddItemReservation(Move iRelAxis,
                | CATSafeArrayVariant iPosition,
                | double iXMin,
                | double iYMin,
                | double iZMin,
                | double iXMax,
                | double iYMax,
                | double iZMax) As ArrangementItemReservation
                | 
                |     Creates an ArrangementItemReservation and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             Relative Axis to be considered. 
                |         iPosition
                |             Position information for the ItemReservation (rotation and
                |             location). 
                |         iXMin
                |             Minium X Coordinate of the bounding box on the Item Reservation.
                |             
                |         iYMin
                |             Minium Y Coordinate of the bounding box on the Item Reservation.
                |             
                |         iZMin
                |             Minium Z Coordinate of the bounding box on the Item Reservation.
                |             
                |         iXMax
                |             Maximum X Coordinate of the bounding box on the Item Reservation.
                |             
                |         iYMax
                |             Maximum Y Coordinate of the bounding box on the Item Reservation.
                |             
                |         iZMax
                |             Maximum Z Coordinate of the bounding box on the Item Reservation.
                |             
                | 
                |     Returns:
                |         Returns the newly created ArrangementItemReservation object and adds it
                |         to the collection.

        :param Move i_rel_axis:
        :param tuple i_position:
        :param float i_x_min:
        :param float i_y_min:
        :param float i_z_min:
        :param float i_x_max:
        :param float i_y_max:
        :param float i_z_max:
        :rtype: ArrangementItemReservation
        """
        return ArrangementItemReservation(
            self.arrangement_item_reservations.AddItemReservation(
                i_rel_axis.com_object,
                i_position,
                i_x_min,
                i_y_min,
                i_z_min,
                i_x_max,
                i_y_max,
                i_z_max
            )
        )

    def item(self, i_index: cat_variant) -> ArrangementItemReservation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementItemReservation
                | 
                |     Returns the specified ArrangementItemReservation item of the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementItemReservation to retrieve
                |             from this collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementItemReservation in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementItemReservation by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ArrangementItemReservation object.

        :param cat_variant i_index:
        :rtype: ArrangementItemReservation
        """
        return ArrangementItemReservation(self.arrangement_item_reservations.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes the specified ArrangementItemReservation object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementItemReservation to remove
                |             from this collection.
                | 
                |             To remove a specific object by number, use the rank of the
                |             ArrangementItemReservation in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To remove a specific
                |                 ArrangementItemReservation by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.arrangement_item_reservations.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(arrangement_item_reservations)
        # #     Dim iIndex (2)
        # #     arrangement_item_reservations.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementItemReservations(name="{self.name}")'
