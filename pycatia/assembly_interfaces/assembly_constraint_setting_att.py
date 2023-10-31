#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class AssemblyConstraintSettingAtt(SettingController):
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
                |                         AsmConstraintSettingAtt
                | 
                | Represents the Assembly Constraints setting controller object.
                | Role: the Assembly Constraints setting controller object deals with the setting
                | parameters displayed in the Assembly Constraints property page. To access this
                | property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of Mechanical Design to unfold the workbench
                |     list
                |     Click Assembly Design: Constraints tab
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_constraint_setting_att = com_object

    @property
    def constraint_creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConstraintCreationMode() As
                | CatAsmConstraintCreationMode
                | 
                |     Returns or sets the constraint creation setting parameter.
                |     Role: The constraint creation setting parameter manages the determination
                |     of the kind of elements to constraint.
                |     Legal values:
                |     catUseAnyGeometry The constraint can be created on any kind of
                |     geometry
                |     catUsePublishedGeometryChildLevel The constraint can only be created on
                |     geometry published on the direct child level
                |     catUsePublishedGeometryAnyLevel The constraint can only be created on
                |     geometry published on any assembly level
                | 
                |     Example:
                |         The following example retrieves the constraint creation setting
                |         parameter of AsmConstraintSettingAtt1 in CreationMode and sets the mode to
                |         catUsePublishedGeometryAnyLevel.
                | 
                |          Set CreationMode = AsmConstraintSettingAtt1.ConstraintCreationMode
                |          AsmConstraintSettingAtt1.ConstraintCreationMode = catUsePublishedGeometryAnyLevel

        :return: enum cat_asm_constraint_creation_mode
        :rtype: int
        """

        return self.assembly_constraint_setting_att.ConstraintCreationMode

    @constraint_creation_mode.setter
    def constraint_creation_mode(self, value: int):
        """
        :param int value: enum cat_asm_constraint_creation_mode
        """

        self.assembly_constraint_setting_att.ConstraintCreationMode = value

    @property
    def paste_component_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PasteComponentMode() As CatAsmPasteComponentMode
                | 
                |     Returns or sets the component paste setting parameter.
                |     Role: The component paste setting parameter manages the keeping of the
                |     contraints of a component after a Copy/Paste or a
                |     Cut/Paste.
                |     Legal values:
                |     catPasteWithoutCsts The component's constraints will not be
                |     recreated
                |     catPasteWithCstOnCopy The component's constraints will only be recreated
                |     after a Copy
                |     catPasteWithCstOnCut The component's constraints will only be recreated
                |     after a Cut
                |     catPasteWithCstOnCopyAndCut The component's constraints will be recreated
                |     after a Copy or a Cut
                | 
                |     Example:
                |         The following example retrieves the component paste setting parameter
                |         of AsmConstraintSettingAtt1 in PasteMode and sets the mode to With Cut
                |         Only.
                | 
                |          Set PasteMode = AsmConstraintSettingAtt1.PasteComponentMode
                |          AsmConstraintSettingAtt1.PasteComponentMode = catPasteWithCstOnCut

        :return: enum cat_asm_paste_component_mode
        :rtype: int
        """

        return self.assembly_constraint_setting_att.PasteComponentMode

    @paste_component_mode.setter
    def paste_component_mode(self, value: int):
        """
        :param int value: enum cat_asm_paste_component_mode
        """

        self.assembly_constraint_setting_att.PasteComponentMode = value

    @property
    def quick_constraint_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property QuickConstraintMode() As CatAsmQuickConstraintMode
                | 
                |     Returns or sets the quick constraint setting parameter.
                |     Role: The quick constraint setting parameter manages the type of contraint
                |     that will be created by tue Quick Constraint command.
                |     Legal values:
                |     catSpecifiedOrder Use the specified order
                |     catVerifiedConstraintFirst Create verified constraint
                |     first
                | 
                |     Example:
                |         The following example retrieves the quick constraint setting parameter
                |         of AsmConstraintSettingAtt1 in QuickMode and sets the mode to
                |         catSpecifiedOrder.
                | 
                |          Set QuickMode = AsmConstraintSettingAtt1.QuickConstraintMode
                |          AsmConstraintSettingAtt1.QuickConstraintMode = catSpecifiedOrder

        :return: enum cat_asm_quick_constraint_mode
        :rtype: int
        """

        return self.assembly_constraint_setting_att.QuickConstraintMode

    @quick_constraint_mode.setter
    def quick_constraint_mode(self, value: int):
        """
        :param int value: enum cat_asm_quick_constraint_mode
        """

        self.assembly_constraint_setting_att.QuickConstraintMode = value

    @property
    def redundancy_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RedundancyMode(CatAsmRedundancyMode
                | iRedundancyMode)
                | 
                |     Sets redundancy check option for constraint creation.
                |     Role: The Redundancy of the constraint is decided to be checked or not to
                |     be checked, for constraint creation.
                |     Legal values:
                |     catUnChecked Redundancy of constraint will be checked while constraint
                |     creation.
                |     catChecked Redundancy of constraint will not be checked while constraint
                |     creation.

        :return: enum cat_asm_redundancy_mode
        :rtype: int
        """

        return self.assembly_constraint_setting_att.RedundancyMode

    @redundancy_mode.setter
    def redundancy_mode(self, value: int):
        """
        :param int value: enum cat_asm_redundancy_mode
        """

        self.assembly_constraint_setting_att.RedundancyMode = value

    def get_constraint_creation_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConstraintCreationModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves informations about the constraint creation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.assembly_constraint_setting_att.GetConstraintCreationModeInfo(io_admin_level, io_locked)

    def get_paste_component_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPasteComponentModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves informations about the component paste setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.assembly_constraint_setting_att.GetPasteComponentModeInfo(io_admin_level, io_locked)

    def get_quick_constraint_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetQuickConstraintModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves informations about the quick constraint setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.assembly_constraint_setting_att.GetQuickConstraintModeInfo(io_admin_level, io_locked)

    def get_quick_constraint_ordered_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetQuickConstraintOrderedList() As CATSafeArrayVariant
                | 
                |     Returns the quick constraint ordered list setting
                |     parameter.
                |     Role: The quick constraint ordered list setting parameter manages the
                |     determination of the kind of elements to constraint.
                | 
                |     Parameters:
                | 
                |         ioList
                |             The ordered list of constraints type The constraints types must be
                |             precise strings 
                | 
                |     Example:
                |         The following example retrieves the quick constraint ordered list of
                |         AsmConstraintSettingAtt1 in QuickList
                | 
                |          Dim QuickList
                |          QuickList = AsmConstraintSettingAtt1.GetQuickConstraintOrderedList()

        :rtype: tuple
        """
        return self.assembly_constraint_setting_att.GetQuickConstraintOrderedList()

    def set_constraint_creation_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConstraintCreationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the constraint creation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_constraint_setting_att.SetConstraintCreationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_constraint_creation_mode_lock'
        # # vba_code = """
        # # Public Function set_constraint_creation_mode_lock(asm_constraint_setting_att)
        # #     Dim iLocked (2)
        # #     asm_constraint_setting_att.SetConstraintCreationModeLock iLocked
        # #     set_constraint_creation_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_paste_component_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPasteComponentModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the component paste setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_constraint_setting_att.SetPasteComponentModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_paste_component_mode_lock'
        # # vba_code = """
        # # Public Function set_paste_component_mode_lock(asm_constraint_setting_att)
        # #     Dim iLocked (2)
        # #     asm_constraint_setting_att.SetPasteComponentModeLock iLocked
        # #     set_paste_component_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_quick_constraint_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetQuickConstraintModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the quick constraint setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_constraint_setting_att.SetQuickConstraintModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_quick_constraint_mode_lock'
        # # vba_code = """
        # # Public Function set_quick_constraint_mode_lock(asm_constraint_setting_att)
        # #     Dim iLocked (2)
        # #     asm_constraint_setting_att.SetQuickConstraintModeLock iLocked
        # #     set_quick_constraint_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_quick_constraint_ordered_list(self, i_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetQuickConstraintOrderedList(CATSafeArrayVariant
                | iList)
                | 
                |     Sets the quick constraint ordered list setting parameter.
                |     Role: The quick constraint ordered list setting parameter manages the
                |     determination of the kind of elements to constraint.
                | 
                |     Parameters:
                | 
                |         iList
                |             The ordered list of constraints type The constraints types must be
                |             precise strings 
                | 
                |     Example:
                |         The following example sets the quick constraint ordered list of
                |         AsmConstraintSettingAtt1
                | 
                |          Dim QuickList(5)
                |          QuickList(0) = "CATAsmCoincidenceType"
                |          QuickList(1) = "CATAsmSurfContactType"
                |          QuickList(2) = "CATAsmAngleType"
                |          QuickList(3) = "CATAsmDistanceType"
                |          QuickList(4) = "CATAsmPerpendType"
                |          QuickList(5) = "CATAsmParallelType"
                |          AsmConstraintSettingAtt1.SetQuickConstraintOrderedListQuickList

        :param tuple i_list:
        :rtype: None
        """
        return self.assembly_constraint_setting_att.SetQuickConstraintOrderedList(i_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_quick_constraint_ordered_list'
        # # vba_code = """
        # # Public Function set_quick_constraint_ordered_list(asm_constraint_setting_att)
        # #     Dim iList (2)
        # #     asm_constraint_setting_att.SetQuickConstraintOrderedList iList
        # #     set_quick_constraint_ordered_list = iList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AssemblyConstraintSettingAtt(name="{self.name}")'
