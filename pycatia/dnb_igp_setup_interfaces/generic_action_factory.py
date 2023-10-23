#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.dnb_igp_setup_interfaces.generic_action import GenericAction
from pycatia.system_interfaces.any_object import AnyObject


class GenericActionFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     GenericActionFactory
                | 
                | Interface representing GenericAction factory.
                | 
                | Role: This allows the creation of a GenericAction under an
                | Operation
                | The following code snippet can be used to obtain a GenericActionFactory from a
                | selected Operation
                | 
                |    Dim oSelectAct As Activity
                |    set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objGenActFact As GenericActionFactory
                |    set objGenActFact = oSelectAct.GetTechnologicalObject("GenericActionFactory")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.generic_action_factory = com_object

    def create_generic_action(
            self,
            i_action_type: str,
            i_before: bool,
            i_reference_activity: Activity
    ) -> GenericAction:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateGenericAction(CATBSTR iActionType,
                | boolean iBefore,
                | Activity iReferenceActivity) As GenericAction
                | 
                |     Creates an Action based on the specified type
                | 
                |     Parameters:
                | 
                |         iActionType
                |             Type of Action to be created. 
                |         iBefore
                |             Created Action can be Predecessor/Successor. 
                |         iReferenceActivitiy
                |             The Reference Activity Before/After which the Action needs to be
                |             created. 
                |         oGenericAction
                |             Created Action. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Action is successfully created and the interface pointer is
                |             successfully returned
                |         E_FAIL
                |             Action was successfully created, but the interface query
                |             failed
                |         E_NOINTERFACE
                |             Action was successfully created, but the it doesn't implement the
                |             requested interface
                |         E_OUTOFMEMORY
                |             The component allocation failed
                | 
                |     Example:
                |
                |            Dim objGenActFact As GenericActionFactory
                |                   ......
                |            Dim refAct As Activity
                |            Dim objGenAct as GenericAction CATIASelection
                |                   ......
                |            Before = TRUE
                |            set refAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |            set objGenAct = objGenActFact.CreateGenericAction("DNBIgpSpotWeld", False, refAct)
                |            ..

        :param str i_action_type:
        :param bool i_before:
        :param Activity i_reference_activity:
        :rtype: GenericAction
        """
        return GenericAction(
            self.generic_action_factory.CreateGenericAction(
                i_action_type,
                i_before,
                i_reference_activity.com_object
            )
        )

    def __repr__(self):
        return f'GenericActionFactory(name="{self.name}")'
