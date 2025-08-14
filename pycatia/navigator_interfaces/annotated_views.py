#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.viewpoint_3d import ViewPoint3D
from pycatia.navigator_interfaces.annotated_view import AnnotatedView
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AnnotatedViews(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnnotatedViews
                | 
                | A collection of AnnotatedView objects.
                | 
                | The method Product.GetTechnologicalObject ("AnnotatedViews") on the root
                | product retrieves this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AnnotatedView)
        self.annotated_views = com_object

    def add(self) -> AnnotatedView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As AnnotatedView
                | 
                |     Creates an annotated view using the current viewpoint and adds it to the
                |     AnnotatedView collection.
                | 
                |     Returns:
                |         The created AnnotatedView 
                |     Example:
                | 
                |              This example creates a new AnnotatedView in the TheAnnotatedViews
                |              collection.
                |             
                | 
                |             Dim NewAnnotatedView As AnnotatedView
                |             Set NewAnnotatedView = TheAnnotatedViews.Add

        :rtype: AnnotatedView
        """
        return AnnotatedView(self.annotated_views.Add())

    def add_from_viewpoint(self, i_viewpoint: ViewPoint3D) -> AnnotatedView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddFromViewpoint(Viewpoint3D iViewpoint) As
                | AnnotatedView
                | 
                |     Creates an annotated view using a given viewpoint and adds it to the
                |     AnnotatedView collection.
                | 
                |     Parameters:
                | 
                |         iViewpoint
                |             The viewpoint. 
                | 
                |     Returns:
                |         The created AnnotatedView 
                |     Example:
                | 
                |              This example creates a new AnnotatedView in the TheAnnotatedViews
                |              collection using a 
                |             AViewpoint viewpoint object.
                |             
                | 
                |             Dim NewAnnotatedView As AnnotatedView
                |             Set NewAnnotatedView = TheAnnotatedViews.AddFromViewpoint(AViewpoint)

        :param ViewPoint3D i_viewpoint:
        :rtype: AnnotatedView
        """
        return AnnotatedView(self.annotated_views.AddFromViewpoint(i_viewpoint.com_object))

    def item(self, i_index: cat_variant) -> AnnotatedView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As AnnotatedView
                | 
                |     Returns an annotated view using its index or its name from the
                |     AnnotatedViews collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the AnnotatedView to retrieve from the
                |             collection of AnnotatedViews. As a numerics, this index is the rank of the
                |             AnnotatedView in the collection. The index of the first AnnotatedView in the
                |             collection is 1, and the index of the last AnnotatedView is Count. As a string,
                |             it is the name you assigned to the AnnotatedView. 
                | 
                |     Returns:
                |         The retrieved AnnotatedView 
                |     Example:
                | 
                |              This example retrieves in ThisAnnotatedView the ninth
                |              AnnotatedView,
                |             and in ThatAnnotatedView the AnnotatedView named
                |             AnnotatedView3 from the TheAnnotatedViews collection.
                |             
                |             
                | 
                |             Dim ThisAnnotatedView As AnnotatedView
                |             Set ThisAnnotatedView = TheAnnotatedViews.Item(9)
                |             Dim ThatAnnotatedView As AnnotatedView
                |             Set ThatAnnotatedView = TheAnnotatedViews.Item("AnnotatedView3")

        :param cat_variant i_index:
        :rtype: AnnotatedView
        """
        return AnnotatedView(self.annotated_views.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an annotated view from the AnnotatedViews
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the AnnotatedView to retrieve from he
                |             collection of AnnotatedViews. As a numerics, this index is the rank of the
                |             AnnotatedView in the collection. The index of the first AnnotatedView in the
                |             collection is 1, and the index of the last AnnotatedView is Count. As a string,
                |             it is the name you assigned to the AnnotatedView. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth AnnotatedView and the
                |              AnnotatedView named
                |             AnnotatedView2 from the TheAnnotatedViews
                |             collection.
                |             
                | 
                |             TheAnnotatedViews.Remove(10)
                |             TheAnnotatedViews.Remove("AnnotatedView2")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.annotated_views.Remove(i_index)

    def __getitem__(self, n: int) -> AnnotatedView:
        if (n + 1) > self.count:
            raise StopIteration

        return AnnotatedView(self.annotated_views.Item(n + 1))

    def __iter__(self) -> Iterator[AnnotatedView]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'AnnotatedViews(name="{self.name}")'
