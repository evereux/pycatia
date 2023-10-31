#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_mhi_interfaces.mhi_load_parameters import MHILoadParameters
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class MHIOpenAccess(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MHIOpenAccess
                | 
                | Interface representing a means to load data from the Hub into
                | V5.
                | 
                | DNBIAMHIOpenAccess is implemented on Application. Applications and CAA partners
                | should NOT implement this interface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mhi_open_access = com_object

    def connect_to_ppr_hub(self, i_username: str, i_password: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ConnectToPPRHub(CATBSTR iUsername,
                | CATBSTR iPassword)
                | 
                |     This method establishes a connection to the PPRHub
                | 
                |     Parameters:
                | 
                |         iUsername
                |             [in] User Login name 
                |         iPassword
                |             [in] User password 
                | 
                |     Returns:
                |         S_OK if connection established OK S_FALSE if connection is already
                |         established for user E_FAIL if connection could not be established

        :param str i_username:
        :param str i_password:
        :rtype: None
        """
        return self.mhi_open_access.ConnectToPPRHub(i_username, i_password)

    def create_load_parameters(self) -> MHILoadParameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateLoadParameters() As MHILoadParameters
                | 
                |     This method creates an object which will contain all the necessary
                |     information required for loading an object (and its structure) from a PPR Hub
                |     into V5
                | 
                |     Parameters:
                | 
                |         oLoadParameters
                |             [out] Interface to the created Load Parameters object
                |
                |     Returns:
                |         S_OK if object created ok and interface returned OK E_FAIL on error

        :rtype: MHILoadParameters
        """
        return MHILoadParameters(self.mhi_open_access.CreateLoadParameters())

    def load_from_ppr_hub(
            self,
            i_load_parameters: MHILoadParameters,
            i_create_default_window: bool,
            i_is_read_only: bool,
            o_error_messages: tuple
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func LoadFromPPRHub(MHILoadParameters iLoadParameters,
                | boolean iCreateDefaultWindow,
                | boolean iIsReadOnly,
                | CATSafeArrayVariant oErrorMessages) As Document
                | 
                |     This method loads an object (and it structure) from a PPR Hub project into
                |     V5 Note: All Tools->Options settings will be respected during the
                |     load
                | 
                |     Parameters:
                | 
                |         iLoadParameters
                |             [in] The object which contains all the necessary information for
                |             the load 
                |         iCreateDefaultWindow
                |             [in] Option to indicate whether a window needs to be created for
                |             the document or not If no window is created, then caller is responsible for
                |             life cycle of document 
                |         iIsReadOnly
                |             [in] Option to indicate if document is to loaded in read-only mode
                |             
                |         oLoadedDoc
                |             [out] The V5 document into which data from the Hub is loaded
                |             
                |         oErrorMessages
                |             [out] The list of message about invalid or insufficient agruments
                |             passed to the method 
                | 
                |     Returns:
                |         S_OK if everything ran OK E_FAIL on error

        :param MHILoadParameters i_load_parameters:
        :param bool i_create_default_window:
        :param bool i_is_read_only:
        :param tuple o_error_messages:
        :rtype: Document
        """
        return Document(
            self.mhi_open_access.LoadFromPPRHub(
                i_load_parameters.com_object,
                i_create_default_window,
                i_is_read_only,
                o_error_messages
            )
        )

    def set_environment_for_vbs_launch(
            self,
            i_obj_id: str,
            i_filter: str,
            i_parent_id: str,
            i_project_id: str,
            i_user_name: str,
            i_pwd: str,
            o_error_messages: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetEnvironmentForVBSLaunch(CATBSTR iObjId,
                | CATBSTR iFilter,
                | CATBSTR iParentId,
                | CATBSTR iProjectId,
                | CATBSTR iUserName,
                | CATBSTR iPwd,
                | CATSafeArrayVariant oErrorMessages)
                | 
                |     This method sets the environment required for Direct Launch Through given
                |     VB Script
                | 
                |     Parameters:
                | 
                |         iObjId
                |             [in] process object ECB ID. Which needs to be opened in DPM
                |             
                |         iFilter
                |             [in] selected Project filters 
                |         iParentId
                |             [in] parent object ECB ID 
                |         iProjectId
                |             [in] project ID 
                |         iUserName
                |             [in] user name to log-on to DPE 
                |         iPwd
                |             [in] password to log-on to DPE 
                |         oErrorMessages
                |             [out] error messages(if any) 
                | 
                |     Returns:
                |         S_OK if everything ran OK E_FAIL on error

        :param str i_obj_id:
        :param str i_filter:
        :param str i_parent_id:
        :param str i_project_id:
        :param str i_user_name:
        :param str i_pwd:
        :param tuple o_error_messages:
        :rtype: None
        """
        return self.mhi_open_access.SetEnvironmentForVBSLaunch(
            i_obj_id,
            i_filter,
            i_parent_id,
            i_project_id,
            i_user_name,
            i_pwd,
            o_error_messages
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_environment_for_vbs_launch'
        # # vba_code = """
        # # Public Function set_environment_for_vbs_launch(mhi_open_access)
        # #     Dim iObjId (2)
        # #     mhi_open_access.SetEnvironmentForVBSLaunch iObjId
        # #     set_environment_for_vbs_launch = iObjId
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MHIOpenAccess(name="{self.name}")'
