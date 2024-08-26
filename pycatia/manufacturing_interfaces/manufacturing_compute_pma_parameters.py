#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingComputePmaParameters(AnyObject):
    """

    Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingComputePMAParameters
                |
                | Interface to compute and get PMA Parameters: - MfgMinimumCornerRadius -
                | MfgMinimumChannelWidth - MfgMaximumChannelWidth - Depth - MfgBottomFilletRadius
                | - BottomColor

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_compute_pma_parameters = com_object

    def compute_parameters(self) -> None:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub ComputeParameters()
                |     This function computes the PMA parameters and stores for 2DMA
                |     feature
                |
                |     Returns:
                |         S_OK or E_FAIL

        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_compute_pma_parameters.ComputeParameters()

    def get_parameter_double_value(self, i_name: str) -> float:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetParameterDoubleValue(CATBSTR iName) As double
                |     Get double parameter
                |
                |     Parameters:
                |
                |         return
                |             double value
                |
                |     Returns:
                |         S_OK or E_FAIL

        :param str i_name:
        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_compute_pma_parameters.GetParameterDoubleValue(i_name)

    def __repr__(self):
        return f'ManufacturingComputePmaParameters(name="{self.name}")'
