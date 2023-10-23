#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.dmaps_interfaces.items import Items
from pycatia.dmaps_interfaces.outputs import Outputs
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.dmaps_interfaces.activities import Activities
    from pycatia.dmaps_interfaces.resources import Resources


class Activity(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Activity
                | 
                | The object that represents an activity.
                | 
                | It groups the most important methods related to an activity and enables to get
                | the management interfaces (hierarchy management, control flow management, *
                | ...).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.activity = com_object

    @property
    def attr_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttrCount() As long (Read Only)
                | 
                |     This property returns the number of attributes of the current
                |     activity.
                | 
                |     Returns:
                |         oNbAttr The number of attributes

        :rtype: int
        """

        return self.activity.AttrCount

    @property
    def beginning_date(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BeginningDate() As double
                | 
                |     This property returns the beginning date of the current
                |     activity.
                | 
                |     Returns:
                |         oBegin The beginning date of the current activity

        :rtype: float
        """

        return self.activity.BeginningDate

    @beginning_date.setter
    def beginning_date(self, value: float):
        """
        :param float value:
        """

        self.activity.BeginningDate = value

    @property
    def calculated_begin_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CalculatedBeginTime() As double (Read Only)
                | 
                |     This property returns and calculated time cyle on the current
                |     activity.
                | 
                |     Returns:
                |         oCBT The calculated begin time of the current activity

        :rtype: float
        """

        return self.activity.CalculatedBeginTime

    @property
    def calculated_cycle_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CalculatedCycleTime() As double (Read Only)
                | 
                |     This property returns and sets the calculated time cyle on the current
                |     activity.
                | 
                |     Returns:
                |         oCCT The calculated time cycle of the current activity

        :rtype: float
        """

        return self.activity.CalculatedCycleTime

    @property
    def children_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChildrenActivities() As Activities (Read Only)
                | 
                |     This property returns the interface which manages the children hierarchy on
                |     the activity. Please note that it used to return all children, but from R20SP4
                |     it returns only exposed children, which could be different from all children.

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.ChildrenActivities)

    @property
    def cycle_time(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CycleTime() As double
                | 
                |     This property returns and set the time cyle on the current
                |     activity.
                | 
                |     Returns:
                |         oCT The time cycle of the current activity 
                |     Parameters:
                | 
                |         iCT
                |             The specified time cycle of the current activity

        :rtype: float
        """

        return self.activity.CycleTime

    @cycle_time.setter
    def cycle_time(self, value: float):
        """
        :param float value:
        """

        self.activity.CycleTime = value

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Description() As CATBSTR
                | 
                |     This property returns and set the description on the current
                |     activity.
                | 
                |     Returns:
                |         oDescriptionBSTR The description of the current activity
                |         
                |     Parameters:
                | 
                |         iDescriptionBSTR
                |             The specified description of the current activity

        :rtype: str
        """

        return self.activity.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.activity.Description = value

    @property
    def end_date(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndDate() As double (Read Only)
                | 
                |     This property returns the end date of the current
                |     activity.
                | 
                |     Returns:
                |         oEnd The end date of the current activity. Till V5R13, this method is
                |         returning S_OK even if there is no good implementation. Starting from V5R14
                |         this method will return E_NOIMPL. Hence all the scripts that use this method
                |         would have to be updated to accomodate this change.

        :rtype: float
        """

        return self.activity.EndDate

    @property
    def items(self) -> Items:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Items() As Items (Read Only)
                | 
                |     This property returns the interface which manages the items or input
                |     products/components assigned to the current activity

        :rtype: Items
        """

        return Items(self.activity.Items)

    @property
    def next_cf_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NextCFActivities() As Activities (Read Only)
                | 
                |     This property returns the interface which manages the downstream control
                |     flow hierarchy on the activity.

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.NextCFActivities)

    @property
    def next_prf_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NextPRFActivities() As Activities (Read Only)
                | 
                |     This property returns the interface which manages the downstream product
                |     flow hierarchy on the activity.

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.NextPRFActivities)

    @property
    def outputs(self) -> Outputs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Outputs() As Outputs (Read Only)
                | 
                |     This property returns the interface which manages the output
                |     products/components of the current activity

        :rtype: Outputs
        """

        return Outputs(self.activity.Outputs)

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Parameters() As Parameters (Read Only)
                | 
                |     This property returns the interface which manages the knowlegde parameters
                |     of the activity.

        :rtype: Parameters
        """

        return Parameters(self.activity.Parameters)

    @property
    def possible_precedence_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PossiblePrecedenceActivities() As Activities (Read
                | Only)
                | 
                |     This property returns list of Possible Precedence Activities defined on
                |     Current Activity.
                | 
                |     Parameters:
                | 
                |         oActivities
                |             List of Activities that must precede the Current
                |             Activity

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.PossiblePrecedenceActivities)

    @property
    def precedence_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PrecedenceActivities() As Activities (Read Only)
                | 
                |     This property returns list of Precedence Activities defined on Current
                |     Activity.
                | 
                |     Parameters:
                | 
                |         oActivities
                |             List of Activities that must precede the Current
                |             Activity

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.PrecedenceActivities)

    @property
    def previous_cf_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PreviousCFActivities() As Activities (Read Only)
                | 
                |     This property returns the interface which manages the upstream control flow
                |     hierarchy on the activity.

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.PreviousCFActivities)

    @property
    def previous_prf_activities(self) -> 'Activities':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PreviousPRFActivities() As Activities (Read Only)
                | 
                |     This property returns the interface which manages the upstream product flow
                |     hierarchy on the activity.

        :rtype: Activities
        """

        from pycatia.dmaps_interfaces.activities import Activities
        return Activities(self.activity.PreviousPRFActivities)

    @property
    def process_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ProcessID() As CATBSTR (Read Only)
                | 
                |     This property returns process identifier on the current
                |     activity.
                | 
                |     Parameters:
                | 
                |         oProcessID
                |             The process ID of the current activity

        :rtype: str
        """

        return self.activity.ProcessID

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Relations() As Relations (Read Only)
                | 
                |     This property returns the interface which manages the knowlegde relations
                |     of the activity.

        :rtype: Relations
        """

        return Relations(self.activity.Relations)

    @property
    def resources(self) -> 'Resources':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Resources() As Resources (Read Only)
                | 
                |     This property returns the interface which manages the resources hierarchy
                |     on the activity.

        :rtype: Resources
        """

        from pycatia.dmaps_interfaces.resources import Resources
        return Resources(self.activity.Resources)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     This method returns the type of the current activity.
                | 
                |     Parameters:
                | 
                |         oType
                |             The type of the current activity

        :rtype: str
        """

        return self.activity.Type

    def add_activity_constraint(
            self,
            i_activity: 'Activity',
            i_constraint_type: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddActivityConstraint(Activity iActivity,
                | SPPProcessConstraintType iConstraintType)
                | 
                |     Create a constraint between current activity and input
                |     activity
                | 
                |     Parameters:
                | 
                |         iActivity
                |             Activity with which the constraint to be created. 
                |         iConstraintType
                |             Type of the Constraint. It may be one of the following:
                |             Precedence_Constraint, Start_Constraint, End_Constraint,
                |             
                | 
                |     Returns:
                |     S_OKOn Success
                |     S_FALSEIf a constraint already exists.
                |     E_FAILIf the constraint is NOT created.

        :param Activity i_activity:
        :param str i_constraint_type:
        :rtype: None
        """
        return self.activity.AddActivityConstraint(i_activity.com_object, i_constraint_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_activity_constraint'
        # # vba_code = """
        # # Public Function add_activity_constraint(activity)
        # #     Dim iActivity (2)
        # #     activity.AddActivityConstraint iActivity
        # #     add_activity_constraint = iActivity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_attr(self, i_attribute_name: str, attr_type: str, i_attribute_prompt_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddAttr(CATBSTR iAttributeName,
                | SPPProcessAttributeType AttrType,
                | CATBSTR iAttributePromptName)
                | 
                |     Adds attribute to an Activity.
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             Name of the attribute to add 
                |         AttrType
                |             Type of the attribute to add. It may be one of the following:
                |             Integer_Attribute or 0 for integer, Double_Attribute or 1 for double, or
                |             String_Attribute or 2 for string 
                |         iAttributePromptName
                |             Prompt Name of the attribute to add

        :param str i_attribute_name:
        :param str attr_type:
        :param str i_attribute_prompt_name:
        :rtype: None
        """
        return self.activity.AddAttr(i_attribute_name, attr_type, i_attribute_prompt_name)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_attr'
        # # vba_code = """
        # # Public Function add_attr(activity)
        # #     Dim iAttributeName (2)
        # #     activity.AddAttr iAttributeName
        # #     add_attr = iAttributeName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def attr_name(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AttrName(long iIndex) As CATBSTR
                | 
                |     This method returns the name for the specified attribute.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The attribute index 
                |         oName
                |             The attribute name

        :param int i_index:
        :rtype: str
        """
        return self.activity.AttrName(i_index)

    def attr_value(self, i_index: cat_variant) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AttrValue(CATVariant iIndex) As CATVariant
                | 
                |     This method returns the value for the specified attribute.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The attribute identifier 
                | 
                |     Returns:
                |         oAttVal The attribute value

        :param cat_variant i_index:
        :rtype: cat_variant
        """
        return self.activity.AttrValue(i_index)

    def create_child(self, i_type_of_child: str) -> 'Activity':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateChild(CATBSTR iTypeOfChild) As Activity
                | 
                |     This method creates a new child activity of the requested
                |     type.
                | 
                |     Parameters:
                | 
                |         iTypeOfChild
                |             The type of the child activity to create. 
                |         oCreatedChild
                |             The new created child activity.

        :param str i_type_of_child:
        :rtype: Activity
        """
        return Activity(self.activity.CreateChild(i_type_of_child))

    def create_link(self, i_second_activity: 'Activity') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateLink(Activity iSecondActivity)
                | 
                |     This method creates a link from the current activity to another
                |     activity.
                | 
                |     Parameters:
                | 
                |         iSecondActivity
                |             The activity that will be linked to the current
                |             activity.

        :param Activity i_second_activity:
        :rtype: None
        """
        return self.activity.CreateLink(i_second_activity.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_link'
        # # vba_code = """
        # # Public Function create_link(activity)
        # #     Dim iSecondActivity (2)
        # #     activity.CreateLink iSecondActivity
        # #     create_link = iSecondActivity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_activity_constraints(self, i_constraint_type: str, o_constrt_list: 'Activities') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetActivityConstraints(SPPProcessConstraintType
                | iConstraintType,
                | Activities oConstrtList)
                | 
                |     Get List of constraint activities that exists on the current
                |     Activity
                | 
                |     Parameters:
                | 
                |         iConstraintType
                |             Type of the Constraints to be returned. It may be one of the
                |             following: Precedence_Constraint, Start_Constraint, End_Constraint,
                |             All_Constraints 
                | 
                |     Returns:
                |         oConstrtList ( Allocate the memory.If not, it allocates internally and
                |         you need to clean it after usage) 
                |     List of Activities with which the current activity has
                |     constraints
                |     Returns:
                |         oConstraintTypeList (It is an optional output used only if user
                |         interested) ( Allocate the memory.If not, it allocates internally and you need
                |         to clean it after usage) 
                |     List of constraint types for each actvity that exists in
                |     oConstrtList
                |     Current activity has a constraint with first activity in oConstrtList and
                |     its constraint type is mentioned in first field of
                |     oConstraintTypeList

        :param str i_constraint_type:
        :param Activities o_constrt_list:
        :rtype: None
        """
        return self.activity.GetActivityConstraints(i_constraint_type, o_constrt_list.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_activity_constraints'
        # # vba_code = """
        # # Public Function get_activity_constraints(activity)
        # #     Dim iConstraintType (2)
        # #     activity.GetActivityConstraints iConstraintType
        # #     get_activity_constraints = iConstraintType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTechnologicalObject(CATBSTR iApplicationType) As
                | CATBaseDispatch
                | 
                |     Returns the process's applicative data which type is the given parameter.
                |     The data returned can be either a collection or a simple
                |     object.
                | 
                |     Parameters:
                | 
                |         iApplicationType
                |             The type of applicative data searched. 
                | 
                |     Example:
                | 
                |           This example retrieves the GraphEditor position for
                |           the
                |          Loading1 activity.
                |          
                | 
                |          Dim GEPosition 
                |          Set GEPosition = Loading1.GetTechnologicalObject("GEPosition")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.activity.GetTechnologicalObject(i_application_type)

    def is_sub_type_of(self, i_name: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsSubTypeOf(CATBSTR iName) As boolean
                | 
                |     This method allows to test the type of a specific
                |     activity.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the type to test 
                | 
                |     Returns:
                |         oVal The logical value returned by the test

        :param str i_name:
        :rtype: bool
        """
        return self.activity.IsSubTypeOf(i_name)

    def remove_activity_constraint(self, i_activity: 'Activity', i_constraint_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveActivityConstraint(Activity iActivity,
                | SPPProcessConstraintType iConstraintType)
                | 
                |     Remove a constraint between current activity and input
                |     activity
                | 
                |     Parameters:
                | 
                |         iActivity
                |             Activity with which the constraint to be removed. 
                |         iConstraintType
                |             Type of the Constraint to be removed. It may be one of the
                |             following: Precedence_Constraint, Start_Constraint, End_Constraint,
                |             All_Constraints 
                | 
                |     Returns:
                |     S_OKOn Success
                |     S_FALSEIf a constraint does not exists.
                |     E_FAILIf the constraint can not be removed or the Function fails because
                |     of any reason.

        :param Activity i_activity:
        :param str i_constraint_type:
        :rtype: None
        """
        return self.activity.RemoveActivityConstraint(i_activity.com_object, i_constraint_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_activity_constraint'
        # # vba_code = """
        # # Public Function remove_activity_constraint(activity)
        # #     Dim iActivity (2)
        # #     activity.RemoveActivityConstraint iActivity
        # #     remove_activity_constraint = iActivity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_attr(self, i_attribute_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAttr(CATBSTR iAttributeName)
                | 
                |     Removes attributes to an Activity type.
                | 
                |     Parameters:
                | 
                |         iAttributeName
                |             Name of the attribute to remove

        :param str i_attribute_name:
        :rtype: None
        """
        return self.activity.RemoveAttr(i_attribute_name)

    def remove_link(self, i_second_activity: 'Activity') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveLink(Activity iSecondActivity)
                | 
                |     This method removes a link existing on the current
                |     activity.
                | 
                |     Parameters:
                | 
                |         iSecondActivity
                |             The activity on which the link will be removed.

        :param Activity i_second_activity:
        :rtype: None
        """
        return self.activity.RemoveLink(i_second_activity.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_link'
        # # vba_code = """
        # # Public Function remove_link(activity)
        # #     Dim iSecondActivity (2)
        # #     activity.RemoveLink iSecondActivity
        # #     remove_link = iSecondActivity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_process_id(self, i_process_id: str, i_check_unique: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProcessID(CATBSTR iProcessID,
                | boolean iCheckUnique)
                | 
                |     Sets the process ID of the current activity
                | 
                |     Parameters:
                | 
                |         iProcessID
                |             Input Process ID string 
                |         iCheckUnique
                |             Option to enable uniqueness check

        :param str i_process_id:
        :param bool i_check_unique:
        :rtype: None
        """
        return self.activity.SetProcessID(i_process_id, i_check_unique)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_process_id'
        # # vba_code = """
        # # Public Function set_process_id(activity)
        # #     Dim iProcessID (2)
        # #     activity.SetProcessID iProcessID
        # #     set_process_id = iProcessID
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Activity(name="{self.name}")'
