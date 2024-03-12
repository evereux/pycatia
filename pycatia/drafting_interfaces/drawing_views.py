#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.types.general import cat_variant
from pycatia.drafting_interfaces.drawing_view import DrawingView
from pycatia.system_interfaces.collection import Collection


class DrawingViews(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingViews
                | 
                | A collection of all the drawing views currently managed by a drawing sheet in a
                | drawing document.
                | 
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingView)
        self.drawing_views = com_object

    @property
    def active_view(self) -> DrawingView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ActiveView() As DrawingView (Read Only)
                | 
                |     Returns the active drawing view of the active drawing
                |     sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example retrieves in ViewToWorkIn the active drawing view
                |         in the DrawingSheets collection of the document named
                |         CATDrawing1
                | 
                |          Dim MyDrawingDoc As Document
                |          Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                |          Dim ViewToWorkIn As DrawingView
                |          Set ViewToWorkIn = MyDrawingDoc.Sheets.ActiveSheet.DrawingViews.ActiveView

        :rtype: DrawingView
        """

        return DrawingView(self.drawing_views.ActiveView)

    def add(self, i_drawing_view_name: str) -> DrawingView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CATBSTR iDrawingViewName) As DrawingView
                | 
                |     Creates a drawing view and adds it to the drawing view collection. This
                |     drawing view becomes the active one.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDrawingViewName
                |             The name to assign to the created drawing view 
                | 
                |     Returns:
                |         The created drawing view 
                | 
                | Example:
                |     The following example creates a drawing view named LeftView and retrieved
                |     in MyView in the drawing view collection of the MySheet drawing sheet. This
                |     sheet belongs to the drawing sheet collection of the drawing document named
                |     CATDrawing1.
                | 
                |      Dim MyDrawingDoc As Document
                |      Set MyDrawingDoc = CATIA.Documents.Item("CATDrawing1")
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = MyDrawingDoc.Sheets.Item("FirstSheet")
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.Add("LeftView")

        :param str i_drawing_view_name:
        :rtype: DrawingView
        """
        return DrawingView(self.drawing_views.Add(i_drawing_view_name))

    def item(self, i_index: cat_variant) -> DrawingView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As DrawingView
                | 
                |     Returns a drawing view using its index or its name from the DrawingViews
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing view to retrieve from the
                |             collection of drawing views. As a numerics, this index is the rank of the
                |             drawing view in the collection. The index of the first drawing view in the
                |             collection is 1, and the index of the last drawing view is Count. As a string,
                |             it is the name you assigned to the drawing view using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Returns:
                |         The retrieved drawing view 
                |     Example:
                | 
                |           This example retrieves in ThisDrawingView the second drawing
                |           view,
                |          and in ThatDrawingView the drawing view named
                |          MyView in the drawing view collection of the active
                |          sheet
                |          in the active document, supposed to be a drawing
                |          document.
                |          
                | 
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = CATIA.ActiveDocument.Sheets.ActiveSheet
                |          Dim ThisDrawingView As DrawingView
                |          Set ThisDrawingView = MySheet.Views.ActiveView.Item(2)
                |          Dim ThatDrawingView As DrawingView
                |          Set ThatDrawingView = MySheet.Views.ActiveView.Item("MyView")

        :param cat_variant i_index:
        :rtype: DrawingView
        """
        return DrawingView(self.drawing_views.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a drawing view from the DrawingViews collection.
                |     Warning: This method is not available with 2D Layout for 3D Design and it's
                |     forbidden and not possible to delete main view and background view contained in
                |     this collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing view to remove from the
                |             collection of drawing views. As a numerics, this index is the rank of the
                |             drawing view in the collection. The index of the first drawing view in the
                |             collection is 1, and the index of the last drawing view is Count. As a string,
                |             it is the name you assigned to the drawing view using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                | 
                | Example:
                |     The following example removes the third drawing view and the drawing view
                |     named TopView in the drawing view collection of the active sheet of the active
                |     document, supposed to be a drawing document.
                | 
                |      Dim MySheet As DrawingSheet
                |      Set MySheet = CATIA.ActiveDocument.Sheets.ActiveSheet
                |      MySheet.ActiveViews.Remove(3)
                |      MySheet.ActiveViews.Remove("TopView")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.drawing_views.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingView:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingView(self.drawing_views.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingView]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingViews(name="{self.name}")'
