#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.drafting_2dL_interfaces.layout_2d_sheet import Layout2DSheet
from pycatia.drafting_2dL_interfaces.layout_2d_sheets import Layout2DSheets
from pycatia.system_interfaces.any_object import AnyObject


class Layout2DRoot(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DRoot
                | 
                | Interface to manage the 2D Layout root.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.layout_2d_root = com_object

    @property
    def active_sheet(self) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveSheet() As Layout2DSheet
                | 
                |     Retrieves or sets the active sheet of the layout.
                | 
                |     Example:
                |         This example retrieves the active sheet currently managed by the layout
                |         root of a part of the active document, supposed to be a part
                |         document.
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayout2DRoot)"
                |          Dim MySheet = MyRoot.GetActiveSheet

        :rtype: Layout2DSheet
        """

        return Layout2DSheet(self.layout_2d_root.ActiveSheet)

    @active_sheet.setter
    def active_sheet(self, value: Layout2DSheet):
        """
        :param Layout2DSheet value:
        """

        self.layout_2d_root.ActiveSheet = value

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Parameters() As Parameters (Read Only)
                | 
                |     Returns the collection of parameters of the layout.
                | 
                |     Example:
                | 
                |           This example retrieves in layoutParameters the collection
                |           of
                |          parameters currently managed by the layout root of a part of the
                |          active document, 
                |          supposed to be a part document.
                |          
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayout2DRoot)"
                |          Dim layoutParameters As Parameters
                |          Set layoutParameters = MyRoot.Parameters

        :rtype: Parameters
        """

        return Parameters(self.layout_2d_root.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Relations() As Relations (Read Only)
                | 
                |     Returns the collection of relations of the part document.
                | 
                |     Example:
                | 
                |           This example retrieves in layoutRelations the collection
                |           of
                |          relations currently managed by the layout root of a part of the active
                |          document, 
                |          supposed to be a part document.
                |          
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayout2DRoot)"
                |          Dim layoutRelations As Relations
                |          Set layoutRelations = MyRoot.Relations

        :rtype: Relations
        """

        return Relations(self.layout_2d_root.Relations)

    @property
    def rendering_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RenderingMode() As CatRenderingMode
                | 
                |     Set/Get the rendering mode of Layout2D. get_RenderingMode method can fail
                |     if rendering value stored on Layout is not a value defined in CatRenderingMode
                |     enum.
                | 
                |     Example:
                |         This example sets the rendering mode to catRenderShadingWithEdges for
                |         the layout root of a part of the active document.
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayout2DRoot)"
                |          MyRoot. RenderingMode  = catRenderShadingWithEdges

        :return: enum cat_rendering_mode
        :rtype: int
        """

        return self.layout_2d_root.RenderingMode

    @rendering_mode.setter
    def rendering_mode(self, value: int):
        """
        :param int value: enum cat_rendering_mode
        """

        self.layout_2d_root.RenderingMode = value

    @property
    def sheets(self) -> Layout2DSheets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Sheets() As Layout2DSheets (Read Only)
                | 
                |     Returns the collection of Layout2D sheets of the part
                |     document.
                | 
                |     Example:
                |         This example retrieves in SheetCollection the collection of sheets
                |         currently managed by the layout root of a part of the active document, supposed
                |         to be a part document.
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayout2DRoot)"
                |          Dim SheetCollection As Layout2DSheets
                |          Set SheetCollection = MyRoot.Sheets.

        :rtype: Layout2DSheets
        """

        return Layout2DSheets(self.layout_2d_root.Sheets)

    @property
    def standard(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Standard() As CatDrawingStandard
                | 
                |     Returns or sets the DrawingStandard of the part document.
                | 
                |     Example:
                |         This example sets the drawing standard currently managed by the layout
                |         root of a part of the active document, supposed to be a part document, to
                |         ISO.
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayout2DRoot)"
                |          MyRoot.Standard = catISO

        :return: enum cat_drawing_standard
        :rtype: int
        """

        return self.layout_2d_root.Standard

    @standard.setter
    def standard(self, value: int):
        """
        :param int value: enum cat_drawing_standard
        """

        self.layout_2d_root.Standard = value

    @property
    def visu_in_3d(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisuIn3D() As CatVisuIn3DMode
                | 
                |     Set/Get the 3D visualization mode of the layout in the 3D Viewer ie in the
                |     3D windows and in the background of each view in every 2D
                |     context.
                | 
                |     See also:
                |         CatVisuIn3DMode

        :return: enum cat_visu_in_3d_mode
        :rtype: int
        """

        return self.layout_2d_root.VisuIn3D

    @visu_in_3d.setter
    def visu_in_3d(self, value: int):
        """
        :param int value: enum cat_visu_in_3d_mode
        """

        self.layout_2d_root.VisuIn3D = value

    def reorder_sheets(self, i_ordered_sheets: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub reorder_Sheets(CATSafeArrayVariant iOrderedSheets)
                | 
                |     Changes the positions of the sheets in this drawing according to the given
                |     ordered list. iOrderedSheets is the result of a permutation applied to the list
                |     of all the sheets of this drawing, with the following constraint: For every
                |     non-detail sheet, there is not any detail sheet appearing before in
                |     iOrderedSheets.
                | 
                |     Example:
                |         This example inverts the sheet order of a drawing made of exactly two
                |         regular sheets.
                | 
                |          Set drwsheetsorder =  CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot")
                |          Set drwsheets = drwsheetsorder.Sheets
                |          Set sheet1 = drwsheets.item(1)
                |          Set sheet2 = drwsheets.item(2)
                |          newsheetorder = Array(sheet2, sheet1)
                |          drwsheetsorder.reorder_Sheets(newsheetorder)

        :param tuple i_ordered_sheets:
        :rtype: None
        """
        return self.layout_2d_root.reorder_Sheets(i_ordered_sheets)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'reorder_sheets'
        # # vba_code = """
        # # Public Function reorder_sheets(layout2_d_root)
        # #     Dim iOrderedSheets (2)
        # #     layout2_d_root.reorder_Sheets iOrderedSheets
        # #     reorder_sheets = iOrderedSheets
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Layout2DRoot(name="{self.name}")'
