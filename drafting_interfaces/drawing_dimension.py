#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_dim_ext_line import DrawingDimExtLine
from pycatia.drafting_interfaces.drawing_dim_line import DrawingDimLine
from pycatia.drafting_interfaces.drawing_dim_value import DrawingDimValue
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.system_interfaces.any_object import AnyObject


class DrawingDimension(AnyObject):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimension
                | 
                | Represents a drawing dimension in a Drawing view.
                | 
                | Returns sub parts of dimension: Extension lines, dimension line and dimension
                | value.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dimension = com_object

    @property
    def cumulate_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CumulateMode() As boolean (Read Only)
                | 
                |     Returns cumulate mode or not.
                | 
                |     Example:
                |         This example retrieves cumulate mode or not MyDimension drawing
                |         dimension.
                | 
                |          oCumulateMode = MyDimension.CumulateMode

        :return: bool
        """

        return self.drawing_dimension.CumulateMode

    @property
    def dim_status(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DimStatus() As CatDimAnalyse (Read Only)
                | 
                |     Returns or sets status of dimension.
                | 
                |     Example:
                |         This example retrieves status of dimension MyDimension drawing
                |         dimension.
                | 
                |          oIsStatus = MyDimension.DimStatus

        :return: enum cat_dim_analyse
        """

        return self.drawing_dimension.DimStatus

    @property
    def dim_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DimType() As CatDimType (Read Only)
                | 
                |     Returns dimension type.
                | 
                |     Example:
                |         This example retrieves the dimension type MyDimension drawing
                |         dimension.
                | 
                |          oTypeDim = MyDimension.DimType

        :return: enum cat_dim_type
        """

        return self.drawing_dimension.DimType

    @property
    def dual_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DualValue() As CatDimDualDisplay
                | 
                |     Returns or sets dual value type of dimension value.
                | 
                |     Example:
                |         This example retrieves dual value type of dimension value MyDimension
                |         drawing dimension.
                | 
                |          oDualValue = MyDimension.DualValue

        :return: enum cat_dim_dual_display
        """

        return self.drawing_dimension.DualValue

    @dual_value.setter
    def dual_value(self, value):
        """
        :param enum cat_dim_dual_display value:
        """

        self.drawing_dimension.DualValue = value

    @property
    def forshortened(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Forshortened() As boolean
                | 
                |     Returns or sets foreshortened mode or not.
                | 
                |     Example:
                |         This example retrieves foreshortened mode or not MyDimension drawing
                |         dimension.
                | 
                |          oForsh = MyDimension.Forshortened

        :return: bool
        """

        return self.drawing_dimension.Forshortened

    @forshortened.setter
    def forshortened(self, value):
        """
        :param bool value:
        """

        self.drawing_dimension.Forshortened = value

    @property
    def half_dim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HalfDimMode() As boolean
                | 
                |     Returns or sets half dimension mode or not.
                | 
                |     Example:
                |         This example retrieves half dimension mode or not MyDimension drawing
                |         dimension.
                | 
                |          oHalfDimMode = MyDimension.HalfDimMode

        :return: bool
        """

        return self.drawing_dimension.HalfDimMode

    @half_dim_mode.setter
    def half_dim_mode(self, value):
        """
        :param bool value:
        """

        self.drawing_dimension.HalfDimMode = value

    @property
    def is_clipped(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property IsClipped() As boolean (Read Only)
                | 
                |     Returns the clipping status of the dimension. Returns TRUE if the dimension
                |     si clipped 
                | Example:
                |     This example gets clipping status of MyDimension path.
                | 
                |      myDimmensionClippingStatus=MyDimension.IsClipped

        :return: bool
        """

        return self.drawing_dimension.IsClipped

    @property
    def nb_ext_line(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NbExtLine() As long (Read Only)
                | 
                |     Returns numbers of extension line of dimension.
                | 
                |     Example:
                |         This example retrieves numbers of extension line of dimension
                |         MyDimension drawing dimension.
                | 
                |          oNbExtline = MyDimension.NbExtLine

        :return: int
        """

        return self.drawing_dimension.NbExtLine

    @property
    def nb_symb(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NbSymb() As long (Read Only)
                | 
                |     Returns numbers of symbol of dimension.
                | 
                |     Example:
                |         This example retrieves numbers of symbol of dimension MyDimension
                |         drawing dimension.
                | 
                |          oNbSymb = MyDimension.NbSymb

        :return: int
        """

        return self.drawing_dimension.NbSymb

    @property
    def parameters(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Parameters() As Parameters (Read Only)
                | 
                |     Returns the collection of parameters of the dimension.
                |     Warning: The returned parameters collection does not support adding
                |     parameters, it is mainly provided to access dimension
                |     value.
                | 
                |     Example:
                | 
                |           This example retrieves in DimensionParameters the collection
                |           of
                |          parameters currently managed by a dimension.
                |          
                | 
                |          Dim DimensionParameters As Parameters
                |          Set DimensionParameters = MyDimension.Parameters
                |          Dim DimValueParameter As Parameter
                |          Set DimValueParameter = DimensionParameters.Item("Measured length")

        :return: Parameters
        """

        return Parameters(self.drawing_dimension.Parameters)

    @property
    def symbols_side(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SymbolsSide() As long
                | 
                |     Returns or sets symbol side of dimension line. Legal values: 0 : Automatic positioning (Inside or Outside). 1 : Symbols are inside. 2 : Symbols are outside. 3 : First symbol inside , second symbol outside. 4 : First symbol outsise, second symbol inside.
                | 
                |     Example:
                |         This example retrieves symbol side of dimension line MyDimension
                |         drawing dimension.
                | 
                |          oSymbSide = MyDimension.SymbolsSide

        :return: int
        """

        return self.drawing_dimension.SymbolsSide

    @symbols_side.setter
    def symbols_side(self, value):
        """
        :param int value:
        """

        self.drawing_dimension.SymbolsSide = value

    @property
    def true_dim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TrueDimMode() As boolean (Read Only)
                | 
                |     Returns or sets true dimension mode or not.
                | 
                |     Example:
                |         This example retrieves true dimension mode or not MyDimension drawing
                |         dimension.
                | 
                |          oTrueDimMode = MyDimension.TrueDimMode

        :return: bool
        """

        return self.drawing_dimension.TrueDimMode

    @property
    def value_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueAngle() As double
                | 
                |     Returns or sets angle of dimension value.
                | 
                |     Example:
                |         This example retrieves angle of dimension value MyDimension drawing
                |         dimension.
                | 
                |          oValueAng = MyDimension.ValueAngle

        :return: float
        """

        return self.drawing_dimension.ValueAngle

    @value_angle.setter
    def value_angle(self, value):
        """
        :param float value:
        """

        self.drawing_dimension.ValueAngle = value

    @property
    def value_auto_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueAutoMode() As long
                | 
                |     Returns or sets auto mode of dimension value or not.
                | 
                |     Example:
                |         This example retrieves auto mode of dimension value or not MyDimension
                |         drawing dimension.
                | 
                |          oValueAutoMode = MyDimension.ValueAutoMode

        :return: int
        """

        return self.drawing_dimension.ValueAutoMode

    @value_auto_mode.setter
    def value_auto_mode(self, value):
        """
        :param int value:
        """

        self.drawing_dimension.ValueAutoMode = value

    @property
    def value_display(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueDisplay() As long
                | 
                |     Returns or sets display of dimension value state.
                | 
                |     Example:
                |         This example retrieves display of dimension value state MyDimension
                |         drawing dimension.
                | 
                |          oValueDisplay = MyDimension.ValueDisplay

        :return: int
        """

        return self.drawing_dimension.ValueDisplay

    @value_display.setter
    def value_display(self, value):
        """
        :param int value:
        """

        self.drawing_dimension.ValueDisplay = value

    @property
    def value_frame(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueFrame() As CatDimFrame
                | 
                |     Returns or sets frame type of dimension value.
                | 
                |     Example:
                |         This example retrieves frame type of dimension value MyDimension
                |         drawing dimension.
                | 
                |          oValueFrame = MyDimension.ValueFrame

        :return: enum cat_dim_frame
        """

        return self.drawing_dimension.ValueFrame

    @value_frame.setter
    def value_frame(self, value):
        """
        :param enum cat_dim_frame value:
        """

        self.drawing_dimension.ValueFrame = value

    @property
    def value_in_out(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueInOut() As long
                | 
                |     Returns or sets in/out mode of dimension value or not.
                | 
                |     Example:
                |         This example retrieves in/out mode of dimension value or not
                |         MyDimension drawing dimension.
                | 
                |          oInOut = MyDimension.ValueInOut

        :return: int
        """

        return self.drawing_dimension.ValueInOut

    @value_in_out.setter
    def value_in_out(self, value):
        """
        :param int value:
        """

        self.drawing_dimension.ValueInOut = value

    @property
    def value_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueOrientation() As CatDimOrientation
                | 
                |     Returns or sets orientation of dimension value.
                | 
                |     Example:
                |         This example retrieves orientation of dimension value MyDimension
                |         drawing dimension.
                | 
                |          oValueOrient = MyDimension.ValueOrientation

        :return: enum cat_dim_orientation
        """

        return self.drawing_dimension.ValueOrientation

    @value_orientation.setter
    def value_orientation(self, value):
        """
        :param enum cat_dim_orientation value:
        """

        self.drawing_dimension.ValueOrientation = value

    @property
    def value_reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ValueReference() As CatDimReference
                | 
                |     Returns or sets reference of dimension value.
                | 
                |     Example:
                |         This example retrieves reference of dimension value MyDimension drawing
                |         dimension.
                | 
                |          oValueRef = MyDimension.ValueReference

        :return: enum cat_dim_reference
        """

        return self.drawing_dimension.ValueReference

    @value_reference.setter
    def value_reference(self, value):
        """
        :param enum cat_dim_reference value:
        """

        self.drawing_dimension.ValueReference = value

    def get_boundary_box(self, o_values=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetBoundaryBox(CATSafeArrayVariant oValues)
                | 
                |     Get boundary box coordinates of dimension value.
                | 
                |     Parameters:
                | 
                |         oValues
                |             List of boundary box coordinates (X1,Y1,X2,Y2,.....X4,Y4).
                |             
                |         Example:
                |             This example gets boundary box coordinates of MyDimension
                |             path.
                | 
                |              MyDimension.GetBoundaryBox(oValues)

        :param tuple o_values:
        :return: None
        """
        return self.drawing_dimension.GetBoundaryBox(o_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_boundary_box'
        # # vba_code = """
        # # Public Function get_boundary_box(drawing_dimension)
        # #     Dim oValues (2)
        # #     drawing_dimension.GetBoundaryBox oValues
        # #     get_boundary_box = oValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_clip(self, x=None, y=None, o_kept_side=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetClip(double X,
                | double Y,
                | long oKeptSide)
                | 
                |     Gets informations of the dimension clipping. The value of this parameter
                |     can be 1 or 2, and the kept side will be the one corresponding respectively to
                |     ptldc1 and ptldc2 from GetGeomInfo method defined in CATIADrawingDimensionLine
                |     idl interface. interface. If iKeptSide==0, there is no dimension
                |     clipping.
                | 
                |     Parameters:
                | 
                |         oX
                |             X coordinate of position. 
                |         oY
                |             Y coordinate of position. 
                |         oKeptSide
                |             returns the part of the dimension line will be clipped.
                |             
                |         Example:
                | 
                |              if MyDimension.IsClipped then
                |                MyDimension.GetClip(X, Y, keptSide)
                |              end if

        :param float x:
        :param float y:
        :param int o_kept_side:
        :return: None
        """
        return self.drawing_dimension.GetClip(x, y, o_kept_side)

    def get_dim_ext_line(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDimExtLine() As DrawingDimExtLine
                | 
                |     Returns the drawing extension line of the drawing
                |     dimension.
                | 
                |     Example:
                |         This example retrieves in DimExtLine extension line of the MyDimension
                |         drawing dimension.
                | 
                |          Dim DimExtLine As DrawingDimExtLine
                |          Set DimExtLine = MyDimension.GetDimExtLine
                |          
                | 
                |     See also:
                |         DrawingDimLine

        :return: DrawingDimExtLine
        """
        return DrawingDimExtLine(self.drawing_dimension.GetDimExtLine())

    def get_dim_line(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDimLine() As DrawingDimLine
                | 
                |     Returns the drawing dimension line of the drawing
                |     dimension.
                | 
                |     Example:
                |         This example retrieves in DimDimLine dimension line of the MyDimension
                |         drawing dimension.
                | 
                |          Dim DimDimLine As DrawingDimLine
                |          Set DimDimLine = MyDimension.GetDimLine
                |          
                | 
                |     See also:
                |         DrawingDimLine

        :return: DrawingDimLine
        """
        return DrawingDimLine(self.drawing_dimension.GetDimLine())

    def get_tolerances(self, o_tol_type=None, o_tol_name=None, o_up_tol=None, o_low_tol=None, od_up_tol=None, od_low_tol=None, o_display_mode=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetTolerances(long oTolType,
                | CATBSTR oTolName,
                | CATBSTR oUpTol,
                | CATBSTR oLowTol,
                | double odUpTol,
                | double odLowTol,
                | long oDisplayMode)
                | 
                |     Get tolerance infomation of dimension value.
                | 
                |     Parameters:
                | 
                |         oTolType
                |             Tolerance type 
                |         oTolName
                |             Tolerance name 
                |         oUpTol
                |             Upper tolerance value (alpha numerical type) 
                |         oLowTol
                |             Lower tolerance value (alpha numerical type) 
                |         odUpTol
                |             Upper tolerance value (numerical type) 
                |         odLowTol
                |             Lower tolerance value (numerical type) 
                |         oDisplayMode
                |             Tolerance display mode 
                |         Example:
                |             This example gets tolerance infomation of MyDimension
                |             path.
                | 
                |              MyDimension.GetTolerances(oTolType, oTolName, oUpTol, oLowTol,
                |              odUpTol, odLowTol, oDisplayMode)

        :param int o_tol_type:
        :param str o_tol_name:
        :param str o_up_tol:
        :param str o_low_tol:
        :param float od_up_tol:
        :param float od_low_tol:
        :param int o_display_mode:
        :return: None
        """
        return self.drawing_dimension.GetTolerances(o_tol_type, o_tol_name, o_up_tol, o_low_tol, od_up_tol, od_low_tol, o_display_mode)

    def get_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetValue() As DrawingDimValue
                | 
                |     Returns the drawing value of the drawing dimension.
                | 
                |     Example:
                |         This example retrieves in DimDimValue value of the MyDimension drawing
                |         dimension.
                | 
                |          Dim DimDimValue As DrawingDimValue
                |          Set DimDimValue = MyDimension.GetValue
                |          
                | 
                |     See also:
                |         DrawingDimValue

        :return: DrawingDimValue
        """
        return DrawingDimValue(self.drawing_dimension.GetValue())

    def move_value(self, x=None, y=None, sub_part=None, dim_angle_behavior=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub MoveValue(double X,
                | double Y,
                | long SubPart,
                | long DimAngleBehavior)
                | 
                |     Move dimension value.
                | 
                |     Parameters:
                | 
                |         X
                |             X coordinate of position. 
                |         Y
                |             Y coordinate of position. 
                |         SubPart
                |             Defines which part of the dimension should be
                |             moved.
                |             -1 = Value (vertical move is take account according ptPos coordinates)
                |             0 = Both dimension line and value
                |             1 = Value
                |             2 = Dimension line
                |             3 = Secondary part
                |             4 = Secondary part and value
                |             5 = Secondary part and dimension line
                |             6 = Secondary part, dimension line and value
                |             7 = Value leader (for dimension line with leader one part or two parts) 
                |         DimAngleBehavior
                |             Defines angle dimension line behavior.
                |             0 = Sector angle is switched when ptPos is in opposite sector (Default)
                |             1 = Sector angle is kept what ever ptPos placement 
                |         Example:
                |             This example move dimension value MyDimension
                |             path.
                | 
                |              MyDimension.MoveValue(X, Y, SubPart,
                |              DimAngleBehavior)

        :param float x:
        :param float y:
        :param int sub_part:
        :param int dim_angle_behavior:
        :return: None
        """
        return self.drawing_dimension.MoveValue(x, y, sub_part, dim_angle_behavior)

    def restore_value_position(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RestoreValuePosition()
                | 
                |     Restore dimension value position. 
                | Example:
                |     This example gets Restore dimension value position of MyDimension
                |     path.
                | 
                |      MyDimension.RestoreValuePosition()

        :return: None
        """
        return self.drawing_dimension.RestoreValuePosition()

    def set_clip(self, x=None, y=None, i_kept_side=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetClip(double X,
                | double Y,
                | long iKeptSide)
                | 
                |     Creates a clip on the dimension at the given point, with respect to the
                |     side given by iKeptSide. The value of this parameter can be 1 or 2, and the
                |     kept side will be the one corresponding respectively to ptldc1 and ptldc2 from
                |     GetGeomInfo method defined in CATIADrawingDimensionLine idl interface.
                |     interface.
                | 
                |     Parameters:
                | 
                |         iX
                |             X coordinate of position. 
                |         iY
                |             Y coordinate of position. 
                |         iKeptSide
                |             Defines which part of the dimension should be kept.
                |             
                |         Example:
                |             This example clips dimension MyDimension path.
                | 
                |              MyDimension.SetClip(X, Y, 1)

        :param float x:
        :param float y:
        :param int i_kept_side:
        :return: None
        """
        return self.drawing_dimension.SetClip(x, y, i_kept_side)

    def set_tolerances(self, i_tol_type=None, itol_name=None, i_up_tol=None, i_low_tol=None, id_up_tol=None, id_low_tol=None, display_mode=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetTolerances(long iTolType,
                | CATBSTR itolName,
                | CATBSTR iUpTol,
                | CATBSTR iLowTol,
                | double idUpTol,
                | double idLowTol,
                | long DisplayMode)
                | 
                |     Set tolerance infomation of dimension value.
                | 
                |     Parameters:
                | 
                |         iTolType
                |             Tolerance type 
                |         itolName
                |             Tolerance name 
                |         iUpTol
                |             Upper tolerance value (alpha numerical type) 
                |         iLowTol
                |             Lower tolerance value (alpha numerical type) 
                |         idUpTol
                |             Upper tolerance value (numerical type) 
                |         idLowTol
                |             Lower tolerance value (numerical type) 
                |         DisplayMode
                |             Tolerance display mode 
                |         Example:
                |             This example sets tolerance infomation of MyDimension
                |             path.
                | 
                |              MyDimension.SetTolerances(iTolType, itolName, iUpTol, iLowTol,
                |              idUpTol, idLowTol, DisplayMode)

        :param int i_tol_type:
        :param str itol_name:
        :param str i_up_tol:
        :param str i_low_tol:
        :param float id_up_tol:
        :param float id_low_tol:
        :param int display_mode:
        :return: None
        """
        return self.drawing_dimension.SetTolerances(i_tol_type, itol_name, i_up_tol, i_low_tol, id_up_tol, id_low_tol, display_mode)

    def unclip(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Unclip()
                | 
                |     Unclip the dimension if it is clipped. 
                | Example:
                |     This example unclip MyDimension path.
                | 
                |      if MyDimension.IsClipped then
                |        MyDimension.Unclip

        :return: None
        """
        return self.drawing_dimension.Unclip()

    def __repr__(self):
        return f'DrawingDimension(name="{ self.name }")'
