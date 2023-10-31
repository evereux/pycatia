#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class SearchSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         SearchSettingAtt
                | 
                | Represents the setting controller for the Search property tab
                | page.
                | Role: The setting controller is the object that enables to get and set setting
                | parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.search_setting_att = com_object

    @property
    def deep_search_activation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DeepSearchActivation() As boolean
                | 
                |     Returns or sets the Deep Search Activation attribute.
                |     Role: The Deep Search Activation attribute manages the Deep Search option
                |     available in the Search dialog box used to determine whether documents in
                |     visualization mode must be transiently loaded during a search query

        :rtype: bool
        """

        return self.search_setting_att.DeepSearchActivation

    @deep_search_activation.setter
    def deep_search_activation(self, value: bool):
        """
        :param bool value:
        """

        self.search_setting_att.DeepSearchActivation = value

    @property
    def default_power_input_context_priority(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultPowerInputContextPriority() As boolean
                | 
                |     Returns or sets the Default Power Input Context Priority
                |     attribute.
                |     Role: The Default Power Input Context Priority attribute manages whether
                |     the default context scope must override the context scope stored in a favorite
                |     query

        :rtype: bool
        """

        return self.search_setting_att.DefaultPowerInputContextPriority

    @default_power_input_context_priority.setter
    def default_power_input_context_priority(self, value: bool):
        """
        :param bool value:
        """

        self.search_setting_att.DefaultPowerInputContextPriority = value

    @property
    def default_power_input_context_scope(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultPowerInputContextScope() As
                | CATSearchContextScope
                | 
                |     Returns or sets the Default Power Input Context Scope
                |     attribute.
                |     Role: The Default Power Input Context Scope attribute manages the default
                |     context scope to be used when none is typed in the Power Input field

        :return: enum cat_search_context_scope
        :rtype: int
        """

        return self.search_setting_att.DefaultPowerInputContextScope

    @default_power_input_context_scope.setter
    def default_power_input_context_scope(self, value: int):
        """
        :param int value: enum cat_search_context_scope
        """

        self.search_setting_att.DefaultPowerInputContextScope = value

    @property
    def default_power_input_prefix(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultPowerInputPrefix() As CATBSTR
                | 
                |     Returns or sets the Default Power Input Prefix attribute.
                |     Role: The Default Power Input Prefix attribute manages the default prefix
                |     to be used when none is typed in the Power Input field

        :rtype: str
        """

        return self.search_setting_att.DefaultPowerInputPrefix

    @default_power_input_prefix.setter
    def default_power_input_prefix(self, value: str):
        """
        :param str value:
        """

        self.search_setting_att.DefaultPowerInputPrefix = value

    @property
    def max_displayed_results(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaxDisplayedResults() As long
                | 
                |     Returns or sets the Max Displayed Results attribute.
                |     Role: The Max Displayed Results attribute indicates the maximum number of
                |     elements that can be displayed in the Search results page. Displaying too many
                |     lines can stick more or less the results list so it is recommended to limit
                |     this number.

        :rtype: int
        """

        return self.search_setting_att.MaxDisplayedResults

    @max_displayed_results.setter
    def max_displayed_results(self, value: int):
        """
        :param int value:
        """

        self.search_setting_att.MaxDisplayedResults = value

    @property
    def max_pre_highlighted_elements(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaxPreHighlightedElements() As long
                | 
                |     Returns or sets the Max Pre-Highlighted Elements
                |     attribute.
                |     Role: The Max Pre-Highlighted Elements attribute indicates the maximum
                |     number of elements that can be displayed in the Search results page. Displaying
                |     too many elements can stick the session so it is strongly recommended to limit
                |     this number.

        :rtype: int
        """

        return self.search_setting_att.MaxPreHighlightedElements

    @max_pre_highlighted_elements.setter
    def max_pre_highlighted_elements(self, value: int):
        """
        :param int value:
        """

        self.search_setting_att.MaxPreHighlightedElements = value

    def get_deep_search_activation_info(self, o_admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDeepSearchActivationInfo(CATBSTR oAdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Deep Search Activation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str o_admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.search_setting_att.GetDeepSearchActivationInfo(o_admin_level, o_locked)

    def get_default_power_input_context_priority_info(self, o_admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultPowerInputContextPriorityInfo(CATBSTR
                | oAdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Default Power Input Context Priority
                |     setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str o_admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.search_setting_att.GetDefaultPowerInputContextPriorityInfo(o_admin_level, o_locked)

    def get_default_power_input_context_scope_info(self, o_admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultPowerInputContextScopeInfo(CATBSTR
                | oAdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Default Power Input Context Scope setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str o_admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.search_setting_att.GetDefaultPowerInputContextScopeInfo(o_admin_level, o_locked)

    def get_default_power_input_prefix_info(self, o_admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultPowerInputPrefixInfo(CATBSTR oAdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Default Power Input Prefix setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str o_admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.search_setting_att.GetDefaultPowerInputPrefixInfo(o_admin_level, o_locked)

    def get_max_displayed_results_info(self, o_admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMaxDisplayedResultsInfo(CATBSTR oAdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Max Displayed Results setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str o_admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.search_setting_att.GetMaxDisplayedResultsInfo(o_admin_level, o_locked)

    def get_max_pre_highlighted_elements_info(self, o_admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMaxPreHighlightedElementsInfo(CATBSTR oAdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Max Displayed Results setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str o_admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.search_setting_att.GetMaxPreHighlightedElementsInfo(o_admin_level, o_locked)

    def set_deep_search_activation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDeepSearchActivationLock(boolean iLocked)
                | 
                |     Locks or unlocks the Deep Search Activation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.search_setting_att.SetDeepSearchActivationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_deep_search_activation_lock'
        # # vba_code = """
        # # Public Function set_deep_search_activation_lock(search_setting_att)
        # #     Dim iLocked (2)
        # #     search_setting_att.SetDeepSearchActivationLock iLocked
        # #     set_deep_search_activation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_power_input_context_priority_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultPowerInputContextPriorityLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the Default Power Input Context Priority setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.search_setting_att.SetDefaultPowerInputContextPriorityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_power_input_context_priority_lock'
        # # vba_code = """
        # # Public Function set_default_power_input_context_priority_lock(search_setting_att)
        # #     Dim iLocked (2)
        # #     search_setting_att.SetDefaultPowerInputContextPriorityLock iLocked
        # #     set_default_power_input_context_priority_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_power_input_context_scope_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultPowerInputContextScopeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Default Power Input Context Scope setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.search_setting_att.SetDefaultPowerInputContextScopeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_power_input_context_scope_lock'
        # # vba_code = """
        # # Public Function set_default_power_input_context_scope_lock(search_setting_att)
        # #     Dim iLocked (2)
        # #     search_setting_att.SetDefaultPowerInputContextScopeLock iLocked
        # #     set_default_power_input_context_scope_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_power_input_prefix_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultPowerInputPrefixLock(boolean iLocked)
                | 
                |     Locks or unlocks the Default Power Input Prefix setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.search_setting_att.SetDefaultPowerInputPrefixLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_power_input_prefix_lock'
        # # vba_code = """
        # # Public Function set_default_power_input_prefix_lock(search_setting_att)
        # #     Dim iLocked (2)
        # #     search_setting_att.SetDefaultPowerInputPrefixLock iLocked
        # #     set_default_power_input_prefix_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_max_displayed_results_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMaxDisplayedResultsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Max Displayed Results setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.search_setting_att.SetMaxDisplayedResultsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_max_displayed_results_lock'
        # # vba_code = """
        # # Public Function set_max_displayed_results_lock(search_setting_att)
        # #     Dim iLocked (2)
        # #     search_setting_att.SetMaxDisplayedResultsLock iLocked
        # #     set_max_displayed_results_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_max_pre_highlighted_elements_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMaxPreHighlightedElementsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Max Displayed Results setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.search_setting_att.SetMaxPreHighlightedElementsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_max_pre_highlighted_elements_lock'
        # # vba_code = """
        # # Public Function set_max_pre_highlighted_elements_lock(search_setting_att)
        # #     Dim iLocked (2)
        # #     search_setting_att.SetMaxPreHighlightedElementsLock iLocked
        # #     set_max_pre_highlighted_elements_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SearchSettingAtt(name="{self.name}")'
