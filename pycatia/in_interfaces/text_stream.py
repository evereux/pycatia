#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class TextStream(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TextStream
                | 
                | The textstream object allows to manage input and output for a text
                | stream.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.text_stream = com_object

    @property
    def at_end_of_line(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AtEndOfLine() As boolean (Read Only)
                | 
                |     Returns a boolean value which specifies if the index position in the stream
                |     is at a end of line.
                | 
                |     Example:
                |         This example retrieves in EndLine the end of line value for the
                |         TextStream TestStream.
                | 
                |          Dim EndLine As Boolean
                |          EndLine = TestStream.AtEndOfLine

        :rtype: bool
        """

        return self.text_stream.AtEndOfLine

    @property
    def at_end_of_stream(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AtEndOfStream() As boolean (Read Only)
                | 
                |     Returns a boolean value which specifies if the index position in the stream
                |     is at a end of stream.
                | 
                |     Example:
                |         This example retrieves in EndStream the end of stream value for the
                |         TextStream TestStream.
                | 
                |          Dim EndStream As Boolean
                |          EndStream = TestStream.AtEndOfStream

        :rtype: bool
        """

        return self.text_stream.AtEndOfStream

    def close(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Close()
                | 
                |     Closes a text stream.
                | 
                |     Example:
                |         This example closes the TextStream TestStream
                | 
                |          TestStream.Close

        :rtype: None
        """
        return self.text_stream.Close()

    def read(self, i_num_of_char: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Read(long iNumOfChar) As CATBSTR
                | 
                |     Returns a string which contains a given number of characters from the
                |     current position in the stream.
                | 
                |     Parameters:
                | 
                |         iNumOfChar
                |             The number of characters to read. 
                | 
                |     Returns:
                |         oReadString The retrieved string.
                | 
                |         Example:
                |             This example retrieves the next fifty characters of the TextStream
                |             TestStream in the stream ReadString.
                | 
                |              Dim ReadString As String
                |              Set ReadString = TestStream.Read(50)

        :param int i_num_of_char:
        :rtype: str
        """
        return self.text_stream.Read(i_num_of_char)

    def read_line(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ReadLine() As CATBSTR
                | 
                |     Returns a string which contains a line of charaters from the current
                |     position in the stream.
                | 
                |     Returns:
                |         oReadLine The retrieved read line.
                | 
                |         Example:
                |             This example retrieves the next line of the TextStream TestStream
                |             in the stream ReadString.
                | 
                |              Dim ReadString As String
                |              Set ReadString = TestStream.ReadLine

        :rtype: str
        """
        return self.text_stream.ReadLine()

    def write(self, i_written_string: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Write(CATBSTR iWrittenString)
                | 
                |     Writes a string in the text stream.
                | 
                |     Parameters:
                | 
                |         iWrittenString
                |             The string to write in the stream.
                | 
                |             Example:
                |                 This example write a string in the the TextStream
                |                 TestStream.
                | 
                |                  TestStream.Write("This is a test")

        :param str i_written_string:
        :rtype: None
        """
        return self.text_stream.Write(i_written_string)

    def __repr__(self):
        return f'TextStream(name="{ self.name }")'
