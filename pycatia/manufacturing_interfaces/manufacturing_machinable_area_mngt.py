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


class ManufacturingMachinableAreaMngt(AnyObject):
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
                |                     ManufacturingMachinableAreaMngt
                |
                | Interface dedicated to machinable area feature managment.
                | Role: This interface delivers services on machinable area
                | features

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_machinable_area_mngt = com_object

    def get_all_datas(self) -> tuple:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetAllDatas() As CATSafeArrayVariant
                |     Gets all the data in the Manufacturing Machinable Feature.
                |
                |     Parameters:
                |
                |         oDatas
                |             The list of data

        :rtype: tuple
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_machinable_area_mngt.GetAllDatas()

    def __repr__(self):
        return f'ManufacturingMachinableAreaMngt(name="{self.name}")'
