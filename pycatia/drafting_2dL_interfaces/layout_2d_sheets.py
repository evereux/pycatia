#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_2dL_interfaces.layout_2d_sheet import Layout2DSheet
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Layout2DSheets(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Layout2DSheets
                | 
                | A collection of all the Layout sheets 2DL currently managed by the
                | LayoutRoot.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Layout2DSheet)
        self.layout_2d_sheets = com_object

    @property
    def active_sheet(self) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveSheet() As Layout2DSheet (Read Only)
                | 
                |     Returns the active Layout sheet of the Layout document.
                | 
                |     Example:
                |         The following example shows how to get the active sheet and retrieved
                |         in MySheet in the Layout sheet collection of the layout root of Part supposed
                |         to be in the active document
                | 
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = CATIA.Documents.Part.GetItem("CATLayoutRoot")
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet =  MyLayoutRoot.Sheets.ActiveSheet

        :rtype: Layout2DSheet
        """

        return Layout2DSheet(self.layout_2d_sheets.ActiveSheet)

    def add(self, i_layout_sheet_name: str) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iLayoutSheetName) As Layout2DSheet
                | 
                |     Creates a Layout sheet and adds it to the Layout2DSheets collection. This
                |     Layout sheet becomes the active one.
                | 
                |     Parameters:
                | 
                |         iLayoutSheetName
                |             The name to assign to the created Layout2DSheet object
                |             
                | 
                |     Returns:
                |         The created Layout sheet 
                |     Example:
                |         The following example creates a Layout sheet named FirstSheet and
                |         retrieved in MySheet in the Layout sheet collection of the layout root of Part
                |         supposed to be in the active document
                | 
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = CATIA.Documents.Part.GetItem("CATLayoutRoot")
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet = MyLayoutRoot.Sheets.Add("FirstSheet").

        :param str i_layout_sheet_name:
        :rtype: Layout2DSheet
        """
        return Layout2DSheet(self.layout_2d_sheets.Add(i_layout_sheet_name))

    def add_detail(self, i_layout_sheet_name: str) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDetail(CATBSTR iLayoutSheetName) As Layout2DSheet
                | 
                |     Creates a detail Layout sheet 2DL and adds it to the LayoutSheets2DL
                |     collection. This detail Layout sheet becomes the active
                |     one.
                | 
                |     Parameters:
                | 
                |         iLayoutSheetName
                |             The name to assign to the created detail LayoutSheet object
                |             
                | 
                |     Returns:
                |         The created layout sheet 
                |     Example:
                |         The following example creates a detail Layout sheet named FirstSheet
                |         and retrieved in MySheet in the Layout sheet collection of the layout root of
                |         Part supposed to be in the active document
                | 
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = CATIA.Documents.Part.GetItem("CATLayoutRoot")
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet = MyLayoutRoot.Sheets.Add("FirstSheet")

        :param str i_layout_sheet_name:
        :rtype: Layout2DSheet
        """
        return Layout2DSheet(self.layout_2d_sheets.AddDetail(i_layout_sheet_name))

    def item(self, i_index: cat_variant) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Layout2DSheet
                | 
                |     Returns a Layout sheet using its index or its name from the Layout2DSheets
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Layout sheet to retrieve from the
                |             collection of Layout sheets. As a numerics, this index is the rank of the
                |             Layout sheet in the collection. The index of the first Layout sheet in the
                |             collection is 1, and the index of the last Layout sheet is Count. As a string,
                |             it is the name you assigned to the Layout sheet using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Returns:
                |         The retrieved Layout sheet 
                |     Example:
                |         This example retrieves in ThisLayoutSheet the third Layout sheet, and
                |         in ThatLayoutSheet the Layout sheet named MySheet in the Layout sheet
                |         collection of the layout root of Part supposed to be in the active
                |         document.
                | 
                |          Dim ThisLayoutRoot As Layout2DRoot
                |          Set ThisLayoutRoot = CATIA.ActiveDocument.Part.GetItem("CATlayoutRoot")
                |          Dim ThisLayoutSheet As Layout2DSheet
                |          Set ThisLayoutSheet = ThisLayoutRoot.Sheets.Item(3)
                |          Dim ThatLayoutSheet As Layout2DSheet
                |          Set ThatLayoutSheet = ThisLayoutRoot.Sheets.Item("MySheet")

        :param cat_variant i_index:
        :rtype: Layout2DSheet
        """
        return Layout2DSheet(self.layout_2d_sheets.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Layout2Dsheet from the Layout2DSheets
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Layout sheet to remove from the
                |             collection of Layout sheets. As a numerics, this index is the rank of the
                |             Layout sheet in the collection. The index of the first Layout sheet in the
                |             collection is 1, and the index of the last Layout sheet is Count. As a string,
                |             it is the name you assigned to the Layout sheet using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Example:
                |         The following example removes the second Layout sheet and the Layout
                |         sheet named SheetToBeRemoved in the Layout sheet collection of the layout root
                |         of Part supposed to be in the active document.
                | 
                |          Dim ThisLayoutRoot As Layout2DRoot
                |          Set ThisLayoutRoot = CATIA.ActiveDocument.Part.GetItem("CATlayoutRoot")
                |         
ThisLayoutRoot.Layout2DSheets.Remove("SheetToBeRemoved")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.layout_2d_sheets.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(layout2_d_sheets)
        # #     Dim iIndex (2)
        # #     layout2_d_sheets.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Layout2DSheets(name="{self.name}")'
