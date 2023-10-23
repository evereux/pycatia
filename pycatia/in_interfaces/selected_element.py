#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject


class SelectedElement(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SelectedElement
                | 
                | Represents an element contained by a Selection object.
                | This object is an object contained by a Selection object. The Selection object
                | contains SelectedElement objects, which are accessed through the
                | Selection.Count2 and Selection.Item2 methods.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.selected_element = com_object

    @property
    def document(self) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Document() As Document (Read Only)
                | 
                |     Returns the document to which the selected element belongs.

        :rtype: Document
        """

        return Document(self.selected_element.Document)

    @property
    def leaf_product(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LeafProduct() As AnyObject (Read Only)
                | 
                |     Returns the leaf product corresponding to the selection in the
                |     specification tree.
                |     Role: Returns the leaf Product (component, corresponding for example to
                |     "Product1.1" in the specification tree). The AnyObject returned is a Product if
                |     a product appears in the specification tree, in the path corresponding to the
                |     current selection, and a fake AnyObject whose AnyObject.Name property equals to
                |     "InvalidLeafProduct" otherwise.
                |     Cumulated with the use of the AnyObject.Parent property (which enables to
                |     navigate into the object structure), the current property enables the scripter
                |     to obtain the path, in the specification tree, corresponding to the
                |     selection.
                | 
                |     Example:
                | 
                |           The following example supposes a 
                | 
                |     Part or a Product is opened. It asks the end user to select a Shape in the
                |     current window. It then sends message boxes containing the names of the
                |     automation objects contained in the specification tree path corresponding to
                |     the shape selected, and, regarding the automation objects which are products
                |     (only products which are components), a message box containing the abcissa of
                |     the translation of the product compared to its reference
                |     product.
                | 
                |      Dim Status,Feature,LeafProduct,LeafProductProcessed,InputObjectType(0)
                |      Dim Document,Selection,AutomationTreeNodeOrProduct,Position,AxisComponentsArray(11)
                |      Set Document = CATIA.ActiveDocument : Set Selection = Document.Selection
                |     'We propose to the user that he select a feature
                |      InputObjectType(0)="AnyObject" 
                |      Status=Selection.SelectElement2(InputObjectType,"Select a
                |      feature",true)
                |      if (Status = "Cancel") then Exit Sub
                |      Set Feature = Selection.Item(1).Value
                |      Set LeafProduct = Selection.Item(1).LeafProduct
                |      LeafProductProcessed = true
                |      if (LeafProduct.Name<>"InvalidLeafProduct") then LeafProductProcessed = false
                |      Set AutomationTreeNodeOrProduct = Feature
                |      do while
                |      (TypeName(AutomationTreeNodeOrProduct)<>"Application")
                |     '  We send a message box, if AutomationTreeNodeOrProduct is not nor a
                |     Shapes object neither a PartDocument object
                |          if ((TypeName(AutomationTreeNodeOrProduct)<>"Shapes") And
                |          _
                |              (TypeName(AutomationTreeNodeOrProduct)<>"Bodies") And
                |              _
                |              (TypeName(AutomationTreeNodeOrProduct)<>"PartDocument") And
                |              _
                |              (TypeName(AutomationTreeNodeOrProduct)<>"Products") And
                |              _
                |              (TypeName(AutomationTreeNodeOrProduct)<>"ProductDocument"))
                |              then
                |              msgbox AutomationTreeNodeOrProduct.Name
                |              if (TypeName(AutomationTreeNodeOrProduct)="Product")
                |              then
                |     '          We display a message box containing the abcissa of the
                |     translation, except in the case of the
                |     '          root product
                |                  if
                |                  (TypeName(AutomationTreeNodeOrProduct.Parent.Parent)<>"Application")
                |                  then
                |                      Set Position = AutomationTreeNodeOrProduct.Position
                |                      Call Position.GetComponents(AxisComponentsArray)
                |                      msgbox AxisComponentsArray(9)
                |                  end if
                |              end if
                |          end if
                |     '  We determine the next automation tree node or product
                |          Set AutomationTreeNodeOrProduct = AutomationTreeNodeOrProduct.Parent
                |          if ((TypeName(AutomationTreeNodeOrProduct)="Application") And (Not
                |          LeafProductProcessed)) then
                |     '      The specification tree path corresponding to the selection contains
                |     at least one product, which the current
                |     '      loop as not yet processed. It means that the parent in the
                |     specification tree of the feature corresponding
                |     '      to the last message box sent is LeafProduct
                |              Set AutomationTreeNodeOrProduct = LeafProduct
                |              LeafProductProcessed = true
                |          end if
                |      loop
                | 
                |     If you run the preceeding piece of script, the current document beeing a
                |     product with the following specification tree:
                | 
                |          +--------+ 
                |          !Product3!
                |          +----+---+
                |               !
                |               +- Product2 (Product2.1)             'translation value:
                |               10
                |               !     !
                |               !     +- Product1 (Product1.1)       'translation value:
                |               20
                |               !           !
                |               !           +- Part1 (Part1.1)       
                |               !                !
                |               !                +- Part1
                |               !                     !
                |               !                     +- PartBody
                |               !                           !
                |               !                           +- Pad.1
                |               +- Part2 (Part2.1)
                | 
                |     and you select Pad.1, the message boxes displayed will be:
                | 
                |          Pad.1
                |          PartBody
                |          Part1
                |          Part1.1
                |          Product1.1
                |          20
                |          Product2.1
                |          10
                |          Product3

        :rtype: AnyObject
        """

        return AnyObject(self.selected_element.LeafProduct)

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Reference() As Reference (Read Only)
                | 
                |     Returns a Reference version of the Value property.
                |     Role: Returns a Reference version of Value .

        :rtype: Reference
        """

        return Reference(self.selected_element.Reference)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the string constant which describes the selected element Automation
                |     type.
                |     This type is returned by the Value property, and may be, for instance "Pad"
                |     or "Line2D".
                |     Caution: This property gives the leaf automation type of the object, in the
                |     inheritance hierarchy. Nevertheless, after a call to Selection.SelectElement2 ,
                |     Selection.SelectElement3 , Selection.SelectElement4 ,
                |     Selection.IndicateOrSelectElement2D or Selection.IndicateOrSelectElement3D ,
                |     this property gives the input filter string constant relative to the effective
                |     selection (more precisely the first filter string constant delivered through
                |     the iFilterType parameter, for which the current automation object fullfills
                |     the string constant). This string constant may be an automation object name
                |     corresponding to the iFilterType parameter with which Selection.SelectElement2
                |     has previously been called, or even a CATSelectionFilter value
                |     name.
                | 
                |     Example:
                | 
                |           Suppose you run the following piece of script: 
                |          
                | 
                |          Set Selection = CATIA.ActiveDocument.Selection
                |         '  We propose to the user that he select a Prism or a
                |         Hole
                |          ReDim InputObjectType(1) : InputObjectType(0)="Prism" : InputObjectType(1)="Hole"
                |          Status=Selection.SelectElement2(InputObjectType,"Select a prism or a
                |          hole",true)
                |          if (Status = "Cancel") then Exit Sub
                |          AutomationType = Selection.Item(1).Type
                | 
                | 
                |          If the user selects a Pad, the script AutomationType variable will
                |          contain "Prism"
                |          and not "Pad".
                |          
                | 
                |         Consequently, in most cases, use the VBScript TypeName function instead
                |         of this property.

        :rtype: str
        """

        return self.selected_element.Type

    @property
    def value(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Value() As CATBaseDispatch (Read Only)
                | 
                |     Returns the actual selected automation object.

        :rtype: AnyObject
        """

        return AnyObject(self.selected_element.Value)

    def get_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCoordinates(CATSafeArrayVariant ioPoint)
                | 
                |     Returns the coordinates of the pick point.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             The coordinates of the pick point, i.e. the hit between the
                |             geometric object and the cursor.
                |             The length of this parameter will be 3, except if the document is a
                |             DrawingDocument
                |     Example:
                | 
                |           This example retrieves the coordinates of the pick point in
                |           the
                |          array myArray:
                | 
                |          Dim oSelElem As SelectedElement
                |          Set oSelElem = CATIA.ActiveDocument.Selection.Item(1)
                |          ReDim myArray(2)
                |          oSelElem.GetCoordinates myArray

        :param tuple io_point:
        :rtype: None
        """
        vba_function_name = 'get_coordinates'
        vba_code = """
        Public Function get_coordinates(selected_element)
            Dim ioPoint (2)
            selected_element.GetCoordinates ioPoint
            get_coordinates = ioPoint
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SelectedElement(name="{self.name}")'
