#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.file import File
from pycatia.system_interfaces.collection import Collection


class Files(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Files
                | 
                | A collection of all the file objects in a folder.
                | It lists all the files contained in the folder. It allows to retrieve File
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=File)
        self.files = com_object

    def item(self, i_number: int) -> File:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iNumber) As File
                | 
                |     Returns a file using its index or its name from the file
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the file to retrieve from the collection
                |             of files. As a numerics, this index is the rank of the file in the collection.
                |             The index of the first file in the collection is 1, and the index of the last
                |             file is Count. As a string, it is the name you assigned to the file using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved file 
                |     Example:
                |         This example retrieves in ThisFile the third file, and it ThatFile the
                |         file named MyFile. in the TestFiles file collection.
                | 
                |          Dim ThisFile As File
                |          Set ThisFile = TestFiles.Item(3)
                |          Dim ThatFile As File
                |          Set ThatFile = TestFiles.Item("MyFile")

        :param int i_number:
        :rtype: File
        """
        return File(self.files.Item(i_number))

    def __getitem__(self, n: int) -> File:
        if (n + 1) > self.count:
            raise StopIteration

        return File(self.files.Item(n + 1))

    def __iter__(self) -> Iterator[File]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Files(name="{self.name}")'
