#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class DrawingThread(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingThread
                | 
                | Represents a drawing thread in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_thread = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Type() As CatThreadType
                | 
                |     Returns or sets a CatThreadType (threaded or taped) on a thread. Be
                |     careful, this method is only available on threads which are linked to 2D circle
                |     geometry 
                | 
                | Example:
                |     The following example sets the type Taped in MyThread
                | 
                |       If MyThread.IsLinkedTo()=cat2DCircle Then
                |          MyThread.Type = catTaped
                |        End If
                |
                |     Methods
                | 
                | o Func IsLinkedTo() As CatThreadLinkedTo
                | 
                |     Specifies which kind of objects the thread is linked to.
                | 
                |     Returns:
                |         oLinkedType The type of thread link 
                | 
                | Example:
                |     The following example retrieves the CatThreadLinkedTo in MyThread This view
                |     belongs to the drawing view collection of the drawing
                |     sheet
                | 
                |      ThreadLinkType = MyThread.IsLinkedTo

        :return: enum cat_thread_type
        :rtype: int
        """

        return self.drawing_thread.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value: enum cat_thread_type
        """

        self.drawing_thread.Type = value

    def is_linked_to(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsLinkedTo() As CatThreadLinkedTo
                |
                |     Specifies which kind of objects the thread is linked to.
                |
                |     Returns:
                |         oLinkedType The type of thread link
                |
                | Example:
                |     The following example retrieves the CatThreadLinkedTo in MyThread This view
                |     belongs to the drawing view collection of the drawing
                |     sheet
                |
                |      ThreadLinkType = MyThread.IsLinkedTo

        :return: enum cat_thread_linked_to
        :rtype: int
        """

        return self.drawing_thread.IsLinkedTo()


def __repr__(self):
    return f'DrawingThread(name="{self.name}")'
