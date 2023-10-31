#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class AMPTag(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AMPTag
                | 
                | This interface provides the methods to handle the feature
                | AMPTag.
                | 
                | DESCRIPTION :
                | AMP generates finally a RobotTask with Operations/RobotMotions( having
                | attributes ) and a set of tags( seam ). RobotTask with Operations/RobotMotions(
                | having attributes ) and the set of tags have information. For example each tag
                | has the information regarding XYZYPR values. RobotMotions have information
                | regarding weld speed etc. The current implementation of AMP is such that these
                | information are first populated in AMPTags. The list of AMPTags is put in an
                | AMPPath. When AMP is nearing its’ end of execution, tags and RobotTask with
                | appropriate Operations/RobotMotions are created and populated with these
                | information by retrieving it from the AMPTags( For each Operation/RobotMotion
                | and tag there is a corresponding AMPTag from which these information are
                | retrieved ). AMPTags are non-persistent and they are just intermediate buffers
                | for holding these information. Through the ability of executing VB script file
                | by embedding the call to it through the "Execute" keyword, these AMPTags are
                | made available to the user for further customization of these information.
                | "Execute" keyword facilitates calling the VB script file’s CATMain method by
                | passing it the AMPPath object as the single argument.
                | 
                | USAGE :
                | This interface can be used only during AMP primitive file execution and not in
                | a stand alone VB script file. This interface can only be used in conjunction
                | with AMPPath interface. Please see the usage instructions in the AMPPath
                | interface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.amp_tag = com_object

    def add_attribute_real(self, name: str, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddAttributeReal(CATBSTR Name,
                | double Value)
                | 
                |     Function to add real attribute on the given AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute to be added. 
                |         Value
                |             Value of the added attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             .

        :param str name:
        :param float value:
        :rtype: None
        """
        return self.amp_tag.AddAttributeReal(name, value)

    def add_attribute_string(self, name: str, value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddAttributeString(CATBSTR Name,
                | CATBSTR Value)
                | 
                |     Function to add string attribute on the given AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute to be added. 
                |         Value
                |             Value of the added attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |             .

        :param str name:
        :param str value:
        :rtype: None
        """
        return self.amp_tag.AddAttributeString(name, value)

    def add_aux_attribute(self, i_name: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddAuxAttribute(CATBSTR iName,
                | CATBSTR iValue)
                | 
                |     Function to add an auxilliary attribute to the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the auxilliary attribute. 
                |         iValue
                |             The value of the auxilliary attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str i_name:
        :param str i_value:
        :rtype: None
        """
        return self.amp_tag.AddAuxAttribute(i_name, i_value)

    def get_attribute_value_real(self, name: str, o_value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAttributeValueReal(CATBSTR Name,
                | double oValue)
                | 
                |     Function to get the value of the given real attribute on the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute whose value has to be obtained.
                |             
                |         Value
                |             Value of the attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str name:
        :param float o_value:
        :rtype: None
        """
        return self.amp_tag.GetAttributeValueReal(name, o_value)

    def get_attribute_value_string(self, name: str, value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAttributeValueString(CATBSTR Name,
                | CATBSTR Value)
                | 
                |     Function to get the value of the given string attribute on the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute whose value has to be obtained.
                |             
                |         Value
                |             Value of the attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param str name:
        :param str value:
        :rtype: None
        """
        return self.amp_tag.GetAttributeValueString(name, value)

    def get_aux_attribute(self, i_index: int, o_name: str, o_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAuxAttribute(short iIndex,
                | CATBSTR oName,
                | CATBSTR oValue)
                | 
                |     Function to get an auxilliary attribute value of the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the auxilliary attribute. 
                |         oName
                |             The name of the auxilliary attribute. 
                |         oValue
                |             The value of the auxilliary attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int i_index:
        :param str o_name:
        :param str o_value:
        :rtype: None
        """
        return self.amp_tag.GetAuxAttribute(i_index, o_name, o_value)

    def get_aux_attribute_num(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAuxAttributeNum(short oNum)
                | 
                |     Function to get the number of auxilliary attributes of the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of auxilliary attributes of the given AMPTag.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int o_num:
        :rtype: None
        """
        return self.amp_tag.GetAuxAttributeNum(o_num)

    def get_aux_axes_values(self, o_auxillary_axis_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAuxAxesValues(CATSafeArrayVariant
                | oAuxillaryAxisValues)
                | 
                |     Function to get the auxilliary axes values of the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         oAuxillaryAxisValues
                |             The auxilliary axes values of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param tuple o_auxillary_axis_values:
        :rtype: None
        """
        return self.amp_tag.GetAuxAxesValues(o_auxillary_axis_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_aux_axes_values'
        # # vba_code = """
        # # Public Function get_aux_axes_values(amp_tag)
        # #     Dim oAuxillaryAxisValues (2)
        # #     amp_tag.GetAuxAxesValues oAuxillaryAxisValues
        # #     get_aux_axes_values = oAuxillaryAxisValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_config(self, oconfig: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetConfig(short oconfig)
                | 
                |     Function to get the config value of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         oconfig
                |             The config value of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int oconfig:
        :rtype: None
        """
        return self.amp_tag.GetConfig(oconfig)

    def get_op_type(self, o_op_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOpType(short oOpType)
                | 
                |     Function to get the operation type of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         oOpType
                |             The operation type of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int o_op_type:
        :rtype: None
        """
        return self.amp_tag.GetOpType(o_op_type)

    def get_position(self, o_transform: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPosition(CATSafeArrayVariant oTransform)
                | 
                |     Function to get the position( array of doubles; X, Y, Z, Yaw, Roll, Pitch
                |     values ) of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         oTransform
                |             Array containing X, Y, Z, Yaw, Roll, Pitch values in sequence.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param tuple o_transform:
        :rtype: None
        """
        return self.amp_tag.GetPosition(o_transform)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_position'
        # # vba_code = """
        # # Public Function get_position(amp_tag)
        # #     Dim oTransform (2)
        # #     amp_tag.GetPosition oTransform
        # #     get_position = oTransform
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_type(self, o_tag_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetType(CATBSTR oTagType)
                | 
                |     Function to get the type of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         oTagType
                |             The type of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param str o_tag_type:
        :rtype: None
        """
        return self.amp_tag.GetType(o_tag_type)

    def get_via(self, o_via_status: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetVia(short oViaStatus)
                | 
                |     Function to get the via status of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         oViaStatus
                |             The via status of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int o_via_status:
        :rtype: None
        """
        return self.amp_tag.GetVia(o_via_status)

    def get_weld_speed(self, o_speed: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetWeldSpeed(double oSpeed)
                | 
                |     Function to get the weld speed of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         oSpeed
                |             The weld speed of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param float o_speed:
        :rtype: None
        """
        return self.amp_tag.GetWeldSpeed(o_speed)

    def remove_attribute(self, name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAttribute(CATBSTR Name)
                | 
                |     Function to remove an existing attribute on the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute to be removed. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param str name:
        :rtype: None
        """
        return self.amp_tag.RemoveAttribute(name)

    def remove_aux_attribute(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAuxAttribute(short iIndex)
                | 
                |     Function to remove an auxilliary attribute of the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the auxilliary attribute. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int i_index:
        :rtype: None
        """
        return self.amp_tag.RemoveAuxAttribute(i_index)

    def set_attribute_value_real(self, name: str, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttributeValueReal(CATBSTR Name,
                | double Value)
                | 
                |     Function to set the value of the given real attribute on the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute whose value has to be set. 
                |         Value
                |             The Value to be set. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param str name:
        :param float value:
        :rtype: None
        """
        return self.amp_tag.SetAttributeValueReal(name, value)

    def set_attribute_value_string(self, name: str, value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttributeValueString(CATBSTR Name,
                | CATBSTR Value)
                | 
                |     Function to set the value of the given string attribute on the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         Name
                |             Name of the attribute whose value has to be set. 
                |         Value
                |             The Value to be set. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param str name:
        :param str value:
        :rtype: None
        """
        return self.amp_tag.SetAttributeValueString(name, value)

    def set_aux_axes_values(self, i_auxillary_axis_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAuxAxesValues(CATSafeArrayVariant
                | iAuxillaryAxisValues)
                | 
                |     Function to set the auxilliary axes values of the given
                |     AMPTag.
                | 
                |     Parameters:
                | 
                |         iAuxillaryAxisValues
                |             The auxilliary axes values of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param tuple i_auxillary_axis_values:
        :rtype: None
        """
        return self.amp_tag.SetAuxAxesValues(i_auxillary_axis_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_aux_axes_values'
        # # vba_code = """
        # # Public Function set_aux_axes_values(amp_tag)
        # #     Dim iAuxillaryAxisValues (2)
        # #     amp_tag.SetAuxAxesValues iAuxillaryAxisValues
        # #     set_aux_axes_values = iAuxillaryAxisValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_config(self, iconfig: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConfig(short iconfig)
                | 
                |     Function to set the config value of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         iconfig
                |             The config value of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int iconfig:
        :rtype: None
        """
        return self.amp_tag.SetConfig(iconfig)

    def set_op_type(self, i_op_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOpType(short iOpType)
                | 
                |     Function to set the operation type of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         iOpType
                |             The operation type to be set for the given AMPTag.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int i_op_type:
        :rtype: None
        """
        return self.amp_tag.SetOpType(i_op_type)

    def set_position(self, i_transform: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPosition(CATSafeArrayVariant iTransform)
                | 
                |     Function to set the position( array of doubles; X, Y, Z, Yaw, Roll, Pitch
                |     values ) of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         iTransform
                |             Array containing X, Y, Z, Yaw, Roll, Pitch values in sequence.
                |             
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param tuple i_transform:
        :rtype: None
        """
        return self.amp_tag.SetPosition(i_transform)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_position'
        # # vba_code = """
        # # Public Function set_position(amp_tag)
        # #     Dim iTransform (2)
        # #     amp_tag.SetPosition iTransform
        # #     set_position = iTransform
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type(self, i_tag_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetType(CATBSTR iTagType)
                | 
                |     Function to set the type of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         iTagType
                |             The type to be set for the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param str i_tag_type:
        :rtype: None
        """
        return self.amp_tag.SetType(i_tag_type)

    def set_via(self, i_via_status: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVia(short iViaStatus)
                | 
                |     Function to set the via status of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         iViaStatus
                |             The via status of the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param int i_via_status:
        :rtype: None
        """
        return self.amp_tag.SetVia(i_via_status)

    def set_weld_speed(self, i_speed: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWeldSpeed(double iSpeed)
                | 
                |     Function to set the weld speed of the given AMPTag.
                | 
                |     Parameters:
                | 
                |         iSpeed
                |             The weld speed to be set for the given AMPTag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise.

        :param float i_speed:
        :rtype: None
        """
        return self.amp_tag.SetWeldSpeed(i_speed)

    def __repr__(self):
        return f'AMPTag(name="{self.name}")'
