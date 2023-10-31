#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Tag(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Tag
                | 
                | Interface representing a Tag.
                | 
                | Role: This interface is used to work with Tag.
                | The following code snippet can be used to obtain a Tag from a selected
                | Product
                | 
                |   Set ParentObject = CATIA.ActiveDocument.Selection.FindObject("CATIAProduct")	
                |   Set objTag = ParentObject.GetTechnologicalObject("Tag")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tag = com_object

    def get_name(self, o_tag_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetName(CATBSTR oTagName)
                | 
                |     Retreives name of the Tag.
                | 
                |     Parameters:
                | 
                |         oTagName
                |             Name of the Tag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              Dim Name as String
                |              objTag.GetName Name

        :param str o_tag_name:
        :rtype: None
        """
        return self.tag.GetName(o_tag_name)

    def get_type(self, o_frame_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetType(CATBSTR oFrameName)
                | 
                |     Get Frame Type of the Tag by Name.
                | 
                |     Parameters:
                | 
                |         oFrameName
                |             Name of the Required Frame.
                |             Legal values : Returned tag frame by Name is either :
                | 
                |             Manufacturing,
                |             Design,
                |             Tool,
                |             Base,
                |             Custom
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              Dim FrameType as String
                |              objTag.GetType FrameType

        :param str o_frame_name:
        :rtype: None
        """
        return self.tag.GetType(o_frame_name)

    def get_xyz(self, io_xyz: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetXYZ(CATSafeArrayVariant ioXYZ)
                | 
                |     Gets the Position(X, Y, Z) of the Tag.
                | 
                |     Parameters:
                | 
                |         ioXYZ
                |             The underlying Tag position. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              Dim List(3)
                |              objTag.GetXYZ List

        :param tuple io_xyz:
        :rtype: None
        """
        return self.tag.GetXYZ(io_xyz)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_xyz'
        # # vba_code = """
        # # Public Function get_xyz(tag)
        # #     Dim ioXYZ (2)
        # #     tag.GetXYZ ioXYZ
        # #     get_xyz = ioXYZ
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_ypr(self, io_ypr: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetYPR(CATSafeArrayVariant ioYPR)
                | 
                |     Gets the Orientation (Y, P, R) of the Tag.
                | 
                |     Parameters:
                | 
                |         ioYPR
                |             The underlying Tag orientation. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              Dim List(3)
                |              objTag.GetYPR List

        :param tuple io_ypr:
        :rtype: None
        """
        return self.tag.GetYPR(io_ypr)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_ypr'
        # # vba_code = """
        # # Public Function get_ypr(tag)
        # #     Dim ioYPR (2)
        # #     tag.GetYPR ioYPR
        # #     get_ypr = ioYPR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_name(self, i_tag_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetName(CATBSTR iTagName)
                | 
                |     Sets name of the Tag.
                | 
                |     Parameters:
                | 
                |         iTagName
                |             Name of the Tag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              objTag.SetName("My_Tag")

        :param str i_tag_name:
        :rtype: None
        """
        return self.tag.SetName(i_tag_name)

    def set_type(self, i_frame_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetType(CATBSTR iFrameName)
                | 
                |     Sets Frame Type of the Tag by Name.
                | 
                |     Parameters:
                | 
                |         iFrameName
                |             Name of the Required Frame.
                |             Legal values : Tag frame can be set by name to either :
                | 
                |             Manufacturing,
                |             Design,
                |             Tool,
                |             Base,
                |             Custom
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              objTag.SetType("Design")

        :param str i_frame_name:
        :rtype: None
        """
        return self.tag.SetType(i_frame_name)

    def set_xyz(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetXYZ(double iX,
                | double iY,
                | double iZ)
                | 
                |     Sets the Position(X, Y, Z) of the Tag.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X value of the position 
                |         iY
                |             The Y value of the position 
                |         iZ
                |             The Z value of the position 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              objTag.SetXYZ 2800.0, 1800.0, 800.0

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :rtype: None
        """
        return self.tag.SetXYZ(i_x, i_y, i_z)

    def set_ypr(self, i_y: float, i_p: float, i_r: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetYPR(double iY,
                | double iP,
                | double iR)
                | 
                |     Sets the Orientation (Y, P, R) of the Tag.
                | 
                |     Parameters:
                | 
                |         iY
                |             The yaw value of the oreintation 
                |         iP
                |             The pitch value of the orientation 
                |         iR
                |             The roll value of the orientation 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             . 
                | 
                |     Example:
                | 
                |               
                | 
                |              Dim objTag As Tag
                |              ...
                |              objTag.SetYPR 1.4, 0.5, 3.14

        :param float i_y:
        :param float i_p:
        :param float i_r:
        :rtype: None
        """
        return self.tag.SetYPR(i_y, i_p, i_r)

    def __repr__(self):
        return f'Tag(name="{ self.name }")'
