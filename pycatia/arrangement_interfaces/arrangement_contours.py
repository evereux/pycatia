#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_contour import ArrangementContour
from pycatia.arrangement_interfaces.arrangement_rectangle import ArrangementRectangle
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementContours(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementContours
                | 
                | A collection object for ArrangementContours of an Area.
                | Role: Use this to manage (create, retrieve and remove) ArrangementContours of
                | an ArrangementArea.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementContour)
        self.arrangement_contours = com_object

    def add_rectangular_contour(self, i_rectangle: ArrangementRectangle) -> ArrangementContour:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddRectangularContour(ArrangementRectangle iRectangle) As
                | ArrangementContour
                | 
                |     Creates a Rectangular Contour by adding a ArrangementRectangle to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iRectangle
                |             ArrangementRectangle to create the contour from. 
                | 
                |     Returns:
                |         Returns the newly created ArrangementContour object and adds it to the
                |         collection.

        :param ArrangementRectangle i_rectangle:
        :rtype: ArrangementContour
        """
        return ArrangementContour(self.arrangement_contours.AddRectangularContour(i_rectangle.com_object))

    def item(self, i_index: cat_variant) -> ArrangementContour:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementContour
                | 
                |     Returns the specified ArrangementContour item of the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementContour to retrieve from
                |             this collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementContour in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementContour by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ArrangementContour object.

        :param cat_variant i_index:
        :rtype: ArrangementContour
        """
        return ArrangementContour(self.arrangement_contours.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes the specified ArrangementContour object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementContour to remove from this
                |             collection.
                | 
                |             To remove a specific object by number, use the rank of the
                |             ArrangementContour in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To remove a specific
                |                 ArrangementContour by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.arrangement_contours.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(arrangement_contours)
        # #     Dim iIndex (2)
        # #     arrangement_contours.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementContours(name="{self.name}")'
