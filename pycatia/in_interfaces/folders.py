#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.folder import Folder
from pycatia.system_interfaces.collection import Collection


class Folders(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Folders
                | 
                | The folders object belongs to a folder.
                | It lists all the folders contained in the folder. It allows to retrieve Folder
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Folder)
        self.folders = com_object

    def item(self, i_number: int) -> Folder:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iNumber) As Folder
                | 
                |     Returns a folder using its index or its name from the folder
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the folder to retrieve from the collection
                |             of folders. As a numerics, this index is the rank of the folder in the
                |             collection. The index of the first folder in the collection is 1, and the index
                |             of the last folder is Count. As a string, it is the name you assigned to the
                |             folder using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved folder 
                |     Example:
                |         This example retrieves in ThisFolder the third folder, and it
                |         ThatFolder the folder named MyFolder. in the TestFolders folder
                |         collection.
                | 
                |          Dim ThisFolder As Folder
                |          Set ThisFolder = TestFolders.Item(3)
                |          Dim ThatFolder As Folder
                |          Set ThatFolder = TestFolders.Item("MyFolder")

        :param int i_number:
        :rtype: Folder
        """
        return Folder(self.folders.Item(i_number))

    def __getitem__(self, n: int) -> Folder:
        if (n + 1) > self.count:
            raise StopIteration

        return Folder(self.folders.Item(n + 1))

    def __iter__(self) -> Iterator[Folder]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Folders(name="{self.name}")'
