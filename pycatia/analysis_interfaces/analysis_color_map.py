#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class AnalysisColorMap(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisColorMap
                | 
                | Represents the Color Map Object of the post-processing Image
                | Object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_color_map = com_object

    @property
    def discrete_mode(self) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DiscreteMode() As CATVariant
                | 
                |     Gets the Discrete mode for the Color Map
                | 
                |     Parameters:
                | 
                |         oDiscreteMode
                |             Output Boolean for the Discrete Mode True : indicates that Discrete mode is enabled for the color map. False: indicates that Discrete mode is disabled for the color map. This Method Returns E_FAIL if the Parent Image is not uptodate. 
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oDiscreteMode = analysisColorMap.DiscreteMode
                |          In this example, oDiscreteMode is the output Discrete Mode for
                |          analysisColorMap.

        :rtype: cat_variant
        """

        return self.analysis_color_map.DiscreteMode

    @discrete_mode.setter
    def discrete_mode(self, value: cat_variant):
        """
        :param cat_variant value:
        """

        self.analysis_color_map.DiscreteMode = value

    @property
    def distribution_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DistributionMode() As SPMDistributionMode
                | 
                |     Gets the Distribution Mode for the Color Map
                | 
                |     Parameters:
                | 
                |         oDistMode
                |             Returns the Distribution Mode (ColorMap type) SPM_LINEAR : For Linear Distribution Mode SPM_HISTOGRAM : For Histogram Distribution Mode SPM_LOG : For Logarithmic Distribution Mode This Method Returns E_FAIL if the Parent Image is not uptodate. 
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oDistMode = analysisColorMap.DistributionMode
                |          In this example, oDistMode is the output distribution mode for
                |          analysisColorMap.

        :return: enum spm_distribution_mode
        :rtype: int
        """

        return self.analysis_color_map.DistributionMode

    @distribution_mode.setter
    def distribution_mode(self, value: int):
        """
        :param int value: enum spm_distribution_mode
        """

        self.analysis_color_map.DistributionMode = value

    @property
    def imposed_max_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImposedMaxValue() As double
                | 
                |     Gets the Imposed Maximum value for the Color Map
                | 
                |     Parameters:
                | 
                |         oMaxValue
                |             Returns Imposed Maximum value Returned value will be in CATIA
                |             Units. This Method Returns E_FAIL if the Parent Image is not uptodate.
                |             
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oMaxValue = analysisColorMap.ImposedMaxValue
                |          In this example, oMaxValue is the output Imposed Maximum value for
                |          analysisColorMap.

        :rtype: float
        """

        return self.analysis_color_map.ImposedMaxValue

    @imposed_max_value.setter
    def imposed_max_value(self, value: float):
        """
        :param float value:
        """

        self.analysis_color_map.ImposedMaxValue = value

    @property
    def imposed_min_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImposedMinValue() As double
                | 
                |     Gets the Imposed Minimum value for the Color Map
                | 
                |     Parameters:
                | 
                |         oMinValue
                |             Returns imposed minimum value Returned value will be in CATIA
                |             Units. This Method Returns E_FAIL if the Parent Image is not uptodate.
                |
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oMinValue = analysisColorMap.ImposedMinValue
                |          In this example, oMinValue is the output Imposed Minimum value for
                |          analysisColorMap.

        :rtype: float
        """

        return self.analysis_color_map.ImposedMinValue

    @imposed_min_value.setter
    def imposed_min_value(self, value: float):
        """
        :param float value:
        """

        self.analysis_color_map.ImposedMinValue = value

    @property
    def inverse_mode(self) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InverseMode() As CATVariant
                | 
                |     Gets the Inverse mode for the Color Map
                | 
                |     Parameters:
                | 
                |         oInverseMode
                |             Output Boolean for the Inverse Mode True : indicates that Inverse mode is enabled for the color map. False: indicates that Inverse mode is disabled for the color map. This Method Returns E_FAIL if the Parent Image is not uptodate. 
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oInverseMode = analysisColorMap.InverseMode
                |          In this example, oInverseMode is the output Inverse Mode for
                |          analysisColorMap.

        :rtype: cat_variant
        """

        return self.analysis_color_map.InverseMode

    @inverse_mode.setter
    def inverse_mode(self, value: cat_variant):
        """
        :param cat_variant value:
        """

        self.analysis_color_map.InverseMode = value

    @property
    def nb_colors(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbColors() As long
                | 
                |     Gets the Number of colors for the Color Map
                | 
                |     Parameters:
                | 
                |         oNbColors
                |             returns number of colors as output from the color map. This Method
                |             Returns E_FAIL if the Parent Image is not uptodate.
                |             
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oNbColors = analysisColorMap.NbColors
                |          In this example, oNbColors is the output Number of colors for
                |          analysisColorMap.

        :rtype: int
        """

        return self.analysis_color_map.NbColors

    @nb_colors.setter
    def nb_colors(self, value: int):
        """
        :param int value:
        """

        self.analysis_color_map.NbColors = value

    @property
    def smooth_mode(self) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SmoothMode() As CATVariant
                | 
                |     Gets the Smooth mode for the Color Map
                | 
                |     Parameters:
                | 
                |         oSmoothMode
                |             Output Boolean for the Smooth Mode True : indicates that Smooth mode is enabled for the color map. False: indicates that Smooth mode is disabled for the color map. This Method Returns E_FAIL if the Parent Image is not uptodate. 
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object oSmoothMode = analysisColorMap.SmoothMode
                |          In this example, oSmoothMode is the output Smooth Mode for
                |          analysisColorMap.

        :rtype: cat_variant
        """

        return self.analysis_color_map.SmoothMode

    @smooth_mode.setter
    def smooth_mode(self, value: cat_variant):
        """
        :param cat_variant value:
        """

        self.analysis_color_map.SmoothMode = value

    def get_distribution_value(self, index_value: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDistributionValue(long indexValue) As double
                | 
                |     Gets the Value for the Distribution of Color Map
                | 
                |     Parameters:
                | 
                |         indexValue
                |             The index whose Value we get. This integer should be greater than 0
                |             and less than NbColors. Else Method Fails. 
                |         oModeValue
                |             Returns the value @param indexValue Returned value will be in CATIA
                |             Units. This Method Returns E_FAIL if the Parent Image is not uptodate.
                |             
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object Set oModeValue = analysisColorMap.GetDistributionValue (3)
                |          In this example, oModeValue is the output value of the Distribution
                |          list at Index 3.

        :param int index_value:
        :rtype: float
        """
        return self.analysis_color_map.GetDistributionValue(index_value)

    def set_distribution_value(self, index_value: int, i_mode_value: float, i_smoothening_flag: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDistributionValue(long indexValue,
                | double iModeValue,
                | CATVariant iSmootheningFlag)
                | 
                |     Sets the Value for the Distribution of Color Map
                | 
                |     Parameters:
                | 
                |         indexValue
                |             The index whose Value will be set. This integer should be greater
                |             than 0 and less than NbColors. Else Method Fails. 
                |         iModeValue
                |             The Value to be set. This value should be in between
                |             Computed/Imposed Min/Max values. Else Method Fails. In addition if @param
                |             iSmootheningFlag is False, this value should be in between the immediate lower
                |             and upper values. Else Method Fails. Value has to be provided in CATIA Units.
                |             
                |         iSmootheningFlag
                |             if True: Does either upper or lower smoothening of values. if
                |             False: Does not smoothen values. But sets only the given index value. This
                |             Method Returns E_FAIL if Color Map is Discrete. 
                | 
                |     Example:
                | 
                |          : analysisColorMap is the ColorMap Object  Example 1:
                | 
                |          Call analysisColorMap.SetDistributionValue(3, 3e+09,
                |          True)
                | 
                |          This sets the value 3e+09 at 3rd Index of the list. It will smoothen
                |          the distribution values
                |          for the color-map object analysisColorMap.
                |          Should be in between Computed/Imposed Min/Max values.
                |          
                |          Example 2:
                | 
                |          Call analysisColorMap.SetDistributionValue(3, 10e+09,
                |          False)
                | 
                |          This sets the value 10e+09 at 3rd Index of the list. It will not
                |          smoothen the distribution
                |          for the color-map object analysisColorMap.
                |          10e+09 should be greater than Index 2 value and lesser than Index 4
                |          value.
                |          Should be in between Computed/Imposed Min/Max values.

        :param int index_value:
        :param float i_mode_value:
        :param cat_variant i_smoothening_flag:
        :rtype: None
        """
        return self.analysis_color_map.SetDistributionValue(index_value, i_mode_value, i_smoothening_flag)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_distribution_value'
        # # vba_code = """
        # # Public Function set_distribution_value(analysis_color_map)
        # #     Dim indexValue (2)
        # #     analysis_color_map.SetDistributionValue indexValue
        # #     set_distribution_value = indexValue
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Update()
                | 
                |     Updates the visualization of the color map. This method should be called
                |     after one or all previous PUT methods are called on Color Map.

        :rtype: None
        """
        return self.analysis_color_map.Update()

    def __repr__(self):
        return f'AnalysisColorMap(name="{self.name}")'
