#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class KnowledgeSheetSettingAtt(SettingController):
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
                |                         KnowledgeSheetSettingAtt
                | 
                | The interface to access a CATIAKnowledgeSheetSettingAtt.
                | This interface may be used to read or modify in the CATIA/Tools/Option the
                | settings values of Knowledge sheet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.knowledge_sheet_setting_att = com_object

    @property
    def design_tables_copy_data(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DesignTablesCopyData() As short
                | 
                |     Returns or sets the DesignTablesCopyData parameter.
                |     Role:Return or Set the DesignTablesCopyData parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oDesignTablesCopyData
                |             Legal values:
                |             0 : default mode for design table : copy data into models
                |             1 : default mode for design table : do not copy data into models.

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.DesignTablesCopyData

    @design_tables_copy_data.setter
    def design_tables_copy_data(self, value: int):
        """
        :param int value:
        """

        self.knowledge_sheet_setting_att.DesignTablesCopyData = value

    @property
    def design_tables_synchronization(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DesignTablesSynchronization() As short
                | 
                |     Returns or sets the DesignTablesSynchronization parameter.
                |     Role:Return or Set the DesignTablesSynchronization parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oDesignTablesSynchronization
                |             Legal values:
                |             0 : automatic synchronization at load for design table
                |             1 : interactive synchronization at load for design table
                |             2 : manual synchronization for design table.

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.DesignTablesSynchronization

    @design_tables_synchronization.setter
    def design_tables_synchronization(self, value: int):
        """
        :param int value:
        """

        self.knowledge_sheet_setting_att.DesignTablesSynchronization = value

    @property
    def parameter_name_surrounded_by_the_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ParameterNameSurroundedByTheSymbol() As short
                | 
                |     Returns or sets the ParameterNameSurroundedByTheSymbol
                |     parameter.
                |     Role:Return or Set the ParameterNameSurroundedByTheSymbol parameter if it
                |     is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oParameterNameSurroundedByTheSymbol
                |             Legal values:
                |             0 : to see parameter name not surrounded by the symbol "'"
                |             1 : to see parameter name surrounded by the symbol "'".

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.ParameterNameSurroundedByTheSymbol

    @parameter_name_surrounded_by_the_symbol.setter
    def parameter_name_surrounded_by_the_symbol(self, value: int):
        """
        :param int value:
        """

        self.knowledge_sheet_setting_att.ParameterNameSurroundedByTheSymbol = value

    @property
    def parameter_tree_view_with_formula(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ParameterTreeViewWithFormula() As short
                | 
                |     Returns or sets the ParameterTreeViewWithFormula
                |     parameter.
                |     Role:Return or Set the ParameterTreeViewWithFormula parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oParameterTreeViewWithFormula
                |             Legal values:
                |             0 : to see parameter tree view without formula
                |             1 : to see parameter tree view with formula.

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.ParameterTreeViewWithFormula

    @parameter_tree_view_with_formula.setter
    def parameter_tree_view_with_formula(self, value: int):
        """
        :param enum value:
        """

        self.knowledge_sheet_setting_att.ParameterTreeViewWithFormula = value

    @property
    def parameter_tree_view_with_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ParameterTreeViewWithValue() As short
                | 
                |     Returns or sets the ParameterTreeViewWithValue parameter.
                |     Role:Return or Set the ParameterTreeViewWithValue parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oParameterTreeViewWithValue
                |             Legal values:
                |             0 : to see parameter tree view without value
                |             1 : to see parameter tree view with value.

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.ParameterTreeViewWithValue

    @parameter_tree_view_with_value.setter
    def parameter_tree_view_with_value(self, value: int):
        """
        :param int value:
        """

        self.knowledge_sheet_setting_att.ParameterTreeViewWithValue = value

    @property
    def relations_update_in_part_context_evaluate_during_update(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RelationsUpdateInPartContextEvaluateDuringUpdate() As
                | short
                | 
                |     Returns or sets the RelationsUpdateInPartContextEvaluateDuringUpdate
                |     parameter.
                |     Role:Return or Set the RelationsUpdateInPartContextEvaluateDuringUpdate
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oRelationsUpdateInPartContextEvaluateDuringUpdate
                |             Legal values:
                |             0 : creation of relations not evaluate during update
                |             1 : creation of relations evaluate during update.

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.RelationsUpdateInPartContextEvaluateDuringUpdate

    @relations_update_in_part_context_evaluate_during_update.setter
    def relations_update_in_part_context_evaluate_during_update(self, value: int):
        """
        :param int value:
        """

        self.knowledge_sheet_setting_att.RelationsUpdateInPartContextEvaluateDuringUpdate = value

    @property
    def relations_update_in_part_context_synchronous_relations(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RelationsUpdateInPartContextSynchronousRelations() As
                | short
                | 
                |     Returns or sets the RelationsUpdateInPartContextSynchronousRelations
                |     parameter.
                |     Role:Return or Set the RelationsUpdateInPartContextSynchronousRelations
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oRelationsUpdateInPartContextSynchronousRelations
                |             Legal values:
                |             0 : creation of unsynchronous relations
                |             1 : creation of synchronous relations.

        :rtype: int
        """

        return self.knowledge_sheet_setting_att.RelationsUpdateInPartContextSynchronousRelations

    @relations_update_in_part_context_synchronous_relations.setter
    def relations_update_in_part_context_synchronous_relations(self, value: int):
        """
        :param int value:
        """

        self.knowledge_sheet_setting_att.RelationsUpdateInPartContextSynchronousRelations = value

    def get_design_tables_copy_data_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDesignTablesCopyDataInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DesignTablesCopyData
                |     parameter.
                |     Role:Retrieves the state of the DesignTablesCopyData parameter in the
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
        return self.knowledge_sheet_setting_att.GetDesignTablesCopyDataInfo(io_admin_level, io_locked)

    def get_design_tables_synchronization_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDesignTablesSynchronizationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DesignTablesSynchronization
                |     parameter.
                |     Role:Retrieves the state of the DesignTablesSynchronization parameter in
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
        return self.knowledge_sheet_setting_att.GetDesignTablesSynchronizationInfo(io_admin_level, io_locked)

    def get_parameter_name_surrounded_by_the_symbol_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetParameterNameSurroundedByTheSymbolInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     ParameterNameSurroundedByTheSymbol parameter.
                |     Role:Retrieves the state of the ParameterNameSurroundedByTheSymbol
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
        return self.knowledge_sheet_setting_att.GetParameterNameSurroundedByTheSymbolInfo(io_admin_level, io_locked)

    def get_parameter_tree_view_with_formula_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetParameterTreeViewWithFormulaInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ParameterTreeViewWithFormula
                |     parameter.
                |     Role:Retrieves the state of the ParameterTreeViewWithFormula parameter in
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
        return self.knowledge_sheet_setting_att.GetParameterTreeViewWithFormulaInfo(io_admin_level, io_locked)

    def get_parameter_tree_view_with_value_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetParameterTreeViewWithValueInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ParameterTreeViewWithValue
                |     parameter.
                |     Role:Retrieves the state of the ParameterTreeViewWithValue parameter in the
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
        return self.knowledge_sheet_setting_att.GetParameterTreeViewWithValueInfo(io_admin_level, io_locked)

    def get_relations_update_in_part_context_evaluate_during_update_info(self,
                                                                         io_admin_level: str,
                                                                         io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetRelationsUpdateInPartContextEvaluateDuringUpdateInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     RelationsUpdateInPartContextEvaluateDuringUpdate
                |     parameter.
                |     Role:Retrieves the state of the
                |     RelationsUpdateInPartContextEvaluateDuringUpdate parameter in the current
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
        return self.knowledge_sheet_setting_att.GetRelationsUpdateInPartContextEvaluateDuringUpdateInfo(io_admin_level,
                                                                                                        io_locked)

    def get_relations_update_in_part_context_synchronous_relations_info(self,
                                                                        io_admin_level: str,
                                                                        io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetRelationsUpdateInPartContextSynchronousRelationsInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     RelationsUpdateInPartContextSynchronousRelations
                |     parameter.
                |     Role:Retrieves the state of the
                |     RelationsUpdateInPartContextSynchronousRelations parameter in the current
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
        return self.knowledge_sheet_setting_att.GetRelationsUpdateInPartContextSynchronousRelationsInfo(io_admin_level,
                                                                                                        io_locked)

    def set_design_tables_copy_data_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDesignTablesCopyDataLock(boolean iLocked)
                | 
                |     Locks or unlocks the DesignTablesCopyData parameter.
                |     Role:Locks or unlocks the DesignTablesCopyData parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
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
        return self.knowledge_sheet_setting_att.SetDesignTablesCopyDataLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_design_tables_copy_data_lock'
        # # vba_code = """
        # # Public Function set_design_tables_copy_data_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetDesignTablesCopyDataLock iLocked
        # #     set_design_tables_copy_data_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_design_tables_synchronization_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDesignTablesSynchronizationLock(boolean iLocked)
                | 
                |     Locks or unlocks the DesignTablesSynchronization
                |     parameter.
                |     Role:Locks or unlocks the DesignTablesSynchronization parameter if it is
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
        return self.knowledge_sheet_setting_att.SetDesignTablesSynchronizationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_design_tables_synchronization_lock'
        # # vba_code = """
        # # Public Function set_design_tables_synchronization_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetDesignTablesSynchronizationLock iLocked
        # #     set_design_tables_synchronization_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameter_name_surrounded_by_the_symbol_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetParameterNameSurroundedByTheSymbolLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the ParameterNameSurroundedByTheSymbol
                |     parameter.
                |     Role:Locks or unlocks the ParameterNameSurroundedByTheSymbol parameter if
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

        :param bool i_locked:
        :rtype: None
        """
        return self.knowledge_sheet_setting_att.SetParameterNameSurroundedByTheSymbolLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameter_name_surrounded_by_the_symbol_lock'
        # # vba_code = """
        # # Public Function set_parameter_name_surrounded_by_the_symbol_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetParameterNameSurroundedByTheSymbolLock iLocked
        # #     set_parameter_name_surrounded_by_the_symbol_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameter_tree_view_with_formula_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetParameterTreeViewWithFormulaLock(boolean iLocked)
                | 
                |     Locks or unlocks the ParameterTreeViewWithFormula
                |     parameter.
                |     Role:Locks or unlocks the ParameterTreeViewWithFormula parameter if it is
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
        return self.knowledge_sheet_setting_att.SetParameterTreeViewWithFormulaLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameter_tree_view_with_formula_lock'
        # # vba_code = """
        # # Public Function set_parameter_tree_view_with_formula_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetParameterTreeViewWithFormulaLock iLocked
        # #     set_parameter_tree_view_with_formula_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameter_tree_view_with_value_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetParameterTreeViewWithValueLock(boolean iLocked)
                | 
                |     Locks or unlocks the ParameterTreeViewWithValue parameter.
                |     Role:Locks or unlocks the ParameterTreeViewWithValue parameter if it is
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
        return self.knowledge_sheet_setting_att.SetParameterTreeViewWithValueLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameter_tree_view_with_value_lock'
        # # vba_code = """
        # # Public Function set_parameter_tree_view_with_value_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetParameterTreeViewWithValueLock iLocked
        # #     set_parameter_tree_view_with_value_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_relations_update_in_part_context_evaluate_during_update_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetRelationsUpdateInPartContextEvaluateDuringUpdateLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the RelationsUpdateInPartContextEvaluateDuringUpdate
                |     parameter.
                |     Role:Locks or unlocks the RelationsUpdateInPartContextEvaluateDuringUpdate
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
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
        return self.knowledge_sheet_setting_att.SetRelationsUpdateInPartContextEvaluateDuringUpdateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relations_update_in_part_context_evaluate_during_update_lock'
        # # vba_code = """
        # # Public Function set_rels_update_in_part_context_evaluate_during_update_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetRelationsUpdateInPartContextEvaluateDuringUpdateLock iLocked
        # #     set_relations_update_in_part_context_evaluate_during_update_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_relations_update_in_part_context_synchronous_relations_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetRelationsUpdateInPartContextSynchronousRelationsLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the RelationsUpdateInPartContextSynchronousRelations
                |     parameter.
                |     Role:Locks or unlocks the RelationsUpdateInPartContextSynchronousRelations
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.knowledge_sheet_setting_att.SetRelationsUpdateInPartContextSynchronousRelationsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relations_update_in_part_context_synchronous_relations_lock'
        # # vba_code = """
        # # Public Function set_relations_update_in_part_context_synchronous_relations_lock(knowledge_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     knowledge_sheet_setting_att.SetRelationsUpdateInPartContextSynchronousRelationsLock iLocked
        # #     set_relations_update_in_part_context_synchronous_relations_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'KnowledgeSheetSettingAtt(name="{self.name}")'
