#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DrawingDimValue(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimValue
                | 
                | Manages dimension value of a dimension in drawing view.
                | 
                | This interface is obtained from DrawingDimension.GetValue
                | method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dim_value = com_object

    @property
    def fake_dim_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FakeDimType() As CatDimFake
                | 
                |     Returns or sets fake dimension type of value.
                | 
                |     Example:
                |         This example retrieves fake dimension type of value MyDimValue drawing
                |         dimension.
                | 
                |          oFakeType = MyDimValue.FakeDimType

        :return: enum cat_dim_fake
        :rtype: int
        """

        return self.drawing_dim_value.FakeDimType

    @fake_dim_type.setter
    def fake_dim_type(self, value: int):
        """
        :param int value: enum cat_dim_fake
        """

        self.drawing_dim_value.FakeDimType = value

    @property
    def scoring_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ScoringMode() As CatDimScore
                | 
                |     Get dimension scoring mode. 
                | Example:
                |     This example gets dimension scoring mode of MyValue path.
                | 
                |      ValueScoreType = MyValue.ScoringMode

        :return: enum cat_dim_score
        :rtype: int
        """

        return self.drawing_dim_value.ScoringMode

    @scoring_mode.setter
    def scoring_mode(self, value: int):
        """
        :param int value: enum cat_dim_score
        """

        self.drawing_dim_value.ScoringMode = value

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Value() As double (Read Only)
                | 
                |     Returns value of dimension.
                | 
                |     Example:
                |         This example retrieves value of dimension MyDimValue drawing
                |         dimension.
                | 
                |          oValue = MyDimValue.Value

        :rtype: float
        """

        return self.drawing_dim_value.Value

    @property
    def value_framed_element(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ValueFramedElement() As CatDimFramedElement
                | 
                |     Get dimension framed element. 
                | Example:
                |     This example gets dimension framed element of MyValue
                |     path.
                | 
                |      ValueFramedElement = MyValue.ValueFramedElement

        :return: enum cat_dim_frame_element
        :rtype: int
        """

        return self.drawing_dim_value.ValueFramedElement

    @value_framed_element.setter
    def value_framed_element(self, value: int):
        """
        :param int value: enum cat_dim_frame_element
        """

        self.drawing_dim_value.ValueFramedElement = value

    @property
    def value_framed_group(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ValueFramedGroup() As CatDimFramedGroup
                | 
                |     Returns or sets dimension framed group.
                | 
                |     Example:
                |         This example retrieves dimension framed group MyDimValue drawing
                |         dimension.
                | 
                |          oValueFramedGroup = MyDimValue.FakeDimType

        :return: enum cat_dim_framed_group
        :rtype: int
        """

        return self.drawing_dim_value.ValueFramedGroup

    @value_framed_group.setter
    def value_framed_group(self, value: int):
        """
        :param int value: enum cat_dim_framed_group
        """

        self.drawing_dim_value.ValueFramedGroup = value

    def get_bault_text(self, i_index: int, o_before: str, o_after: str, o_upper: str, o_lower: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetBaultText(long iIndex,
                | CATBSTR oBefore,
                | CATBSTR oAfter,
                | CATBSTR oUpper,
                | CATBSTR oLower)
                | 
                |     Get bault text of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oBefore
                |             before text. 
                |         oAfter
                |             after text 
                |         oUpper
                |             upper text 
                |         oLower
                |             lower text 
                |         Example:
                |             This example gets bault text of MyValue path.
                | 
                |              MyValue.GetBaultText(iIndex, oBefore, oAfter, oUpper,
                |              oLower)

        :param int i_index:
        :param str o_before:
        :param str o_after:
        :param str o_upper:
        :param str o_lower:
        :rtype: None
        """
        return self.drawing_dim_value.GetBaultText(i_index, o_before, o_after, o_upper, o_lower)

    def get_display_unit(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDisplayUnit(long iIndex) As long
                | 
                |     Get display unit of dimension value.
                | 
                |     Parameters:
                | 
                |         Index
                |             1: main value 2: dual value 
                |         oDisplUnit
                |             before text. 
                |         Example:
                |             This example gets format unit of MyValue path.
                | 
                |              FrmUnit = MyValue.GetDisplayUnit(iIndex)

        :param int i_index:
        :rtype: int
        """
        return self.drawing_dim_value.GetDisplayUnit(i_index)

    def get_fake_dim_value(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFakeDimValue(long iIndex) As CATBSTR
                | 
                |     Get fake value of dimension.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oFakeDimValue
                |             before text. 
                |         Example:
                |             This example gets fake value of MyValue path.
                | 
                |              FakeDimValue = MyValue.GetFakeDimValue(iIndex)

        :param int i_index:
        :rtype: str
        """
        return self.drawing_dim_value.GetFakeDimValue(i_index)

    def get_format_display_factor(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFormatDisplayFactor(long iIndex) As long
                | 
                |     Get format display factor of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oFrmDspFact
                |             before text. 
                |         Example:
                |             This example gets format display factor of MyValue
                |             path.
                | 
                |              FrmDspFact = MyValue.GetFormatDisplayFactor(iIndex)

        :param int i_index:
        :rtype: int
        """
        return self.drawing_dim_value.GetFormatDisplayFactor(i_index)

    def get_format_name(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFormatName(long iIndex) As CATBSTR
                | 
                |     Get format name of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oFmName
                |             before text. 
                |         Example:
                |             This example gets format name of MyValue path.
                | 
                |              FmName = MyValue.GetFormatName(iIndex)

        :param int i_index:
        :rtype: str
        """
        return self.drawing_dim_value.GetFormatName(i_index)

    def get_format_precision(self, index: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFormatPrecision(long Index) As double
                | 
                |     Get format precision of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oFrmPrecision
                |             before text. 
                |         Example:
                |             This example gets format precision of MyValue
                |             path.
                | 
                |              FrmPrecision = MyValue.GetFormatPrecision(iIndex)

        :param int index:
        :rtype: float
        """
        return self.drawing_dim_value.GetFormatPrecision(index)

    def get_format_type(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFormatType(long iIndex) As long
                | 
                |     Get format type of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oFrmType
                |             before text. 
                |         Example:
                |             This example gets format type of MyValue path.
                | 
                |              FrmType = MyValue.GetFormatType(iIndex)

        :param int i_index:
        :rtype: int
        """
        return self.drawing_dim_value.GetFormatType(i_index)

    def get_format_unit(self, i_index: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFormatUnit(long iIndex) As long
                | 
                |     Get format unit of dimension value.
                | 
                |     Parameters:
                | 
                |         Index
                |             1: main value 2: dual value 
                |         oFrmUnit
                |             before text. 
                |         Example:
                |             This example gets format unit of MyValue path.
                | 
                |              FrmUnit = MyValue.GetFormatUnit(iIndex)

        :param int i_index:
        :rtype: int
        """
        return self.drawing_dim_value.GetFormatUnit(i_index)

    def get_ps_text(self, i_index: int, o_prefix: str, o_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPSText(long iIndex,
                | CATBSTR oPrefix,
                | CATBSTR oSuffix)
                | 
                |     Get PS text to dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oPrefix
                |             prefix text. 
                |         oSuffix
                |             suffix text 
                |         Example:
                |             This example gets PS text of MyValue path.
                | 
                |              MyValue.GetBaultText(iIndex, oPrefix, oSuffix)

        :param int i_index:
        :param str o_prefix:
        :param str o_suffix:
        :rtype: None
        """
        return self.drawing_dim_value.GetPSText(i_index, o_prefix, o_suffix)

    def get_scored_element(self, i_index: int) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetScoredElement(long iIndex) As boolean
                | 
                |     Get dimension scored element.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         oScoredElement
                |             TRUE: Scoring is applied to the all bloc text. FALSE: Scoring is
                |             only applied to the value. 
                |         Example:
                |             This example gets dimension scored element of MyValue
                |             path.
                | 
                |              ScoredElement = MyValue.GetScoredElement(iIndex)

        :param int i_index:
        :rtype: bool
        """
        return self.drawing_dim_value.GetScoredElement(i_index)

    def set_bault_text(self, i_index: int, i_before: str, i_after: str, i_upper: str, i_lower: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetBaultText(long iIndex,
                | CATBSTR iBefore,
                | CATBSTR iAfter,
                | CATBSTR iUpper,
                | CATBSTR iLower)
                | 
                |     Set bault text to dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iBefore
                |             before text. 
                |         iAfter
                |             after text 
                |         iUpper
                |             upper text 
                |         iLower
                |             lower text 
                |         Example:
                |             This example sets bault text of MyValue path.
                | 
                |              MyValue.SetBaultText(iIndex, iBefore, iAfter, iUpper,
                |              iLower)

        :param int i_index:
        :param str i_before:
        :param str i_after:
        :param str i_upper:
        :param str i_lower:
        :rtype: None
        """
        return self.drawing_dim_value.SetBaultText(i_index, i_before, i_after, i_upper, i_lower)

    def set_fake_dim_value(self, i_index: int, i_fake_dim_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFakeDimValue(long iIndex,
                | CATBSTR iFakeDimValue)
                | 
                |     Set fake value of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iFakeDimValue
                |             before text. 
                |         Example:
                |             This example gets fake value of MyValue path.
                | 
                |              MyValue.SetFakeDimValue(iIndex, iFakeDimValue)

        :param int i_index:
        :param str i_fake_dim_value:
        :rtype: None
        """
        return self.drawing_dim_value.SetFakeDimValue(i_index, i_fake_dim_value)

    def set_format_display_factor(self, i_index: int, i_frm_dsp_fact: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFormatDisplayFactor(long iIndex,
                | long iFrmDspFact)
                | 
                |     Set format display factor of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iFrmDspFact
                |             before text. 
                |         Example:
                |             This example gets format display factor of MyValue
                |             path.
                | 
                |              MyValue.SetFormatDisplayFactor(iIndex,
                |              iFrmDspFact)

        :param int i_index:
        :param int i_frm_dsp_fact:
        :rtype: None
        """
        return self.drawing_dim_value.SetFormatDisplayFactor(i_index, i_frm_dsp_fact)

    def set_format_name(self, i_index: int, i_frm_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFormatName(long iIndex,
                | CATBSTR iFrmName)
                | 
                |     Set format name of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iFrmName
                |             before text. 
                |         Example:
                |             This example gets format name of MyValue path.
                | 
                |              MyValue.SetFormatName(iIndex, iFrmName)

        :param int i_index:
        :param str i_frm_name:
        :rtype: None
        """
        return self.drawing_dim_value.SetFormatName(i_index, i_frm_name)

    def set_format_precision(self, i_index: int, i_frm_precision: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFormatPrecision(long iIndex,
                | double iFrmPrecision)
                | 
                |     Set format precision of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iFrmPrecision
                |             before text. 
                |         Example:
                |             This example gets format precision of MyValue
                |             path.
                | 
                |              MyValue.SetFormatPrecision(iIndex, iFrmPrecision)

        :param int i_index:
        :param float i_frm_precision:
        :rtype: None
        """
        return self.drawing_dim_value.SetFormatPrecision(i_index, i_frm_precision)

    def set_format_type(self, i_index: int, i_frm_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFormatType(long iIndex,
                | long iFrmType)
                | 
                |     Set format type of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iFrmType
                |             before text. 
                |         Example:
                |             This example gets format type of MyValue path.
                | 
                |              MyValue.SetFormatType(iIndex, iFrmType)

        :param int i_index:
        :param int i_frm_type:
        :rtype: None
        """
        return self.drawing_dim_value.SetFormatType(i_index, i_frm_type)

    def set_format_unit(self, i_index: int, i_frm_unit: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFormatUnit(long iIndex,
                | long iFrmUnit)
                | 
                |     Set format unit of dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iFrmUnit
                |             before text. 
                |         Example:
                |             This example gets format unit of MyValue path.
                | 
                |              MyValue.SetFormatUnit(iIndex, iFrmUnit)

        :param int i_index:
        :param int i_frm_unit:
        :rtype: None
        """
        return self.drawing_dim_value.SetFormatUnit(i_index, i_frm_unit)

    def set_ps_text(self, i_index: int, i_prefix: str, i_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPSText(long iIndex,
                | CATBSTR iPrefix,
                | CATBSTR iSuffix)
                | 
                |     Set PS text to dimension value.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iPrefix
                |             prefix text. 
                |         iSuffix
                |             suffix text 
                |         Example:
                |             This example sets PS text of MyValue path.
                | 
                |              MyValue.SetBaultText(iIndex, iPrefix, iSuffix)

        :param int i_index:
        :param str i_prefix:
        :param str i_suffix:
        :rtype: None
        """
        return self.drawing_dim_value.SetPSText(i_index, i_prefix, i_suffix)

    def set_scored_element(self, i_index: int, i_scored_element: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetScoredElement(long iIndex,
                | boolean iScoredElement)
                | 
                |     Set dimension scored element.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             1: main value 2: dual value 
                |         iScoredElement
                |             TRUE: Scoring is applied to the all bloc text. FALSE: Scoring is
                |             only applied to the value. 
                |         Example:
                |             This example gets dimension scored element of MyValue
                |             path.
                | 
                |              MyValue.SetScoredElement(iIndex, iScoredElement)

        :param int i_index:
        :param bool i_scored_element:
        :rtype: None
        """
        return self.drawing_dim_value.SetScoredElement(i_index, i_scored_element)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_scored_element'
        # # vba_code = """
        # # Public Function set_scored_element(drawing_dim_value)
        # #     Dim iIndex (2)
        # #     drawing_dim_value.SetScoredElement iIndex
        # #     set_scored_element = iIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DrawingDimValue(name="{self.name}")'
