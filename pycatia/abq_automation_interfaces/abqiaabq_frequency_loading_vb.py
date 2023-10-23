#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_load import ABQLoad


class ABQIAABQFrequencyLoadingVB(ABQLoad):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQLoad
                |                         ABQIAABQFrequencyLoadingVB
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement ABQIAABQFrequencyLoading are
                | ...
                | 
                | Do not use the ABQIAABQFrequencyLoading interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abqiaabq_frequency_loading_vb = com_object

    @property
    def dof(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DOF() As double

        :rtype: float
        """

        return self.abqiaabq_frequency_loading_vb.DOF

    @dof.setter
    def dof(self, value: float):
        """
        :param float value:
        """

        self.abqiaabq_frequency_loading_vb.DOF = value

    @property
    def data_type(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DataType() As boolean

        :rtype: bool
        """

        return self.abqiaabq_frequency_loading_vb.DataType

    @data_type.setter
    def data_type(self, value: bool):
        """
        :param bool value:
        """

        self.abqiaabq_frequency_loading_vb.DataType = value

    @property
    def frequency_data_values(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FrequencyDataValues(CATSafeArrayVariant iFreqDataVal) (Write
                | Only)

        :rtype: int
        """

        return self.abqiaabq_frequency_loading_vb.FrequencyDataValues

    @frequency_data_values.setter
    def frequency_data_values(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_frequency_loading_vb.FrequencyDataValues = value

    @property
    def imaginary_data_values(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImaginaryDataValues(CATSafeArrayVariant iImaginaryDataValues)
                | (Write Only)

        :rtype: int
        """

        return self.abqiaabq_frequency_loading_vb.ImaginaryDataValues

    @imaginary_data_values.setter
    def imaginary_data_values(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_frequency_loading_vb.ImaginaryDataValues = value

    @property
    def real_data_values(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RealDataValues(CATSafeArrayVariant iRealDataVal) (Write
                | Only)

        :rtype: int
        """

        return self.abqiaabq_frequency_loading_vb.RealDataValues

    @real_data_values.setter
    def real_data_values(self, value: int):
        """
        :param int value:
        """

        self.abqiaabq_frequency_loading_vb.RealDataValues = value

    @property
    def scale(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Scale() As double

        :rtype: float
        """

        return self.abqiaabq_frequency_loading_vb.Scale

    @scale.setter
    def scale(self, value: float):
        """
        :param float value:
        """

        self.abqiaabq_frequency_loading_vb.Scale = value

    def __repr__(self):
        return f'ABQIAABQFrequencyLoadingVB(name="{self.name}")'
