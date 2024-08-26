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


class ManufacturingActivityToolPath(AnyObject):
    """

    Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivityToolPath
                |
                | Interface to compute the tool path of an activity.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_activity_tool_path = com_object

    def compute_and_set_tool_path(self) -> None:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub ComputeAndSetToolPath()
                |     Compute and set Tool Path for this operation

        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_activity_tool_path.ComputeAndSetToolPath()

    def __repr__(self):
        return f'ManufacturingActivityToolPath(name="{self.name}")'
