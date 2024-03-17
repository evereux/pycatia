#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-03 17:02:05.216737

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
from typing import Iterator

from pywintypes import com_error

from pycatia.exception_handling import CATIAApplicationException
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.selected_element import SelectedElement
from pycatia.in_interfaces.vis_property_set import VisPropertySet
from pycatia.scripts.checking import check_type
from pycatia.system_interfaces.any_object import AnyObject


class Selection(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Selection
                |
                | Represents the selection.
                | The Selection object contains the features the end user selected, usually with
                | the mouse, and which are candidates as subjects for the next
                | action.
                |
                | A feature possess parent objects in the specification tree (hierarchy). For
                | example, the Pad below possess parent objects in the specification
                | tree:
                |
                |    +--------+
                |    !Product3!
                |    +--------+
                |        !
                |        +- Product2 (Product2.1)
                |        !     !
                |        !     +- Product1 (Product1.1)
                |        !           !
                |        !           +- Part1 (Part1.1)
                |        !                !
                |        !                +- Part1
                |        !                     !
                |        !                     +- PartBody
                |        !                           !
                |        +------------------+
                |        !                           +- Pad.1               ! Selected feature
                |        !
                |        !                                !
                |        +------------------+
                |        !                                +- Sketch.1
                |        +- Part2 (Part2.1)
                |
                |
                | For a given selected feature, its parent objects which are exposed to
                | automation can be accessed through a recursive call to the AnyObject.Parent
                | property. When a given feature is selected, there are three
                | possibilities:
                |
                |     The feature is exposed to automation (a Pad for example, this is the common
                |     case): the feature can be accessed by all Selection object
                |     methods
                |     The feature is not exposed to automation, but at least one of its parent
                |     objects is exposed to automation (a DMU Navigator URL for example: the
                |     Hyperlink is not exposed to automation, but the root Product, which contains
                |     the Hyperlink, is exposed to automation):
                |         no access is given to the feature through the Count2 and Item2 methods
                |         of the Selection object
                |         nevertheless, the first parent object of the feature, which is exposed
                |         to automation (the root Product in our example) can be accessed through the
                |         Item2 and Count2 methods
                |         The Search, Delete, VisProperties, Copy, Cut, Paste and PasteSpecial
                |         methods of the Selection object, take into account the
                |         feature.
                |         For example, if the user:
                |             Puts a DMU Navigator URL in the clipboard
                |             Runs a script calling the PasteSpecial method
                |         then, during the paste, the DMU Navigator URL will be
                |         pasted
                |     The feature is not exposed to automation, and he has no parent object which
                |     is exposed to automation (a ResourcesList object of a .CATProcess for
                |     example):
                |         no access is given to the feature through the Count2 and Item2 methods
                |         of the Selection object
                |         no access is given neither to any parent object of the feature through
                |         the Item2 and Count2 methods
                |         The Search, Delete, VisProperties, Copy, Cut, Paste and PasteSpecial
                |         methods of the Selection object take into account the
                |         feature.
                |         For example, if the user:
                |             Go to the "DPM - Process and Resource Definition"
                |             workshop
                |             Puts a ResourcesList object in the clipboard
                |             Runs a script calling the Selection.PasteSpecial
                |             method
                |         then, during the paste, the ResourcesList object will be
                |         pasted.
                |
                | Note: The Selection object can be accessed through the Document.Selection
                | property . However, when the active window contains the tree described above,
                | the Selection object to use is the one associated to the Product3 Document ,
                | which can be accessed through the application of the Document.Selection to this
                | document. You will, for example, determine the Selection object the following
                | way:
                |
                |  Set ActiveProductDocument = CATIA.ActiveDocument
                |  Set Product3 = ActiveProductDocument.Product
                |  Set Product3Products = Product3.Products
                |  Set Product2Dot1 = Product3Products.Item("Product2.1") : Set Product2 = Product2Dot1.ReferenceProduct
                |  Set ProductDocument2 = Product2.Parent
                |  Set Product2Products = Product2.Products
                |  Set Product1Dot1 = Product2Products.Item("Product1.1") : Set Product1 = Product1Dot1.ReferenceProduct
                |  Set ProductDocument1 = Product1.Parent
                |  Set Product1Products = Product1.Products
                |  Set Part1Dot1 = Product1Products.Item("Part1.1") : Set Part1 = Part1Dot1.ReferenceProduct
                |  Set PartDocument1 = Part1.Parent
                |  Set Selection = ActiveProductDocument.Selection
                |
                |
                | Another Selection object, such as:
                |
                |  Set ProductDocument2Selection = ProductDocument2.Selection
                |  Set ProductDocument1Selection = ProductDocument1.Selection
                |  Set PartDocument1Selection = PartDocument1.Selection
                |
                |
                | (lets take ProductDocument2Selection for example) can only be used if, among
                | the different Window , there is at least one whose root Document is
                | ProductDocument2 . Otherwise, results are unpredictable.

    """

    def __init__(self, com_object, child_object=SelectedElement):
        super().__init__(com_object)
        self.selection = com_object
        self.child_object = child_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Count() As long (Read Only)
                | 
                |     Deprecated:
                |         V5R16 #Count2 . The Count and Item Methods have been replaced by the
                |         Count2 and Item2 methods because they did not process correctly features which
                |         are not exposed to automation (such as a ResourcesList feature of a .CATProcess
                |         document).

        :rtype: int
        """

        return self.selection.Count

    @property
    def count2(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Count2() As long (Read Only)
                | 
                |     Returns the number of SelectedElement objects contained by the current
                |     selection.
                |     Role: This method returns the number of SelectedElement objects contained
                |     by the Selection. The Value property of a given SelectedElement object is an
                |     automation object associated to a selected feature.

        :rtype: int
        """

        return self.selection.Count2

    @property
    def vis_properties(self) -> VisPropertySet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property VisProperties() As VisPropertySet (Read Only)
                | 
                |     Manages graphic properties on current selection.
                |     Role: Gives a VisPropertySet automation object so that graphic properties
                |     of the selected objects can be read or modified.
                |     Note: After the execution of the VisProperties methods which update graphic
                |     properties of the features, selected features which are not exposed to
                |     automation will be updated. After the execution of the VisProperties methods
                |     which consult the selection to give the graphic properties, selected features
                |     which are not exposed to automation will be consulted.
                | 
                |     Example:
                |         This example sets in no show all elements of the current
                |         selection:
                | 
                |          Dim Selection,VisPropertySet
                |          Set Selection = CATIA.ActiveDocument.Selection
                |          Set VisPropertySet = Selection.VisProperties
                |          VisPropertySet.SetShow catVisPropertiesNoShowAttr

        :rtype: VisPropertySet
        """

        return VisPropertySet(self.selection.VisProperties)

    def add(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Add(AnyObject iObject)
                | 
                |     Creates a SelectedElement object which Value property is the given
                |     automation object, and adds it to the selection.
                |     Note: In a product structure aggregating a "Part1 (Part1.1)" Part document,
                |     if you double-clic Part1 in the spectification tree:
                | 
                |         the "Part Design" workbench becomes active
                |         the Part1 node is inside a blue button
                | 
                |     Here, Part1 is the UI Active Object.
                |     Some editors, such as CatalogDocument editors, do not possess any UI Active
                |     Object.
                |     When this method is used in a CATAnalysis context, a CATPart (such as Part1
                |     in our example) must be UI active. Otherwise, Selection.Add does not work
                |     correctly (the 3D is not highlighted properly).
                |     Role: Creates a SelectedElement object and adds it to the current
                |     selection. Depending on the type of the parent Document of the Selection
                |     object:
                |
                |         if it is one of the following:
                |             CATIAPartDocument
                |             CATIADrawingDocument
                |             CATIAMaterialDocument
                |             CATIAAnalysisDocument
                |             CATIAFunctionalDocument
                |         then, regarding the created SelectedElement , the SelectedElement.Value
                |         property will be equal to iObject
                |         Otherwise:
                |             first case: the specification tree contains a
                |             path:
                |                 whose leaf node is iObject
                |                 the UI Active Object belongs to the path
                |             then, the method will create a SelectedElement object corresponding
                |             to this path.
                |             Otherwise: the method will create a SelectedElement object
                |             corresponding to the first path, in the specification tree, whose leaf node is
                |             iLeafNode
                | 
                |     Example:
                |         This example creates a SelectedElement object, which Value property is
                |         the ObjectToAdd automation object, the SelectedElement being added to the
                |         current selection.
                | 
                |          CATIA.ActiveDocument.Selection.Add(ObjectToAdd)

        :param AnyObject i_object:
        :rtype: None
        """
        return self.selection.Add(i_object.com_object)

    def clear(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Clear()
                | 
                |     Clears the selection.
                | 
                |     Example:
                |         This example clears the selection. The selection is then
                |         empty.
                | 
                |          CATIA.ActiveDocument.Selection.Clear()

        :rtype: None
        """
        return self.selection.Clear()

    def copy(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Copy()
                | 
                |     Copies, in a copy and paste operation.
                |     Role: Puts the contents of the selection in the clipboard, but leaves the
                |     selected elements in the document, and clears the selection. This is the
                |     programming equivalent of the Copy command from the Edit
                |     menu.
                |     Note: The method (and the script execution) fails if one of the following
                |     errors occurs:
                | 
                |         The CSO is empty. The Copy operation could not be
                |         performed.
                |         No CSO element remains after the filtering through the UI active
                |         object. The Copy operation could not be performed.
                | 
                |     Note: If a selected feature is not exposed to automation, it will be copied
                |     into the clipboard all the way.
                | 
                |     Example:
                |         This example copies, in a copy and paste operation. A selected DMU
                |         Navigator URL will be put into the clipboard although it is not exposed to
                |         automation.
                | 
                |          CATIA.ActiveDocument.Selection.Copy()

        :rtype: None
        """
        return self.selection.Copy()

    def cut(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Cut()
                | 
                |     Cuts, in a cut and paste operation.
                |     Role: Puts the contents of the selection in the clipboard, and removes the
                |     selected elements from the document, and clears the selection. This is the
                |     programming equivalent of the Cut command from the Edit
                |     menu.
                |     Note: The method (and the script execution) fails if one of the following
                |     errors occurs:
                | 
                |         The CSO is empty. The Cut operation could not be
                |         performed.
                |         No CSO element remains after the filtering through the UI active
                |         object. The Cut operation could not be performed.
                | 
                |     Note: If a selected feature is not exposed to automation, it will be copied
                |     into the clipboard and removed from the document all the
                |     way.
                | 
                |     Example:
                |         This example cuts, in a cut and paste opertation. A selected DMU
                |         Navigator URL will be put into the clipboard and removed from the document,
                |         although it is not exposed to automation.
                | 
                |          CATIA.ActiveDocument.Selection.Cut()

        :rtype: None
        """
        return self.selection.Cut()

    def delete(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Delete()
                | 
                |     Deletes all selected objects.
                |     Role: For all the SelectedElement objects contained by the selection, the
                |     SelectedElement.Value automation object is deleted from the
                |     document.
                |     Note: If a selected feature is not exposed to automation, it will deleted
                |     all the way.
                | 
                |     Example:
                |         This example deletes all the selected objects. A selected DMU Navigator
                |         URL will be removed from the document, although it is not exposed to
                |         automation.
                | 
                |          CATIA.ActiveDocument.Selection.Delete()

        :rtype: None
        """
        return self.selection.Delete()

    def filter_correspondence(self, i_filter_type: tuple) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func FilterCorrespondence(CATSafeArrayVariant iFilterType) As
                | boolean
                | 
                |     Specifies if the automation objects appearing as Value property of
                |     SelectedElement objects fit a given filter.
                |     Role: FilterCorrespondence filters the selection with respect to provided
                |     automation types. The use of this method coupled with the use of the
                |     SelectElement2 will enable to offer a multi-selection written programmatically,
                |     which is the common way to write multi-selection is CATIA.
                |     It will enable, for example, to write a script reproducing the
                |     functionalities of the "Fillet" command of the "Part Design"
                |     workbench.
                |     This method, called before a loop onto SelectElement2 calls, will enable if
                |     all the selection objects correspond to the filter (which will be the same as
                |     the filter given to SelectElement2 ), to take them into account, and,
                |     otherwise, to clear the selection.
                |     This multi-selection written programmatically will generally be used
                |     coupled with the fact that already selected elements remain selected during the
                |     selections.
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of strings constants to be used as a filter for the kind
                |             of element to which current selection object must correspond. See the
                |             iFilterType parameter of the
                |
                |         SelectElement2 method.
                |     oAllFit
                |         All current selection objects fit the iFilterType filter, i.e.
                |         regarding each of the current selection objects, they all fit one of the
                |         iFilterType string constant.
                |     Example:
                |
                |           The following example scripts an edge fillet creation command. It
                |           supposes that a part is currently edited,
                |          containing a Pad. It loops onto the following:
                |
                |
                |
                |
                |             it asks the end user to select an edge (see
                |
                |     TriDimFeatEdge ). If the selected edge has not already been selected, the
                |     selected edge is added to the selection, otherwise it is removed from the
                |     selection
                |     it asks the end user if another edge has to be selected
                |     until the answer of the user to the preceding question is
                |     no.
                |     Then, it creates an edge fillet (see ConstRadEdgeFillet ) taking into
                |     account all the selected edges as fillet specifications.
                |
                |     Note: The edges which were selected before the script execution are taken
                |     into account. Nevertheless, if, before the script execution, the selection
                |     contained an object which was not a TriDimFeatEdge element, the selection is
                |     cleared before the first selection proposal.
                |     Note: During the selection of a given edge, the edges already selected
                |     remain highlighted.
                |
                |      Dim Document,Part,Selection,ShapeFactory,EdgeSaveAllocatedCount,EdgeIndex,
                |          AllEdgesHaveBeenSelected,AllFit
                |      Dim EdgeSaveCount,SelectedEdge,SelectedElementBelongsToSaveVariables,AlreadySelectedEdgeIndex
                |      Dim OtherEdgeAnswer,Fillet
                |      Set Document = CATIA.ActiveDocument : Set Part = Document.Part
                |          : Set Selection = Document.Selection
                |      Set ShapeFactory = Part.ShapeFactory
                |      ReDim InputObjectType(0) : InputObjectType(0)="TriDimFeatEdge" : EdgeSaveCount = 0
                |     'We determine if the selection contains an object which is not a
                |     TriDimFeatEdge element
                |      AllFit = Selection.FilterCorrespondence(InputObjectType)
                |     'If the selection contains an object which is not a TriDimFeatEdge element,
                |     we clear the selection
                |      if (Not AllFit) then Selection.Clear
                |      EdgeSaveAllocatedCount = Selection.Count+10 : ReDim EdgeSave(EdgeSaveAllocatedCount-1)
                |     'We loop onto interactive selections
                |      AllEdgesHaveBeenSelected = false
                |      do while (Not AllEdgesHaveBeenSelected)
                |     '  We save the selection content in save variables.
                |     '  This corresponds to the fact that:
                |     '    - we want that, during the following call to SelectElement2, the
                |     TriDimFeatEdge elements previously selected
                |     '      remain highlighted
                |     '    - this is done using the False value for the
                |     iObjectSelectionBeforeCommandUsePossibility
                |     '      parameter of the SelectElement2 method, the selection containing the
                |     TriDimFeatEdge elements. It requires that
                |     '      the selection content be saved
                |          if (EdgeSaveAllocatedCount < Selection.Count) then
                |              EdgeSaveAllocatedCount = EdgeSaveAllocatedCount + 10
                |                  : ReDim EdgeSave(EdgeSaveAllocatedCount-1)
                |          end if
                |          for EdgeIndex = 0 to Selection.Count2-1
                |              Set EdgeSave(EdgeIndex) = Selection.Item2(EdgeIndex+1).Value
                |          next
                |          EdgeSaveCount = Selection.Count
                |     '  We propose to the user that he select an edge
                |          Status=Selection.SelectElement2(InputObjectType,"Select an
                |          edge",false)
                |          if (Status="Cancel") then
                |              Selection.Clear : Exit Sub
                |          end if
                |     '  We save the selected edge in a dedicated variable
                |          Set SelectedEdge = Selection.Item2(1).Value
                |     '  We merge the selected element with the save variables, and put the
                |     result in the selection.
                |     '  At first, we determine if the selected edge already belongs to the
                |     EdgeSave array
                |          EdgeIndex = 0 : SelectedElementBelongsToSaveVariables = False
                |          do while ((EdgeIndex < EdgeSaveCount) And (Not
                |          SelectedElementBelongsToSaveVariables))
                |              if (EdgeSave(EdgeIndex).Name=SelectedEdge.Name)
                |              then
                |                  SelectedElementBelongsToSaveVariables = True
                |                  AlreadySelectedEdgeIndex = EdgeIndex
                |              end if
                |              EdgeIndex = EdgeIndex + 1
                |          loop
                |     '  Effective merge
                |          if (Not SelectedElementBelongsToSaveVariables) then
                |     '      The selected element does not belong to the save variables. We add
                |     the save variables to the selection
                |              for EdgeIndex = 0 to EdgeSaveCount-1
                |                  Selection.Add EdgeSave(EdgeIndex)
                |              next
                |          else
                |     '      We remove the selected element from the save
                |     variables
                |              for EdgeIndex = AlreadySelectedEdgeIndex to EdgeSaveCount-2
                |                  Set EdgeSave(EdgeIndex) = EdgeSave(EdgeIndex+1)
                |              next
                |              EdgeSaveCount = EdgeSaveCount - 1
                |     '      We clear the selection
                |              Selection.Clear
                |     '      We add the save variables to the selection
                |              for EdgeIndex = 0 to EdgeSaveCount -1
                |                  Selection.Add EdgeSave(EdgeIndex)
                |              next
                |          end if
                |     '  We ask the end user if another edge has to be selected
                |          OtherEdgeAnswer = msgbox ("do you want to select another edge?",3,"Edge Fillet Definition")
                |          if (OtherEdgeAnswer = 2) then Exit Sub
                |          if (OtherEdgeAnswer = 7) then AllEdgesHaveBeenSelected = true
                |      loop
                |     'We create an edge fillet taking into account all the selected edges as
                |     fillet specifications
                |      if (Selection.Count > 0) then
                |          Set Fillet = ShapeFactory.AddNewEdgeFilletWithConstantRadius(Selection.Item(1).Value, 1, 5.0)
                |          Fillet.EdgePropagation = 1
                |          for EdgeIndex = 2 to Selection.Count
                |              Fillet.AddObjectToFillet
                |              Selection.Item(EdgeIndex).Value
                |          next
                |          Part.Update : Selection.Clear : Selection.Add Fillet
                |      end if

        :param tuple i_filter_type:
        :rtype: bool
        """
        return self.selection.FilterCorrespondence(i_filter_type)

    def find_object(self, i_object_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func FindObject(CATBSTR iObjectType) As AnyObject
                | 
                |     Finds an object in the current selection and deletes it from the
                |     selection.
                |     Role: Determines the first automation object specified in
                |     SelectedElement.Value (for the SelectedElement objects contained in the current
                |     selection), or which is a Parent (see AnyObject.Parent ) of the automation
                |     object specified in SelectedElement.Value , which type is equal to the type
                |     specified in input. It returns directly the automation object and deletes the
                |     corresponding SelectedElement object from the current
                |     selection.
                |     Note: If the string specified in input is he "CATIAProduct" string, the
                |     possible automation object specified in SelectedElement.LeafProduct is also
                |     looked at.
                | 
                |     Example:
                |         This example searches a Pad object in the current selection and puts it
                |         into FoundObject.
                | 
                |          Dim FoundObject As AnyObject
                |          Set FoundObject = CATIA.ActiveDocument.Selection.FindObject("CATIAPad")

        :param str i_object_type:
        :rtype: AnyObject
        """
        return AnyObject(self.selection.FindObject(i_object_type))

    def indicate_or_select_element_2d(self,
                                      i_message: str,
                                      i_filter_type: tuple,
                                      i_object_selection_before_command_use_possibility: bool,
                                      i_tooltip: bool,
                                      i_triggering_on_mouse_move: bool) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func IndicateOrSelectElement2D(CATBSTR iMessage,
                | CATSafeArrayVariant iFilterType,
                | boolean iObjectSelectionBeforeCommandUsePossibility,
                | boolean iTooltip,
                | boolean iTriggeringOnMouseMove,
                | boolean oObjectSelected,
                | CATSafeArrayVariant oDocumentWindowLocation) As CATBSTR
                |
                |     Runs an interactive command enabling both indication and selection, 2D
                |     version.
                |     Role: IndicateOrSelectElement2D asks the end user to select either a
                |     location into the window, or a feature (in the geometry or in the specification
                |     tree).
                |     During execution, when entering this method, the active document must be a
                |     2D document. See Document.Indicate2D and SelectElement3
                |
                |     Parameters:
                |
                |         iMessage
                |             A string which instructs the user that he must select a location
                |             into the document window or select an object.
                |         iFilterType
                |             An array of strings constants defining the automation object types
                |             with which the selection will be filtered.
                |         iObjectSelectionBeforeCommandUsePossibility
                |             Enables the script to support the possibility, for the user, to
                |             select a required object before running the script. See
                |
                |
                |         SelectElement2 .
                |     iTooltip
                |         Displays a tooltip as soon as an object is located under the mouse
                |         without being selected.
                |     iTriggeringOnMouseMove
                |         Triggers as soon as a mouse move event is detected. This option beeing
                |         set, oOutputState may be valued to "MouseMove".
                |     oObjectSelected
                |         Flag précising if the user choosed the selection or the indication.
                |
                |     oDocumentWindowLocation
                |         An array made of 2 doubles: X, Y - coordinates array of the location
                |         the user specified in the document window. This parameter is valuated only if
                |         oObjectSelected equals to false.
                |     oOutputState
                |         The state of the interactive command once IndicateOrSelectElement2D
                |         returns. The possible values are the same than the values described regarding
                |         the oOutputState parameter of the SelectElement2 method, except that the
                |         "MouseMove" value can also be returned.
                |     Example:
                |
                |           The following example suppose a drawing is currently edited. It
                |           creates a point (see
                |
                |     Point2D ), and asks the end user to click to define the circle
                |     center.
                |     When it is done, as the mouse moves without clicking the left button, the
                |     script determines the location into the drawing window, and the script creates
                |     a temporary circle as a feedback.
                |     A click into the document window or the selection of a point creates
                |     definitively the circle (see Circle2D ) located at the specified location
                |     (whether the location is a location into the drawing window or whether it is
                |     the existing point location).
                |
                |      Dim Document,Selection,DrawingSheets,DrawingSheet,DrawingViews,WindowLocation(1),DrawingView,
                |          Factory2D,Radius,Circle2D
                |      Dim HardCodedPoint,Status,XCenter,YCenter,InputObjectType(0),TempCircleHasBeenCreatedAtLeastOnce,
                |          ExistingPoint
                |      Dim ObjectSelected
                |      Set Document = CATIA.ActiveDocument : Set Selection = Document.Selection
                |          : Set DrawingSheets  = Document.Sheets
                |      Set DrawingSheet = DrawingSheets.ActiveSheet : Set DrawingViews = DrawingSheet.Views
                |      Set DrawingView = DrawingViews.ActiveView : Set Factory2D = DrawingView.Factory2D
                |     'We create a point
                |      Set HardCodedPoint = Factory2D.CreatePoint(700.,400.)
                |      HardCodedPoint.ReportName = 1 : HardCodedPoint.Construction = False
                |     'We propose to the user to click to define the circle
                |     center
                |      Status=Document.Indicate2D("click to define the circle
                |      center",WindowLocation)
                |      if (Status = "Cancel" Or Status = "Undo" Or Status = "Redo") then Exit Sub
                |      XCenter = WindowLocation(0) : YCenter = WindowLocation(1)
                |     'We propose to the user that he specify a location into the drawing window
                |     or a point
                |      InputObjectType(0)="Point2D"
                |      Status = "MouseMove" : TempCircleHasBeenCreatedAtLeastOnce = 0
                |      Status=Selection.IndicateOrSelectElement2D(
                |           "select a point or click to locate the circle radius point", _
                |           InputObjectType,false,false,true, _ObjectSelected,WindowLocation)
                |     ' We loop onto mouse moves without click
                |      do while (Status = "MouseMove")
                |          if (TempCircleHasBeenCreatedAtLeastOnce) then
                |              Selection.Add Circle2D : Selection.Delete
                |          end if
                |          Radius = Sqr(((WindowLocation(0)-XCenter)*(WindowLocation(0)-XCenter))+ _
                |                      ((WindowLocation(1)-YCenter)*(WindowLocation(1)-YCenter)))
                |          Set Circle2D = Factory2D.CreateClosedCircle(XCenter,YCenter,Radius)
                |          TempCircleHasBeenCreatedAtLeastOnce = 1
                |          Status=Selection.IndicateOrSelectElement2D("select a point or click to
                |          locate the circle radius point", _
                |                                                InputObjectType,false,false,true, _
                |                                              ObjectSelected,WindowLocation)
                |      loop
                |     'We go out if necessary
                |      if (Status = "Cancel" Or Status = "Undo" Or Status = "Redo") then
                |          if (TempCircleHasBeenCreatedAtLeastOnce) then
                |              Selection.Add Circle2D : Selection.Add HardCodedPoint : Selection.Delete
                |          end if
                |          Exit Sub
                |      end if
                |     'We determine the possible selected point coordinates
                |      if (ObjectSelected) then
                |          Set ExistingPoint = Selection.Item2(1).Value : ExistingPoint.GetCoordinates WindowLocation
                |              : Selection.Clear
                |      end if
                |     'We clean-up the temporary circle
                |      if (TempCircleHasBeenCreatedAtLeastOnce) then
                |          Selection.Add Circle2D : Selection.Delete
                |      end if
                |     'We create the circle
                |      Radius = Sqr(((WindowLocation(0)-XCenter)*(WindowLocation(0)-XCenter))+ _
                |          ((WindowLocation(1)-YCenter)*(WindowLocation(1)-YCenter)))
                |      Set Circle2D = Factory2D.CreateClosedCircle(XCenter,YCenter,Radius) : Selection.Add Circle2D

        :param str i_message:
        :param tuple i_filter_type:
        :param bool i_object_selection_before_command_use_possibility:
        :param bool i_tooltip:
        :param bool i_triggering_on_mouse_move:
        :param bool o_object_selected:
        :param tuple o_document_window_location:
        :rtype: str
        """
        vba_function_name = 'indicate_or_select_element_2d_2'
        vba_code = f'''   
                    Public Function {vba_function_name}(selection, i_message, i_filterType, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move)
                    Dim o_object_selected
                    Dim o_document_window_location (1)
                    Dim o_output_state (3)

                    o_output_state (0) = selection.IndicateOrSelectElement2D(i_message, i_filterType, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move, o_object_selected, o_document_window_location)
                    o_output_state (1) = o_object_selected
                    o_output_state (2) = o_document_window_location
                    {vba_function_name} = o_output_state
                    End Function
                    '''

        system_service = self.application.system_service
        result = system_service.evaluate(vba_code,
                                         0,
                                         vba_function_name,
                                         [
                                             self.selection,
                                             i_message,
                                             i_filter_type,
                                             i_object_selection_before_command_use_possibility,
                                             i_tooltip,
                                             i_triggering_on_mouse_move
                                         ]
                                         )

        return result

    def indicate_or_select_element_3d(self,
                                      i_planar_geometric_object: AnyObject,
                                      i_message: str,
                                      i_filter_type: tuple,
                                      i_object_selection_before_command_use_possibility: bool,
                                      i_tooltip: bool,
                                      i_triggering_on_mouse_move: bool) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func IndicateOrSelectElement3D(AnyObject
                | iPlanarGeometricObject,
                | CATBSTR iMessage,
                | CATSafeArrayVariant iFilterType,
                | boolean iObjectSelectionBeforeCommandUsePossibility,
                | boolean iTooltip,
                | boolean iTriggeringOnMouseMove,
                | boolean oObjectSelected,
                | CATSafeArrayVariant oWindowLocation2D,
                | CATSafeArrayVariant oWindowLocation3D) As CATBSTR
                |
                |     Runs an interactive command enabling both indication and selection, 3D
                |     version.
                |     Role: IndicateOrSelectElement3D asks the end user to select either a
                |     location into the window, or a feature (in the geometry or in the specification
                |     tree).
                |     During execution, when entering this method, the active document must be a
                |     3D document. See Document.Indicate3D and SelectElement3
                |
                |     Parameters:
                |
                |         iPlanarGeometricObject
                |             A planar geometric object.
                |         iMessage
                |             A string which instructs the user that he must select a location
                |             into the document window or select an object.
                |         iFilterType
                |             An array of strings constants defining the automation object types
                |             with which the selection will be filtered.
                |         iObjectSelectionBeforeCommandUsePossibility
                |             Enables the script to support the possibility, for the user, to
                |             select a required object before running the script. See
                |
                |
                |         SelectElement2 .
                |     iTooltip
                |         Displays a tooltip as soon as an object is located under the mouse
                |         without being selected.
                |     iTriggeringOnMouseMove
                |         Triggers as soon as a mouse move event is detected. This option being
                |         set, oOutputState may be valued to "MouseMove".
                |     oObjectSelected
                |         Flag precising if the user chose the selection or the indication.
                |
                |     oWindowLocation2D
                |         X, Y - coordinates array of the location the user specified into the
                |         document window. This parameter is valuated only if oObjectSelected equals to
                |         false.
                |     oWindowLocation3D
                |         X, Y, Z - coordinates array of the location the user specified in the
                |         document window. This parameter is valuated only if oObjectSelected equals to
                |         false.
                |     oOutputState
                |         The state of the interactive command once IndicateOrSelectElement3D
                |         returns. The possible values are the same than the values described regarding
                |         the oOutputState parameter of the SelectElement2 method, except that the
                |         "MouseMove" value can also be returned.
                |     Example:
                |
                |           The following example suppose a part is currently edited, containing
                |           a plane. It creates a point
                |          (see
                |
                |     HybridShapePointOnPlane ), asks the end user to select a location into the
                |     part window, onto the Plane.1 plane, or to select a point.
                |     As the mouse moves without clicking the left button, the location into the
                |     drawing window is determined, and the script creates a temporary point as a
                |     feedback.
                |     A click into the document window or the selection of a point creates
                |     definitively the point (see HybridShapePointOnPlane ) located at the specified
                |     location (whether the location is a location into the part window or whether it
                |     is the existing point location).
                |
                |      Dim Document,Part,HybridShapeFactory,Selection,Body,HybridShapePlane,PlaneReference,
                |          HardCodedPoint,Point
                |      Dim InputObjectType(0),WindowLocation2D(1),WindowLocation3D(2),
                |          TempPointHasBeenCreatedAtLeastOnce,Status
                |      Dim ObjectSelected,ExistingPoint
                |      Set Document = CATIA.ActiveDocument : Set Part = Document.Part
                |      Set HybridShapeFactory = Part.HybridShapeFactory : Set Selection = Document.Selection
                |      Set Body = Part.Bodies.Item("PartBody")
                |      Set HybridShapePlane = Body.HybridShapes.Item("Plane.1")
                |      Set PlaneReference = Part.CreateReferenceFromObject(HybridShapePlane)
                |     'We create a point
                |      Set HardCodedPoint = HybridShapeFactory.AddNewPointOnPlane(PlaneReference,30.,30.)
                |      Body.InsertHybridShape HardCodedPoint : Part.InWorkObject = HardCodedPoint : Part.Update
                |     'We propose to the user that he specify a location into the part window or
                |     a point
                |      InputObjectType(0)="HybridShapePointOnPlane"
                |      Status = "MouseMove" : TempPointHasBeenCreatedAtLeastOnce = 0 : Selection.Clear
                |      Status=Selection.IndicateOrSelectElement3D(HybridShapePlane,"select a
                |      point or click to locate the point", _
                |                                                InputObjectType,false,false,true, _
                |                                                ObjectSelected,WindowLocation2D,WindowLocation3D)
                |     ' We loop onto mouse moves without click
                |      do while (Status = "MouseMove")
                |          if (TempPointHasBeenCreatedAtLeastOnce) then
                |              Selection.Add Point : Selection.Delete
                |          end if
                |          Set Point = HybridShapeFactory.AddNewPointOnPlane(PlaneReference,WindowLocation2D(0),
                |              WindowLocation2D(1))
                |          Body.InsertHybridShape Point : Part.InWorkObject = Point : Part.Update
                |          TempPointHasBeenCreatedAtLeastOnce = 1
                |          Status=Selection.IndicateOrSelectElement3D(HybridShapePlane,"select a
                |          point or click to locate the point", _
                |                                                InputObjectType,false,false,true, _
                |              ObjectSelected,WindowLocation2D,WindowLocation3D)
                |      loop
                |     'We go out if necessary
                |      if (Status = "Cancel" Or Status = "Undo" Or Status = "Redo") then
                |          if (TempPointHasBeenCreatedAtLeastOnce) then
                |              Selection.Add Point : Selection.Add HardCodedPoint : Selection.Delete : Part.Update
                |          end if
                |          Exit Sub
                |      end if
                |     'We determine the possible selected point coordinates
                |      if (ObjectSelected) then
                |          Set ExistingPoint = Selection.Item2(1).Value
                |          WindowLocation2D(0) = ExistingPoint.XOffset.Value
                |          WindowLocation2D(1) = ExistingPoint.YOffset.Value
                |          Selection.Clear
                |      end if
                |     'We clean up the temporary point
                |      if (TempPointHasBeenCreatedAtLeastOnce) then
                |          Selection.Add Point : Selection.Delete
                |      end if
                |     'We create the point
                |      Set Point = HybridShapeFactory.AddNewPointOnPlane(PlaneReference,WindowLocation2D(0),
                |          WindowLocation2D(1))
                |      Body.InsertHybridShape Point : Part.InWorkObject = Point : Part.Update

        :param AnyObject i_planar_geometric_object:
        :param str i_message:
        :param tuple i_filter_type:
        :param bool i_object_selection_before_command_use_possibility:
        :param bool i_tooltip:
        :param bool i_triggering_on_mouse_move:
        :rtype: str
        """
        vba_function_name = 'indicate_or_select_element_3d'
        vba_code = f'''   
        Public Function {vba_function_name}(selection, i_planar_geometric_object, i_message, i_filterType, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move)
        Dim o_object_selected
        Dim o_window_location_2d (1)
        Dim o_window_location_3d (2)
        Dim o_output_state (3)
        o_output_state (0) = selection.IndicateOrSelectElement3D(i_planar_geometric_object, i_message, i_filterType, i_object_selection_before_command_use_possibility, i_tooltip, i_triggering_on_mouse_move, o_object_selected, o_window_location_2d, o_window_location_3d)
        o_output_state (1) = o_object_selected
        o_output_state (2) = o_window_location_2d
        o_output_state (3) = o_window_location_3d
        {vba_function_name} = o_output_state
        End Function
        '''

        system_service = self.application.system_service
        result = system_service.evaluate(
            vba_code,
            0,
            vba_function_name,
            [
                self.selection,
                i_planar_geometric_object.com_object,
                i_message, i_filter_type,
                i_object_selection_before_command_use_possibility,
                i_tooltip,
                i_triggering_on_mouse_move

            ]
        )

        return result

    def item(self, i_index: int) -> SelectedElement:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(long iIndex) As SelectedElement
                | 
                |     Deprecated:
                |         V5R16 #Item2 . The Count and Item Methods have been replaced by the
                |         Count2 and Item2 methods because they did not process correctly features which
                |         are not exposed to automation (such as a ResourcesList feature of a .CATProcess
                |         document).

        :param int i_index:
        :rtype: SelectedElement
        """
        return SelectedElement(self.selection.Item(i_index))

    def item2(self, i_index: int) -> SelectedElement:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item2(long iIndex) As SelectedElement
                | 
                |     Returns the iIndex-th SelectedElement object contained by the current
                |     selection.
                |     Role: Returns the iIndex-th SelectedElement object contained by the current
                |     Selection. The Value property of the SelectedElement object is an automation
                |     object associated to a selected feature.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the 
                | 
                |         SelectedElement object to return, 1≤iIndex≤Selection.Count2 .
                |         
                |     oSelectedElement
                |         The SelectedElement object
                |     Example:
                | 
                |           See the 
                | 
                |     SelectElement3 method first example.

        :param int i_index:
        :rtype: SelectedElement
        """
        return SelectedElement(self.selection.Item2(i_index))

    def items(self):
        """
        :return: [self.child_object()]
        """
        items_list = []

        for i in range(self.com_object.Count):
            item = self.child_object(self.com_object.Item(i + 1))
            items_list.append(item)

        return items_list

    def paste(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Paste()
                | 
                |     Puts the contents of the clipboard in the document at the indicated
                |     location.
                |     Role: After the execution of the Paste method, there may be, among the
                |     pasted features, some which are not exposed to automation. If the selected
                |     feature after which the clipboard must be pasted is not exposed to automation,
                |     the Paste will be done all the way.
                |     Note: The method (and the script execution) fails if one of the following
                |     errors occurs:
                |
                |         The CSO is empty. The Paste operation could not be
                |         performed.
                |         No CSO element remains after the filtering through the UI active
                |         object. The Paste operation could not be performed.
                |
                |     Example:
                |         This example pastes, in a cut, or copy, and paste operation. A selected
                |         DMU Navigator URL will be put into the clipboard and removed from the document,
                |         although it is not exposed to automation.
                |
                |          CATIA.ActiveDocument.Selection.Paste()

        :rtype: None
        """
        return self.selection.Paste()

    def paste_special(self, i_format: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Sub PasteSpecial(CATBSTR iFormat)
                |
                |     Puts the contents of the clipboard in the document at the indicated
                |     location, according to the specified format.
                |     Role: After the execution of the Paste method, there may be, among the
                |     pasted features, some which are not exposed to automation. If the selected
                |     feature after which the clipboard must be pasted is not exposed to automation,
                |     the Paste will be done all the way.
                |     Note: The method (and the script execution) fails if one of the following
                |     errors occurs:
                |
                |         The CSO is empty. The PasteSpecial operation could not be
                |         performed.
                |         No CSO element remains after the filtering through the UI active
                |         object. The PasteSpecial operation could not be
                |         performed.
                |
                |
                |     Formats are:
                |
                |         In all the containers
                |         "CATIA_LINK_FORMAT" to paste "Catia Link Source",
                |         "OLE_LINK_FORMAT" to paste "Ole Link Source",
                |         "OLE_EMBED_FORMAT" to paste "Ole Embed Source".
                |
                |
                |         In a Part container
                |         "CATPrtCont" to paste "As Specified In Part Document",
                |         "CATPrtResultWithOutLink" to paste "AsResult",
                |         "CATPrtResult" to paste "AsResultWithLink",
                |         "CATMaterialCont" to paste "As material",
                |         "AsMaterialLink" to paste "As material link",
                |         "CATMechProdCont" to paste "As specified in Assembly",
                |         "CATProdCont" to paste "As specified in Product
                |         Structure",
                |         "CATIA_SPEC" to paste "CATIA_SPEC",
                |         "CATIA_RESULT" to paste "CATIA_RESULT".
                |
                |
                |         In a Product container
                |         "CATProdCont" to paste "As specified in Product
                |         Structure",
                |         "CATSpecBreakLink" to paste "Break Link".
                |
                |
                |         In a Process container
                |         "SPPProcessCont" to paste "Simple paste",
                |         "SPP_I" to paste "Paste with Items",
                |         "SPP_R" to paste "Paste with Resources",
                |         "SPP_IR" to paste "Paste with Items and Resources",
                |         "SPPI_I" to paste "Paste with Items and entire
                |         hierarchy",
                |         "SPPI_R" to paste "Paste with Resources and entire
                |         hierarchy",
                |         "SPPI_IR" to paste "Paste with Items and Resources and entire
                |         hierarchy".
                |
                |
                |         In a Material container
                |         "CATMaterialCont" to paste "As material",
                |         "AsMaterialLink" to paste "As material link".
                |
                |
                |         In a Catalog container
                |         "CATDescriptionFormat" to paste "As defined in catalog
                |         instanciation",
                |         "CATCtlgChapterFormat" to paste "As defined in catalog
                |         document".
                |
                |
                |         In a Rendering Scene container
                |         "CATRscLightContainer" to paste "As light",
                |         "CATRscEnvironmentContainer" to paste "As
                |         environment",
                |         "CATRscShootingContainer" to paste "As shooting",
                |         "CATRscTurntableContainer" to paste "As turntable".
                |
                |
                |         In a Deneb Resource Program container
                |         "DNBProgCont" to paste "Resource Program".
                |
                |
                |         In a Behavior container
                |         "Behaviors" to paste "Behaviors".
                |
                |
                |         In a CATCamera container
                |         "CATCameraContainer" to paste "Camera".
                |
                |
                |     To know more about those formats, refer to the interactive
                |     command.
                |
                |     Example:
                |         This example pastes, in a cut, or copy, and paste special operation. A
                |         selected DMU Navigator URL will be pasted from the clipboard at the specified
                |         location, although it is not exposed to automation.
                |
                |          CATIA.ActiveDocument.Selection.PasteSpecial
                |          "CATPrtResultWithOutLink"

        :param str i_format:
        :return: None
        """
        return self.selection.PasteSpecial(i_format)

    def remove(self, i_index):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Sub Remove(long iIndex)
                |
                |     Deprecated:
                |         V5R16 #Remove2 . This method does the same as the Remove2 method, but
                |         it does know how to manage features which are not exposed to automation (such
                |         as a ResourcesList feature of a .CATProcess document).

        :param int i_index:
        :return: None
        """
        return self.selection.Remove(i_index)

    def remove2(self, i_index):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Sub Remove2(long iIndex)
                |
                |     Removes the iIndex-th SelectedElement object contained by the current
                |     selection.
                |     Role: Removes the iIndex-th SelectedElement object contained by the current
                |     selection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the
                |
                |         SelectedElement object to remove, 1≤iIndex≤Selection.Count2
                |         .
                |
                |         Example:
                |             This example removes the second SelectedElement object contained by
                |             the current selection.
                |
                |              CATIA.ActiveDocument.Selection.Remove2(2)

        :param int i_index:
        :return: None
        """
        return self.selection.Remove2(i_index)

    def search(self, i_string_bstr):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Sub Search(CATBSTR iStringBSTR)
                |
                |     Finds an object in the document using the Edit/Search
                |     grammar.
                |     Role: Finds an object in the document using the Edit/Search grammar, and
                |     fills the selection with the found objects. A criterium is created, based on
                |     the Search grammar, which defines in addition the depth of the investigation
                |     field.
                |     Note: After the execution of the Search method, there may be, among the
                |     selected features, some which are not exposed to
                |     automation.
                |
                |     Example:
                |         The following example searches the objects matching the following
                |         criterium in all the document: Part.Sketcher.Color='White' . A selected DMU
                |         Navigator URL put into the selection although it is not exposed to
                |         automation.
                |
                |         CATIA.ActiveDocument.Selection.Search("Part.Sketcher.Color='White',all")

        :param str i_string_bstr:
        :rtype: None
        """
        try:
            return self.selection.Search(i_string_bstr)
        except com_error:
            raise CATIAApplicationException(
                f'The method Search failed with search string "{i_string_bstr}". Try changing your search string.')

    def select_element2(self,
                        i_filter_type: tuple,
                        i_message: str,
                        i_object_selection_before_command_use_possibility: bool) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Func SelectElement2(CATSafeArrayVariant iFilterType,
                | CATBSTR iMessage,
                | boolean iObjectSelectionBeforeCommandUsePossibility) As
                | CATBSTR
                |
                |     Runs an interactive selection command.
                |     Role: SelectElement2 asks the end user to select a feature (in the geometry
                |     or in the specification tree) in a Window of the active Document . During the
                |     selection, when the end user will move the mouse above a feature which maps the
                |     given filter, the mouse pointer will be the "hand" cursor, and when end user
                |     will move the mouse above a feature which does not map the given filter, the
                |     mouse pointer will be the "no entry" cursor.
                |
                |         If iObjectSelectionBeforeCommandUsePossibility is equal to
                |         False:
                |         The end user is asked to interactively select an appropriate element.
                |         When this is done, the Selection object is cleared, and filled with the
                |         selected element.
                |
                |         If iObjectSelectionBeforeCommandUsePossibility is equal to
                |         True:
                |         SelectElement2 determines whether the automation objects specified in
                |         SelectedElement.Value, for the SelectedElement objects contained in the current
                |         selection, or one of the parents of the automation objects (see
                |         AnyObject.Parent ) is an appropriate element:
                |             If it is the case, no interaction is asked to the end user, the
                |             Selection object is cleared, and filled with the appropriate
                |             element.
                |             Otherwise, the Selection object is cleared, and the end user is
                |             asked to interactively select an appropriate element. When this is done, the
                |             selection is filled with the selected element.
                |         Note: The Selection object on which the Selection.SelectElement2 method
                |         must be called must be the Selection object obtained the following
                |         way:
                |             determine the active document, for example, in the following
                |             case:
                |
                |                 Product3
                |                    !
                |                    +- Product2 (Product2.1)
                |                    !     !
                |                    !     ! +---------------------+
                |                    !     +-!Product1 (Product1.1)!
                |                    !       +----------+----------+
                |                    !                  !
                |                    !                  +- Part1 (Part1.1)
                |
                |                    !                       !
                |                    !                       +- Part1
                |                    !                            !
                |                    !                            +- PartBody
                |                    !                                  !
                |                    +------------------+
                |                    !                                  +- Pad.1               !
                |                    Selected feature !
                |                    !                                       !
                |                    +------------------+
                |                    !                                       +- Sketch.1
                |
                |                    +- Part2 (Part2.1)
                |
                |
                |             it will be Product3
                |             call the Document.Selection property onto this
                |             document
                |         Otherwise, results are unpredictable. Note: During the selection scan
                |         to find an automation object, a "Product" string constant specified in
                |         iFilterType will imply that SelectElement2 will also look at the possible
                |         automation object specified in SelectedElement.LeafProduct
                |         .
                |
                |     After a call to SelectElement2, if the return value equals to "Normal", a
                |     call to the Count2 method will return one, and a call to Item2(1) will return
                |     the selected element.
                |
                |     Note: If the scripting language is Visual Basic for Applications or Visual
                |     Basic 6 Development Studio, then, you have to know that the use of an
                |     interactive selection method such as this one from a form (dialog box) method
                |     requires some constraints regarding the content of an average form
                |     method.
                |     If your macro possess a form method which calls the SelectElement2 method,
                |     then, the content of an average form method of your macro must begin by a test,
                |     which checks that no form method is currently being executed and, otherwise, go
                |     out of the method. This constraint enable to prevent that, during the execution
                |     of the SelectElement2 method from a form method, when CATIA asks the end user
                |     to select a feature:
                |
                |         the users select a dialog object of a form (CATIA going on asking the
                |         end user to select a feature)
                |         this selection trigger the corresponding form method
                |         this run CATIA automation objects methods, CATIA going on asking the
                |         end user to select a feature
                |
                |     which would lead to unpredictable results.
                |     The code will be the following way:
                |
                |       - macro module main variables:
                |         Dim AFormMethodIsBeingExecuted As Boolean
                |       - form method calling SelectElement2:
                |         Private Sub
                |         FormPossessingOneMethodCallingSelectElement2_Click()
                |             Dim InputObjectType(0), Status
                |             AFormMethodIsBeingExecuted = True
                |             InputObjectType(0)="TriDimFeatEdge"
                |             Status=Selection.SelectElement2(InputObjectType,"Select an
                |             edge",false)
                |             AFormMethodIsBeingExecuted = False
                |         End Sub
                |       - average form method:
                |         Private Sub AverageForm_Click()
                |             If (AFormMethodIsBeingExecuted) Then Exit Sub
                |                . . .
                |          '     content of the form method itself
                |                . . .
                |         End Sub
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of strings constants defining the automation object types
                |             with which the selection will be filtered. During the selection, when the end
                |             user will move the mouse (above the geometry or the specification tree), if the
                |             feature under the mouse does not map iFilterType, the cursor will be the "no
                |             entry" cursor.
                |             The resulting filter is a logical OR of the supplied strings
                |             constants. For instance if the array contains two elements "Point" and "Line",
                |             when the end user will move the mouse above the geometry, if there is a feature
                |             under a mouse, which is a
                |
                |         HybridShapePointCoord object (you have to know that the Point object is
                |         a parent object of the HybridShapePointCoord object ), then, the cursor will be
                |         a "hand" cursor. At the opposite, if there is a feature under a mouse, which is
                |         neither a Point nor a Line, the cursor will be a "no entry"
                |         cursor.
                |
                |         Beside the automation object names, the CATSelectionFilter value names
                |         are supported.
                |     iMessage
                |         A string which instructs the user what to select. This string is
                |         displayed in the message area located at the left of the power input area.
                |
                |     iObjectSelectionBeforeCommandUsePossibility
                |         Enables the script to support the possibility, for the user, to select
                |         a required object before running the script.
                |
                |         If the scripter:
                |
                |             writes a script calling SelectElement2, giving as iFilterType
                |             parameter an array containing one string: "Pad"
                |             for the first call to SelectElement2 made by the script, the
                |             iObjectSelectionBeforeCommandUsePossibility is set to
                |             True
                |             the scripter associates the script to an Icon. He will proceed as
                |             following:
                |                 in the Tools menu, select the Customize item. A window
                |                 appears.
                |                 select the Commands Tab. The window contains two
                |                 lists.
                |                 in the list on the left, select the Macros
                |                 value
                |                 select the "Show Properties" push button
                |                 select the button on the right of the Icon label. A window
                |                 containing a list of icons appears
                |                 select an Icon
                |                 select the Close button. The window containing the icon list
                |                 disappears
                |                 in the list on the right, push the key 1 of the mouse, the
                |                 cursor beeing on the macro to associate to an Icon. Then drag to a desired
                |                 Toolbar. The Icon has been added to the
                |                 Toolbar.
                |
                |
                |         Then the user will be able to implement the following
                |         scenario:
                |
                |             select a Pad
                |             select the Icon mentioned above. This runs the
                |             script.
                |
                |
                |         During the execution of the script, the script will detect that the
                |         selected Pad is required as input, and the first call to SelectElement2 will
                |         not ask to the user to interactively select a Pad: the Pad selected before the
                |         script execution will be taken.
                |         Note:Regarding the features selected by the user (a Pad in the example
                |         above), all the automation objects specified in SelectedElement.Value for the
                |         current selection SelectedElement objects must be used: if an automation object
                |         specified in SelectedElement.Value is not asked by the input filter, the
                |         SelectElement2 method will ask the user to interactively select an appropriate
                |         element.
                |
                |     A False value for the iObjectSelectionBeforeCommandUsePossibility parameter
                |     may be used although the selection is not empty before entering the method.
                |     This enables that, during the selection, the selected elements remain
                |     highlighted.
                |     Caution: After a call to SelectElement2 , the
                |     iObjectSelectionBeforeCommandUsePossibility parameter being set to False, the
                |     elements which were selected before the call to SelectElement2 are not any more
                |     in the selection (unless the user selected one of them!). Consequently, such a
                |     use of the False value for the iObjectSelectionBeforeCommandUsePossibility
                |     parameter requires the following code:
                |
                |         save the selection content in save variables
                |         call the SelectElement2 method, the
                |         iObjectSelectionBeforeCommandUsePossibility parameter being set to
                |         False
                |         copy the selected element to a dedicated variable
                |         merge the selected element with the save variables, and put the result
                |         in the selection. This mean:
                |             if the selected element does not belong to the save variables, add
                |             the save variables to the selection
                |             otherwise, remove the selected element from the save variables,
                |             clear the selection and then, add the save variables to the
                |             selection
                |
                |     oOutputState
                |         The state of the selection command once SelectElement2 returns. It can
                |         be either "Normal" (the selection has succeeded), "Cancel" (the user wants to
                |         cancel the VB command, which must exit immediately), "Undo" or
                |         "Redo".
                |         Note:The "Cancel" value is returned if one of the following cases
                |         occured:
                |
                |             an external command has been selected
                |             the ESCAPE key has been selected
                |             another window has been selected, the window document beeing
                |             another document than the current document
                |
                |         Caution:All scripts should exit (after the necessary cleanings) when
                |         the "Cancel" value is returned.
                |         If the script does not exit (beside the cleanings) when the "Cancel"
                |         value is returned, but calls another interactive method such as SelectElement2
                |         , and, during execution, the user select an external command (which triggers
                |         the return of the "Cancel" value), then, the execution of the other interactive
                |         method will display an error message.
                |     Example:
                |
                |           The following example asks the end user to select a sketch (see
                |
                |
                |     Sketch ) in the current window, and creates a Pad (see
                |     ShapeFactory.AddNewPad ). If, before the script execution, a sketch was already
                |     selected, it will be taken into account and the end user will ne be asked to
                |     select a sketch.
                |     Then, it asks the end user to select an edge of the pad, and creates an
                |     edge fillet. Then, is asks the end user to select a 1-D entity whose geometry
                |     is rectilinear (see CATSelectionFilter ), such as an edge of the
                |     Pad.
                |     Then, it asks the end user to select a pad face perpendicular to the 1-D
                |     entity previously selected. Then, it creates a hole at the face selected point,
                |     the hole direction being the direction of the 1-D selected
                |     entity.
                |     During the face selection, the 1-D entity previously selected is
                |     highlighted.
                |
                |      Dim Document,Part,Selection,ShapeFactory,SketchHasBeenAcquiredAtLeastOnce,
                |          EdgeHasBeenAcquiredAtLeastOnce
                |      Dim FaceHasBeenAcquiredAtLeastOnce,MonoDimEntityHasBeenAcquiredAtLeastOnce,
                |          FirstExtrudeNotFinished,FilletEdge
                |      Dim PadNotFinished,Status,SketchForPad,Pad,FilletNotFinished,Fillet,
                |          MonoDimEntityDeterminationNotFinished
                |      Dim SelectedElement,MonoDimEntity,HoleNotFinished,PadFace,Hole,InputObjectType(0),
                |          HoleLocation(2),MonoDimEntitySave
                |      Dim SketchForPadPartBody
                |      Set Document = CATIA.ActiveDocument : Set Part = Document.Part
                |      Set Selection = Document.Selection
                |      Set ShapeFactory = Part.ShapeFactory
                |      SketchHasBeenAcquiredAtLeastOnce = False : EdgeHasBeenAcquiredAtLeastOnce = False
                |      FaceHasBeenAcquiredAtLeastOnce = False : MonoDimEntityHasBeenAcquiredAtLeastOnce = False
                |      FirstExtrudeNotFinished = True : PadNotFinished = True : ReDim SelectionAtBeginning(1)
                |     'We save the current selection content
                |      ReDim SelectionAtBeginning(Selection.Count2)
                |      for SelectionObjectIndex = 0 to Selection.Count2-1
                |          Set SelectionAtBeginning(SelectionObjectIndex) = Selection.Item2(1).Value
                |      next
                |      SelectionAtBeginningLength = Selection.Count2
                |     'Feature creation
                |      do while PadNotFinished
                |     '  We propose to the user that he select a sketch
                |          InputObjectType(0)="Sketch"
                |          Status=Selection.SelectElement2(InputObjectType,"Select a
                |          sketch",true)
                |          if ((Status = "Cancel") Or (Status = "Undo")) then
                |     '      We restore the selection to its initial content
                |              Selection.Clear
                |              for SelectionObjectIndex = 0 to SelectionAtBeginningLength-1
                |                  Selection.Add
                |                  SelectionAtBeginning(SelectionObjectIndex)
                |              next
                |              Exit Sub
                |          elseif (Status = "Redo" And Not SketchHasBeenAcquiredAtLeastOnce ) then
                |     '      We do nothing: Redo has no meaning in this context
                |          else
                |              if (Status <> "Redo") then Set SketchForPad = Selection.Item2(1).Value
                |              SketchHasBeenAcquiredAtLeastOnce = True
                |     '      We determine the PartBody corresponding to the
                |     Sketch
                |              Set SketchForPadPartBody = SketchForPad.Parent.Parent
                |     '      We create the Pad
                |              Set Pad = ShapeFactory.AddNewPad(SketchForPad,20.0)
                |              Pad.SecondLimit.Dimension.Value = 0.0 : Part.Update
                |              PadNotFinished = False
                |              Selection.Clear
                |     '      We create the fillet and the hole
                |              FilletNotFinished = True
                |              do while (FilletNotFinished And Not
                |              PadNotFinished)
                |     '          We propose to the user that he select an edge
                |                  InputObjectType(0)="TriDimFeatEdge"
                |                  Status=Selection.SelectElement2(InputObjectType,"Select an
                |                  edge of the Pad",false)
                |                  if (Status = "Cancel") then
                |     '              We remove the pad, restore the selection to its initial
                |     content and go out
                |                      Selection.Clear : Selection.Add(Pad) : Selection.Delete
                |                      Part.Update
                |                      Selection.Clear
                |                      for SelectionObjectIndex = 0 to SelectionAtBeginningLength-1
                |                          Selection.Add SelectionAtBeginning(SelectionObjectIndex)
                |                      next
                |                      Exit Sub
                |                  elseif (Status = "Redo" And Not EdgeHasBeenAcquiredAtLeastOnce ) then
                |     '              We do nothing: Redo has no meaning in this
                |     context
                |                  elseif (Status = "Undo") then
                |     '              We copy the sketch to the clipboard
                |                      Selection.Clear : Selection.Add(SketchForPad)
                |     '              We remove the pad
                |                      Selection.Clear : Selection.Add(Pad) : Selection.Delete : Part.Update
                |     '              We re-create the sketch
                |                      Selection.Clear : Selection.Add(SketchForPadPartBody) : Selection.Paste()
                |     '              We store the fact that the Pad is not finished
                |                      PadNotFinished = True
                |                  else
                |                      if (Status <> "Redo") then Set FilletEdge = Selection.Item2(1).Value
                |                      EdgeHasBeenAcquiredAtLeastOnce = True
                |     '              Create the Fillet
                |                      Set Fillet = ShapeFactory.AddNewSolidEdgeFilletWithConstantRadius(FilletEdge,
                |                          catTangencyFilletEdgePropagation,5.0)
                |                      Part.Update
                |                      FilletNotFinished = False
                |                      Selection.Clear
                |     '              Determine the 1-D entity
                |                      MonoDimEntityDeterminationNotFinished = True
                |                      do while (MonoDimEntityDeterminationNotFinished And Not
                |                      FilletNotFinished)
                |     '                  We propose to the user that he select 1-D entity whose
                |     geometry is rectilinear
                |                          InputObjectType(0)="RectilinearMonoDim"
                |
                |                          Status=Selection.SelectElement2(InputObjectType, _
                |
                |                                                          "Select a 1-D entity
                |                                                          whose geometry is rectilinear",false)
                |
                |                          if (Status = "Cancel") then
                |     '                      We remove the fillet, the pad, restore the selection
                |     to its initial content and go out
                |                              Selection.Clear : Selection.Add(Fillet) : Selection.Delete
                |                              Selection.Clear : Selection.Add(Pad) : Selection.Delete
                |                              Part.Update
                |                              Selection.Clear
                |                              for SelectionObjectIndex = 0 to SelectionAtBeginningLength-1
                |                                  Selection.Add SelectionAtBeginning(SelectionObjectIndex)
                |                              next
                |                              Exit Sub
                |                          elseif (Status = "Redo" And Not MonoDimEntityHasBeenAcquiredAtLeastOnce )
                |                          then
                |     '                      We do nothing: Redo has no meaning in this context
                |                          elseif (Status = "Undo") then
                |     '                      We remove the fillet
                |                              Selection.Clear : Selection.Add(Fillet) : Selection.Delete
                |                              Part.Update
                |                              FilletNotFinished = True
                |                          else
                |                              if (Status = "Redo") then
                |                                Selection.Clear : Selection.Add(MonoDimEntity)
                |                              else
                |                                Set SelectedElement = Selection.Item2(1)
                |                                Set MonoDimEntity = SelectedElement.Value
                |                              end if
                |                              MonoDimEntityHasBeenAcquiredAtLeastOnce = True
                |                              MonoDimEntityDeterminationNotFinished = False
                |     '                      Create the Hole
                |                              HoleNotFinished = True
                |                              do while (HoleNotFinished And Not MonoDimEntityDeterminationNotFinished)
                |     '                          We save the selection content in save
                |     variables.
                |     '                          This corresponds to the fact
                |     that:
                |     '                            - we want that, during the following call to
                |     SelectElement2, the 1-D entity previously
                |     '                              selected remain highlighted
                |     '                            - this is done using the False value for the
                |     iObjectSelectionBeforeCommandUsePossibility
                |     '                              parameter, the selection containing the 1-D
                |     entity. It requires that the selection
                |     '                              content be saved
                |                                Set MonoDimEntitySave = Selection.Item2(1).Value
                |     '                          We propose to the user that he select a
                |     face
                |                                  InputObjectType(0)="Face"
                |
                |                                 Status=Selection.SelectElement2(InputObjectType, _
                |
                |                                                                "Select a face
                |                                                                perpendicular to the 1-D entity",false)
                |                                  if (Status = "Cancel") then
                |     '                              We remove the fillet, the pad, restore the
                |     selection to its initial content and go out
                |                                      Selection.Clear : Selection.Add(Fillet) : Selection.Delete
                |                                      Selection.Clear : Selection.Add(Pad) : Selection.Delete
                |                                      Selection.Clear
                |                                      for SelectionObjectIndex = 0 to SelectionAtBeginningLength-1
                |                                          Selection.Add SelectionAtBeginning(SelectionObjectIndex)
                |                                      next
                |                                      Part.Update
                |                                      Exit Sub
                |                                  elseif (Status = "Redo" And Not FaceHasBeenAcquiredAtLeastOnce ) then
                |     '                              We do nothing: Redo has no meaning in this context
                |                                  elseif (Status = "Undo") then
                |                                    Selection.Clear
                |     '                              The 1-D entity must be
                |     re-selected
                |                                      MonoDimEntityDeterminationNotFinished = True
                |                                  else
                |                                      if (Status <> "Redo") then
                |
                |                                          Set SelectedElement = Selection.Item2(1)
                |                                          Set PadFace = SelectedElement.Value
                |                                          SelectedElement.GetCoordinates
                |                                          HoleLocation
                |     '                                  We merge the selected element with the
                |     save variables, and put the result in the selection
                |                                          Selection.Add
                |                                          MonoDimEntitySave
                |                                      end if
                |                                      FaceHasBeenAcquiredAtLeastOnce = True
                |     '                              We create the Hole
                |                                      Set Hole = Part.ShapeFactory.AddNewHoleFromPoint(HoleLocation(0),
                |                                          HoleLocation(1),HoleLocation(2),PadFace,10.0)
                |                                      Hole.ThreadingMode = 1 : Hole.ThreadSide = 0 :
                |                                      Hole.Diameter.Value = 5.0
                |                                      Hole.SetDirection
                |                                      FilletEdge
                |                                      Part.Update
                |                                      HoleNotFinished = False
                |     '                              We clear the selection
                |                                      Selection.Clear
                |                                  end if
                |                              loop
                |                          end if
                |                      loop
                |                  end if
                |              loop
                |          end if
                |      loop

        :param tuple i_filter_type:
        :param str i_message:
        :param bool i_object_selection_before_command_use_possibility:
        :rtype: str
        """

        check_type(i_filter_type, tuple)

        return self.selection.SelectElement2(i_filter_type,
                                             i_message,
                                             i_object_selection_before_command_use_possibility)

    def select_element3(self,
                        i_filter_type: tuple,
                        i_message: str,
                        i_object_selection_before_command_use_possibility: bool,
                        i_multi_selection_mode: int,
                        i_tooltip: bool) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Func SelectElement3(CATSafeArrayVariant iFilterType,
                | CATBSTR iMessage,
                | boolean iObjectSelectionBeforeCommandUsePossibility,
                | CATMultiSelectionMode iMultiSelectionMode,
                | boolean iTooltip) As CATBSTR
                |
                |     Runs an interactive selection command, exhaustive version.
                |     Role: SelectElement3 asks the end user to select a feature (in the geometry
                |     or in the specification tree). It is identical to the SelectElement2 method
                |     except that it manages complex uses through the specification of 2 more
                |     parameters.
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of strings constants defining the automation object types
                |             with which the selection will be filtered.
                |         iMessage
                |             A string which instructs the user what to select. This string is
                |             displayed in the message area located at the left of the power input area.
                |
                |         iObjectSelectionBeforeCommandUsePossibility
                |             Enables the script to support the possibility, for the user, to
                |             select required object(s) before running the script. See
                |
                |
                |         SelectElement2 .
                |     iMultiSelectionMode
                |         The type of multi-selection which will be offered to the user.
                |
                |     iTooltip
                |         Displays a tooltip as soon as an object is located under the mouse
                |         without being selected.
                |     oOutputState
                |         The state of the selection command once SelectElement3 returns. It can
                |         be either "Normal", "Cancel", "Undo" or "Redo". See SelectElement2
                |         .
                |     Example:
                |
                |           This first example asks the end user to select several points (see
                |
                |
                |     Point ) into the current Part window, drawing a trap, and performs a
                |     symmetry with respect to the XZ plane on the selected points (see
                |     HybridShapeSymmetry ). The points can be selected before the script be
                |     run.
                |
                |      Dim Document,Part,Selection,HybridShapeFactory,HybridBodies,HybridBody,OriginElements,Plane,
                |          PlaneReference,Status
                |      Dim InputObjectType(0),PointIndex,PointReference,HybridShapeSymmetry
                |      Set Document = CATIA.ActiveDocument : Set Part = Document.Part :
                |      Set Selection = Document.Selection
                |      Set HybridShapeFactory = Part.HybridShapeFactory
                |      Set Bodies = Part.Bodies
                |      Set Body = Bodies.Item("PartBody")
                |      Set OriginElements = Part.OriginElements
                |      Set Plane = OriginElements.PlaneZX
                |      Set PlaneReference = Part.CreateReferenceFromObject(Plane)
                |     'We propose to the user that he select several points, drawing a
                |     trap
                |      InputObjectType(0)="Point"
                |      Status=Selection.SelectElement3(InputObjectType,"Select points",
                |      _
                |      true,CATMultiSelTriggWhenSelPerf,false)
                |      if (Status = "Cancel") then Exit Sub
                |      For PointIndex = 1 to Selection.Count2
                |          Set PointReference = Part.CreateReferenceFromObject(Selection.Item2(PointIndex).Value)
                |          Set HybridShapeSymmetry = HybridShapeFactory.AddNewSymmetry(PointReference,PlaneReference)
                |          HybridShapeSymmetry.VolumeResult = False
                |          Body.InsertHybridShape HybridShapeSymmetry
                |          Part.InWorkObject = HybridShapeSymmetry
                |          Part.Update
                |      next
                |      Selection.Clear
                |
                |
                |     Example:
                |
                |           This second example illustrates the use of the
                |           CATMultiSelTriggWhenUserValidatesSelection value for the
                |
                |          iMultiSelectionMode parameter. This example is a training tool
                |          enabling the user to learn how to use the "Symmetry"
                |          command of the "Geometry Modification" toolbar of the Drafting
                |          workbench.
                |
                |          It creates a drawing containing a line and three points, and guides
                |          the user in:
                |
                |             the selection of points
                |             the selection of the symmetry axis
                |
                |          the selected points being moved by symmetry according to the selected
                |          axis.
                |
                |         'We create a drawing
                |          Set Documents = CATIA.Documents : Set Document = Documents.Add("Drawing")
                |              : Document.Standard = catISO
                |          Set DrawingSheets = Document.Sheets : Set DrawingSheet = DrawingSheets.Item("Sheet.1")
                |          DrawingSheet.PaperSize = catPaperA0 : DrawingSheet.Scale = 1.000000
                |              : DrawingSheet.Orientation = catPaperLandscape
                |          Set DrawingViews = DrawingSheet.Views : Set DrawingView = DrawingViews.ActiveView
                |          Set Factory2D = DrawingView.Factory2D : Set Selection = Document.Selection
                |              : Dim Coordinates(2)
                |          ReDim InputObjectType(0) : Dim SelectedPoint(3) : SelectedPointCount = 0
                |         'We create a horizontal line with a zero ordinate
                |          Set LineLeftExtremity = Factory2D.CreatePoint(-100.0, 0.0)
                |              : LineLeftExtremity.ReportName = 3
                |          Set LineRightExtremity = Factory2D.CreatePoint(100.0, 0.0)
                |              : LineRightExtremity.ReportName = 4
                |          Set Line2D = Factory2D.CreateLine(-100.0, 0.0, 100.0, 0.0) : Line2D.ReportName = 5
                |          Line2D.StartPoint = LineLeftExtremity : Line2D.EndPoint = LineRightExtremity
                |         'We create three points
                |          Set Point2D1 = Factory2D.CreatePoint(-50.0, 50.0)
                |              : Point2D1.ReportName = 6 : Point2D1.Construction = False
                |          Set Point2D2 = Factory2D.CreatePoint(0.0, 70.0) : Point2D2.ReportName = 7
                |              : Point2D1.Construction = False
                |          Set Point2D3 = Factory2D.CreatePoint(50.0, 50.0) : Point2D3.ReportName = 8
                |              : Point2D3.Construction = False
                |         'We mention to the user that he will select the set of elements to be
                |         symmetrized
                |          msgbox "This tool will enable you to learn how to use the Symmetry
                |          command." & Chr(13) & Chr(13) & _
                |                 "Suppose you selected the Symmetry command." & Chr(13) & _
                |
                |                 "You will first select several points to be
                |                 symmetrized"
                |         'We propose to the user that he select several points
                |          InputObjectType(0)="Point2D"
                |          Status=Selection.SelectElement3(InputObjectType,"Select the set of
                |          elements to be symmetrized", _true,CATMultiSelTriggWhenUserValidatesSelection,false)
                |          if (Status = "Cancel") then Exit Sub
                |         'We add the selected points to SelectedPoint
                |          for PointIndex = 0 to Selection.Count2-1
                |              Set SelectedPoint(PointIndex) = Selection.Item2(PointIndex+1).Value
                |                  : SelectedPointCount = SelectedPointCount+1
                |          next
                |         'We mention to the user that he will select the axis from which the
                |         elements will remain equidistant
                |          msgbox "You will then select the line from which the elements will
                |          remain equidistant"
                |         'We propose to the user that he select the line
                |          InputObjectType(0)="Line2D"
                |          Status=Selection.SelectElement2(InputObjectType, _
                |                                          "Select the line or axis from which
                |                                          the elements will remain equidistant",
                |                                          false)
                |          if (Status = "Cancel") then Exit Sub
                |         'We move the selected points by symmetry according to the selected
                |         line
                |          for PointIndex = 0 to SelectedPointCount-1
                |              Set CurrentPoint2D = SelectedPoint(PointIndex)
                |              CurrentPoint2D.GetCoordinates Coordinates
                |              CurrentPoint2D.SetData Coordinates(0),
                |              -Coordinates(1)
                |          next
                |          Selection.Clear
                |         'We mention to the user that the points have successfully been
                |         moved
                |          msgbox "The points have successfully been moved."

        :param tuple i_filter_type:
        :param str i_message:
        :param bool i_object_selection_before_command_use_possibility:
        :param int i_multi_selection_mode: enum cat_multi_selection_mode
        :param bool i_tooltip:
        :rtype: str
        """

        check_type(i_filter_type, tuple)

        return self.selection.SelectElement3(i_filter_type,
                                             i_message,
                                             i_object_selection_before_command_use_possibility,
                                             i_multi_selection_mode,
                                             i_tooltip)

    def select_element4(self,
                        i_filter_type: tuple,
                        i_active_document_message: str,
                        i_non_active_document_message: str,
                        i_tooltip: bool,
                        o_document: Document) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-03 17:02:05.216737))
                | o Func SelectElement4(CATSafeArrayVariant iFilterType,
                | CATBSTR iActiveDocumentMessage,
                | CATBSTR iNonActiveDocumentMessage,
                | boolean iTooltip,
                | Document oDocument) As CATBSTR
                |
                |     Runs an interactive selection command, enabling the selection in a non
                |     active document.
                |     Role: SelectElement4 asks the end user to select a feature (in the geometry
                |     or in the specification tree) of a non active document. During the selection,
                |     when end user will move the mouse above a window corresponding to a non active
                |     document, when he will move the mouse above a feature which maps the given
                |     filter, the mouse pointer will be the "hand" cursor. When he will move the
                |     mouse above a feature which does not map the given filter, the mouse pointer
                |     will be the "no entry" cursor.
                |     This method may be used, for example, to write a script which does the
                |     following:
                |
                |         a drawing is currently edited
                |         request that the user select a reference plane in the 3D geometry (a
                |         part)
                |         creation of a front view in the drawing, projecting the 3D geometry
                |         onto the selected reference plane
                |
                |
                |     Compared to the SelectElement2 , the result of the selection will not be
                |     accessed through the Count2 and Item2 methods of the current selection object,
                |     but through the Count2 and Item2 methods of the Selection object aggregated by
                |     the Document object returned through the oDocument
                |     parameter.
                |     Note:The Selection object aggregated by the Document object returned
                |     through the oDocument parameter is emptied by before the effective interactive
                |     selection.
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of strings constants defining the automation object types
                |             with which the selection will be filtered.
                |         iActiveDocumentMessage
                |             A string which instructs the user what to select, which will be
                |             displayed into the active document. This string is displayed in the message
                |             area located at the left of the power input area.
                |         iNonActiveDocumentMessage
                |             A string which instructs the user what to select, which will be
                |             displayed into the non active document.
                |         iTooltip
                |             Displays a tooltip as soon as an object is located under the mouse
                |             without being selected.
                |         oOutputState
                |             The state of the selection command once SelectElement3 returns. It
                |             can be either "Normal", "Cancel", "Undo".
                |
                |     Example:
                |
                |           The following example supposes a part, containing a pad, and drawing
                |           are currently edited, the drawing
                |          window beeing the current window. It asks the end user to select a 2-D
                |          topological entity, such as a
                |
                |
                |     Plane , in a part. Then it creates a front view in the drawing, projecting
                |     the 3D geometry onto the selected 2-D topological entity.
                |
                |      Dim DrawingSelection,DrawingSheets,DrawingSheet,DrawingViews,DrawingFrontView
                |      ReDim DrawingSelectionAtBeginning(1)
                |      Dim Status,InputObjectType(0),Plane,Drawing,DrawingViewGenerativeBehavior,V1(2),V2(2),
                |          PartDocument
                |      Set Drawing = CATIA.ActiveDocument : Set DrawingSelection = Drawing.Selection
                |          : Set DrawingSheets  = Drawing.Sheets
                |      Set DrawingSheet = DrawingSheets.ActiveSheet
                |     'We save the current selection content
                |      ReDim
                |      DrawingSelectionAtBeginning(DrawingSelection.Count2)
                |      for SelectionObjectIndex = 0 to DrawingSelection.Count2-1
                |          Set DrawingSelectionAtBeginning(SelectionObjectIndex) = DrawingSelection.Item2(1).Value
                |      next
                |      SelectionAtBeginningLength = DrawingSelection.Count2
                |     'Feature creation
                |      InputObjectType(0)="BiDimInfinite"
                |      Status=DrawingSelection.SelectElement4(InputObjectType,"Select a 2-D
                |      topological entity in a 3-D geometry", _"Select a 2-D topologicalentity",false,PartDocument)
                |      if ((Status = "Cancel") Or (Status = "Undo") Or (Status = "Redo")) then
                |     '  We restore the selection to its initial content
                |          PartDocument.Selection.Clear
                |          for SelectionObjectIndex = 0 to SelectionAtBeginningLength-1
                |              DrawingSelection.Add
                |              DrawingSelectionAtBeginning(SelectionObjectIndex)
                |          next
                |          Exit Sub
                |      else
                |          Set BiDimFeature = PartDocument.Selection.Item2(1).Value
                |          BiDimFeatureType = TypeName(BiDimFeature)
                |          if ((BiDimFeatureType="Plane") Or (BiDimFeatureType="PlanarFace"))
                |          then
                |            BiDimFeature.GetFirstAxis V1
                |            BiDimFeature.GetSecondAxis V2
                |          else
                |            Exit Sub
                |          end if
                |     '  We create a view called "Front View" in the current sheet, using Plane
                |     as projection plane, and whose origin
                |     '  coordinates are 300,150
                |          Set DrawingFrontView = DrawingSheet.Views.Add("Front View")
                |          Set DrawingViewGenerativeBehavior = DrawingFrontView.GenerativeBehavior
                |          DrawingViewGenerativeBehavior.Document = PartDocument
                |          DrawingViewGenerativeBehavior.DefineFrontView V1(0), V1(1), V1(2),
                |          V2(0), V2(1), V2(2)
                |          DrawingFrontView.x = 300
                |          DrawingFrontView.y = 150
                |          DrawingViewGenerativeBehavior.Update
                |     '  We clear the PartDocument Selection object
                |          PartDocument.Selection.Clear
                |      end if

        :param tuple i_filter_type:
        :param str i_active_document_message:
        :param str i_non_active_document_message:
        :param bool i_tooltip:
        :param Document o_document:
        :rtype: str
        """

        check_type(i_filter_type, tuple)
        check_type(o_document, Document)

        return self.selection.SelectElement4(i_filter_type,
                                             i_active_document_message,
                                             i_non_active_document_message,
                                             i_tooltip,
                                             o_document.com_object)

    def __len__(self):

        return self.count

    def __getitem__(self, n: int) -> SelectedElement:
        if (n + 1) > self.count:
            raise StopIteration

        return SelectedElement(self.selection.Item(n + 1))

    def __iter__(self) -> Iterator[SelectedElement]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Selection(name="{self.name}")'
