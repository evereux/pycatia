#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Thread(DressUpShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Thread
                | 
                | Represents the Thread feature.
                | It threads or taps cylindrical surface .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.thread = com_object

    @property
    def depth(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Depth() As double
                | 
                |     Returns the thread/tap depth.
                | 
                |     Returns:
                |         oDepth Value of the thread/tap depth
                | 
                |         Example:
                |             The following example returns in Depth the depth of thread
                |             firstthread:
                | 
                |              Set Depth = firstthread.Depth

        :rtype: float
        """

        return self.thread.Depth

    @depth.setter
    def depth(self, value: float):
        """
        :param float value:
        """

        self.thread.Depth = value

    @property
    def diameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Diameter() As double
                | 
                |     Returns the thread/tap diameter.
                | 
                |     Returns:
                |         oDiameter Value of the thread/tap diameter
                | 
                |         Example:
                |             The following example returns in ThreadDiameter the diameter of
                |             thread firstthread:
                | 
                |              Set ThreadDiameter = firstthread.Diameter

        :rtype: float
        """

        return self.thread.Diameter

    @diameter.setter
    def diameter(self, value: float):
        """
        :param float value:
        """

        self.thread.Diameter = value

    @property
    def lateral_face_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LateralFaceElement() As Reference
                | 
                |     Returns or sets the lateral face (must be cylindrical) .
                |     To set the property, you can use the following Boundary object: Face.

        :rtype: Reference
        """

        return Reference(self.thread.LateralFaceElement)

    @lateral_face_element.setter
    def lateral_face_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.thread.LateralFaceElement = value.com_object

    @property
    def limit_face_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LimitFaceElement() As Reference
                | 
                |     Returns or sets the limit face (must be planar ) .
                |     To set the property, you can use the following Boundary object: PlanarFace.

        :rtype: Reference
        """

        return Reference(self.thread.LimitFaceElement)

    @limit_face_element.setter
    def limit_face_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.thread.LimitFaceElement = value.com_object

    @property
    def pitch(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Pitch() As double
                | 
                |     Returns the thread/tap pitch.
                | 
                |     Returns:
                |         oPitch Value of the thread/tap pitch
                | 
                |         Example:
                |             The following example returns in ThreadPitch the thread pitch of
                |             thread firstthread:
                | 
                |              Set ThreadPitch = firstthread.ThreadPitch

        :rtype: float
        """

        return self.thread.Pitch

    @pitch.setter
    def pitch(self, value: float):
        """
        :param float value:
        """

        self.thread.Pitch = value

    @property
    def side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Side() As CatThreadSide
                | 
                |     Returns the thread or tap side.
                | 
                |     Returns:
                |         oThreadSide The thread/tap side (see CatThreadSide for list of possible
                |         sides)
                | 
                |         Example:
                |             The following example returns in ThreadSide the thread/tap side of
                |             thread firstthread:
                | 
                |              Set ThreadSide = firstthreadoThreadSide

        :return: enum cat_thread_side
        :rtype: int
        """

        return self.thread.Side

    @side.setter
    def side(self, value: int):
        """
        :param int value: enum cat_thread_side
        """

        self.thread.Side = value

    @property
    def thread_description(self) -> StrParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThreadDescription() As StrParam (Read Only)
                | 
                |     Returns the thread/tap description parameter. This call is valid only when
                |     a standard/user design table created
                | 
                |     Returns:
                |         oThreadDescParam A Parameter object controlling the thread/tap
                |         description (see StrParam for more information)
                | 
                |         Example:
                |             The following example returns in threadDescription the thread
                |             description (M12 etc) of thread firstthread:
                | 
                |              Set threadDescription = firstthread.ThreadDescription

        :rtype: StrParam
        """

        return StrParam(self.thread.ThreadDescription)

    def create_standard_thread_design_table(self, i_standard_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CreateStandardThreadDesignTable(CatThreadStandard
                | iStandardType)
                | 
                |     Creates a Standard Thread design table .
                | 
                |     Parameters:
                | 
                |         iStandardType
                |             Standard type for thread (see 
                | 
                |         CatThreadStandard for list of possible types)
                | 
                |         Example:
                |             The following example creates a standard table for MetricThinPitch
                |             for thread firstthread:
                | 
                |              firstthread.CreateStandardThreadDesignTable
                |              catMetricThinPitch

        :param int i_standard_type: enum cat_thread_standard
        :rtype: None
        """
        return self.thread.CreateStandardThreadDesignTable(i_standard_type)

    def create_user_standard_design_table(self, i_standard_name: str, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub CreateUserStandardDesignTable(CATBSTR iStandardName,
                | CATBSTR iPath)
                | 
                |     Creates a UserStandard Thread design table .
                | 
                |     Parameters:
                | 
                |         iStandardName
                |             Name of the UserStandard thread. iStandardName should be empty if
                |             filepath is to be defined. 
                |         iPath
                |             Path of the UserStandard file. iPath is empty if the filepath is
                |             already defined through CATReffilesPath.
                | 
                |             Example1:
                |                 The following example creates a standard table for UserStandard
                |                 for thread firstThread. The file path is already defined thru
                |                 CATReffilesPath:
                | 
                |                  firstThread.CreateUserStandardDesignTable
                |                  "UserStandard",""
                | 
                |             Example2:
                |                 The following example creates a standard table for UserStandard
                |                 for thread firstThread when file path is not defined thru
                |                 CATReffilesPath:
                | 
                |                  firstThread.CreateUserStandardDesignTable
                |                  "","E:\\user\\standard\\UserStandard.txt"

        :param str i_standard_name:
        :param str i_path:
        :rtype: None
        """
        return self.thread.CreateUserStandardDesignTable(i_standard_name, i_path)

    def reverse_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReverseDirection()
                | 
                |     Swap the direction of the thread or the tap.

        :rtype: None
        """
        return self.thread.ReverseDirection()

    def set_explicit_polarity(self, i_thread_polarity: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExplicitPolarity(CatThreadPolarity iThreadPolarity)
                | 
                |     Sets the thread polarity explicit. Thread polarity is no more evaluated
                |     implicitly on basis of support face polarity
                | 
                |     Parameters:
                | 
                |         iThreadPolarity
                |             Standard type for thread (see 
                | 
                |         CatThreadPolarity for list of possible types)
                | 
                |         Example:
                |             The following example sets the thread polarity to Tap explicitly
                |             thread firstthread:
                | 
                |              firstthread.SetExplicitPolarity catTap

        :param int i_thread_polarity: enum cat_thread_polarity
        :rtype: None
        """
        return self.thread.SetExplicitPolarity(i_thread_polarity)

    def __repr__(self):
        return f'Thread(name="{self.name}")'
