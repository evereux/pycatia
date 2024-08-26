#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.manufacturing_interfaces.manufacturing_operation import ManufacturingOperation
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingProgram2(AnyObject):
    """

    Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingProgram2
                |
                | A ManufacturingProgram for a Manufacturing Document.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_program2 = com_object

    def append_operation_after(
            self,
            i_manufacturing_operation: ManufacturingOperation,
            type_: str,
            auto_sequence: int) -> ManufacturingOperation:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func AppendOperationAfter(ManufacturingOperation
                | iManufacturingOperation,CATBSTR type,short AutoSequence) As
                | ManufacturingOperation
                |     Create and Insert a Manufacturing Operation of a specified type after the
                |     existing operation.
                |     if AutoSequence is set to 1, the new operation will be sequenced in the
                |     Program.
                |
                |     Example:
                |         The following example creates, inserts and sequences
                |         in firstProgram the manufacturing operation ManufacturingOperation
                |         of type : type
                |
                |         Set ManufacturingOperation = firstProgram.AppendOperationAfter(operation,Type,1)

        :param ManufacturingOperation i_manufacturing_operation:
        :param str type_:
        :param int auto_sequence:
        :rtype: ManufacturingOperation
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return ManufacturingOperation(
            self.manufacturing_program2.AppendOperationAfter(
                i_manufacturing_operation.com_object,
                type_,
                auto_sequence
            )
        )

    def append_operation_before(
            self,
            i_manufacturing_operation: ManufacturingOperation,
            type_: str,
            auto_sequence: int
    ) -> ManufacturingOperation:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func AppendOperationBefore(ManufacturingOperation
                | iManufacturingOperation,CATBSTR type,short AutoSequence) As
                | ManufacturingOperation
                |     Create and Insert a Manufacturing Operation of a specified type before the
                |     existing operation.
                |     if AutoSequence is set to 1, the new operation will be sequenced in the
                |     Program.
                |
                |     Example:
                |         The following example creates, inserts and sequences
                |         in firstProgram the manufacturing operation ManufacturingOperation
                |         of type : type
                |
                |          Set ManufacturingOperation = firstProgram.AppendOperationBefore(operation,Type,1)

        :param ManufacturingOperation i_manufacturing_operation:
        :param str type_:
        :param int auto_sequence:
        :rtype: ManufacturingOperation
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return ManufacturingOperation(
            self.manufacturing_program2.AppendOperationBefore(
                i_manufacturing_operation.com_object,
                type_,
                auto_sequence
            )
        )

    def __repr__(self):
        return f'ManufacturingProgram2(name="{self.name}")'
