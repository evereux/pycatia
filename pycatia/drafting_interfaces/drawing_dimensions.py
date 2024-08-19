#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator, Union

from pycatia.drafting_interfaces.drawing_dimension import DrawingDimension
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant
from pycatia.scripts.vba import VBANothing
from pycatia.scripts.vba import vba_nothing


class DrawingDimensions(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingDimensions
                | 
                | A collection of all the drawing dimensions currently managed by a drawing view
                | of drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingDimension)
        self.drawing_dimensions = com_object

    def add(self, i_type_dim: int, i_geom_elem: tuple, i_pt_coord_elem: tuple, i_line_rep: int) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CatDimType iTypeDim,
                | CATSafeArrayVariant iGeomElem,
                | CATSafeArrayVariant iPtCoordElem,
                | CatDimLineRep iLineRep) As DrawingDimension
                | 
                |     Creates a drawing dimension and adds it to the DrawingDimensions
                |     collection.
                | 
                |     Parameters:
                | 
                |         iTypeDim
                |             Dimension type 
                |         iGeomElem
                |             Parent geometrical element(s) of dimension 
                |         iPtCoordElem
                |             Array of pointers on the selection points of each element of
                |             iGeomElem 
                |         iLineRep
                |             Basic representation mode 
                | 
                |     Returns:
                |         The created drawing dimension 
                | 
                | Example:
                |     The following example creates a drawing angle dimension between two lines
                |     and a partial curvilinear length dimension on an ellipse and retrieved in
                |     MyDimension1 and MyDimension2 in the drawing view collection of the MyView
                |     drawing view. This view belongs to the drawing view collection of the drawing
                |     sheet
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim Fact2D  As Factory2D
                |      Set Fact2D = MyView.Factory2D
                |      Dim Line1 As Line2D
                |      Dim Line2 As Line2D
                |      Set Line1 = Fact2D.CreateLine(50, 10, 150, 10)
                |      Set Line2 = Fact2D.CreateLine(50, 10, 120, 100)
                |      Dim Ellipse1 As Ellipse2D
                |      Set Ellipse1 = Fact2D.CreateEllipse(-40, 100, 120, 180,120,90,0, 3)
                |      Dim Point1 As Point2D
                |      Dim Point2 As Point2D
                |      Set Point1 = Fact2D.CreatePoint(-10,190)
                |      Set Point2 = Fact2D.CreatePoint(-120,90)
                |      Dim iType As catDimType
                |      iType = catDimAngle
                |      Dim myElements1(1)
                |      myElements1(1) = Array(Line1,Line2)
                |      Dim selpoints(3)
                |      selpoints(3) = Array(150, 10, 120, 100)
                |      Dim MyDimension1 As DrawingDimension
                |      Set MyDimension1 = MyView.Dimensions.Add(iType, myElements1(1), selpoints(3),catDimAuto)
                |      iType = catDimLengthCurvilinear
                |      Dim myElements2(2)
                |      myElements2(2) = Array(Point1,Point2,Ellipse1)
                |      selpoints(3) = Array(0, 0, 0, 0)
                |      Dim MyDimension2 As DrawingDimension
                |      Set MyDimension2 = MyView.Dimensions.Add(iType, myElements2(1), selpoints(3),catDimOffset)

        :param int i_type_dim: enum cat_dim_type
        :param tuple i_geom_elem:
        :param tuple i_pt_coord_elem:
        :param int i_line_rep:
        :rtype: DrawingDimension
        """

        i_geom_elem = [elem.com_object for elem in i_geom_elem]

        return DrawingDimension(
            self.drawing_dimensions.Add(
                i_type_dim,
                i_geom_elem,
                i_pt_coord_elem,
                i_line_rep)
        )

    def add2(self,
             i_type_dim: int,
             i_geom_elem: tuple,
             i_pt_coord_elem: tuple,
             i_ldc_ref_elem: Union[cat_variant, VBANothing],
             i_ldc_ref_angle: int) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add2(CatDimType iTypeDim,
                | CATSafeArrayVariant iGeomElem,
                | CATSafeArrayVariant iPtCoordElem,
                | CATVariant iLDCRefElem,
                | long iLDCRefAngle) As DrawingDimension
                | 
                |     Creates a drawing dimension along a direction and adds it to the
                |     DrawingDimensions collection.
                | 
                |     Parameters:
                | 
                |         iTypeDim
                |             Dimension type (available types : catDimDistance, catDimLength, catDimRadiusTangent and
                |             catDimDiameterTangent)
                |         iGeomElem
                |             Parent geometrical element(s) of dimension
                |         iPtCoordElem
                |             Array of pointers on the selection points of each element of
                |             iGeomElem 
                |         iLDCRefElem
                |             Reference geometrical element for the direction of the dimension
                |             line .iLDCRefElem can be null: in this case, the view is the reference element
                |         iLDCRefAngle
                |             Angle between the reference element and the direction of the
                |             dimension line 
                | 
                |     Returns:
                |         The created drawing dimension (The property CATDimLineRep of the
                |         dimension line of the created dimension is set to catDimUserDefined)
                |         
                | 
                | Example:
                |     The following example creates a drawing distance dimension between two
                |     points along the direction of a line and retrieved in MyDimension in the
                |     drawing view collection of the MyView drawing view. This view belongs to the
                |     drawing view collection of the drawing sheet
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim Fact2D  As Factory2D
                |      Set Fact2D = MyView.Factory2D
                |      Dim Point1 As Point2D
                |      Dim Point2 As Point2D
                |      Set Point1 = Fact2D.CreatePoint(40, 230)
                |      Set Point2 = Fact2D.CreatePoint(80, 210)
                |      Dim Line1 As Line2D
                |      Set Line1 = Fact2D.CreateLine(50, 10, 150, 10)
                |      Dim iType As catDimType
                |      iType = catDimDistance
                |      Dim myElements(1)
                |      myElements(1) = Array(Point1,Point2)
                |      Dim selpoints(3)
                |      selpoints(3) = Array(0, 0, 0, 0)
                |      Dim MyDimension As DrawingDimension
                |      Set MyDimension = MyView.Dimensions.Add2(iType, myElements(1), selpoints(3), Line1, 0)

        :param int i_type_dim: enum cat_dim_type
        :param tuple i_geom_elem:
        :param tuple i_pt_coord_elem:
        :param cat_variant i_ldc_ref_elem:
        :param int i_ldc_ref_angle:
        :rtype: DrawingDimension
        """

        i_geom_elem = [elem.com_object for elem in i_geom_elem]

        if i_ldc_ref_elem == vba_nothing:
            i_ldc_ref_elem = self.application.system_service.evaluate(vba_nothing, 0, 'N', [])
        else:
            i_ldc_ref_elem = i_ldc_ref_elem.com_object

        return DrawingDimension(
            self.drawing_dimensions.Add2(
                i_type_dim,
                i_geom_elem,
                i_pt_coord_elem,
                i_ldc_ref_elem,
                i_ldc_ref_angle)
        )

    def item(self, i_index: cat_variant) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As DrawingDimension
                | 
                |     Returns a drawing dimension using its index or its name from the
                |     DrawingDimensions collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing dimension to retrieve from the
                |             collection of drawing dimensions. As a numerics, this index is the rank of the
                |             drawing dimension in the collection. The index of the first drawing dimension
                |             in the collection is 1, and the index of the last drawing dimension is Count.
                |             As a string, it is the name you assigned to the drawing dimension using the
                |             
                | 
                |         AnyObject.Name property or when creating it using the Add method.
                |         
                |     Returns:
                |         The retrieved drawing dimension 
                |     Example:
                | 
                |           This example retrieves in ThisDrawingDimension the second drawing
                |           dimension,
                |          and in ThatDrawingDimension the drawing dimension
                |          named
                |          MyDimension in the drawing dimension collection of the active
                |          view.
                |          
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingDimension As DrawingDimension
                |          Set ThisDrawingDimension = MyView.Dimensions.Item(2)
                |          Dim ThatDrawingDimension As DrawingDimension
                |          Set ThatDrawingDimension = MyView.Dimensions.Item("MyDimension")

        :param cat_variant i_index:
        :rtype: DrawingDimension
        """
        return DrawingDimension(self.drawing_dimensions.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a drawing dimension from the DrawingDimensions
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing dimension to remove from the collection of
                |             drawing dimensions. As a numerics, this index is the rank of the drawing
                |             dimension in the collection. The index of the first drawing dimension in the
                |             collection is 1, and the index of the last drawing dimension is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing dimension in the
                |         drawing dimension collection of the active view of the active document,
                |         supposed to be a drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.Dimensions.Remove(3)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.drawing_dimensions.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingDimension:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingDimension(self.drawing_dimensions.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingDimension]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingDimensions(name="{self.name}")'
