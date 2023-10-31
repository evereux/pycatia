#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class VisPropertySet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VisPropertySet
                | 
                | Represents the graphic properties for the current selection.
                | Role: We retrieve the graphic properties of the current selection thanks to
                | Selection.VisProperties
                | 
                | The graphic properties are:
                | 
                |     The Color
                | 
                |     The Color is defined by 3 components (red,green,blue). Each component
                |     ranges from 0 to 255
                |     The Opacity
                | 
                |     The opacity is defined from 255 (total opacity) to 0 (total transparency).
                |     In Material visualization mode the transparency is real, so the element is
                |     truly more or less opaque. But in another visualization mode, the transparency
                |     is a simulation, so if the opacity is between 0 and 254 the element is
                |     transparent but with the same visual effect and if the opacity is 255 the
                |     element is opaque.
                |     The width of a line
                | 
                |     Each index defines a width customizable in Tools/Options.
                |     The type of a line
                | 
                |     Solid, Dashed, ...
                |     The symbol of a point
                | 
                |     Star, Dot, ... 
                | 
                | A partial modification of an object
                | A part (for example) contains faces, edges, lines, points. Interactively with
                | the Edit Properties command the end user can change their color, their line
                | type and so one. To go faster there is the Graphic Toolbar which contains a
                | sub-set of properties. So this interface follows the behavior of the graphic
                | toolbar. The color, the line type ... is applicated to the sub-element of the
                | object defined by the application, and that you can retrieve in the graphic
                | toolbar.
                | 
                | A multiple selection
                | When we modify a graphic property using the Setxxx methods, we modify one by
                | one each element of the current selection.
                | When we read a graphic property using the Getxxx methods, we retrieve an
                | information which is valid for all elements of the current
                | selection.
                | 
                | Real versus Visible graphic properties
                | Elements of the current selection are inside a specification
                | tree:
                | 
                |    Example :
                |     
                |    Product0
                |         Part1
                |            Part3
                |         Part2
                | 
                |  
                | 
                | In this sample, product0 and Part1 are nodes and Part3 and Part2 are
                | leaves.
                | Each element (node and leaf) of this tree has its own graphic properties: that
                | is the "Real" graphic properties.
                | But there is an inheritance mecanism, so each element has also "Visible"
                | graphic properties. An element can be displayed with an another graphic
                | properties that its real graphic properties.
                | 
                | The inheritance is the following:
                | From the root of the tree, the first node with an inheritance flag to 1, gives
                | its property to each element below it. For each graphic property there is an
                | independantly inheritance.
                | 
                |    Example with the color property: ( color inheritance flag,
                |    color)
                |     
                |    Product0    (1,red)
                |         Part1    (0,blue)
                |            Part3   (1,green)
                |         Part2    (0,Yellow)
                | 
                |  
                | 
                | In this sample the real colord of the product0 is red, blue for the part1,
                | green for the part3 and yellow for the part2. But the visible color of each
                | element is red, because the product0 gives the red color at all the
                | tree.
                | 
                | See also:
                |     Selection
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.vis_property_set = com_object

    def get_layer(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLayer(CatVisLayerType oLayerType,
                | long oLayerValue) As CatVisPropertyStatus
                | 
                |     Returns the layer for the current selection.
                |     Note: This property is global for the object.
                | 
                |     Parameters:
                | 
                |         oLayerType
                |             the type of the layer
                |             When the type is equal to catVisLayerNone, the layer of the current
                |             selection is "none".
                |             When the type is equal to catVisLayerBasic, the layer of the
                |             currection selection is indicated by the following
                |             parameter.
                |         oLayerValue
                |             A value between 0 to 1000
                |             This parameter is usefull only when the type of the layer is
                |             catVisLayerBasic. 
                |
                |     Example:
                | 
                |           The following sample shows how to retrieve layer of current
                |           selection.
                |          
                |          Dim layer
                |          layer = CLng(0) 
                |          Dim layertype As CatVisLayerType
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetLayer layertype, layer
                |          If (layertype = catVisLayerNone) Then 
                |          MsgBox "Layer None"
                |          End If
                |          If (layertype = catVisLayerBasic) Then 
                |          MsgBox "layer =" & layer
                |          End If

        :return:
        :rtype: tuple
        """
        return self.vis_property_set.GetLayer()

    def get_pick(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPick(CatVisPropertyPick oPick) As
                | CatVisPropertyStatus
                | 
                |     Returns the state pick mode for the current selection.
                |     Note: This property is global for the object.
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve pick mode of current
                |           selection.
                |          
                | 
                |          Dim pickstate As CatVisPropertyPick
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetPick pickstate
                |          MsgBox "pick = " & pickstate

        :return: enum cat_vis_property_status
        :rtype: int
        """
        return self.vis_property_set.GetPick()

    def get_real_color(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRealColor(long oRed,
                | long oGreen,
                | long oBlue) As CatVisPropertyStatus
                | 
                |     Retrieves the real color for the current selection.
                | 
                |     Parameters:
                | 
                |         oRed
                |             A value between 0 and 255 
                |         oGreen
                |             A value between 0 and 255 
                |         oBlue
                |             A value between 0 and 255 
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same real color,
                |                 so oRed, oGreen and oBlue are valid 
                |             catVisPropertyUnDefined
                |                 The real color is not the same for all elements of the current
                |                 selection, so oRed, oGreen and oBlue are not valid
                |
                |     Example:
                |           The following sample shows how to retrieve real colors of current
                |           selection.
                |
                |          Dim r, g, b 
                |          r = CLng(0) 
                |          g = CLng(0) 
                |          b = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetRealColor r, g, b 
                |          MsgBox "r = " & r & " g = " & g & " b = " & b

        :rtype: tuple
        """
        return self.vis_property_set.GetRealColor()

    def get_real_inheritance(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRealInheritance(CatVisPropertyType iPropertyType,
                | long oInheritance) As CatVisPropertyStatus
                | 
                |     Retrieves the real inheritance flag for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         iPropertyType
                |             The type of property: Color, Opacity, Line Width, Line Type
                |         oInheritance
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                |         oStatus
                |             Legal value:
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same real
                |                 inheritance flag for the iPropertyType , so oInheritance is valid
                |             catVisPropertyUnDefined
                |                 The real inheritance flag for iPropertyType is not the same for
                |                 all elements of the current selection, so oInheritance is not valid
                |
                |     Example:
                | 
                |           The following sample shows how to retrieve inheritance of current
                |           selection.
                |
                |          Dim inhLineType, inhWidth, inhColor, inhOpacity
                |          inhLineType = CLng(0) 
                |          inhWidth = CLng(0) 
                |          inhColor = CLng(0) 
                |          inhOpacity = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetRealInheritance catVisPropertyLineType,
                |          inhLineType
                |          visProperties1.GetRealInheritance catVisPropertyWidth,
                |          inhWidth
                |          visProperties1.GetRealInheritance catVisPropertyColor,
                |          inhColor
                |          visProperties1.GetRealInheritance catVisPropertyOpacity,
                |          inhOpacity
                |          MsgBox "Inheritance : linetype = " & inhLineType & "width =" & inhWidth & "Colour ="
                |                 & inhColor & "Opacity =" & inhOpacity

        :rtype: tuple
        """
        return self.vis_property_set.GetRealInheritance()

    def get_real_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRealLineType(long oLineType) As
                | CatVisPropertyStatus
                | 
                |     Retrieves the real line type for the current selection.
                | 
                |     Parameters:
                | 
                |         oLineType
                |             The value ranges from 1 to 63. Each indice is a line type
                |             customizable in the page Tools/Options/General/Display/Line Type.
                |             
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same real line
                |                 type , so oLineType is valid 
                |             catVisPropertyUnDefined
                |                 The real line type is not the same for all elements of the
                |                 current selection, so oLineType is not valid 
                |             catVisProperty?
                |                 At least one element of the current selection is not concerned
                |                 by this property, so oLineType is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve real line type of current
                |           selection.
                |          
                | 
                |          Dim linetype
                |          linetype = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetRealLineType linetype
                |          MsgBox "linetype = " & linetype

        :rtype: int
        """
        return self.vis_property_set.GetRealLineType()

    def get_real_opacity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRealOpacity(long oOpacity) As CatVisPropertyStatus
                | 
                |     Retrieves the real opacity for the current selection.
                | 
                |     Parameters:
                | 
                |         oOpacity
                |             a value between 0 (total transparency) and 255 (total opacity)
                |             
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same real
                |                 opacity value, so oOpacity is valid 
                |             catVisPropertyUnDefined
                |                 The real opacity value is not the same for all elements of the
                |                 current selection, so oOpacity is not valid 
                |             catVisProperty?
                |                 At least one element of the current selection is not concerned
                |                 by this property, so oOpacity is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve real opacity of current
                |           selection.
                |          
                | 
                |          Dim op
                |          op = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetRealOpacity op 
                |          MsgBox "opacity = " & op

        :rtype: int
        """
        return self.vis_property_set.GetRealOpacity()

    def get_real_width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRealWidth(long oLineWidth) As CatVisPropertyStatus
                | 
                |     Retrieves the real line width for the current selection.
                | 
                |     Parameters:
                | 
                |         oLineWidth
                |             The value ranges from 1 to 63. Each indice is a thickness
                |             customizable in the page Tools/Options/General/Display/thickness.
                |             
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same real width
                |                 , so oLineWidth is valid 
                |             catVisPropertyUnDefined
                |                 The real width is not the same for all elements of the current
                |                 selection, so oLineWidth is not valid 
                |             catVisProperty?
                |                 At least one element of the current selection is not concerned
                |                 by this property, so oLineWidth is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve real line width of current
                |           selection.
                |          
                | 
                |          Dim width
                |          width = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetRealWidth width
                |          MsgBox "width = " & width

        :rtype: int
        """
        return self.vis_property_set.GetRealWidth()

    def get_show(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetShow(CatVisPropertyShow oShow) As
                | CatVisPropertyStatus
                | 
                |     Returns the state show mode for the current selection.
                |     Note: This property is global for the object.
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve show mode of current
                |           selection.
                |          
                | 
                |          Dim showstate As CatVisPropertyShow
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetShow showstate
                |          MsgBox "show = " & showstate

        :rtype: int
        """
        return self.vis_property_set.GetShow()[1]

    def get_symbol_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSymbolType(long oSymbolType) As
                | CatVisPropertyStatus
                | 
                |     Retrieves the symbol type for the current selection.
                | 
                |     Parameters:
                | 
                |     oSymbolType
                |         The symbol type. See SetSymbolType to have values.
                |     oStatus
                |         Legal value:
                | 
                |         catVisPropertyDefined
                |             All elements in the current selection have the same symbol type ,
                |             so oLineType is valid 
                |         catVisPropertiesUnDefined
                |             The symbol type is not the same for all elements of the current
                |             selection, so oLineType is not valid 
                |         catVisProperty?
                |             At least one element of the current selection is not concerned by
                |             this property, so oSymbolType is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve symbol line type of
                |           current selection.
                |          
                | 
                |          Dim symbol
                |          symbol = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetSymbolType symbol
                |          MsgBox "Symbol = " & symbol

        :rtype: int
        """
        return self.vis_property_set.GetSymbolType()

    def get_visible_color(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetVisibleColor(long oRed,
                | long oGreen,
                | long oBlue) As CatVisPropertyStatus
                | 
                |     Retrieves the displayed (visible) color for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         oRed
                |             a value between 0 and 255 
                |         oGreen
                |             a value between 0 and 255 
                |         oBlue
                |             a value between 0 and 255 
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same visible
                |                 color, so oRed, oGreen and oBlue are valid 
                |             catVisPropertyUnDefined
                |                 The visible color is not the same for all elements of the
                |                 current selection, so oRed, oGreen and oBlue are not valid
                |                 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve displayed colors of
                |           current selection.
                |          
                | 
                |          Dim r, g, b 
                |          r = CLng(0) 
                |          g = CLng(0) 
                |          b = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetVisibleColor r, g, b 
                |          MsgBox "r = " & r & " g = " & g & " b = " & b

        :rtype: int
        """
        return self.vis_property_set.GetVisibleColor()

    def get_visible_inheritance(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetVisibleInheritance(CatVisPropertyType
                | iPropertyType,
                | long oInheritance) As CatVisPropertyStatus
                | 
                |     Checks if the real property is hidden.
                | 
                |     Parameters:
                | 
                |         iPropertyType
                |             The type of property : Color, Opacity, Line Width, Line Type 
                |         oInheritance
                | 
                |             0
                |                 No heritance: All parents of each element of the current
                |                 selection have an inheritance flag to 0. 
                |             1
                |                 Heritance: one parent of each element, perhaps the element
                |                 itself, as a inheritance flag to 1. 
                | 
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same inheritance
                |                 flag for the iPropertyType , so oInheritance is valid
                |                 
                |             catVisPropertyUnDefined
                |                 The inheritance flag for iPropertyType is not the same for all
                |                 elements of the current selection, so oInheritance is not valid

        :rtype: int
        """
        return self.vis_property_set.GetVisibleInheritance()

    def get_visible_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetVisibleLineType(long oLineType) As
                | CatVisPropertyStatus
                | 
                |     Retrieves the displayed (visible) line type for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         oLineType
                |             A value ranges from 1 to 63. 
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same visible
                |                 line type , so oLineType is valid 
                |             catVisPropertyUnDefined
                |                 The visible line type is not the same for all elements of the
                |                 current selection, so oLineType is not valid 
                |             catVisProperty?
                |                 At least one element of the current selection is not concerned
                |                 by this property, so oLineType is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve displayed line type of
                |           current selection.
                |          
                | 
                |          Dim linetype
                |          linetype = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetVisibleLineType linetype
                |          MsgBox "linetype = " & linetype

        :rtype: int
        """
        return self.vis_property_set.GetVisibleLineType()

    def get_visible_opacity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetVisibleOpacity(long oOpacity) As
                | CatVisPropertyStatus
                | 
                |     Retrieves the displayed (visible) opacity for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         oOpacity
                |             a value between 0 (total transparency) and 255 (total opacity)
                |             
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same visible
                |                 opacity value, so oOpacity is valid 
                |             catVisPropertyUnDefined
                |                 The visible opacity value is not the same for all elements of
                |                 the current selection, so oOpacity is not valid
                |                 
                |             catVisProperty?
                |                 At least one element of the current selection is not concerned
                |                 by this property, so oOpacity is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve displayed opacity of
                |           current selection.
                |          
                | 
                |          Dim op
                |          op = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetVisibleOpacity op 
                |          MsgBox "opacity = " & op

        :rtype: int
        """
        return self.vis_property_set.GetVisibleOpacity()

    def get_visible_width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetVisibleWidth(long oLineWidth) As
                | CatVisPropertyStatus
                | 
                |     Retrieves the displayed (visible) line width for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         oLineWidth
                |             A value ranges from 1 to 63. 
                |         oStatus
                |             Legal value:
                | 
                |             catVisPropertyDefined
                |                 All elements in the current selection have the same visible
                |                 width , so oLineWidth is valid 
                |             catVisPropertyUnDefined
                |                 The visible width is not the same for all elements of the
                |                 current selection, so oLineWidth is not valid 
                |             catVisProperty?
                |                 At least one element of the current selection is not concerned
                |                 by this property, so oLineWidth is not valid 
                | 
                |     Example:
                | 
                |           The following sample shows how to retrieve displayed line width of
                |           current selection.
                |
                |          Dim width
                |          width = CLng(0) 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.GetVisibleWidth width
                |          MsgBox "width = " & width


        :rtype: int
        """
        return self.vis_property_set.GetVisibleWidth()

    def set_layer(self, i_layer_type: int, i_layer_value: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLayer(CatVisLayerType iLayerType,
                | long iLayerValue)
                | 
                |     Sets the layer for the current selection.
                |     Note: This property is global for the object.
                | 
                |     Parameters:
                | 
                |         iLayerType
                |             the type of the layer 
                |         iLayerValue
                |             A value between 0 to 1000
                |             This parameter is used only when the type of the layer is
                |             catVisLayerBasic. 
                | 
                |     Example:
                | 
                |           The following sample shows how to change layer of current
                |           selection.
                |          
                | 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.SetLayer catVisLayerBasic, 100

        :param int i_layer_type: enum cat_vis_layer_type
        :param int i_layer_value:
        :rtype: None
        """
        return self.vis_property_set.SetLayer(i_layer_type, i_layer_value)

    def set_pick(self, i_pick: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPick(CatVisPropertyPick iPick)
                | 
                |     Sets the state pick mode for the current selection.
                |     Note: This property is global for the object.
                | 
                |     Example:
                | 
                |           The following sample shows how to change pick mode of current
                |           selection.
                |          
                | 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.SetPick catVisPropertyNoPickAttr

        :param int i_pick: enum cat_vis_property_pick
        :rtype: None
        """
        return self.vis_property_set.SetPick(i_pick)

    def set_real_color(self, i_red: int, i_green: int, i_blue: int, i_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRealColor(long iRed,
                | long iGreen,
                | long iBlue,
                | long iInheritance)
                | 
                |     Sets the real color and the color inheritance flag for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         iRed
                |             A value between 0 and 255 
                |         iGreen
                |             A value between 0 and 255 
                |         iBlue
                |             A value between 0 and 255 
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |           The following sample shows how to change colour of current
                |           selection.
                |          
                | 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.SetRealColor 255,0,0,1

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :param int i_inheritance:
        :rtype: None
        """
        return self.vis_property_set.SetRealColor(i_red, i_green, i_blue, i_inheritance)

    def set_real_line_type(self, i_line_type: int, i_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRealLineType(long iLineType,
                | long iInheritance)
                | 
                |     Sets the real line type and the line type inheritance flag for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         iLineType
                |             The value ranges from 1 to 63. Each indice is a line type
                |             customizable in the page Tools/Options/General/Display/Line Type.
                |             
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |     The following sample shows how to change line type of current
                |     selection.
                |       Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties
                |       visProperties1.SetRealLineType 4,1

        :param int i_line_type:
        :param int i_inheritance:
        :rtype: None
        """
        return self.vis_property_set.SetRealLineType(i_line_type, i_inheritance)

    def set_real_opacity(self, i_opacity: int, i_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRealOpacity(long iOpacity,
                | long iInheritance)
                | 
                |     Sets the opacity and the opacity inheritance flag for the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         iOpacity
                |             A value between 0 (total transparency) and 255 (total opacity).
                |             
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                | 
                |     Example:
                | 
                |           The following sample shows how to change opacity of current
                |           selection.
                |          
                | 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.SetRealOpacity 128,1

        :param int i_opacity:
        :param int i_inheritance:
        :rtype: None
        """
        return self.vis_property_set.SetRealOpacity(i_opacity, i_inheritance)

    def set_real_width(self, i_line_width: int, i_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRealWidth(long iLineWidth,
                | long iInheritance)
                | 
                |     Sets the real line width and the line width inheritance flag for the
                |     current selection.
                | 
                |     Parameters:
                | 
                |         iLineWidth
                |             The value ranges from 1 to 63. Each indice is a thickness
                |             customizable in the page Tools/Options/General/Display/thickness.
                |             
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |           The following sample shows how to change line width of current
                |           selection.
                |          
                | 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.SetRealWidth 4,1

        :param int i_line_width:
        :param int i_inheritance:
        :rtype: None
        """
        return self.vis_property_set.SetRealWidth(i_line_width, i_inheritance)

    def set_show(self, i_show: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetShow(CatVisPropertyShow iShow)
                | 
                |     Sets the state show mode for the current selection.
                |     Note: This property is global for the object.
                | 
                |     Example:
                | 
                |           The following sample shows how to change show mode of current
                |           selection.
                |          
                | 
                |          Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties 
                |          visProperties1.SetShow catVisPropertyNoShowAttr

        :param int i_show: enum cat_vis_property_show
        :rtype: None
        """
        return self.vis_property_set.SetShow(i_show)

    def set_symbol_type(self, i_symbol_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSymbolType(long iSymbolType)
                | 
                |     Sets the symbol type.
                |     Note:There is no heritage for symbols. That is why there is only one
                |     function "SetSymbolType" and no function "SetRealSymbolType" or
                |     "SetVisibleSymbolType"
                | 
                |     Parameters:
                | 
                |         iSymbolType
                |             The symbol type
                |             legal values:
                | 
                |                 1 : a cross which looks like a "X".
                |                 2 : a cross which looks like a "+"
                |                 3 : an unfilled circle
                |                 4 : two unfilled concentric circles
                |                 5 : a filled circle
                |                 6 : a filled square
                |                 7 : a star which is the union of a 2D marker CROSS ,a 2D marker PLUS and a 2D marker
                |                     DOT
                |                 8 : a dot
                |                 9 : a smalldot (one pixel)
                |                 10 : a kind of arrow which points to the bottom-left
                |                 
                |                 11 : a kind of arrow which points to the top-right
                | 
                |                 FULLCIRCLE2 : a big 12
                |                 FULLSQUARE2 : a big 13
                | 
                |     Example:
                |     The following sample shows how to change symbol type of current
                |     selection.
                |
                |       Set visProperties1 = CATIA.ActiveDocument.Selection.VisProperties
                |       visProperties1.SetSymbolType 4

        :param int i_symbol_type:
        :rtype: None
        """
        return self.vis_property_set.SetSymbolType(i_symbol_type)

    def __repr__(self):
        return f'VisPropertySet(name="{self.name}")'
