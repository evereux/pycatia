#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_report_objects import ExpertReportObjects
from pycatia.manufacturing_interfaces.manufacturing_activities import ManufacturingActivities
from pycatia.manufacturing_interfaces.manufacturing_activity import ManufacturingActivity
from pycatia.manufacturing_interfaces.manufacturing_operation import ManufacturingOperation


class ManufacturingProgram(ManufacturingActivity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                        ManufacturingInterfaces.ManufacturingActivity
                |                             ManufacturingProgram
                | 
                | A ManufacturingProgram for a Manufacturing Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_program = com_object

    @property
    def activities(self) -> ManufacturingActivities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Activities() As MfgActivities (Read Only)
                | 
                |     Give the List of Activities linked to a Manufacturing
                |     Program.
                | 
                |     Example:
                |         The following example returns the list of Activities ActivitiesList
                |         linked to the manufacturing Program CurrentProgram
                | 
                |          Set ActivitiesList = CurrentProgram.Activities

        :rtype: MfgActivities
        """

        return ManufacturingActivities(self.manufacturing_program.Activities)

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR
                | 
                |     Return the Default Comment of a Manufacturing Program.
                | 
                |     Example:
                |         The following example return the comment ProgramComment of to the
                |         manufacturing Program CurrentProgram
                | 
                |          Set CurrentProgram.Comment

        :rtype: str
        """

        return self.manufacturing_program.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_program.Comment = value

    def add_goto_point(self, i_point_name: str) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddGotoPoint(CATBSTR iPointName) As
                | ManufacturingActivity
                | 
                |     Add a Goto Point Operation to a Manufacturing Program.
                | 
                |     Example:
                |         The following example create, inserts and sequences in Program
                |         firstProgram a PTP point instruction GOTO1 to the Point wich alias
                |         isMyPoint
                | 
                |          Set GOTO1 = firstProgram.AddGotoPoint(MyPoint)

        :param str i_point_name:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(self.manufacturing_program.AddGotoPoint(i_point_name))

    def add_goto_point_from_coordinates(self, i_x: float, i_y: float, i_z: float) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddGotoPointfromCoordinates(double iX,
                | double iY,
                | double iZ) As ManufacturingActivity
                | 
                |     Add a Goto Point Operation to a Manufacturing Program.
                | 
                |      The coordinates you give as input for this method have to be expressed
                |      into
                |      the 'Absolute Axis System' not in the 'Machining Axis System' of the Part
                |      Operation.
                | 
                |     Example:
                |         The following example create, inserts and sequences in Program
                |         firstProgram a PTP point instruction GOTO1 to the Point wich coordinates
                |         areX,Y,Z
                | 
                |          Set GOTO1 = firstProgram.AddGotoPointfromCoordinates(X,Y,Z)

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(self.manufacturing_program.AddGotoPointfromCoordinates(i_x, i_y, i_z))

    def add_pp_instruction(self, i_pp_instruction: str) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddPPInstruction(CATBSTR iPPInstruction) As
                | ManufacturingActivity
                | 
                |     Add a PP Instruction to a Manufacturing Program.
                | 
                |     Example:
                |         The following example create, inserts and sequences in Program
                |         firstProgram a PP Instruction PPWORD1 with textPPWORD
                | 
                |          Set PPWORD1 = firstProgram.AddPPInstruction(PPWORD)

        :param str i_pp_instruction:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(self.manufacturing_program.AddPPInstruction(i_pp_instruction))

    def add_rotabl(self, i_rotabl: str, i_sens: str, ival: float) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddRotabl(CATBSTR iRotabl,
                | CATBSTR iSens,
                | double ival) As ManufacturingActivity
                | 
                |     Add a Table Head Rotation instruction to a Manufacturing
                |     Program.
                | 
                |     Example:
                |         The following example create, inserts and sequences in Program
                |         firstProgram a Rotabl ROTABL1 with argumentMODE and
                |         angleANGLE1
                | 
                |          Set ROTABL1 = firstProgram.AddRotabl(MODE,ANGLE1)

        :param str i_rotabl:
        :param str i_sens:
        :param float ival:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(self.manufacturing_program.AddRotabl(i_rotabl, i_sens, ival))

    def add_tool_change(
            self,
            i_tool_name: str,
            i_tool_type: str,
            i_tool_catalog: str,
            i_num_syntaxe: int
    ) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddToolChange(CATBSTR iToolName,
                | CATBSTR iToolType,
                | CATBSTR iToolCatalog,
                | short iNumSyntaxe) As ManufacturingActivity
                | 
                |     Add a Tool Change Operation to a Manufacturing Program.
                | 
                |     Example:
                |         The following example create, inserts and sequences in firstProgram a
                |         Tool Change Instruction with specified toolMyTool of specified type ToolTypein
                |         specified catalogToolCatalog
                | 
                |          Set ToolChange1 = firstProgram.AddToolChange(MyTool,ToolType,ToolCatalog,Num)

        :param str i_tool_name:
        :param str i_tool_type:
        :param str i_tool_catalog:
        :param int i_num_syntaxe:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(
            self.manufacturing_program.AddToolChange(
                i_tool_name,
                i_tool_type,
                i_tool_catalog,
                i_num_syntaxe
            )
        )

    def add_tool_change_multiple_feeds(
            self,
            i_tool_name: str,
            i_tool_type: str,
            i_tool_catalog: str,
            i_num_fs_data: int,
            i_num_syntax: int
    ) -> ManufacturingActivity:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddToolChangeMultipleFeeds(CATBSTR iToolName,
                | CATBSTR iToolType,
                | CATBSTR iToolCatalog,
                | short iNumFSData,
                | short iNumSyntaxe) As ManufacturingActivity
                | 
                |     Add a Tool Change Operation to a Manufacturing Program.
                | 
                |     Example:
                |         The following example create, inserts and sequences in firstProgram a
                |         Tool Change Instruction with specified toolMyTool of specified type ToolTypein
                |         specified catalogToolCatalog
                | 
                |          Set ToolChange1 = firstProgram.AddToolChangeMultipleFeeds(MyTool,ToolType,ToolCatalog,NumFSData,Num)

        :param str i_tool_name:
        :param str i_tool_type:
        :param str i_tool_catalog:
        :param int i_num_fs_data:
        :param int i_num_syntax:
        :rtype: ManufacturingActivity
        """
        return ManufacturingActivity(
            self.manufacturing_program.AddToolChangeMultipleFeeds(
                i_tool_name,
                i_tool_type,
                i_tool_catalog,
                i_num_fs_data,
                i_num_syntax
            )
        )

    def append_operation(self, type: str, auto_sequence: int) -> ManufacturingOperation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppendOperation(CATBSTR type,
                | short AutoSequence) As ManufacturingOperation
                | 
                |     Create and Insert a Manufacturing Operation of a specified type to a
                |     Manufacturing Program.
                |     if AutoSequence is set to 1, the new operation will be sequenced in the
                |     Program.
                | 
                |     Example:
                |         The following example creates, inserts and sequences in firstProgram the manufacturing operation ManufacturingOperation of type : type
                | 
                |          Set ManufacturingOperation = firstProgram.AppendOperation(Type,1)

        :param str type:
        :param int auto_sequence:
        :rtype: ManufacturingOperation
        """
        return ManufacturingOperation(self.manufacturing_program.AppendOperation(type, auto_sequence))

    def associate_output_code(self, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AssociateOutputCode(CATBSTR iFileName)
                | 
                |     Method is used for associate APT file to V4 program iFileName = path for APT file.... Call on V4 ManufacturingProgram

        :param str i_file_name:
        :rtype: None
        """
        return self.manufacturing_program.AssociateOutputCode(i_file_name)

    def complete_with_polar_strategy(
            self,
            i_liste_mfg_activity: ManufacturingActivities,
            i_axe_ref: str,
            i_sens_rotation: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CompletewithPolarStrategy(MfgActivities
                | iListeMfgActivity,
                | CATBSTR iAxeRef,
                | CATBSTR iSensRotation)
                | 
                |     Complete a list of Operation in a Manufacturing Program in Polar
                |     Mode.
                | 
                |     Example:
                |         The following example complete in Program firstProgram a liste of
                |         Operation ListeMo with Reference Axis A and sens CLW
                | 
                |          Call
                |          firstProgram.CompletewithPolarStrategy(ListeMo,A,CLW)

        :param MfgActivities i_liste_mfg_activity:
        :param str i_axe_ref:
        :param str i_sens_rotation:
        :rtype: None
        """
        return self.manufacturing_program.CompletewithPolarStrategy(
            i_liste_mfg_activity.com_object,
            i_axe_ref,
            i_sens_rotation)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'completewith_polar_strategy'
        # # vba_code = """
        # # Public Function completewith_polar_strategy(manufacturing_program)
        # #     Dim iListeMfgActivity (2)
        # #     manufacturing_program.CompletewithPolarStrategy iListeMfgActivity
        # #     completewith_polar_strategy = iListeMfgActivity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_mo_from_report(self, i_report_succeed: ExpertReportObjects, i_type_mo: str) -> ManufacturingActivities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateMOfromReport(ExpertReportObjects
                | iReportSucceed,
                | CATBSTR iTypeMo) As MfgActivities
                | 
                |     Create a list of Operation in a Manufacturing Program, of a specified
                |     type.
                | 
                |     Example:
                |         The following example create in Program firstProgram a liste of
                |         Operation ListeMo with type Drilling from a CATIAExpertReportSucceedCollection
                |         ReportSucceed.
                | 
                |          Set ListeMO = firstProgram.CreateMOfromReport(ReportSucceed,Drilling)

        :param ExpertReportObjects i_report_succeed:
        :param str i_type_mo:
        :rtype: MfgActivities
        """
        return ManufacturingActivities(
            self.manufacturing_program.CreateMOfromReport(i_report_succeed.com_object, i_type_mo))

    def get_nc_output_file(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNCOutputFile() As CATBSTR
                | 
                |     Get the output file (APT or ISO) associated to the program (if associated
                |     during computation).

        :rtype: str
        """
        return self.manufacturing_program.GetNCOutputFile()

    def get_table_current_absolute_position(self, i_activity_ref: ManufacturingActivity) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTableCurrentAbsolutePosition(ManufacturingActivity iActivityRef) As
                | double
                | 
                |     Get the current absolute position of the Machine Table.
                | 
                |     Example:
                |         The following example gets in Program firstProgram the current Machine
                |         Table absolute position Angle from the Manufacturing activity reference
                |         iActivityRef
                | 
                |          Angle = firstProgram.GetTableCurrentAbsolutePosition(iActivityRef)

        :param ManufacturingActivity i_activity_ref:
        :rtype: float
        """
        return self.manufacturing_program.GetTableCurrentAbsolutePosition(i_activity_ref.com_object)

    def import_nc_output_on_program(self, i_type: str, i_nc_output_file: str, i_pp_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportNCOutputOnProgram(CATBSTR iType,
                | CATBSTR iNCOutputFile,
                | CATBSTR iPPName)
                | 
                |     Import an NC File on a program.
                | 
                |     Example:
                |         The following example imports in a Program firstProgram an NC File of
                |         type TYPE available in the file path PATH using the PP PPNAME if
                |         required.
                | 
                |          Call firstProgram.ImportNCOutputOnProgram(TYPE,PATH,PPNAME)

        :param str i_type:
        :param str i_nc_output_file:
        :param str i_pp_name:
        :rtype: None
        """
        return self.manufacturing_program.ImportNCOutputOnProgram(i_type, i_nc_output_file, i_pp_name)

    def insert_operation(
            self,
            i_reference_operation: ManufacturingOperation,
            i_manufacturing_operation: ManufacturingOperation
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InsertOperation(ManufacturingOperation
                | iReferenceOperation,
                | ManufacturingOperation iManufacturingOperation)
                | 
                |     Insert an existing Manufacturing Operation to a Manufacturing
                |     Program.
                | 
                |     Example:
                |         The following example inserts in firstProgram the manufacturing
                |         operation ExistingOperation after ReferenceOperation:
                | 
                |          call firstProgram.InsertOperation(ReferenceOperation,ExistingOperation)

        :param ManufacturingOperation i_reference_operation:
        :param ManufacturingOperation i_manufacturing_operation:
        :rtype: None
        """
        return self.manufacturing_program.InsertOperation(
            i_reference_operation.com_object,
            i_manufacturing_operation.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_operation'
        # # vba_code = """
        # # Public Function insert_operation(manufacturing_program)
        # #     Dim iReferenceOperation (2)
        # #     manufacturing_program.InsertOperation iReferenceOperation
        # #     insert_operation = iReferenceOperation
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def lock_activities_within_program(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LockActivitesWithinProgram()
                | 
                |     Method is used for Locking and Unloking all activity in program Call on
                |     ManufacturingProgram on which Lock and Unlock want

        :rtype: None
        """
        return self.manufacturing_program.LockActivitesWithinProgram()

    def move_operation(
            self,
            i_reference_operation: ManufacturingActivity,
            i_manufacturing_operation: ManufacturingActivity
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub MoveOperation(ManufacturingActivity
                | iReferenceOperation,
                | ManufacturingActivity iManufacturingOperation)
                | 
                |     Move an existing Manufacturing Operation to a Manufacturing
                |     Program.
                | 
                |     Example:
                |         The following example moves in firstProgram the manufacturing operation
                |         MovedOperation after the manufacturing
                |         operationExistingOperation:
                | 
                |          call firstProgram.MoveOperation(ExistingOperation,
                |          MovedOperation)

        :param ManufacturingActivity i_reference_operation:
        :param ManufacturingActivity i_manufacturing_operation:
        :rtype: None
        """
        return self.manufacturing_program.MoveOperation(
            i_reference_operation.com_object,
            i_manufacturing_operation.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'move_operation'
        # # vba_code = """
        # # Public Function move_operation(manufacturing_program)
        # #     Dim iReferenceOperation (2)
        # #     manufacturing_program.MoveOperation iReferenceOperation
        # #     move_operation = iReferenceOperation
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def order_and_create_mo_from_report(
            self,
            i_report_succeed: ExpertReportObjects,
            i_type_mo: str,
            i_axe_rotabl: str,
            i_sens_rotation: str
    ) -> ManufacturingActivities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func OrderAndCreateMOfromReport(ExpertReportObjects
                | iReportSucceed,
                | CATBSTR iTypeMo,
                | CATBSTR iAxeRotabl,
                | CATBSTR iSensRotation) As MfgActivities
                | 
                |     Create a list of Operation in a Manufacturing Program, of a specified
                |     type.
                | 
                |     Example:
                |         The following example create in Program firstProgram a liste of
                |         Operation ListeMo with type Drilling from a CATIAExpertReportSucceedCollection
                |         ReportSucceed with Rotabl of Axis A and sens CLW.
                | 
                |          Set ListeMO = firstProgram.OrderAndCreateMOfromReport(ReportSucceed,Drilling)

        :param ExpertReportObjects i_report_succeed:
        :param str i_type_mo:
        :param str i_axe_rotabl:
        :param str i_sens_rotation:
        :rtype: MfgActivities
        """
        return ManufacturingActivities(
            self.manufacturing_program.OrderAndCreateMOfromReport(
                i_report_succeed.com_object,
                i_type_mo,
                i_axe_rotabl,
                i_sens_rotation
            )
        )

    def unlock_activities_within_program(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnlockActivitesWithinProgram()

        :rtype: None
        """
        return self.manufacturing_program.UnlockActivitesWithinProgram()

    def __repr__(self):
        return f'ManufacturingProgram(name="{self.name}")'
