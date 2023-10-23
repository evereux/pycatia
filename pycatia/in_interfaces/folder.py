#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.in_interfaces.file_component import FileComponent
from pycatia.in_interfaces.files import Files

if TYPE_CHECKING:
    from pycatia.in_interfaces.folders import Folders

class Folder(FileComponent):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.FileComponent
                |                         Folder
                | 
                | Represents the folder object.
                | It allows you to manipulate folders and gives access to information about
                | them.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.folder = com_object

    @property
    def files(self) -> Files:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Files() As Files (Read Only)
                | 
                |     Returns the file collection of the folder.
                | 
                |     Example:
                |         This example retrieves in TestFiles the file collection of the folder
                |         TestFolder.
                | 
                |          Dim TestFiles As Files
                |          Set TestFiles = TestFolder.Files

        :rtype: Files
        """

        return Files(self.folder.Files)

    @property
    def sub_folders(self) -> 'Folders':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SubFolders() As Folders (Read Only)
                | 
                |     Returns the folder collection of the folder.
                | 
                |     Example:
                |         This example retrieves in TestSubFolders the folder colection of the
                |         folder TestFolder.
                | 
                |          Dim TestSubFolders As CATIAFolders
                |          Set TestSubFolders = TestFolder.SubFolders

        :rtype: Folders
        """
        from pycatia.in_interfaces.folders import Folders
        return Folders(self.folder.SubFolders)

    def __repr__(self):
        return f'Folder(name="{self.name}")'
