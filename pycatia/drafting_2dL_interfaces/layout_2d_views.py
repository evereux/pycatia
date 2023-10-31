#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.drafting_2dL_interfaces.layout_2d_view import Layout2DView
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Layout2DViews(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Layout2DViews

    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Layout2DView)
        self.layout2_d_views = com_object

    @property
    def active_view(self) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveView() As Layout2DView (Read Only)
                | 
                |     Returns the active Layout2D view of the active Layout2D
                |     sheet.
                | 
                |     Example:
                |         The following example retrieves in ViewToWorkIn the active Layout2D
                |         view in the Layout2DSheets collection of the
                |         layoutRoot
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.Documents.Part.GetItem("CATLayoutRoot")
                |          Dim ViewToWorkIn As Layout2DView
                |          Set ViewToWorkIn = MyRoot.Sheets.ActiveSheet.Layout2DViews.ActiveView

        :rtype: Layout2DView
        """

        return Layout2DView(self.layout2_d_views.ActiveView)

    def add_auxiliary(self, i_reference_view: Layout2DView, i_bc_segment: tuple, i_xorient: float, i_yorient: float,
                      i_section_type: int, i_x: float, i_y: float) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAuxiliary(Layout2DView iReferenceView,
                | CATSafeArrayVariant iBCSegment,
                | double iXorient,
                | double iYorient,
                | CatViewType iSectionType,
                | double iX,
                | double iY) As Layout2DView
                | 
                |     Creates a section or section-cut or auxiliary View2DL from a given Layout
                |     View2DL. The View2DL must be in this collection. Caracteristics of new view
                |     (view plane etc) are computed based on the given basic callout and reference
                |     view 2DL viewplane.
                |     Precondition : 1/ The reference View2DL must be in this collection
                |     Precondition : 2/ The reference View2DL must be a projection view.
                |     Precondition : 3/ The callout segment's length must not be 0.
                |     Precondition : 4/ iViewType must be either auxiliary or section or section cut.
                | 
                |     Parameters:
                | 
                |         iReferenceView
                |             [in] The reference view. Must be a projection View.
                |             
                |         iBCSegment
                |             [in] The callout's segment gives the trace of the auxiliary
                |             View2DL's projection plane in the reference View2DL. It has the following
                |             contents:
                | 
                |             iBCSegment[0] = X1
                |                 x coordinate of the first point 
                |             iBCSegment[1] = Y1
                |                 y coordinate of the first point 
                |             iBCSegment[2] = X2
                |                 x coordinate of the second point 
                |             iBCSegment[3] = Y2
                |                 y coordinate of the second point 
                | 
                |         iBCOrient
                |             [in] The callout's orientation gives the direction taken into
                |             account when Layout2D the auxilliary View2DL. 
                |         iXorient
                |             [in] 
                |         iYorient
                |             [in] This point determine the type taken into account when Layout2D
                |             the auxilliary View2DL. 
                |         iSectionType
                |         iX
                |             [in] 
                |         iY
                |             [in] The coordinate in the Sheet2DL for the new View2DL.
                |             
                | 
                |     Returns:
                |         The created Layout2D view 
                | 
                | Example:
                |     The following example creates a Layout2D view named from the active view
                |     and retrieved in MyView in the Layout2D view collection of the MySheet Layout2D
                |     sheet. This sheet belongs to the Layout2D sheet collection of the
                |     layoutRoot
                | 
                |      Dim x As double
                |      Set x = 10.
                |      Dim y As double
                |      Set y = 10.
                |      Dim MySegment 
                |      ReDim MySegment(3)
                |          MySegment(0) = 10.
                |          MySegment(1) = 200.
                |          MySegment(2) = 100.
                |          MySegment(3) = 200.
                |      Dim MyRoot As Layout2DRoot
                |      Set MyRoot = CATIA.Documents.Part.GetItem("CATLayoutRoot")
                | 
                |      Dim MyFirstView As Layout2DView
                |      Set MyFirstView = MyRoot.Sheets.ActiveSheet.Views.ActiveView
                |      Dim MyView As Layout2DView
                |      Set MyView = MyRoot.Sheets.ActiveSheet.Views.

        :param Layout2DView i_reference_view:
        :param tuple i_bc_segment:
        :param float i_xorient:
        :param float i_yorient:
        :param int i_section_type: enum cat_view_type
        :param float i_x:
        :param float i_y:
        :rtype: Layout2DView
        """
        return Layout2DView(
            self.layout2_d_views.AddAuxiliary(i_reference_view.com_object, i_bc_segment, i_xorient, i_yorient,
                                              i_section_type, i_x, i_y))

    def add_detail(self, i_detail_name: str) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddDetail(CATBSTR iDetailName) As Layout2DView
                | 
                |     Creates a detail view and adds it to the layout view collection. This
                |     layout view becomes the active one.
                |     Precondition : The collection view must be a Detail Sheet
                | 
                |     Parameters:
                | 
                |         iDetailName
                |             The name to assign to the created layout view 
                | 
                |     Returns:
                |         The created layout view 
                |     Example:
                | 
                |           The following example creates a detail view named
                |           Ditto
                |          and retrieved in MyView in the layout view collection
                |          
                |          of the MyDetailSheet layout sheet. Where
                |          MyDetailSheet
                |          is the active sheet of the layout sheet collection of the layout
                |          root
                |          
                | 
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = CATIA.Documents.Part.GetItem("CATLayoutRoot")
                |          Dim MyDetailSheet As Layout2DSheet
                |          Set MyDetailSheet = .Sheets.ActiveSheet
                |          Dim MyView As Layout2DView
                |          Set MyView = MyDetailSheet.Views.AddDetail("Ditto")
                |          
                | 
                | 
                |          
                | 
                |     Dim MyView As Layout2DView Set MyView = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot").Sheets.ActiveSheet. Views.AddDetail()

        :param str i_detail_name:
        :rtype: Layout2DView
        """
        return Layout2DView(self.layout2_d_views.AddDetail(i_detail_name))

    def add_from_3d_plane(self, i_plane: tuple, i_view_type: int, i_x: float, i_y: float) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddFrom3DPlane(CATSafeArrayVariant iPlane,
                | CatViewType iViewType,
                | double iX,
                | double iY) As Layout2DView
                | 
                |     Creates a viewFrom3D View2DL with the given 3Dplane as its view plane at
                |     the given position in the given Sheet2DL.
                | 
                |     Parameters:
                | 
                |         iPlane
                |             [in] Define the plane on wich the view as to be created It has the
                |             following contents:
                | 
                |             iPlane[0] = X
                |                 x coordinate of plane origin in 3D space 
                |             iPlane[1] = Y
                |                 y coordinate of plane origin in 3D space 
                |             iPlane[2] = Z
                |                 z coordinate of plane origin in 3D space 
                |             iPlane[3] = H1
                |                 Define the direction which the view's viewplane H
                |                 
                |             iPlane[4] = H2
                |                 axis has to be colinear with 
                |             iPlane[5] = H3
                |             iPlane[6] = V1
                |                 Define the direction which the view's viewplane V
                |                 
                |             iPlane[7] = V2
                |                 axis has to be colinear with 
                |             iPlane[8] = V3
                | 
                | 
                |             Precondition : 1/iViewType must be either auxiliary or section or section cut.
                |             Precondition : 2/ iFirstDirection and iSecondDirection must be orthogonal. 
                |         iViewType
                |             The view type: catAuxiliary or catSectionCut or catSectionView
                |             
                |         iX
                |             [in] 
                |         iY
                |             [in] The coordinate of the new View2DL in the Sheet2DL
                |             
                | 
                |     Returns:
                |         The created Layout2D view

        :param tuple i_plane:
        :param int i_view_type: enum cat_view_type
        :param float i_x:
        :param float i_y:
        :rtype: Layout2DView
        """
        return Layout2DView(self.layout2_d_views.AddFrom3DPlane(i_plane, i_view_type, i_x, i_y))

    def add_primary(self, i_x: float, i_y: float) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddPrimary(double iX,
                | double iY) As Layout2DView
                | 
                |     Creates a Layout view and adds it to the Layout view collection. This
                |     Layout view becomes the active one.
                | 
                |     Parameters:
                | 
                |         iX
                |             [in] 
                |         iY
                |             [in] The coordinate in the Sheet2DL for the new View2DL.
                |             
                | 
                |     Returns:
                |         The created Layout2D view 
                | 
                | Example:
                |     The following example creates a Layout2D view and retrieved in MyView in
                |     the Layout2D view collection of the Layout2D sheet. This sheet belongs to the
                |     Layout2D sheet collection.
                | 
                |      Dim x as double
                |      Set x = 10.
                |      Dim y as double
                |      Set y = 10.
                |      Dim MyView As Layout2DView
                |      Set MyView = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot").Sheets.ActiveSheet.
                |                   Views.AddPrimary(x, y).

        :param float i_x:
        :param float i_y:
        :rtype: Layout2DView
        """
        return Layout2DView(self.layout2_d_views.AddPrimary(i_x, i_y))

    def add_related(self, i_reference_view: Layout2DView, i_side: int, i_x: float, i_y: float) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddRelated(Layout2DView iReferenceView,
                | CatViewSide iSide,
                | double iX,
                | double iY) As Layout2DView
                | 
                |     Creates a projection or isometric Layout View2DL from a given View2DL. The
                |     view will be created in the same collection as the given View2DL, at the given
                |     position. The caracteristics (ex: view plane etc) of this new View2DL are
                |     computed based on the caracteristics stored in the ViewBox its iReferenceView
                |     is associated with.
                | 
                |     Parameters:
                | 
                |         iReferenceView
                |             [in] The reference View2DL from which the new View2DL is created.
                |             
                |         iSide
                |             [in] Used with the ViewBox and iReferenceView to give the related
                |             view to create (type etc). 
                |         iX
                |             [in] 
                |         iY
                |             [in] The coordinate in the Sheet2DL for the new View2DL.
                |             
                | 
                |     Returns:
                |         The created Layout2D view
                |         Precondition : The reference View2DL must be in this collection 
                | 
                | Example:
                |     The following example creates a Layout2D view named from the active view
                |     and retrieved in MyView in the Layout2D view collection of the MySheet Layout2D
                |     sheet. This sheet belongs to the Layout2D sheet collection of the
                |     layoutRoot.
                | 
                |      Dim x as double
                |      Set x = 10.
                |      Dim y as double
                |      Set y = 10.
                |      Dim MyFirstView As Layout2DView
                |      Set MyFirstView = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot").Sheets.ActiveSheet.Views.ActiveView
                |      Dim MyView As Layout2DView
                |      Set MyView = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot").Sheets.ActiveSheet.Views.
                |                   AddRelated(MyFirstView,catLeftSide, x, y)

        :param Layout2DView i_reference_view:
        :param int i_side: enum cat_view_side
        :param float i_x:
        :param float i_y:
        :rtype: Layout2DView
        """
        return Layout2DView(self.layout2_d_views.AddRelated(i_reference_view.com_object, i_side, i_x, i_y))

    def item(self, i_index: cat_variant) -> Layout2DView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Layout2DView
                | 
                |     Returns a Layout2D view using its index or its name from the Layout2DViews
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Layout2D view to retrieve from the
                |             collection of Layout2D views. As a numerics, this index is the rank of the
                |             Layout2D view in the collection. The index of the first Layout2D view in the
                |             collection is 1, and the index of the last Layout2D view is Count. As a string,
                |             it is the name you assigned to the Layout2D view using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Returns:
                |         The retrieved Layout2D view 
                |     Example:
                | 
                |           This example retrieves in ThisLayout2DView the second Layout2D
                |           view,
                |          and in ThatLayout2DView the Layout2D view named
                |          MyView in the Layout2D view collection of the active sheet of a
                |          layoutRoot
                |          of a part of the active document, supposed to be a part
                |          document.
                |          
                | 
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot").Sheets.ActiveSheet
                |          Dim ThisLayout2DView As Layout2DView
                |          Set ThisLayout2DView = MySheet.Views.ActiveView.Item(2)
                |          Dim ThatLayout2DView As Layout2DView
                |          Set ThatLayout2DView = MySheet.Views.ActiveView.Item("MyView")

        :param cat_variant i_index:
        :rtype: Layout2DView
        """
        return Layout2DView(self.layout2_d_views.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a layout2D view from the Layout2DViews collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Layout2D view to remove from the
                |             collection of Layout2D views. As a numerics, this index is the rank of the
                |             Layout2D view in the collection. The index of the first Layout2D view in the
                |             collection is 1, and the index of the last Layout2D view is Count. As a string,
                |             it is the name you assigned to the Layout2D view using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                | 
                | Example:
                |     The following example removes the third Layout2D view and the Layout2D view
                |     named TopView in the Layout2D view collection of the active sheet of a
                |     layoutRoot of a part of the active document, supposed to be a part
                |     document.
                | 
                |      Dim MySheet As Layout2DSheet
                |      Set MySheet = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot").Sheets.ActiveSheet
                |      MySheet.ActiveViews.Remove(3)
                |      MySheet.ActiveViews.Remove("TopView")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.layout2_d_views.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(layout2_d_views)
        # #     Dim iIndex (2)
        # #     layout2_d_views.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Layout2DViews(name="{self.name}")'
