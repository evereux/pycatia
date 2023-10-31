#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.structure_interfaces.str_cutback import StrCutback
from pycatia.system_interfaces.any_object import AnyObject


class StrMemberExtremity(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrMemberExtremity
                | 
                | Represents an extremity of a member object.
                | One is called the start extremity and the other the end
                | extremity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_member_extremity = com_object

    @property
    def angle_cut(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AngleCut() As double (Read Only)
                | 
                |     Returns the angle cut for a member extremity.

        :rtype: float
        """

        return self.str_member_extremity.AngleCut

    @property
    def cutback(self) -> StrCutback:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Cutback() As StrCutback (Read Only)
                | 
                |     Returns the cutback object.

        :rtype: StrCutback
        """

        return StrCutback(self.str_member_extremity.Cutback)

    @property
    def input(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Input() As Reference
                | 
                |     Returns or sets the input object defining the extremity. The input object
                |     may not belong to the support object.

        :rtype: Reference
        """

        return Reference(self.str_member_extremity.Input)

    @input.setter
    def input(self, value: Reference):
        """
        :param Reference value:
        """

        self.str_member_extremity.Input = value.com_object

    @property
    def offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Offset() As Parameter (Read Only)
                | 
                |     Returns the offset parameter defined on this extremity. This parameter can
                |     be null.

        :rtype: Parameter
        """

        return Parameter(self.str_member_extremity.Offset)

    @property
    def point(self) -> Point:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Point() As Point (Read Only)
                | 
                |     Returns the point defining the extremity. This point belongs to the support
                |     object.

        :rtype: Point
        """

        return Point(self.str_member_extremity.Point)

    def add_offset(self, i_offset: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddOffset(double iOffset)
                | 
                |     Adds an offset on the extremity. This method has to be used when the
                |     extremity has no offset already defined, else you will get an error.

        :param float i_offset:
        :rtype: None
        """
        return self.str_member_extremity.AddOffset(i_offset)

    def get_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCoordinates(CATSafeArrayVariant oCoordinates)
                | 
                |     Retrieves the coordinates of the extremity.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinates of the the extremity

        :param tuple o_coordinates:
        :rtype: None
        """
        return self.str_member_extremity.GetCoordinates()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_coordinates'
        # # vba_code = """
        # # Public Function get_coordinates(str_member_extremity)
        # #     Dim oCoordinates (2)
        # #     str_member_extremity.GetCoordinates oCoordinates
        # #     get_coordinates = oCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reset_cutback(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetCutback()
                | 
                |     Resets the defined cutback object.

        :rtype: None
        """
        return self.str_member_extremity.ResetCutback()

    def set_extremity_from_coordinates(self, i_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExtremityFromCoordinates(CATSafeArrayVariant
                | iCoordinates)
                | 
                |     Modifies the coordinates of the extremity defined by a
                |     point.
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             The coordinates to modify the extremity

        :param tuple i_coordinates:
        :rtype: None
        """
        return self.str_member_extremity.SetExtremityFromCoordinates(i_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_extremity_from_coordinates'
        # # vba_code = """
        # # Public Function set_extremity_from_coordinates(str_member_extremity)
        # #     Dim iCoordinates (2)
        # #     str_member_extremity.SetExtremityFromCoordinates iCoordinates
        # #     set_extremity_from_coordinates = iCoordinates
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'StrMemberExtremity(name="{self.name}")'
