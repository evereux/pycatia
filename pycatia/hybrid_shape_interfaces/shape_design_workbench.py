#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2026-02-21 14:49:57.443389

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.in_interfaces.workbench import Workbench


class ShapeDesignWorkbench(Workbench):
    """

    Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         ShapeDesignWorkbench

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.com_object = com_object

    def __repr__(self):
        return f'ShapeDesignWorkbench(name="{self.name}")'
