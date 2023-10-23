#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingOutput(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingOutput
                | 
                | Object that represents the output machining code.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_output = com_object

    @property
    def size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Size() As long (Read Only)
                | 
                |     Returns the number of bytes written to this data output.
                | 
                |     Parameters:
                | 
                |         oBytes
                |             The integer value of the number of bytes

        :rtype: int
        """

        return self.manufacturing_output.Size

    def close_stream(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CloseStream()
                | 
                |     Close the Stream.

        :rtype: None
        """
        return self.manufacturing_output.CloseStream()

    def decrement_tabulation(self, i_tab: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DecrementTabulation(long iTab)
                | 
                |     Decrement the tabulation of the current block of text by the specified
                |     number of characters.

        :param int i_tab:
        :rtype: None
        """
        return self.manufacturing_output.DecrementTabulation(i_tab)

    def end_block(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub EndBlock()
                | 
                |     Specify that the Block is ended.

        :rtype: None
        """
        return self.manufacturing_output.EndBlock()

    def end_line(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub EndLine()
                | 
                |     Specify that the line is ended.

        :rtype: None
        """
        return self.manufacturing_output.EndLine()

    def flush(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Flush()
                | 
                |     Flush all Data in the Stream.

        :rtype: None
        """
        return self.manufacturing_output.Flush()

    def increment_tabulation(self, i_tab: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub IncrementTabulation(long iTab)
                | 
                |     Increment the tabulation of the current block of text by the specified
                |     number of characters.

        :param int i_tab:
        :rtype: None
        """
        return self.manufacturing_output.IncrementTabulation(i_tab)

    def new_block(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub NewBlock()
                | 
                |     Create a New Block in the underlying output stream.

        :rtype: None
        """
        return self.manufacturing_output.NewBlock()

    def new_line(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub NewLine()
                | 
                |     Create a New Line in the underlying output stream.

        :rtype: None
        """
        return self.manufacturing_output.NewLine()

    def set_buffer_length(self, i_lines: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBufferLength(long iLines)
                | 
                |     Set the number of lines of the buffer before it will be flushed (default is
                |     200).
                | 
                |     Parameters:
                | 
                |         iLines
                |             The integer value of the number of lines

        :param int i_lines:
        :rtype: None
        """
        return self.manufacturing_output.SetBufferLength(i_lines)

    def write_chars(self, i_text: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub write_Chars(CATBSTR iText)
                | 
                |     Write the specified string to the underlying output stream.

        :param str i_text:
        :rtype: None
        """
        return self.manufacturing_output.write_Chars(i_text)

    def write_double(self, i_val: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub write_Double(double iVal)
                | 
                |     Write the specified double to the underlying output stream.

        :param float i_val:
        :rtype: None
        """
        return self.manufacturing_output.write_Double(i_val)

    def write_long(self, i_val: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub write_Long(long iVal)
                | 
                |     Write the specified long to the underlying output stream.

        :param int i_val:
        :rtype: None
        """
        return self.manufacturing_output.write_Long(i_val)

    def __repr__(self):
        return f'ManufacturingOutput(name="{ self.name }")'
