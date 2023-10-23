#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class FunctionalSystemSettingAtt(SettingController):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         FunctionalSystemSettingAtt
                | 
                | Enables attribute access to PFD options.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_system_setting_att = com_object

    @property
    def document_content_at_creation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DocumentContentAtCreation() As long
                | 
                |     Returns or sets the DocumentContentAtCreation parameter.
                | 
                |     Parameters:
                | 
                |         iDocumentContentAtCreation
                |             oDocumentContentAtCreation Document Content At Creation Attribute
                |             Legal values:
                |             0 : Sample elements
                |             1: empty 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.functional_system_setting_att.DocumentContentAtCreation

    @document_content_at_creation.setter
    def document_content_at_creation(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.DocumentContentAtCreation = value

    @property
    def functional_action_presentation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FunctionalActionPresentation() As long
                | 
                |     Returns or sets the FunctionalActionPresentation
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iDocumentContentAtCreation
                |             or oDocumentContentAtCreation Functional Action Presentation Legal
                |             values:
                |             0 : A : Action
                |             1: SAO : Subject Action Object
                |             2: ASO : Action Subject Object 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.functional_system_setting_att.FunctionalActionPresentation

    @functional_action_presentation.setter
    def functional_action_presentation(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.FunctionalActionPresentation = value

    @property
    def show_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShowParameters() As long
                | 
                |     Returns or sets the ShowParameters parameter.
                | 
                |     Parameters:
                | 
                |         iShowParameters
                |             or oShowParameters Show Parameters Legal values:
                |             False :
                |             True: 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.functional_system_setting_att.ShowParameters

    @show_parameters.setter
    def show_parameters(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.ShowParameters = value

    @property
    def show_relations(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShowRelations() As long
                | 
                |     Returns or sets the ShowRelations parameter.
                | 
                |     Parameters:
                | 
                |         iShowRelations
                |             or oShowRelations Show Relations Legal values:
                |             False :
                |             True:

        :rtype: int
        """

        return self.functional_system_setting_att.ShowRelations

    @show_relations.setter
    def show_relations(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.ShowRelations = value

    @property
    def show_synchro_status_of_local_param_cache(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShowSynchroStatusOfLocalParamCache() As long
                | 
                |     Returns or sets the ShowSynchroStatusOfLocalParamCache
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iShowSynchroStatusOfLocalParamCache
                |             or oShowSynchroStatusOfLocalParamCache Show Synchronisation Status
                |             OfLocal Parameter Cache Legal values:
                |             False :
                |             True :

        :rtype: int
        """

        return self.functional_system_setting_att.ShowSynchroStatusOfLocalParamCache

    @show_synchro_status_of_local_param_cache.setter
    def show_synchro_status_of_local_param_cache(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.ShowSynchroStatusOfLocalParamCache = value

    @property
    def split_functional_object_name(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplitFunctionalObjectName() As long
                | 
                |     Returns or sets the SplitFunctionalObjectName parameter.
                | 
                |     Parameters:
                | 
                |         iSplitFunctionalObjectName
                |             or oSplitFunctionalObjectName Legal values:
                |             False : don't split functional object name
                |             True : split Functional object name 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.functional_system_setting_att.SplitFunctionalObjectName

    @split_functional_object_name.setter
    def split_functional_object_name(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.SplitFunctionalObjectName = value

    @property
    def string_used_as_carriage_return(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StringUsedAsCarriageReturn() As CATBSTR
                | 
                |     Returns or sets the StringUsedAsCarriageReturn parameter.
                | 
                |     Parameters:
                | 
                |         iStringUsedAsCarriageReturn
                |             or oStringUsedAsCarriageReturn String Used As Carriage Return
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: str
        """

        return self.functional_system_setting_att.StringUsedAsCarriageReturn

    @string_used_as_carriage_return.setter
    def string_used_as_carriage_return(self, value: str):
        """
        :param str value:
        """

        self.functional_system_setting_att.StringUsedAsCarriageReturn = value

    @property
    def type_of_icon_on_functional_element(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TypeOfIconOnFunctionalElement() As long
                | 
                |     Returns or sets the TypeOfIconOnFunctionalElement
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iTypeOfIconOnFunctionalElement
                |             or oTypeOfIconOnFunctionalElement Type Of Icon On Functional
                |             Elements Legal values:
                |             0 : indicate a current association with PPR links.
                |             1: indicate a current generative script.

        :rtype: int
        """

        return self.functional_system_setting_att.TypeOfIconOnFunctionalElement

    @type_of_icon_on_functional_element.setter
    def type_of_icon_on_functional_element(self, value: int):
        """
        :param int value:
        """

        self.functional_system_setting_att.TypeOfIconOnFunctionalElement = value

    def get_document_content_at_creation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDocumentContentAtCreationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DocumentContentAtCreation
                |     parameter.
                |     Role:Retrieves the state of the DocumentContentAtCreation parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetDocumentContentAtCreationInfo(io_admin_level, io_locked)

    def get_functional_action_presentation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFunctionalActionPresentationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the FunctionalActionPresentation
                |     parameter.
                |     Role:Retrieves the state of the FunctionalActionPresentation parameter in
                |     the current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetFunctionalActionPresentationInfo(io_admin_level, io_locked)

    def get_show_parameters_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetShowParametersInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ShowParameters
                |     parameter.
                |     Role:Retrieves the state of the ShowParameters parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetShowParametersInfo(io_admin_level, io_locked)

    def get_show_relations_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetShowRelationsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ShowRelations
                |     parameter.
                |     Role:Retrieves the state of the ShowRelations parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetShowRelationsInfo(io_admin_level, io_locked)

    def get_show_synchro_status_of_local_param_cache_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetShowSynchroStatusOfLocalParamCacheInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     ShowSynchroStatusOfLocalParamCache parameter.
                |     Role:Retrieves the state of the ShowSynchroStatusOfLocalParamCache
                |     parameter in the current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetShowSynchroStatusOfLocalParamCacheInfo(io_admin_level, io_locked)

    def get_split_functional_object_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSplitFunctionalObjectNameInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SplitFunctionalObjectName
                |     parameter.
                |     Role:Retrieves the state of the SplitFunctionalObjectName parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetSplitFunctionalObjectNameInfo(io_admin_level, io_locked)

    def get_string_used_as_carriage_return_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStringUsedAsCarriageReturnInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the StringUsedAsCarriageReturn
                |     parameter.
                |     Role:Retrieves the state of the StringUsedAsCarriageReturn parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetStringUsedAsCarriageReturnInfo(io_admin_level, io_locked)

    def get_type_of_icon_on_functional_element_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTypeOfIconOnFunctionalElementInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TypeOfIconOnFunctionalElement
                |     parameter.
                |     Role:Retrieves the state of the TypeOfIconOnFunctionalElement parameter in
                |     the current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.functional_system_setting_att.GetTypeOfIconOnFunctionalElementInfo(io_admin_level, io_locked)

    def set_document_content_at_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDocumentContentAtCreationLock(boolean iLocked)
                | 
                |     Locks or unlocks the DocumentContentAtCreation parameter.
                |     Role:Locks or unlocks the DocumentContentAtCreation parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetDocumentContentAtCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_document_content_at_creation_lock'
        # # vba_code = """
        # # Public Function set_document_content_at_creation_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetDocumentContentAtCreationLock iLocked
        # #     set_document_content_at_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_functional_action_presentation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFunctionalActionPresentationLock(boolean iLocked)
                | 
                |     Locks or unlocks the FunctionalActionPresentation
                |     parameter.
                |     Role:Locks or unlocks the FunctionalActionPresentation parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetFunctionalActionPresentationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_functional_action_presentation_lock'
        # # vba_code = """
        # # Public Function set_functional_action_presentation_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetFunctionalActionPresentationLock iLocked
        # #     set_functional_action_presentation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_parameters_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShowParametersLock(boolean iLocked)
                | 
                |     Locks or unlocks the ShowParameters parameter.
                |     Role:Locks or unlocks the ShowParameters parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetShowParametersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_parameters_lock'
        # # vba_code = """
        # # Public Function set_show_parameters_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetShowParametersLock iLocked
        # #     set_show_parameters_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_relations_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShowRelationsLock(boolean iLocked)
                | 
                |     Locks or unlocks the ShowRelations parameter.
                |     Role:Locks or unlocks the ShowRelations parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetShowRelationsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_relations_lock'
        # # vba_code = """
        # # Public Function set_show_relations_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetShowRelationsLock iLocked
        # #     set_show_relations_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_synchro_status_of_local_param_cache_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShowSynchroStatusOfLocalParamCacheLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the ShowSynchroStatusOfLocalParamCache
                |     parameter.
                |     Role:Locks or unlocks the ShowSynchroStatusOfLocalParamCache parameter if
                |     it is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetShowSynchroStatusOfLocalParamCacheLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_synchro_status_of_local_param_cache_lock'
        # # vba_code = """
        # # Public Function set_show_synchro_status_of_local_param_cache_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetShowSynchroStatusOfLocalParamCacheLock iLocked
        # #     set_show_synchro_status_of_local_param_cache_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_split_functional_object_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSplitFunctionalObjectNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the SplitFunctionalObjectName parameter.
                |     Role:Locks or unlocks the SplitFunctionalObjectName parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetSplitFunctionalObjectNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_split_functional_object_name_lock'
        # # vba_code = """
        # # Public Function set_split_functional_object_name_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetSplitFunctionalObjectNameLock iLocked
        # #     set_split_functional_object_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_string_used_as_carriage_return_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStringUsedAsCarriageReturnLock(boolean iLocked)
                | 
                |     Locks or unlocks the StringUsedAsCarriageReturn parameter.
                |     Role:Locks or unlocks the StringUsedAsCarriageReturn parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetStringUsedAsCarriageReturnLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_string_used_as_carriage_return_lock'
        # # vba_code = """
        # # Public Function set_string_used_as_carriage_return_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetStringUsedAsCarriageReturnLock iLocked
        # #     set_string_used_as_carriage_return_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type_of_icon_on_functional_element_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTypeOfIconOnFunctionalElementLock(boolean iLocked)
                | 
                |     Locks or unlocks the TypeOfIconOnFunctionalElement
                |     parameter.
                |     Role:Locks or unlocks the TypeOfIconOnFunctionalElement parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.functional_system_setting_att.SetTypeOfIconOnFunctionalElementLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_type_of_icon_on_functional_element_lock'
        # # vba_code = """
        # # Public Function set_type_of_icon_on_functional_element_lock(functional_system_setting_att)
        # #     Dim iLocked (2)
        # #     functional_system_setting_att.SetTypeOfIconOnFunctionalElementLock iLocked
        # #     set_type_of_icon_on_functional_element_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'FunctionalSystemSettingAtt(name="{ self.name }")'
