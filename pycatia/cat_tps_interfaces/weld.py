#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.drafting_interfaces.drawing_welding import DrawingWelding
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class Weld(AnyObject):
    """

    Introduced in V5-6R2017.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Weld

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.weld = com_object

    def get_2d_annot(self) -> DrawingWelding:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Get2dAnnot() As DrawingWelding
                | 
                |     Retrieves Drafting Weld annotation.

        :rtype: DrawingWelding
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return DrawingWelding(self.weld.Get2dAnnot())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Gets the annotation on TPSParallelOnScreen interface.

        :rtype: TPSParallelOnScreen
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return TPSParallelOnScreen(self.weld.TPSParallelOnScreen())

    def __repr__(self):
        return f'Weld(name="{self.name}")'
