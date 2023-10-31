#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_output_request import ABQOutputRequest


class ABQDataOutputRequest(ABQOutputRequest):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQOutputRequest
                |                         ABQDataOutputRequest
                | 
                | Represents an Abaqus data output request (ABQDataOutputRequest)
                | object.
                | Role: Access an Abaqus data output request object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_data_output_request = com_object

    def set_specified_output_variables(self, i_variable_name_bstr: str, i_dat_output_var_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSpecifiedOutputVariables(CATBSTR iVariableNameBSTR,
                | ABQDatOutputVarType iDatOutputVarType)
                | 
                |     Sets the specified variables and category type for which results are
                |     requested.
                | 
                |     Parameters:
                | 
                |         iVariableNameBSTR
                |             The list of variables for which output is requested For example: If
                |             user wants to request for output for variables 'U' and 'S', then
                |             iVariableNameBSTR will be "U, S" 
                |         iDatOutputVarType
                |             The variable type: Node based, Element based etc.
                | 
                |             Legal values:
                | 
                |             "DATOUTPUTTYPE_NODE"
                |             "DATOUTPUTTYPE_ELEMENT"
                |             "DATOUTPUTTYPE_CONTACT"
                |             "DATOUTPUTTYPE_ENERGY"

        :param str i_variable_name_bstr:
        :param int i_dat_output_var_type: enum abq_dat_output_var_type
        :rtype: None
        """
        return self.abq_data_output_request.SetSpecifiedOutputVariables(i_variable_name_bstr, i_dat_output_var_type)

    def unset_output_type(self, i_dat_output_var_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnsetOutputType(ABQDatOutputVarType iDatOutputVarType)
                | 
                |     Unset the data output request for specified type
                | 
                |     Parameters:
                | 
                |         iDatOutputVarType
                |             The variable type: Node based, Element based etc. User can unset
                |             the request for the variable type, if user does not want result for this type
                |             and it it was requested in previous step
                | 
                |             Legal values:
                | 
                |             "DATOUTPUTTYPE_NODE"
                |             "DATOUTPUTTYPE_ELEMENT"
                |             "DATOUTPUTTYPE_CONTACT"
                |             "DATOUTPUTTYPE_ENERGY"

        :param int i_dat_output_var_type: enum abq_dat_output_var_type
        :rtype: None
        """
        return self.abq_data_output_request.UnsetOutputType(i_dat_output_var_type)

    def __repr__(self):
        return f'ABQDataOutputRequest(name="{self.name}")'
