#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ArrBendableString(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrBendableString
                | 
                | The interface to access a CATIAArrBendableString
                | 
                | Using this prefered syntax will enable mkdoc to document your
                | class.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arr_bendable_string = com_object

    def get_num_of_segments(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNumOfSegments() As long
                | 
                |     Returns the cumulative number of the straight/arc segments that make up the
                |     Bendable object.
                | 
                |     Example:
                |         This example shows how to number of segments of
                |         BendablePipe001.
                | 
                |          Dim NumOfBendSegments
                |          NumOfBendSegments = BendablePipe001.GetNumOfSegments

        :return: int
        :rtype: int
        """
        return self.arr_bendable_string.GetNumOfSegments()

    def get_num_of_segments_local_axis(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNumOfSegmentsLocalAxis() As long
                | 
                |     Returns the cumulative number of the straight/arc segments that make up the
                |     Bendable object.

        :return: int
        :rtype: int
        """
        return self.arr_bendable_string.GetNumOfSegmentsLocalAxis()

    def get_segment_data(self, i_index: int, o_segment_data: tuple) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSegmentData(long iIndex,
                | CATSafeArrayVariant oSegmentData)
                | 
                |     Returns the data of the segment (Point Indices, Slope angle, Rotation
                |     Angle).
                | 
                |     Example:
                |         This example shows how to retrieve segment #2 of
                |         BendablePipe001.
                | 
                |          Dim SegmentData(14) As double
                |          BendablePipe001.GetSegmentData(2, SegmentData)
                |          where the data is returned in the Array in the following
                |          format...
                |          SegmentData(0)  = Starting Point of Segment (X Coord)
                |          SegmentData(1)  = Starting Point of Segment (Y Coord)
                |          SegmentData(2)  = Starting Point of Segment (Z Coord)
                |          SegmentData(3)  = End Point of Segment (X Coord)
                |          SegmentData(4)  = End Point of Segment (Y Coord)
                |          SegmentData(5)  = End Point of Segment (Z Coord)
                |          SegmentData(6)  = Bend Point of Segment (X Coord) '//Valid only if SegmentData(9) > 0
                |          SegmentData(7)  = Bend Point of Segment (Y Coord) '//Valid only if SegmentData(9) > 0
                |          SegmentData(8)  = Bend Point of Segment (Z Coord) '//Valid only if SegmentData(9) > 0
                |          SegmentData(9)  = Bend Radius at Bend Point '//Valid only if SegmentData(9) > 0
                |          SegmentData(10) = Bend Angle at Bend Point  '//Valid only if SegmentData(9) > 0
                |          SegmentData(11) = Rotation Angle of Segment
                |          SegmentData(12) = Slope Angle of Segment
                |          SegmentData(13) = Length of linear Segment
                |          SegmentData(14) = Length of Arc Segment '//Valid only if SegmentData(9) > 0

        :param int i_index:
        :param tuple o_segment_data:
        :return: float
        :rtype: float
        """
        return self.arr_bendable_string.GetSegmentData(i_index, o_segment_data)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_segment_data'
        # # vba_code = """
        # # Public Function get_segment_data(arr_bendable_string)
        # #     Dim iIndex (2)
        # #     arr_bendable_string.GetSegmentData iIndex
        # #     get_segment_data = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def instance_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func InstanceName() As CATBSTR
                | 
                |     Returns the Bendable's Instance Name.
                | 
                |     Example:
                |         This example shows how to retrieve the Bendable Instance Name of
                |         BendablePipe001.
                | 
                |          Dim _BendInstanceName
                |          _BendInstanceName = BendablePipe001.InstanceName

        :return: str
        :rtype: str
        """
        return self.arr_bendable_string.InstanceName()

    def __repr__(self):
        return f'ArrBendableString(name="{ self.name }")'
