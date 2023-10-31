#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_mhi_interfaces.mhi_load_parameters import MHILoadParameters
from pycatia.system_interfaces.any_object import AnyObject


class MHISaveAccess(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MHISaveAccess
                | 
                | Interface representing a means to (1) Save data to the Hub (2) Retrieve certain
                | information on the loaded document
                | 
                | DNBIAMHISaveAccess is implemented on Document.
                | Applications and CAA partners should NOT implement this
                | interface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mhi_save_access = com_object

    def get_detailing_names(self, o_currently_loaded_detailing: str) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDetailingNames(CATBSTR oCurrentlyLoadedDetailing) As
                | CATSafeArrayVariant
                | 
                |     Gets the name of the currently loaded detailing and the names of all the
                |     other detailings that exist for the loaded object.
                | 
                |     Parameters:
                | 
                |         oCurrentlyLoadedDetailing
                |             [inout] The name of the currently loaded detailing. This will be
                |             empty if no detailing was loaded 
                |         oListDetailingNames
                |             [out] The names of all the detailings that exist on the loaded
                |             object 
                | 
                |     Returns:
                |         S_OK if names returned OK S_FALSE if no detailings exist for the loaded
                |         object E_FAIL on error

        :param str o_currently_loaded_detailing:
        :rtype: tuple
        """
        return self.mhi_save_access.GetDetailingNames(o_currently_loaded_detailing)

    def get_load_parameters(self) -> MHILoadParameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLoadParameters() As MHILoadParameters
                | 
                |     Gets the interface to the Load Parameters object that contains all the
                |     information pertaining to the load of the document
                | 
                |     Parameters:
                | 
                |         oLoadParameters
                |             [out] Interface to the Load Parameters object 
                | 
                |     Returns:
                |         S_OK if everything ran OK E_FAIL on error

        :rtype: MHILoadParameters
        """
        return MHILoadParameters(self.mhi_save_access.GetLoadParameters())

    def save_to_ppr_hub(self, i_detailing_name: str, i_overwrite_detailing: bool) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SaveToPPRHub(CATBSTR iDetailingName,
                | boolean iOverwriteDetailing) As CATSafeArrayVariant
                | 
                |     This method saves a document from V5 to the PPR Hub Note: All
                |     Tools->Options settings will be respected during the save
                | 
                |     Parameters:
                | 
                |         iDetailingName
                |             [in] The name of the detailing to save Note: If the Tools->Options
                |             'Save Without Detailing' is checked ON, then NO detailing will be saved. This
                |             argument will be ignored and only the exposed data will be saved to the Hub
                |             
                |         iOverwriteDetailing
                |             [in] Option to indicate if a detailing with the same name needs to
                |             overwritten If this argument is FALSE and a detailing with the same name
                |             exists, then the save will be aborted (Neither detailing nor exposed data will
                |             be saved) 
                |         oListErrorMessages
                |             [out] List of error messages about invalid or incorrect arguments
                |             (for example Tools->Options settings conflicting with input arguments to
                |             method). Note: This will not contain the error messages that occured during the
                |             save (for e.g., failure to save an object/relation in the database)
                |
                |     Returns:
                |         S_OK if everything ran OK E_FAIL on error

        :param str i_detailing_name:
        :param bool i_overwrite_detailing:
        :rtype: tuple
        """
        return self.mhi_save_access.SaveToPPRHub(i_detailing_name, i_overwrite_detailing)

    def __repr__(self):
        return f'MHISaveAccess(name="{self.name}")'
