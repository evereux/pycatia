#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class OrderGenerator(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OrderGenerator
                | 
                | Interface representing Create Shop Order APIs which generates Shop Order
                | Instance(SOI), against user-given option(s).
                | 
                | 
                | Following gvies the major-steps encountered in a single SOI generation 1) Logs
                | in and secures connection with DPE. 2) Loads the specified job Node. 3) Reslves
                | the Work Instrucitons. 4) Captures Images for activities 5) Generates JobXML
                | and Precedence XML 6) Generates PackNGo data ( Lite or Full) 7) Zips the SOI
                | contents. 8) FTPs the zipped file to FTP server 9) Updates the Release table.
                | 10) Disconnects from DPE.
                | 
                | 
                | Role: Component that implement DNBIAOrderCreation is
                | "OrderGenerator"
                | 
                | 
                | Do not extend this interface
                | 
                | 
                | Example : Refer to CreateShopOrder.CATScript or CreateSOI CATScript at intel_a/VBScript/DPM_SOR
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.order_generator = com_object

    def create_shop_order(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateShopOrder() As short
                | 
                |     Create Shop Order method
                | 
                |     Returns:
                |         SOI response, which in-turn can be obtained using
                |         OrderGenerator.GetErrorDescription

        :rtype: int
        """
        return self.order_generator.CreateShopOrder()

    def create_shop_order2(self, i_xml_input: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateShopOrder2(CATBSTR iXMLInput)
                | 
                |     Create Shop Order using XML as SOI input.
                | 
                |     Parameters:
                | 
                |         iXMLInput
                |             XML input file path Sample schema: Refer
                |             intel_a/resources/xsd/DPM_SOR/CreateSOI.xsd Sample XML input: Refer
                |             intel_a/resources/xml/DPM_SOR/CreateSOI.xml

        :param str i_xml_input:
        :rtype: None
        """
        return self.order_generator.CreateShopOrder2(i_xml_input)

    def get_error_description(self, error_code: int) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetErrorDescription(short ErrorCode) As CATBSTR
                | 
                |     Get Error Description. It deciphers return ERROR code of Create Shop Order
                |     API.
                | 
                |     Parameters:
                | 
                |         iErrorCode
                |             Create Shop Order API return code 
                | 
                |     Returns:
                |         oErrDescription Create Shop Order API return code description

        :param int error_code:
        :rtype: str
        """
        return self.order_generator.GetErrorDescription(error_code)

    def set_dpe_login_info(self, i_dpe_login_id: str, i_dpe_password: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_DPELoginInfo(CATBSTR iDPELoginId,
                | CATBSTR iDPEPassword)
                | 
                |     Set DPE Login Information.
                | 
                |     Parameters:
                | 
                |         iDPELoginId
                |             E5 Login ID for authentication 
                |         iDPEPassword
                |             E5 Password for authentication

        :param str i_dpe_login_id:
        :param str i_dpe_password:
        :rtype: None
        """
        return self.order_generator.set_DPELoginInfo(i_dpe_login_id, i_dpe_password)

    def set_export_3dxml(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_Export3DXML(boolean iRequired)
                | 
                |     Set Export 3D XML Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_Export3DXML(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export3_dxml'
        # # vba_code = """
        # # Public Function set_export3_dxml(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_Export3DXML iRequired
        # #     set_export3_dxml = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_image_capture(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportImageCapture(boolean iRequired)
                | 
                |     Set Export Image Capture Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_ExportImageCapture(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_image_capture'
        # # vba_code = """
        # # Public Function set_export_image_capture(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_ExportImageCapture iRequired
        # #     set_export_image_capture = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_job_xml(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportJobXML(boolean iRequired)
                | 
                |     Set Export Job XML Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_ExportJobXML(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_job_xml'
        # # vba_code = """
        # # Public Function set_export_job_xml(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_ExportJobXML iRequired
        # #     set_export_job_xml = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_prec_xml(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportPrecXML(boolean iRequired)
                | 
                |     Set Export Precedence XML Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_ExportPrecXML(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_prec_xml'
        # # vba_code = """
        # # Public Function set_export_prec_xml(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_ExportPrecXML iRequired
        # #     set_export_prec_xml = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ftp(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_FTP(boolean iRequired)
                | 
                |     Set FTP Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_FTP(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ftp'
        # # vba_code = """
        # # Public Function set_ftp(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_FTP iRequired
        # #     set_ftp = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ftp_server_information(
            self,
            iftp_host_name: str,
            iftp_login_name: str,
            iftp_password: str,
            iftp_outputlocation: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_FTPServerInformation(CATBSTR iftpHostName,
                | CATBSTR iftpLoginName,
                | CATBSTR iftpPassword,
                | CATBSTR iftpOutputlocation)
                | 
                |     Set FTP Information.
                | 
                |     Parameters:
                | 
                |         iftpHostName
                |             Service Host Name for transferering the data 
                |         iftpLoginName
                |             Login Name for authentication to the Service Host Machine for
                |             transfering the data 
                |         iftpPassword
                |             Password for the above login 
                |         iftpOutputlocation
                |             Output Dir where to tranfer the data in the
                |             Machine

        :param str iftp_host_name:
        :param str iftp_login_name:
        :param str iftp_password:
        :param str iftp_outputlocation:
        :rtype: None
        """
        return self.order_generator.set_FTPServerInformation(
            iftp_host_name,
            iftp_login_name,
            iftp_password,
            iftp_outputlocation
        )

    def set_filter_input_string(self, ifilter_input_string: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_FilterInputString(CATBSTR ifilterInputString)
                | 
                |     Specifies the filters to be applied while loading the project. The filters
                |     can be specified either in the new way (V5R18 onwards) or the old
                |     way.
                | 
                |      New Way of Filtering:
                |      
                |      In the new way of filtering different filters can be set for
                |      P,P,R
                |      by specifiying different filter sets for each area and also a global
                |      filter set.
                | 
                | 
                |      Old way of Filtering:
                | 
                |      In case of P,P,R filters, either
                |       (a) A Filter string can be supplied OR
                |       (b) A Calculation Model ID can be supplied
                |      Note: Calculation Model filters MUST only be supplied through their IDs.
                |      
                | 
                |      In case of extended filters, either
                |       (a) A Filter string can be supplied OR
                |       (b) A Calculation Model ID can be supplied OR
                |       (c) Both string AND Model ID can be supplied (Combined effectivity
                |       case)
                |      Note: Calculation Model filters MUST only be supplied through their IDs.
                |      
                | 
                |      In case of effectivity filter mode, one of the following rules can be
                |      supplied
                |       (a) Give the objects whose begin & end dates contains the begin & end
                |       date filters values.
                |           The rule value is 1.
                |       (b) Give the object whose begin & end dates are with in the begin & end
                |       dates filter values.
                |           The rule value is 2.
                |       (c) Give the object whose begin date value is lesser than the begin date
                |       filter value &
                |           the end date value on the object is contained with in the begin & end
                |           date filter values.
                |           The rule value is 4.
                |       (d) Give the object whose begin date value is contained with in the begin
                |       & end date filter values &
                |           the end date value on the object is greater than the end date filter
                |           value.
                |           The rule value is 8.
                |       (e) Give the object whose begin & end dates exactly match with that of
                |       the begin & end date filter values
                |           The rule value is 16.
                |      Note: Combination of the above said rules can also be
                |      used.
                |           For example: If the user wants the combination of rule a & c, then
                |           the value of 5 should be passed
                |      Note: If the user has not specified any value for this filter, then a
                |      default value of 31 (combination of all rules) will be
                |      used.
                |      
                | 
                |     Parameters:
                | 
                |         iFilters
                |             [in]
                | 
                |               The filters to be set. 
                |               This is a list of values separated by XML type tags. User Should
                |               specify tags only from one of the below 
                |               set of tags applicable for new and old
                |               filtering.
                | 
                |               The following tags are supported for New way of
                |               Filtering:
                | 
                |                  <GlobalFilterSetName>Global Filter
                |                  Name</GlobalFilterSetName>
                |                  <ProductFilterSetName>Product Filter
                |                  Name</ProductFilterSetName>
                |                  <ProcessFilterSetName>Process Filter
                |                  Name</ProcessFilterSetName>
                |                  <ResourceFilterSetName>Process Filter
                |                  Name</ResourceFilterSetName>   
                |                  <ModStatementFilterID>Filter
                |                  Value</ModStatementFilterID>
                |                  <ProductFilterByCO>Filter
                |                  Value</ProductFilterByCO>
                |                  <PreFilter>Filter Value</PreFilter>
                |                  <PostFilter>Filter Value</PostFilter>
                |                  <PrePostFilter>Filter Value</PrePostFilter>
                |                  <PlanningStateOwnerFilterID>ID of Planning
                |                  State</PlanningStateOwnerFilterID>
                |                  <PlanningStateOtherFilterID>ID of Planning
                |                  State</PlanningStateOtherFilterID>
                |                  <ApplyImplicitFilter>TRUE or
                |                  FALSE</ApplyImplicitFilter>
                | 
                | 
                |               The following tags are supported for Old way of
                |               Filtering:
                | 
                |                  <ProcessFilter>Filter Value</ProcessFilter>
                |                  <ProcessFilterCalcModelID>ID of Calculation Model
                |                  Filter</ProcessFilterCalcModelID>  
                |                  <ProductFilter>Filter Value</ProductFilter>
                |                  <ProductFilterCalcModelID>ID of Calculation Model
                |                  Filter</ProductFilterCalcModelID>
                |                  <ResourceFilter>Filter Value</ResourceFilter>
                |                  <ResourceFilterCalcModelID>ID of Calculation Model
                |                  Filter</ResourceFilterCalcModelID>
                |                  <StartDateEffectivityFilter>Filter
                |                  Value</StartDateEffectivityFilter>
                |                  <EndDateEffectivityFilter>Filter
                |                  Value</EndDateEffectivityFilter>
                |                  <EffectivityFilterMode>Filter
                |                  Value</EffectivityFilterMode>
                |                  <LineNumberFilter>Filter
                |                  Value</LineNumberFilter>
                |                  <LabelFilter>Filter Value</LabelFilter>
                |                  <ModStatementFilterID>Filter
                |                  Value</ModStatementFilterID>
                |                  <PlanningStateOwnerFilterID>ID of Planning
                |                  State</PlanningStateOwnerFilterID>
                |                  <PlanningStateOtherFilterID>ID of Planning
                |                  State</PlanningStateOtherFilterID>
                |                  <ApplyImplicitFilter>TRUE or
                |                  FALSE</ApplyImplicitFilter>
                |                  <ProcessExtendedEffectivityFilter>Filter
                |                  Value</ProcessExtendedEffectivityFilter>
                |                  <ProcessExtendedEffectivityFilterCalcModelID>ID of Calculation
                |                  ModelFilter</ProcessExtendedEffectivityFilterCalcModelID>
                |                  <ProductExtendedEffectivityFilter>Filter
                |                  Value</ProductExtendedEffectivityFilter>
                |                  <ProductExtendedEffectivityFilterCalcModelID>ID of Calculation
                |                  ModelFilter</ProductExtendedEffectivityFilterCalcModelID>
                |                  <ResourceExtendedEffectivityFilter>Filter
                |                  Value</ResourceExtendedEffectivityFilter> 
                |                  <ResourceExtendedEffectivityFilterCalcModelID>ID of
                |                  Calculation ModelFilter</ResourceExtendedEffectivityFilterCalcModelID>
                |
                |               Attribute filters can be supplied using the following
                |               tags
                |               <AttributeFilters>
                |                  <ProcessAttributeFilters>
                |                    <AttributeFilter>
                |                       <PlanTypeName>Name of the
                |                       Plantype</PlanTypeName>
                |                       <AttributeName>Name of the
                |                       Attribute</AttributeName>
                |                       <Operator>Type of Operator. See list of legal values
                |                       below</Operator>
                |                       <AttributeValue>Value of the
                |                       Attribute</AttributeValue>
                |                       Add more <AttributeValue>...</AttributeValue> if more
                |                       attribute values need to be specified
                |                    </AttributeFilter>
                |                    Add more <AttributeFilter>...</AttributeFilter> if more
                |                    attribute filters need to be specified
                |                  </ProcessAttributeFilters>   
                |                  <ProductAttributeFilters>
                |                    Add <AttributeFilter>...</AttributeFilter> as specified
                |                    above
                |                  </ProductAttributeFilters>
                |                  <ResourceAttributeFilters>
                |                    Add <AttributeFilter>...</AttributeFilter> as specified
                |                    above
                |                  </ResourceAttributeFilters>
                |               </AttributeFilters>
                |               
                | 
                |             Note: Instead of specifying plantype name, the object typename
                |             (e.g., "ergocompprocessdefault, "ergocomporgprocess", etc) can also be supplied
                |             if filter is to be applicable to all plantypes
                |             Note: For the <Operator> tag, the following are the legal
                |             values
                |                =
                |                !=
                |                <
                |                >
                |                <=
                |                >=
                |                LIKE
                |                NOT LIKE
                | 
                |     Example:
                | 
                |             In new way of filtering:
                |            iFilters = "<ProcessFilterSetName>Name</ProcessFilterSetName><ProductFilterSetName>Name</ProductFilterSetName><ResourceFilterSetName>Name</ResourceFilterSetName>"
                |            
                |         The order is NOT important. e.g.,
                |         "<ResourceFilterSetName>...</ResourceFilterSetName>" can come before
                |         "<ProcessFilterSetName>...</ProcessFilterSetName>"
                |          
                |     Example:
                | 
                |             In old way of filtering:
                |            iFilters = "<ProcessFilter>Process Type A</ProcessFilter><LabelFilter>Label B</LabelFilter><LineNumberFilter>10</LineNumberFilter>"
                |            
                |         The order is NOT important. e.g., "<LabelFilter>...</LabelFilter>" can
                |         come before "<ProcessFilter>...</ProcessFilter>"
                |
                |     Example:
                | 
                |             In old way of filtering:
                |            Example with attribute filers. Assuming user wishes to filter on
                |            Line Number 10 and load only those Workplans that are labelled "Workplan A" and
                |            "Workplan C"
                |            
                |         iFilters = "<LineNumberFilter>10</LineNumberFilter><AttributeFilters><ProcessAttributeFilters><AttributeFilter>
                |            <PlanTypeName>Workplan</PlanTypeName>
                |            <AttributeName>name</AttributeName>
                |            <Operator>=</Operator>
                |            <AttributeValue>Workplan A</AttributeValue>
                |            <AttributeValue>Workplan C</AttributeValue>
                |           </AttributeFilter></ProcessAttributeFilters></AttributeFilters>"
                |
                |     Returns:
                |         S_OK if all OK E_INVALIDARG if incorrect input format Refer
                |         DNBMHIInterfaces/PublicInterfaces/DNBIAMHILoadParameters.idl :: SetFilters
                |         method for additional information

        :param str ifilter_input_string:
        :rtype: None
        """
        return self.order_generator.set_FilterInputString(ifilter_input_string)

    def set_generate_pack_n_go(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_GeneratePackNGo(boolean iRequired)
                | 
                |     Set Generate PackNGo Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_GeneratePackNGo(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_generate_pack_n_go'
        # # vba_code = """
        # # Public Function set_generate_pack_n_go(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_GeneratePackNGo iRequired
        # #     set_generate_pack_n_go = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_generate_smg_mapping_xml(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_GenerateSMGMappingXML(boolean iRequired)
                | 
                |     Set Generate SMG Mapping XML Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_GenerateSMGMappingXML(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_generate_smg_mapping_xml'
        # # vba_code = """
        # # Public Function set_generate_smg_mapping_xml(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_GenerateSMGMappingXML iRequired
        # #     set_generate_smg_mapping_xml = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_generate_smg_xml(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_GenerateSMGXML(boolean iRequired)
                | 
                |     Set Generate SMG XML Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_GenerateSMGXML(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_generate_smgxml'
        # # vba_code = """
        # # Public Function set_generate_smgxml(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_GenerateSMGXML iRequired
        # #     set_generate_smgxml = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_generate_smg_xml_exe_path(self, i_required: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_GenerateSMGXmlExePath(CATBSTR iRequired)
                | 
                |     Set Generate SMG XML EXE Path.
                | 
                |     Parameters:
                | 
                |         iRequired
                |             Path to the SMG Generator EXE

        :param str i_required:
        :rtype: None
        """
        return self.order_generator.set_GenerateSMGXmlExePath(i_required)

    def set_lite_pack_n_go(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_LitePackNGo(boolean iRequired)
                | 
                |     Set Lite PackNGo Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_LitePackNGo(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lite_pack_n_go'
        # # vba_code = """
        # # Public Function set_lite_pack_n_go(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_LitePackNGo iRequired
        # #     set_lite_pack_n_go = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_load_context(self, i_required: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_LoadContext(CATBSTR iRequired)
                | 
                |     Set Load Context Type.
                | 
                |     Parameters:
                | 
                |         iRequestType
                |             Type Of Request
                | 
                |                 Manufacturing
                |                 Volumetric
                |                 User

        :param str i_required:
        :rtype: None
        """
        return self.order_generator.set_LoadContext(i_required)

    def set_load_positions(self, i_required: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_LoadPositions(CATBSTR iRequired)
                | 
                |     Set Load Positions Type.
                | 
                |     Parameters:
                | 
                |         iRequestType
                |             Type Of Request
                | 
                |                 3DStates
                |                 PublishedSimulation

        :param str i_required:
        :rtype: None
        """
        return self.order_generator.set_LoadPositions(i_required)

    def set_manufacturing_context(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ManufacturingContext(boolean iRequired)
                | 
                |     Set Manufacturing Context Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_ManufacturingContext(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_manufacturing_context'
        # # vba_code = """
        # # Public Function set_manufacturing_context(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_ManufacturingContext iRequired
        # #     set_manufacturing_context = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_process_name(self, iprocess_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ProcessName(CATBSTR iprocessName)
                | 
                |     Set Process Name.
                | 
                |     Parameters:
                | 
                |         iprocessName
                |             Process Name to be set for PackNGo CATProcess

        :param str iprocess_name:
        :rtype: None
        """
        return self.order_generator.set_ProcessName(iprocess_name)

    def set_request_type(self, i_requset_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_RequestType(CATBSTR iRequsetType)
                | 
                |     Set Request Type.
                | 
                |     Parameters:
                | 
                |         iRequestType
                |             Type Of Request
                | 
                |                 DPMSingleSOIGeneration
                |                 DPMMultiSOIGeneration
                |                 DPMMultiSOIGenerationAtCS

        :param str i_requset_type:
        :rtype: None
        """
        return self.order_generator.set_RequestType(i_requset_type)

    def set_requested_node_details(self, i_proj_id: str, i_requested_node_id: str, i_effectivity: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_RequestedNodeDetails(CATBSTR iProjID,
                | CATBSTR iRequestedNodeID,
                | CATBSTR iEffectivity)
                | 
                |     Set Requested Node Details.
                | 
                |     Parameters:
                | 
                |         iProjID
                |             Object ID of the PPR Based Project 
                |         iRequestedNodeID
                |             Object ID of the node selected from PPR Based Project
                |             
                |         iEffectivity
                | 
                |             THIS PARAMETER HAS BEEN DEPRICATED FROM R17SP1 USE
                |             
                | 
                |         OrderGenerator.set_FilterInputString method to set your filters

        :param str i_proj_id:
        :param str i_requested_node_id:
        :param str i_effectivity:
        :rtype: None
        """
        return self.order_generator.set_RequestedNodeDetails(i_proj_id, i_requested_node_id, i_effectivity)

    def set_set_encryption_mode(self, i_encryptmode: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_SetEncryptionMode(boolean iEncryptmode)
                | 
                |     Set Encryption Mode.
                | 
                |     Parameters:
                | 
                |         iEncryptmode
                |             Encryption to be done?(True/False) for encrypting the SOR Package
                |             data

        :param bool i_encryptmode:
        :rtype: None
        """
        return self.order_generator.set_SetEncryptionMode(i_encryptmode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_set_encryption_mode'
        # # vba_code = """
        # # Public Function set_set_encryption_mode(order_generator)
        # #     Dim iEncryptmode (2)
        # #     order_generator.set_SetEncryptionMode iEncryptmode
        # #     set_set_encryption_mode = iEncryptmode
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_transaction_id(self, i_transaction_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_TransactionID(CATBSTR iTransactionID)
                | 
                |     Set Transaction Type.
                | 
                |     Parameters:
                | 
                |         iTransactionID
                |             Transaction ID

        :param str i_transaction_id:
        :rtype: None
        """
        return self.order_generator.set_TransactionID(i_transaction_id)

    def set_update_release_table(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_UpdatereleaseTable(boolean iRequired)
                | 
                |     Set Update Release Table Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_UpdatereleaseTable(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_updaterelease_table'
        # # vba_code = """
        # # Public Function set_updaterelease_table(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_UpdatereleaseTable iRequired
        # #     set_updaterelease_table = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_zip(self, i_required: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_Zip(boolean iRequired)
                | 
                |     Set Zip Flag.
                | 
                |     Parameters:
                | 
                |         iRequired
                | 
                |             Legal values: TRUE/FALSE

        :param bool i_required:
        :rtype: None
        """
        return self.order_generator.set_Zip(i_required)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_zip'
        # # vba_code = """
        # # Public Function set_zip(order_generator)
        # #     Dim iRequired (2)
        # #     order_generator.set_Zip iRequired
        # #     set_zip = iRequired
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'OrderGenerator(name="{self.name}")'
