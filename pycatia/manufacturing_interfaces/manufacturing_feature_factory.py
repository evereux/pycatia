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


class ManufacturingFeatureFactory(AnyObject):
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
                |                     ManufacturingFeatureFactory
                |
                | Interface dedicated to machining features creation.
                | Role: This interface is used to create new machining features.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_feature_factory = com_object

    def create_machining_feature(self, i_type: str) -> AnyObject:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func CreateMachiningFeature(CATBSTR iType) As AnyObject
                |     Creates a new machining feature.
                |
                |     Parameters:
                |
                |         iType
                |             The type of feature (ex: MfgInstructionSet, MfgOffsetPosition)
                |
                |
                |     Returns:
                |         The created machining feature

        :param str i_type:
        :rtype: AnyObject
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return AnyObject(self.manufacturing_feature_factory.CreateMachiningFeature(i_type))

    def __repr__(self):
        return f'ManufacturingFeatureFactory(name="{self.name}")'
