#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.dmaps_interfaces.activity import Activity
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.manufacturing_interfaces.manufacturing_machinable_area import ManufacturingMachinableArea
from pycatia.manufacturing_interfaces.manufacturing_tool import ManufacturingTool
from pycatia.manufacturing_interfaces.manufacturing_tool_assembly import ManufacturingToolAssembly

if TYPE_CHECKING:
    from pycatia.manufacturing_interfaces.manufacturing_precedences import ManufacturingPrecedences


class ManufacturingActivity(Activity):
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
                |                         ManufacturingActivity
                | 
                | ManufacturingActivity defines a set of methods and mainly adds some specific
                | methods and services in Manufacturing on ProcessPlan
                | Activities.
                | Some methods have to be used carefully, they can have no meanly on a specific
                | Activity. This methods allows to support operation from other domain either
                | then Manufacturing.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_activity = com_object

    @property
    def active(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Active() As boolean
                | 
                |     Returns the activation state of the activity.
                | 
                |     Returns:
                |         oActive The activation state of the activity 
                |     Example:
                |         The following example returns in bActive the activation state of the
                |         activity firstActivity:
                | 
                |          Dim firstActivity As ManufacturingActivity
                |          Set firstActivity = ...
                |          Dim bActive As boolean
                |          Set bActive = firstActivity.Active

        :rtype: bool
        """

        return self.manufacturing_activity.Active

    @active.setter
    def active(self, value: bool):
        """
        :param bool value:
        """

        self.manufacturing_activity.Active = value

    @property
    def machinable_feature(self) -> ManufacturingMachinableArea:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MachinableFeature() As ManufacturingMachinableArea
                | 
                |     Retrieve the machinable area of a Manufacturing Activity.
                | 
                |     Example:
                |         The following example retrieves in theMAF the machinable area of the
                |         activity firstActivity.
                | 
                |          Dim firstActivity As ManufacturingActivity
                |          Set firstActivity = ...
                |          Dim theMAF As ManufacturingMachinableArea
                |          Set theMAF = firstActivity.MachinableArea

        :rtype: ManufacturingMachinableArea
        """

        return ManufacturingMachinableArea(self.manufacturing_activity.MachinableFeature)

    @machinable_feature.setter
    def machinable_feature(self, value: ManufacturingMachinableArea):
        """
        :param ManufacturingMachinableArea value:
        """

        self.manufacturing_activity.MachinableFeature = value

    @property
    def machining_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MachiningTime() As double (Read Only)
                | 
                |     Retreive the milling time of a Manufacturing Activity.
                | 
                |     Example:
                |         The following example retreives in theMachiningTime the time when the
                |         tool meets the workpiece (in minutes).
                | 
                |          theMachiningTime = firstActivity.MachiningTime

        :rtype: float
        """

        return self.manufacturing_activity.MachiningTime

    @property
    def number_of_feedrate_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfFeedrateAttributes() As short (Read Only)
                | 
                |     This property returns the number of Feedrate attributes of a Manufacturing
                |     Activity.

        :rtype: int
        """

        return self.manufacturing_activity.NumberOfFeedrateAttributes

    @property
    def number_of_geom_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfGeomAttributes() As short (Read Only)
                | 
                |     This property returns the number of Geometry attributes of a Manufacturing
                |     Activity.

        :rtype: int
        """

        return self.manufacturing_activity.NumberOfGeomAttributes

    @property
    def number_of_strategy_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfStrategyAttributes() As short (Read Only)
                | 
                |     This property returns the number of Strategy attributes of a Manufacturing
                |     Activity.

        :rtype: int
        """

        return self.manufacturing_activity.NumberOfStrategyAttributes

    @property
    def precedences(self) -> 'ManufacturingPrecedences':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Precedences() As ManufacturingPrecedences (Read
                | Only)
                | 
                |     This property returns the interface which manages the precedences on the
                |     operation. These collection defines the list of precedences for a manufacturing
                |     Activity.
                | 
                |     Example:
                |         The following example returns in precedences the interface that manage
                |         the precedences for the myActivity Activity :
                | 
                |          ...
                |          Set myActivity  = ... 
                |          Set precedences = myActivity.Precedences

        :rtype: ManufacturingPrecedences
        """
        
        from pycatia.manufacturing_interfaces.manufacturing_precedences import ManufacturingPrecedences
        return ManufacturingPrecedences(self.manufacturing_activity.Precedences)

    @property
    def representation(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Representation() As CATBSTR
                | 
                |     This property returns the path of the representation file for a
                |     manufacturing Activity.

        :rtype: str
        """

        return self.manufacturing_activity.Representation

    @representation.setter
    def representation(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_activity.Representation = value

    @property
    def tool(self) -> ManufacturingTool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tool() As ManufacturingTool (Read Only)
                | 
                |     Retreive the Tool of a Manufacturing Activity.
                | 
                |     Example:
                |         The following example retreives in CurTool the manufacturing tool of
                |         Manufacturing Activity firstActivity
                | 
                |          Set CurTool = firstActivity.GetTool

        :rtype: ManufacturingTool
        """

        return ManufacturingTool(self.manufacturing_activity.Tool)

    @property
    def tool_assembly(self) -> ManufacturingToolAssembly:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolAssembly() As ManufacturingToolAssembly (Read
                | Only)
                | 
                |     Retreive the ToolAssembly of a Manufacturing Activity.
                | 
                |     Example:
                |         The following example retrieves in CurrAssembly the manufacturing tool
                |         assembly of the manufacturing activity CurrActivity
                | 
                |          Set CurrAssembly = CurrActivity.ToolAssembly

        :rtype: ManufacturingToolAssembly
        """

        return ManufacturingToolAssembly(self.manufacturing_activity.ToolAssembly)

    @property
    def total_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TotalTime() As double (Read Only)
                | 
                |     Retreive the total Time of a Manufacturing Activity.
                | 
                |     Example:
                |         The following example retreives in theTotalTime the total time of the
                |         activity firstActivity (in minutes).
                | 
                |          theTotalTime = firstActivity.TotalTime

        :rtype: float
        """

        return self.manufacturing_activity.TotalTime

    @property
    def video_result(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VideoResult() As CATBSTR (Read Only)
                | 
                |     Retreive the video result path of a Manufacturing Activity. The path is
                |     empty if no video result.
                | 
                |     Example:
                |         The following example retreives in theVideoResult the video result of
                |         the activity firstActivity (in minutes).
                | 
                |          theVideoResult = firstActivity.VideoResult

        :rtype: str
        """

        return self.manufacturing_activity.VideoResult

    def get_attribute(self, i_attribut: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retreive the Attribute of a Manufacturing Activity.
                | 
                |     Example:
                |         The following example retreives in RapidFeed the attribute MfgRapidFeed
                |         of Manufacturing Activity firstActivity
                | 
                |          Set RapidFeed = firstActivity.GetAttribute(MfgRapidFeed)

        :param str i_attribut:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_activity.GetAttribute(i_attribut))

    def get_attribute_nls_name(self, i_attribut_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttributeNLSName(CATBSTR iAttributName) As CATBSTR
                | 
                |     Retrieve the NLS name from the attribute name of a Manufacturing
                |     Activity.

        :param str i_attribut_name:
        :rtype: str
        """
        return self.manufacturing_activity.GetAttributeNLSName(i_attribut_name)

    def get_list_of_feedrate_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfFeedrateAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Feedrate attributes of a Manufacturing
                |     Activity.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of
                |         feedrate attributes of the Manufacturing Activity
                |         myActivity
                | 
                |          call myActivity.GetListOfFeedrateAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_activity.GetListOfFeedrateAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_feedrate_attributes'
        # # vba_code = """
        # # Public Function get_list_of_feedrate_attributes(manufacturing_activity)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_activity.GetListOfFeedrateAttributes oListOfAttributes
        # #     get_list_of_feedrate_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_geom_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfGeomAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Geometry attributes of a Manufacturing
                |     Activity.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of
                |         Geometry attributes of the Manufacturing Activity
                |         myActivity
                | 
                |          call
                |          myActivity.GetListOfGeomAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_activity.GetListOfGeomAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_geom_attributes'
        # # vba_code = """
        # # Public Function get_list_of_geom_attributes(manufacturing_activity)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_activity.GetListOfGeomAttributes oListOfAttributes
        # #     get_list_of_geom_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_strategy_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfStrategyAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of Strategy attributes of a Manufacturing
                |     Activity.
                |     Each attribute is returned as the name of a CKE object.
                | 
                |     Example:
                |         The following example retrieves in oListOfAttributes the list of
                |         Strategy attributes of the Manufacturing Activity
                |         myActivity
                | 
                |          call myActivity.GetListOfStrategyAttributes(oListOfAttributes)

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_activity.GetListOfStrategyAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_strategy_attributes'
        # # vba_code = """
        # # Public Function get_list_of_strategy_attributes(manufacturing_activity)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_activity.GetListOfStrategyAttributes oListOfAttributes
        # #     get_list_of_strategy_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_machining_direction(self, o_x_axis: float, o_y_axis: float, o_z_axis: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetMachiningDirection(double oXAxis,
                | double oYAxis,
                | double oZAxis)
                | 
                |     Retreives the Machining Direction coordinates of a Manufacturing
                |     Operation.

        :param float o_x_axis:
        :param float o_y_axis:
        :param float o_z_axis:
        :rtype: None
        """
        return self.manufacturing_activity.GetMachiningDirection(o_x_axis, o_y_axis, o_z_axis)

    def get_tool_axis(self, o_x_axis: float, o_y_axis: float, o_z_axis: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetToolAxis(double oXAxis,
                | double oYAxis,
                | double oZAxis)
                | 
                |     Retreives the ToolAxis coordinates of a Manufacturing
                |     Activity.

        :param float o_x_axis:
        :param float o_y_axis:
        :param float o_z_axis:
        :rtype: None
        """
        return self.manufacturing_activity.GetToolAxis(o_x_axis, o_y_axis, o_z_axis)

    def set_machining_direction(self, i_x_axis: float, i_y_axis: float, i_z_axis: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMachiningDirection(double iXAxis,
                | double iYAxis,
                | double iZAxis)
                | 
                |     Defines the Machining Direction coordinates of a Manufacturing
                |     Operation.

        :param float i_x_axis:
        :param float i_y_axis:
        :param float i_z_axis:
        :rtype: None
        """
        return self.manufacturing_activity.SetMachiningDirection(i_x_axis, i_y_axis, i_z_axis)

    def set_tool_axis(self, i_x_axis: float, i_y_axis: float, i_z_axis: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToolAxis(double iXAxis,
                | double iYAxis,
                | double iZAxis)
                | 
                |     Defines the ToolAxis coordinates of a Manufacturing
                |     Activity.

        :param float i_x_axis:
        :param float i_y_axis:
        :param float i_z_axis:
        :rtype: None
        """
        return self.manufacturing_activity.SetToolAxis(i_x_axis, i_y_axis, i_z_axis)

    def __repr__(self):
        return f'ManufacturingActivity(name="{self.name}")'
