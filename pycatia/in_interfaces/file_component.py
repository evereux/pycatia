#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.in_interfaces.folder import Folder

class FileComponent(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FileComponent
                | 
                | Represents the file object.
                | Role: The file object allows to manipulate files with UNIX and Windows. Use it
                | instead of the one of Visual Basic to make portable macros. Its gives access to
                | information about the file and can open a file as a TextStream
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.file_component = com_object

    @property
    def parent_folder(self) -> 'Folder':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ParentFolder() As Folder
                | 
                |     Returns or sets the parent folder of the file.
                | 
                |     Example:
                |         This example sets the folder ParentFold as parent of the file TestFile.
                |         This moves the file into ParentFold.
                | 
                |          TestFile.ParentFolder

        :rtype: Folder
        """
        from pycatia.in_interfaces.folder import Folder
        return Folder(self.file_component.ParentFolder)

    @parent_folder.setter
    def parent_folder(self, value: 'Folder'):
        """
        :param Folder value:
        """

        self.file_component.ParentFolder = value

    @property
    def path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Path() As CATBSTR (Read Only)
                | 
                |     Returns the full path of the file.
                | 
                |     Example:
                |         This example retrieves in FilePath the path of the File
                |         TestFile.
                | 
                |          Dim FilePath As String
                |          FilePath = TestFile.Path

        :rtype: str
        """

        return self.file_component.Path

    def __repr__(self):
        return f'FileComponent(name="{self.name}")'
