#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.drafting_interfaces.drawing_gdt import DrawingGDT
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class NonSemanticGDT(AnyObject):
    """

    Introduced in V5-6R2014.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NonSemanticGDT

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_gdt = com_object

    def get_2d_annot(self) -> DrawingGDT:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func Get2dAnnot() As DrawingGDT
                |     Retrieves Drafting GDT.

        :rtype: DrawingGDT
        """
        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return DrawingGDT(self.non_semantic_gdt.Get2dAnnot())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """

        Introduced in V5-6R2017.

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
        return TPSParallelOnScreen(self.non_semantic_gdt.TPSParallelOnScreen())

    def __repr__(self):
        return f'NonSemanticGdt(name="{self.name}")'
