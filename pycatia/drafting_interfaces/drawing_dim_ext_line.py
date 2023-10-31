#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DrawingDimExtLine(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimExtLine
                | 
                | Manages extension lines of a dimension in drawing view.
                | 
                | This interface is obtained from DrawingDimension.GetExtLine
                | method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dim_ext_line = com_object

    @property
    def color(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Color() As long
                | 
                |     Returns or sets color of extension line.
                | 
                |     Example:
                |         This example retrieves color of extension line MyExtLine drawing
                |         dimension.
                | 
                |          oColorExtLine = MyExtLine.Color

        :rtype: int
        """

        return self.drawing_dim_ext_line.Color

    @color.setter
    def color(self, value: int):
        """
        :param int value:
        """

        self.drawing_dim_ext_line.Color = value

    @property
    def ext_line_slant(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtLineSlant() As double
                | 
                |     Returns or sets slant angle of extension line.
                | 
                |     Example:
                |         This example retrieves slant angle of extension line MyExtLine drawing
                |         dimension.
                | 
                |          oExtLineSlant = MyExtLine.ExtLineSlant

        :rtype: float
        """

        return self.drawing_dim_ext_line.ExtLineSlant

    @ext_line_slant.setter
    def ext_line_slant(self, value: float):
        """
        :param float value:
        """

        self.drawing_dim_ext_line.ExtLineSlant = value

    @property
    def ext_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExtLineType() As long (Read Only)
                | 
                |     Returns extension line type of dimension.
                | 
                |     Example:
                |         This example retrieves extension line type of dimension MyExtLine
                |         drawing dimension.
                | 
                |          oExtLineType = MyExtLine.ExtLineType

        :rtype: int
        """

        return self.drawing_dim_ext_line.ExtLineType

    @property
    def thickness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Thickness() As double
                | 
                |     Returns or sets thickness of extension line.
                | 
                |     Example:
                |         This example retrieves thickness of extension line MyExtLine drawing
                |         dimension.
                | 
                |          oThickExtLine = MyExtLine.Thickness

        :rtype: float
        """

        return self.drawing_dim_ext_line.Thickness

    @thickness.setter
    def thickness(self, value: float):
        """
        :param float value:
        """

        self.drawing_dim_ext_line.Thickness = value

    def add_interrupt(self, i_index: int, i_two_points: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddInterrupt(long iIndex,
                | CATSafeArrayVariant iTwoPoints)
                | 
                |     Add an interrupt to an extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iTwoPoints
                |             Defines the first and second point of the gap to create.
                |             
                |         Example:
                |             This example adds an interrupt to MyExtLine path.
                | 
                |              MyExtLine.AddInterrupt(iIndex, iTwoPoints)

        :param int i_index:
        :param tuple i_two_points:
        :rtype: None
        """
        return self.drawing_dim_ext_line.AddInterrupt(i_index, i_two_points)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_interrupt'
        # # vba_code = """
        # # Public Function add_interrupt(drawing_dim_ext_line)
        # #     Dim iIndex (2)
        # #     drawing_dim_ext_line.AddInterrupt iIndex
        # #     add_interrupt = iIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_funnel(self, i_index: int, o_mode: int, o_angle: float, o_height: float, o_width: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetFunnel(long iIndex,
                | long oMode,
                | double oAngle,
                | double oHeight,
                | double oWidth)
                | 
                |     Get funnel information of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oMode
                |             funnel inside/outside mode. 
                |         oAngle
                |             funnel angle. 
                |         oHeight
                |             funnel height. 
                |         oWidth
                |             funnel width. 
                |         Example:
                |             This example gets funnel information of MyExtLine
                |             path.
                | 
                |              MyExtLine.GetFunnel(iIndex, oMode, oAngle, oHeight,
                |              oWidth)

        :param int i_index:
        :param int o_mode:
        :param float o_angle:
        :param float o_height:
        :param float o_width:
        :rtype: None
        """
        return self.drawing_dim_ext_line.GetFunnel(i_index, o_mode, o_angle, o_height, o_width)

    def get_gap(self, i_index: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGap(long iIndex) As double
                | 
                |     Get gap of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oGap
                |             Gap. 
                |         Example:
                |             This example gets gap of MyExtLine path.
                | 
                |              Gap = MyExtLine.GetGap(iIndex)

        :param int i_index:
        :rtype: float
        """
        return self.drawing_dim_ext_line.GetGap(i_index)

    def get_geom_info(self, i_index: int, o_geom_infos: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetGeomInfo(long iIndex,
                | CATSafeArrayVariant oGeomInfos)
                | 
                |     Get geometrical information of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oGeomInfos
                |             List of geometric coordinates (X1,Y1,X2,Y2,X3,Y3).
                |             
                |         Example:
                |             This example gets geometrical information of MyExtLine
                |             path.
                | 
                |              MyExtLine.GetGeomInfo(iIndex, oGeomInfos)

        :param int i_index:
        :param tuple o_geom_infos:
        :rtype: None
        """
        return self.drawing_dim_ext_line.GetGeomInfo(i_index, o_geom_infos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_geom_info'
        # # vba_code = """
        # # Public Function get_geom_info(drawing_dim_ext_line)
        # #     Dim iIndex (2)
        # #     drawing_dim_ext_line.GetGeomInfo iIndex
        # #     get_geom_info = iIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_interrupt(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetInterrupt(long iIndex) As long
                | 
                |     Get the number of interruptions stored in each extension
                |     lines.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oNbIntOnExtLine
                |             The number of interruptions. 
                |         Example:
                |             This example gets the number of interruptions of MyExtLine
                |             path.
                | 
                |              NbIntOnExtLine = MyExtLine.GetInterrupt(iIndex)

        :param int i_index:
        :rtype: int
        """
        return self.drawing_dim_ext_line.GetInterrupt(i_index)

    def get_overrun(self, i_index: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetOverrun(long iIndex) As double
                | 
                |     Get overrun of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oOverrun
                |             Overrun 
                |         Example:
                |             This example gets overrun of MyExtLine path.
                | 
                |              Overrun = MyExtLine.GetOverrun(iIndex)

        :param int i_index:
        :rtype: float
        """
        return self.drawing_dim_ext_line.GetOverrun(i_index)

    def get_visibility(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetVisibility(long iIndex) As long
                | 
                |     Get visibility of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         oGap
                |             Gap. 
                |         Example:
                |             This example gets visibility of MyExtLine path.
                | 
                |              ExtlineVisibility = MyExtLine.GetVisibility(iIndex)

        :param int i_index:
        :rtype: int
        """
        return self.drawing_dim_ext_line.GetVisibility(i_index)

    def remove_interrupt(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveInterrupt(long iIndex)
                | 
                |     Remove interruption on extension lines.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         Example:
                |             This example Remove interruption on MyExtLine
                |             path.
                | 
                |              MyExtLine.RemoveInterrupt(iIndex)

        :param int i_index:
        :rtype: None
        """
        return self.drawing_dim_ext_line.RemoveInterrupt(i_index)

    def set_funnel(self, i_index: int, i_mode: int, i_angle: float, i_height: float, i_width: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFunnel(long iIndex,
                | long iMode,
                | double iAngle,
                | double iHeight,
                | double iWidth)
                | 
                |     Set funnel information of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iMode
                |             funnel inside/outside mode. 
                |         iAngle
                |             funnel angle. 
                |         iHeight
                |             funnel height. 
                |         iWidth
                |             funnel width. 
                |         Example:
                |             This example sets funnel information of MyExtLine
                |             path.
                | 
                |              MyExtLine.SetFunnel(iIndex, iMode, iAngle, iHeight,
                |              iWidth)

        :param int i_index:
        :param int i_mode:
        :param float i_angle:
        :param float i_height:
        :param float i_width:
        :rtype: None
        """
        return self.drawing_dim_ext_line.SetFunnel(i_index, i_mode, i_angle, i_height, i_width)

    def set_gap(self, i_index: int, i_gap: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGap(long iIndex,
                | double iGap)
                | 
                |     Set gap of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iGap
                |             gap 
                |         Example:
                |             This example sets gap of MyExtLine path.
                | 
                |              MyExtLine.SetGap(iIndex, iGap)

        :param int i_index:
        :param float i_gap:
        :rtype: None
        """
        return self.drawing_dim_ext_line.SetGap(i_index, i_gap)

    def set_overrun(self, i_index: int, i_overrun: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetOverrun(long iIndex,
                | double iOverrun)
                | 
                |     Set overrun of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iOverrun
                |             Overrun 
                |         Example:
                |             This example sets overrun of MyExtLine path.
                | 
                |              MyExtLine.SetOverrun(iIndex, iOverrun)

        :param int i_index:
        :param float i_overrun:
        :rtype: None
        """
        return self.drawing_dim_ext_line.SetOverrun(i_index, i_overrun)

    def set_visibility(self, i_index: int, i_extline_visibility: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetVisibility(long iIndex,
                | long iExtlineVisibility)
                | 
                |     Set visibility of dimension extension line.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: first extension line 2: second extension line 
                |         iExtlineVisibility
                |             visibility
                |         Example:
                |             This example sets visibility of MyExtLine path.
                | 
                |              MyExtLine.SetVisibility(iIndex,
                |              iExtlineVisibility)

        :param int i_index:
        :param int i_extline_visibility:
        :rtype: None
        """
        return self.drawing_dim_ext_line.SetVisibility(i_index, i_extline_visibility)

    def __repr__(self):
        return f'DrawingDimExtLine(name="{self.name}")'
