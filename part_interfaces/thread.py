#! usr/bin/python3.6
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
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

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
    def depth(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: float
        """

        return self.thread.Depth

    @depth.setter
    def depth(self, value):
        """
        :param float value:
        """

        self.thread.Depth = value

    @property
    def diameter(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: float
        """

        return self.thread.Diameter

    @diameter.setter
    def diameter(self, value):
        """
        :param float value:
        """

        self.thread.Diameter = value

    @property
    def lateral_face_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property LateralFaceElement() As Reference
                | 
                |     Returns or sets the lateral face (must be cylindrical) .
                |     To set the property, you can use the following Boundary object: Face.

        :return: Reference
        """

        return Reference(self.thread.LateralFaceElement)

    @lateral_face_element.setter
    def lateral_face_element(self, value):
        """
        :param Reference value:
        """

        self.thread.LateralFaceElement = value

    @property
    def limit_face_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property LimitFaceElement() As Reference
                | 
                |     Returns or sets the limit face (must be planar ) .
                |     To set the property, you can use the following Boundary object: PlanarFace.

        :return: Reference
        """

        return Reference(self.thread.LimitFaceElement)

    @limit_face_element.setter
    def limit_face_element(self, value):
        """
        :param Reference value:
        """

        self.thread.LimitFaceElement = value

    @property
    def pitch(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: float
        """

        return self.thread.Pitch

    @pitch.setter
    def pitch(self, value):
        """
        :param float value:
        """

        self.thread.Pitch = value

    @property
    def side(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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
        """

        return self.thread.Side

    @side.setter
    def side(self, value):
        """
        :param enum cat_thread_side value:
        """

        self.thread.Side = value

    @property
    def thread_description(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: StrParam
        """

        return StrParam(self.thread.ThreadDescription)

    def create_standard_thread_design_table(self, i_standard_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param CatThreadStandard i_standard_type:
        :return: None
        """
        return self.thread.CreateStandardThreadDesignTable(i_standard_type.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_standard_thread_design_table'
        # # vba_code = """
        # # Public Function create_standard_thread_design_table(thread)
        # #     Dim iStandardType (2)
        # #     thread.CreateStandardThreadDesignTable iStandardType
        # #     create_standard_thread_design_table = iStandardType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_user_standard_design_table(self, i_standard_name, i_path):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
                |                  "","E://user//standard//UserStandard.txt"

        :param str i_standard_name:
        :param str i_path:
        :return: None
        """
        return self.thread.CreateUserStandardDesignTable(i_standard_name, i_path)

    def reverse_direction(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ReverseDirection()
                | 
                |     Swap the direction of the thread or the tap.

        :return: None
        """
        return self.thread.ReverseDirection()

    def set_explicit_polarity(self, i_thread_polarity):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param CatThreadPolarity i_thread_polarity:
        :return: None
        """
        return self.thread.SetExplicitPolarity(i_thread_polarity.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_explicit_polarity'
        # # vba_code = """
        # # Public Function set_explicit_polarity(thread)
        # #     Dim iThreadPolarity (2)
        # #     thread.SetExplicitPolarity iThreadPolarity
        # #     set_explicit_polarity = iThreadPolarity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Thread(name="{self.name}")'
