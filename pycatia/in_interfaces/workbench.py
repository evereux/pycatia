#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Workbench(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Workbench
                | 
                | Represents a workbench on a document.
                | Role:A workbench is a set of commands that can be used to create, modify and
                | edit the objects making up the document.
                | 
                | See also:
                |     Document 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.workbench = com_object

    def __repr__(self):
        return f'Workbench(name="{self.name}")'
