#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.file_component import FileComponent
from pycatia.in_interfaces.text_stream import TextStream


class File(FileComponent):

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
                |                         File
                | 
                | Represents the file object.
                | Role: The file object allows to manipulate files with UNIX and Windows. Use it
                | instead of the one of Visual Basic to make portable macros. Its gives access to
                | information about the file and can open a file as a TextStream
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.file = com_object

    @property
    def size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Size() As long (Read Only)
                | 
                |     Returns the size of the file.
                | 
                |     Example:
                |         This example retrieves in FileSize the size of the File
                |         TestFile.
                | 
                |          Dim FileSize As Long
                |          FileSize = TestFile.Size

        :rtype: int
        """

        return self.file.Size

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the file. For instance, if the file has a .txt or .doc
                |     extension, its type will be "Text Document".
                | 
                |     Example:
                |         This example retrieves in FileType the type of the File
                |         TestFile.
                | 
                |          Dim FileType As String
                |          FileSize = TestFile.Size

        :rtype: str
        """

        return self.file.Type

    def open_as_text_stream(self, i_mode: str) -> TextStream:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func OpenAsTextStream(CATBSTR iMode) As TextStream
                | 
                |     Opens the file and retrieves it as a TextSteam object. Paramater iMode can
                |     have the value "ForReading", "ForWriting" or
                |     "ForAppending".
                | 
                |     Example:
                |         This example opens the file TestFile for reading and retrieves in the
                |         text stream TextStr.
                | 
                |          Dim TextStr As CATIATextSteam
                |          Set TextStr = TestFile.OpenAsTextStream("ForReading")

        :param str i_mode:
        :rtype: TextStream
        """
        return TextStream(self.file.OpenAsTextStream(i_mode))

    def __repr__(self):
        return f'File(name="{ self.name }")'
