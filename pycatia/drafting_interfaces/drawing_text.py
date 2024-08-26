#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
from pycatia.drafting_interfaces.drawing_text_properties import DrawingTextProperties
from pycatia.system_interfaces.any_object import AnyObject


class DrawingText(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingText
                | 
                | Represents a drawing text in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_text = com_object

    @property
    def anchor_position(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AnchorPosition() As CatTextAnchorPosition
                | 
                |     Returns or sets the anchor position of the drawing text.
                | 
                |     Example:
                |         This example sets the anchor position of the MyText drawing text to top
                |         left position.
                | 
                |          MyText.AnchorPosition = TopLeft

        :return: enum cat_text_anchor_position
        :rtype: int
        """

        return self.drawing_text.AnchorPosition

    @anchor_position.setter
    def anchor_position(self, value: int):
        """
        :param int value: enum cat_text_anchor_position
        """

        self.drawing_text.AnchorPosition = value

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As double
                | 
                |     Returns or sets the angle of the drawing text. The angle is measured
                |     between the axis system of the drawing view and the local axis system of the
                |     drawing text. The angle is measured in radians and is counted
                |     counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyText drawing Text to 90 degrees
                |         clockwise. You first need to compute the angle in degrees and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          Angle90Clockwise = -90
                |          MyText.Angle = Angle90Clockwise

        :rtype: float
        """

        return self.drawing_text.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.drawing_text.Angle = value

    @property
    def associative_element(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AssociativeElement() As CATBaseDispatch
                | 
                |     Returns or sets the associative object of the drawing
                |     text.
                | 
                |     Example:
                |         This example sets an associative line of the MyText drawing text to top
                |         left position.
                | 
                |          MyText.AssociativeElement = line

        :rtype: AnyObject
        """

        return AnyObject(self.drawing_text.AssociativeElement)

    @associative_element.setter
    def associative_element(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.drawing_text.AssociativeElement = value

    @property
    def frame_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FrameType() As CatTextFrameType
                | 
                |     Returns or sets the frame type of the drawing text.
                | 
                |     Example:
                |         This example sets the frame type of the MyText drawing text to an
                |         ellipse.
                | 
                |          MyText.FrameType = catEllipse

        :return: enum cat_text_frame_type
        :rtype: int
        """

        return self.drawing_text.FrameType

    @frame_type.setter
    def frame_type(self, value: int):
        """
        :param int value: enum cat_text_frame_type
        """

        self.drawing_text.FrameType = value

    @property
    def leaders(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Leaders() As DrawingLeaders (Read Only)
                | 
                |     Returns the drawing leader collection of the drawing text.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the MyText drawing text.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyText.Leaders

        :rtype: DrawingLeaders
        """

        return DrawingLeaders(self.drawing_text.Leaders)

    @property
    def nb_link(self) -> int:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property NbLink() As long (Read Only)
                |     Returns the number of attributes link
                |
                |     Example:
                |         This example gets number of attributes link of MyText drawing
                |         text.
                |
                |          nbLink = MyText.NbLink

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_text.NbLink

    @property
    def orientation_reference(self) -> int:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property OrientationReference() As long
                |     Returns or sets the orientation reference of the drawing
                |     text.
                |     0 : Sheet orientation
                |     1 : View/Label/2Dcomponent orientation
                |
                |     Example:
                |         This example sets the orientation reference of MyText drawing text to
                |         sheet orientation
                |
                |          MyText.OrientationReference = 0

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_text.OrientationReference

    @orientation_reference.setter
    def orientation_reference(self, value: int):
        """
        :param int value:
        """

        self.drawing_text.OrientationReference = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Text() As CATBSTR
                | 
                |     Returns or sets character string that makes up the text.
                | 
                |     Example:
                |         This example retrieves in CharString the character string of the MyText
                |         drawing text.
                | 
                |          CharString = MyText.Text

        :rtype: str
        """

        return self.drawing_text.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.drawing_text.Text = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TextProperties() As DrawingTextProperties (Read
                | Only)
                | 
                |     Returns the text properties of the drawing text. Allows to modify the whole
                |     text properties. To manage a sub part of the text use
                |     GetParameterOnSubString
                | 
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyText drawing text.
                | 
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyText.TextProperties

        :rtype: DrawingTextProperties
        """

        return DrawingTextProperties(self.drawing_text.TextProperties)

    @property
    def wrapping_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WrappingWidth() As double
                | 
                |     Returns or sets the wrapping width of the drawing text.
                | 
                |     Example:
                |         This example sets the wrapping width of the MyText drawing text to
                |         50.
                | 
                |          MyText.WrappingWidth = 50.

        :rtype: float
        """

        return self.drawing_text.WrappingWidth

    @wrapping_width.setter
    def wrapping_width(self, value: float):
        """
        :param float value:
        """

        self.drawing_text.WrappingWidth = value

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property x() As double
                | 
                |     Returns or sets the x coordinate of the text. It is expressed with respect
                |     to the current view coordinate system. This coordinate, like any length, is
                |     measured in meters.
                | 
                |     Example:
                |         This example retrieves the x coordinate of the text MyText drawing
                |         text.
                | 
                |          X = MyText.x

        :rtype: float
        """

        return self.drawing_text.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_text.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property y() As double
                | 
                |     Returns or sets the y coordinate of the text. It is expressed with respect
                |     to the view coordinate system. This coordinate, like any length, is measured in
                |     meters.
                | 
                |     Example:
                |         This example sets the y coordinate of the text MyText drawing text to 5
                |         inches. You need first to convert the 5 inches into
                |         meters.
                | 
                |          NewYCoordinate = 5*25.4/1000
                |          MyText.y =  NewYCoordinate

        :rtype: float
        """

        return self.drawing_text.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_text.y = value

    def activate_frame(self, itype: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ActivateFrame(CatTextFrameType itype)
                | 
                |     Activates the text frame of the drawing text.
                | 
                |     Example:
                |         This example adds a rectangle frame to MyText drawing
                |         text.
                | 
                |          CatTextFrameType ityp = catRectangle
                |          MyText.ActivateFrame(itype)
                |          
                | 
                |         This example removes the frame to MyText drawing text.
                | 
                |          CatTextFrameType ityp = catNone
                |          MyText.ActivateFrame(itype)

        :param int itype: enum cat_text_frame_type
        :rtype: None
        """
        return self.drawing_text.ActivateFrame(itype)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'activate_frame'
        # # vba_code = """
        # # Public Function activate_frame(drawing_text)
        # #     Dim itype (2)
        # #     drawing_text.ActivateFrame itype
        # #     activate_frame = itype
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_font_name(self, i_first, inb_character):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFontName(long iFirst,
                | long inbCharacter) As CATBSTR
                | 
                |     Returns the font name on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                | 
                |     Returns:
                |         oFontName The name of the font 
                |     Example:
                |         This example gets the MyText drawing text font.
                | 
                |          oFontName = MyText.GetFontName(0, 0)

        :param int i_first:
        :param int inb_character:
        :rtype: str
        """
        return self.drawing_text.GetFontName(i_first, inb_character)

    def get_font_size(self, i_first: int, inb_character: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFontSize(long iFirst,
                | long inbCharacter) As double
                | 
                |     Returns the font size on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                | 
                |     Returns:
                |         oFontSize The size of the font 
                |     Example:
                |         This example gets the MyText font size.
                | 
                |          oFontSize = MyText.GetFontSize(0, 0)

        :param int i_first:
        :param int inb_character:
        :rtype: float
        """
        return self.drawing_text.GetFontSize(i_first, inb_character)

    def get_modifiable_in_2d_component_instances(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetModifiableIn2DComponentInstances() As boolean
                | 
                |     Returns if the text is modifiable or not in 2D component instances. The
                |     text must own to a 2D component (NOT to a view)
                | 
                |     Example:
                |         This example retrieves if MyText drawing text is modifiable or
                |         not
                | 
                |          IsModifiable = MyText.GetModifiableIn2DComponentInstances

        :rtype: bool
        """
        return self.drawing_text.GetModifiableIn2DComponentInstances()

    def get_parameter_link(self, i_index: int) -> AnyObject:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetParameterLink(long iIndex) As CATBaseDispatch
                |     Returns the pointed parameter link
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the pointed parameter link. 1 <= iIndex <=
                |             NbLink
                |
                |             Example:
                |                 This example gets the first parameter link of MyText drawing
                |                 text.
                |
                |                  Dim MyParm As Parameter
                |                  MyParm = MyText.GetParameterLink(1)
                |                  If MyParm.Value<>"Front view" Then
                |                    'Do something
                |                  End If

        :param int i_index:
        :rtype: AnyObject
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_text.GetParameterLink(i_index)

    def get_parameter_on_sub_string(self, i_param: int, i_first: int, inb_character: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetParameterOnSubString(CatTextProperty iParam,
                | long iFirst,
                | long inbCharacter) As long
                | 
                |     Returns a property on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The drawing text property 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                | 
                |     Returns:
                |         oval The value corresponding to the property 
                |     Example:
                |         This example gets the parameter Italic on MyText drawing
                |         text.
                | 
                |          CatTextProperty iParam = catItalic 
                |          iFirst = 0
                |          inbCharacter = 0
                |          oval = MyText.GetParameterOnsubString(iParam, iFirst, inbCharacter)

        :param int i_param: enum cat_text_property
        :param int i_first:
        :param int inb_character:
        :rtype: int
        """
        return self.drawing_text.GetParameterOnSubString(i_param, i_first, inb_character)

    def insert_variable(self, i_first: int, inb_character: int, ibase: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub InsertVariable(long iFirst,
                | long inbCharacter,
                | CATBaseDispatch ibase)
                | 
                |     Sets a Parameter in a string of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character from which the parameter is inserted
                |             
                |         inbCharacter
                |             The number of characters the parameter will replace
                |             
                |         iParameter
                |             The parameter to be inserted 
                |         Example:
                |             This example sets a parameter right at the end of MyText drawing
                |             text.
                | 
                |              Dim DrwDocument As DrawingDocument
                |              Set DrwDocument = CATIA.ActiveDocument
                | 
                |              Dim iParameter As Parameter
                |              Set iParameter = DrwDocument.Parameters.Item("Drawing/Sheet.1/ViewMakeUp.1/Scale")
                | 
                |              MyText.InsertVariable 0, 0, iParameter

        :param int i_first:
        :param int inb_character:
        :param AnyObject ibase:
        :rtype: None
        """
        return self.drawing_text.InsertVariable(i_first, inb_character, ibase.com_object)

    def set_font_name(self, i_first: int, inb_character: int, i_font_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFontName(long iFirst,
                | long inbCharacter,
                | CATBSTR iFontName)
                | 
                |     Sets the font size on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                |         iFontName
                |             The name of the font
                | 
                |             Example:
                |                 This example sets the MyText drawing text font as Courrier 10
                |                 BT.
                | 
                |                  MyText.SetFontName 0,  0, "Courrier 10 BT"

        :param int i_first:
        :param int inb_character:
        :param str i_font_name:
        :rtype: None
        """
        return self.drawing_text.SetFontName(i_first, inb_character, i_font_name)

    def set_font_size(self, i_first: int, inb_character: int, i_font_size: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFontSize(long iFirst,
                | long inbCharacter,
                | double iFontSize)
                | 
                |     Sets the font size on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                |         iFontSize
                |             The size of the font 
                |         Example:
                |             This example sets the MyText font size to 3.5.
                | 
                |              iFontSize = 3.5
                |              MyText.SetFontSize 0,  0, iFontSize

        :param int i_first:
        :param int inb_character:
        :param float i_font_size:
        :rtype: None
        """
        return self.drawing_text.SetFontSize(i_first, inb_character, i_font_size)

    def set_modifiable_in_2d_component_instances(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetModifiableIn2DComponentInstances()
                | 
                |     Sets the text as modifiable in 2D component instances.The text must own to
                |     a 2D component (NOT to a view).then ,its content will be modifiable inside
                |     instances of this 2D component.
                | 
                |     Example:
                |         This example sets the MyText drawing text as
                |         modifiable.
                | 
                |          MyText.SetModifiableIn2DComponentInstances

        :rtype: None
        """
        return self.drawing_text.SetModifiableIn2DComponentInstances()

    def set_parameter_on_sub_string(self, i_param: int, i_first: int, inb_character: int, i_val: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetParameterOnSubString(CatTextProperty iParam,
                | long iFirst,
                | long inbCharacter,
                | long iVal)
                | 
                |     Sets a property on a substring of the drawing text.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The drawing text property 
                |         iFirst
                |             The first character to which the property should apply
                |             
                |         inbCharacter
                |             The number of characters to which the property should apply
                |             
                |         iVal
                |             The value to be applied according to the property 
                |         Example:
                |             This example sets all MyText drawing text in bold
                |             character.
                | 
                |              CatTextProperty iParam = catBold 
                |              iFirst = 0
                |              inbCharacter = 0
                |              ival = 1
                |              MyText.SetParameterOnsubString iParam, iFirst, inbCharacter,
                |              ival

        :param int i_param: enum cat_text_property
        :param int i_first:
        :param int inb_character:
        :param int i_val:
        :rtype: None
        """
        return self.drawing_text.SetParameterOnSubString(i_param, i_first, inb_character, i_val)

    def __repr__(self):
        return f'DrawingText(name="{self.name}")'
