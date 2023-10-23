#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.drafting_interfaces.drawing_view import DrawingView
    from pycatia.drafting_interfaces.drawing_sheet import DrawingSheet


class DrawingComponent(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingComponent
                | 
                | Represents a drawing component instance (ditto) in a drawing
                | view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_component = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As double
                | 
                |     Returns or sets the angle of the drawing component instance. The angle is
                |     given in the axis system of the drawing view The angle is measured in radians
                |     and is counted counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyComponent drawing component
                |         instance to 90 degrees clockwise. You first need to compute the angle in
                |         radians and set the minus sign to indicate the rotation is
                |         clockwise.
                | 
                |          PI = 3.1415926535
                |          Angle90Clockwise = -PI/2
                |          MyComponent.Angle = Angle90Clockwise

        :rtype: float
        """

        return self.drawing_component.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.drawing_component.Angle = value

    @property
    def comp_ref(self) -> 'DrawingView':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CompRef() As DrawingView (Read Only)
                | 
                |     Returns the component reference of this drawing component instance. this is
                |     a CATIADrawingView
                | 
                |     Example:
                |         This example gets the drawing component reference of the MyComponent
                |         drawing component instance.
                | 
                |          Dim ComponentRef As DrawingView
                |          Set ComponentRef = MyComponent.CompRef

        :rtype: DrawingView
        """
        from pycatia.drafting_interfaces.drawing_view import DrawingView
        return DrawingView(self.drawing_component.CompRef)

    @property
    def scale2(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Scale2() As double
                | 
                |     Returns or sets the scale of the drawing component instance (Workaround for
                |     VBA keyword).
                | 
                |     Example:
                |         This example sets the scale of the MyComponent drawing component
                |         instance to 0.5.
                | 
                |          MyComponent.Scale2 = 0.5

        :rtype: float
        """

        return self.drawing_component.Scale2

    @scale2.setter
    def scale2(self, value: float):
        """
        :param float value:
        """

        self.drawing_component.Scale2 = value

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property x() As double
                | 
                |     Returns or sets the x coordinate of the drawing component instance
                |     position. It is expressed with respect to the view coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the x coordinate of the position of the MyComponent
                |         drawing component instance to 5 inches. You need first to convert the 5 inches
                |         into millimeters.
                | 
                |          NewXCoordinate = 5*25.4
                |          MyComponent.x =  NewXCoordinate

        :rtype: float
        """

        return self.drawing_component.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.drawing_component.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property y() As double
                | 
                |     Returns or sets the y coordinate of the drawing component instance
                |     position. It is expressed with respect to the view coordinate system. This
                |     coordinate, like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the position of the MyComponent
                |         drawing component instance to 5 inches. You need first to convert the 5 inches
                |         into millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyComponent.y =  NewYCoordinate

        :rtype: float
        """

        return self.drawing_component.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.drawing_component.y = value

    def explode(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Explode()
                | 
                |     Explodes the drawing component instance (every sub elements of the drawing
                |     component are created). Note: The drawing component is not removed by Explode
                |     method
                | 
                |     Example:
                |         This example Explodes the MyComponent drawing component instance and
                |         removes it.
                | 
                |          MyComponent.Explode
                |          Set MySelection = CATIA.ActiveDocument.Selection
                |          MySelection.clear
                |          MySelection.add MyComponent
                |          MySelection.delete

        :rtype: None
        """
        return self.drawing_component.Explode()

    def explode_and_select(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ExplodeAndSelect()
                | 
                |     Explodes the drawing component instance (every sub elements of the drawing
                |     component are created) and put created sub elements in selection
                |     set.
                | 
                |     Example:
                |         This example Explodes the MyComponent drawing component
                |         instance.
                | 
                |          MyComponent.ExplodeAndSelect

        :rtype: None
        """
        return self.drawing_component.ExplodeAndSelect()

    def expose_comp_ref(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ExposeCompRef()
                | 
                |     Exposes the component reference of this drawing component instance in a new
                |     detail sheet.
                | 
                |     Example:
                |         This example exposes the component reference of the MyComponent drawing
                |         component instance in a new detail sheet.
                | 
                |          MyComponent.ExposeCompRef

        :rtype: None
        """
        return self.drawing_component.ExposeCompRef()

    def expose_comp_ref_in_sheet(self, i_sheet: 'DrawingSheet') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ExposeCompRefInSheet(DrawingSheet iSheet)
                | 
                |     Exposes the component reference of this drawing component instance in a
                |     specific detail sheet.
                | 
                |     Parameters:
                | 
                |         iSheet
                |             The drawing sheet where the reference component has to be exposed.
                |             This sheet has to be a detail sheet, if not the component reference will be
                |             placed in a new detail sheet.
                | 
                |             Example:
                |                 This example exposes the component reference of the MyComponent
                |                 drawing component instance in the MyDetailSheet drawing
                |                 sheet.
                | 
                |                  MyComponent.ExposeCompRefInSheet
                |                  MyDetailSheet

        :param DrawingSheet i_sheet:
        :rtype: None
        """
        return self.drawing_component.ExposeCompRefInSheet(i_sheet.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'expose_comp_ref_in_sheet'
        # # vba_code = """
        # # Public Function expose_comp_ref_in_sheet(drawing_component)
        # #     Dim iSheet (2)
        # #     drawing_component.ExposeCompRefInSheet iSheet
        # #     expose_comp_ref_in_sheet = iSheet
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def flip(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Flip()
                | 
                |     Flips the drawing component instance around X axis To flip around Y axis
                |     you have to flip the component around X and to add a rotation of 180
                |     degrees.
                | 
                |     Example:
                |         This example Flips the MyComponent drawing component
                |         instance.
                | 
                |          MyComponent.Flip

        :rtype: None
        """
        return self.drawing_component.Flip()

    def get_flip(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFlip() As boolean
                | 
                |     Returns the flip state of a drawing component instance around X
                |     axis.
                | 
                |     Example:
                |         This example Get the flip info of the MyComponent drawing component
                |         instance.
                | 
                |          IsFlipped = MyComponent.GetFlip

        :rtype: bool
        """
        return self.drawing_component.GetFlip()

    def get_matrix(self, io_matrix: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetMatrix(CATSafeArrayVariant ioMatrix)
                | 
                |     Gets the matrix of the drawing component instance. This matrix enables you
                |     to define the position (index 4 and 5 of the matrix) and the scale, the angle
                |     and the flip (index 0,1,2 and 3) of the drawing component instance at the same
                |     time.
                | 
                |     Parameters:
                | 
                |         ioMatrix[0]
                |             The 1st coordinate of the first vector 
                |         ioMatrix[1]
                |             The 2nd coordinate of the first vector 
                |         ioMatrix[2]
                |             The 1st coordinate of the second vector 
                |         ioMatrix[3]
                |             The 2nd coordinate of the second vector 
                |         ioMatrix[4]
                |             The x value of the translation vector 
                |         ioMatrix[5]
                |             The y value of the translation vector

        :param tuple io_matrix:
        :rtype: None
        """
        return self.drawing_component.GetMatrix(io_matrix)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_matrix'
        # # vba_code = """
        # # Public Function get_matrix(drawing_component)
        # #     Dim ioMatrix (2)
        # #     drawing_component.GetMatrix ioMatrix
        # #     get_matrix = ioMatrix
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_modifiable_object(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetModifiableObject(CATVariant iIndex) As AnyObject
                | 
                |     Gets a modifiable object by index or name in this drawing component
                |     instance.
                | 
                |     Example:
                |         This example Gets the first modifiable object in the MyComponent
                |         drawing component instance.
                | 
                |          Object = MyComponent.GetModifiableObject(1)

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.drawing_component.GetModifiableObject(i_index))

    def get_modifiable_objects_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetModifiableObjectsCount() As long
                | 
                |     Gets the number of modifiable objects in this drawing component
                |     instance.
                | 
                |     Example:
                |         This example Gets the number of modifiable objects in MyComponent
                |         drawing component instance.
                | 
                |          Count = MyComponent.GetModifiableObjectsCount

        :rtype: int
        """
        return self.drawing_component.GetModifiableObjectsCount()

    def set_matrix(self, i_matrix: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetMatrix(CATSafeArrayVariant iMatrix)
                | 
                |     Sets the matrix of the drawing component instance. This matrix enables you
                |     to define the position (index 4 and 5 of the matrix) and the scale, the angle
                |     and the flip (index 0,1,2 and 3) of the drawing component instance at the same
                |     time.
                | 
                |     Parameters:
                | 
                |         ioMatrix[0]
                |             The 1st coordinate of the first vector 
                |         ioMatrix[1]
                |             The 2nd coordinate of the first vector 
                |         ioMatrix[2]
                |             The 1st coordinate of the second vector 
                |         ioMatrix[3]
                |             The 2nd coordinate of the second vector 
                |         ioMatrix[4]
                |             The x value of the translation vector 
                |         ioMatrix[5]
                |             The y value of the translation vector

        :param tuple i_matrix:
        :rtype: None
        """
        return self.drawing_component.SetMatrix(i_matrix)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_matrix'
        # # vba_code = """
        # # Public Function set_matrix(drawing_component)
        # #     Dim iMatrix (2)
        # #     drawing_component.SetMatrix iMatrix
        # #     set_matrix = iMatrix
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DrawingComponent(name="{self.name}")'
