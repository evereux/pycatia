#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_interfaces.drawing_text import DrawingText
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class Text(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Text
                | 
                | Interface for the TPS Text object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.text_com = com_object

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Text() As CATBSTR
                | 
                |     Gets the annotation's text.

        :rtype: str
        """

        return self.text_com.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.text_com.Text = value

    def get_2d_annot(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Get2dAnnot() As DrawingText
                | 
                |     Retrieves Drafting text.

        :rtype: DrawingText
        """
        return DrawingText(self.text_com.Get2dAnnot())

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
        return TPSParallelOnScreen(self.text_com.TPSParallelOnScreen())

    def __repr__(self):
        return f'Text(name="{self.name}")'
