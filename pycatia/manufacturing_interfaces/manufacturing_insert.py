#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingInsert(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingInsert
                | 
                | The interface to access a CATIAManufacturingInsert.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_insert = com_object

    @property
    def insert_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InsertType() As CATBSTR (Read Only)
                | 
                |     Return the technological type of a the insert. Example: The following
                |     example return the insert type theType of to the insert CurrentInsert
                |     theType=CurrentInsert.InsertType.

        :rtype: str
        """

        return self.manufacturing_insert.InsertType

    @property
    def number_of_attributes(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NumberOfAttributes() As short (Read Only)
                | 
                |     Give the Number of attributes of an insert object.
                |
                |     Example: The following example returns the Number of attributes of the
                |     insert object CurrentInsert.
                |
                |     Number = CurrentInsert.NumberOfAttributes.

        :rtype: int
        """

        return self.manufacturing_insert.NumberOfAttributes

    def get_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retrieve by is name the attribute of an insert object. Each attribute is a
                |     CKE object. Example: The following example retreives in MachiningQuality the
                |     attribute MfgMachiningQuality of the insert CurrentInsert
                | 
                |      Set MachiningQuality = CurrentInsert.GetAttribute(MfgMachiningQuality).

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_insert.GetAttribute(i_attribute))

    def get_attribute_nls_name(self, i_attribut_name: str) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttributeNLSName(CATBSTR iAttributName) As CATBSTR
                | 
                |     Gives the NLS value of an insert object
                |
                |     Example: The following example gives in NLSresult the NLS value of the "MFG_COMMENT"
                |     attributes of the insert CurrentInsert
                |
                |     NLSresult = CurrentInsert.GetAttributeNLSName("MFG_COMMENT").

        :param str i_attribut_name:
        :rtype: str
        """
        return self.manufacturing_insert.GetAttributeNLSName(i_attribut_name)

    def get_list_of_attribute_units(self, o_list_of_attribute_units: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributeUnits(CATSafeArrayVariant
                | oListOfAttributeUnits)
                | 
                |     Retrieve the list of attribute units of an insert object. The number of
                |     items in the output array is equal to the number of attributes of the insert.
                |     When an attribute has no unit definition, the corresponding unit item in the
                |     output array is a blank string. Example: The following example retrieves in
                |     TabAttributeUnits the list of attribute units of the insert object
                |     CurrentInsert call CurrentInsert.GetListOfAttributeUnits(TabAttributeUnits).

        :param tuple o_list_of_attribute_units:
        :rtype: None
        """
        return self.manufacturing_insert.GetListOfAttributeUnits(o_list_of_attribute_units)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attribute_units'
        # # vba_code = """
        # # Public Function get_list_of_attribute_units(manufacturing_insert)
        # #     Dim oListOfAttributeUnits (2)
        # #     manufacturing_insert.GetListOfAttributeUnits oListOfAttributeUnits
        # #     get_list_of_attribute_units = oListOfAttributeUnits
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_attributes(self, o_list_of_attributes: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetListOfAttributes(CATSafeArrayVariant
                | oListOfAttributes)
                | 
                |     Retrieve the list of attributes of an insert object. Each attribute is
                |     returned as the name of a CKE object. Example: The following example retrieves
                |     in TabAttributes the list of attributes of the insert object CurrentInsert call
                |     CurrentInsert.GetListOfAttributes(TabAttributes).

        :param tuple o_list_of_attributes:
        :rtype: None
        """
        return self.manufacturing_insert.GetListOfAttributes(o_list_of_attributes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_list_of_attributes'
        # # vba_code = """
        # # Public Function get_list_of_attributes(manufacturing_insert)
        # #     Dim oListOfAttributes (2)
        # #     manufacturing_insert.GetListOfAttributes oListOfAttributes
        # #     get_list_of_attributes = oListOfAttributes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ManufacturingInsert(name="{self.name}")'
