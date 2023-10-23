#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class MHILoadParameters(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MHILoadParameters
                | 
                | Interface representing a means to set information that is needed for the load
                | and also to retrieve this information on the loaded document.
                | Note: All the IDs in the Get and Set methods defined in this inteface deal with
                | Object ID (attribute name: oid), not the Object UUID (attribute name:
                | objectuuid)
                | 
                | Access to this interface is provided via DNBIAMHIOpenAccess and
                | DNBIAMHISaveAccess. Applications and CAA partners should NOT implement this
                | interface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mhi_load_parameters = com_object

    def get_branch_ids(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetBranchIDs() As CATSafeArrayVariant
                | 
                |     Gets the "subcompitem" IDs (oid) of the Branch. Branch is a list of parents
                |     of the selected object. Please refer to the following PES for details on
                |     Branch. "PES_DELMIA_V5R17_Manufacturing Hub Infrastructure_Manufacturing Hub
                |     Integration_R17MHI031_ExposeLoadSave.doc"
                | 
                |     Example:
                | 
                |            For the following structure, if PWP is the object loaded,
                |
                |             PV
                |              |_PP
                |                 |_WP
                |                    |_PWP
                |                        |_OP1
                |                        |_OP2
                |
                |          the branch is the "subcompitem" ID of PWP, the "subcompitem" ID of WP
                |          and 
                |          the "subcompitem" ID of PP. 
                |          
                |         Note: The list will be filled in that order.
                |
                |     Parameters:
                | 
                |         oListBranchIDs
                |             [out] List of IDs of the Branch in the order mentioned above
                |
                |     Returns:
                |         S_OK in one/more IDs returned S_FALSE if empty output list

        :rtype: tuple
        """
        return self.mhi_load_parameters.GetBranchIDs()

    def get_detailing_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDetailingID() As CATBSTR
                | 
                |     Gets the ID (oid) of the loaded detailing
                | 
                |     Parameters:
                | 
                |         oDetailingID
                |             [inout] ID of the loaded detailing 
                | 
                |     Returns:
                |         S_OK if non-empty string returned S_FALSE if empty string

        :rtype: str
        """
        return self.mhi_load_parameters.GetDetailingID()

    def get_process_tree_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProcessTreeID() As CATBSTR
                | 
                |     Gets the "subcompitem" ID (oid) of the process tree selected for the load
                |     For the topmost node in the tree, since no "subcompitem" ID is available, the
                |     "ergocompbase" ID is supplied as the BOM
                | 
                |     Parameters:
                | 
                |         oProcessTreeID
                |             [inout] ID of the select process tree 
                | 
                |     Returns:
                |         S_OK if non-empty string returned S_FALSE if empty string

        :rtype: str
        """
        return self.mhi_load_parameters.GetProcessTreeID()

    def get_product_bom_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProductBOMID() As CATBSTR
                | 
                |     Gets the "subcompitem" ID (oid) of the product BOM selected for the load
                |     For the topmost node in the tree, since no "subcompitem" ID is available, the
                |     "ergocompbase" ID is supplied as the BOM
                | 
                |     Parameters:
                | 
                |         oProductBOMID
                |             [inout] ID of the select product BOM 
                | 
                |     Returns:
                |         S_OK if non-empty string returned S_FALSE if empty string

        :rtype: str
        """
        return self.mhi_load_parameters.GetProductBOMID()

    def get_resource_tree_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetResourceTreeID() As CATBSTR
                | 
                |     Gets the "subcompitem" ID (oid) of the resource tree selected for the load
                |     For the topmost node in the tree, since no "subcompitem" ID is available, the
                |     "ergocompbase" ID is supplied as the BOM
                | 
                |     Parameters:
                | 
                |         oResourceTreeID
                |             [inout] ID of the select resource tree 
                | 
                |     Returns:
                |         S_OK if non-empty string returned S_FALSE if empty string

        :rtype: str
        """
        return self.mhi_load_parameters.GetResourceTreeID()

    def get_selected_object_id(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSelectedObjectID() As CATBSTR
                | 
                |     Gets the "ergocompbase" ID (oid) of the selected object (object used to
                |     start the load)
                | 
                |     Parameters:
                | 
                |         oSelectedObjectID
                |             [inout] ID of the selected object 
                | 
                |     Returns:
                |         S_OK if non-empty string returned S_FALSE if empty string

        :rtype: str
        """
        return self.mhi_load_parameters.GetSelectedObjectID()

    def set_branch_i_ds(self, i_list_branch_i_ds: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBranchIDs(CATSafeArrayVariant iListBranchIDs)
                | 
                |     Sets the "subcompitem" IDs (oid) of the Branch. Branch is a list of parents
                |     of the selected object. Please refer to the following PES for details on
                |     Branch. "PES_DELMIA_V5R17_Manufacturing Hub Infrastructure_Manufacturing Hub
                |     Integration_R17MHI031_ExposeLoadSave.doc"
                | 
                |     Example:
                | 
                |            For the following structure, if PWP is the object to be loaded,
                |
                |             PV
                |              |_PP
                |                 |_WP
                |                    |_PWP
                |                        |_OP1
                |                        |_OP2
                |
                |          the branch is the "subcompitem" ID of PWP, the "subcompitem" ID of WP
                |          and the "subcompitem" ID of PP.
                |          
                |         Note: The list MUST be filled in that order.
                |
                |     Parameters:
                | 
                |         iListBranchIDs
                |             [in] List of IDs of the Branch in the order mentioned above
                |
                |     Returns:
                |         S_OK in all cases

        :param tuple i_list_branch_i_ds:
        :rtype: None
        """
        return self.mhi_load_parameters.SetBranchIDs(i_list_branch_i_ds)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_branch_i_ds'
        # # vba_code = """
        # # Public Function set_branch_i_ds(mhi_load_parameters)
        # #     Dim iListBranchIDs (2)
        # #     mhi_load_parameters.SetBranchIDs iListBranchIDs
        # #     set_branch_i_ds = iListBranchIDs
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_detailing_id(self, i_detailing_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDetailingID(CATBSTR iDetailingID)
                | 
                |     Sets the ID (oid) of detailing to be loaded
                | 
                |     Parameters:
                | 
                |         iDetailingID
                |             [in] ID of the detailing 
                | 
                |     Returns:
                |         S_OK in all cases

        :param str i_detailing_id:
        :rtype: None
        """
        return self.mhi_load_parameters.SetDetailingID(i_detailing_id)

    def set_filters(self, i_filters: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFilters(CATBSTR iFilters)
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
                |      Old way of Filtering:
                | 
                |      In case of P,P,R filters, either
                |       (a) A Filter string can be supplied OR
                |       (b) A Calculation Model ID can be supplied
                |      Note: Calculation Model filters MUST only be supplied through their IDs.
                |
                |      In case of extended filters, either
                |       (a) A Filter string can be supplied OR
                |       (b) A Calculation Model ID can be supplied OR
                |       (c) Both string AND Model ID can be supplied (Combined effectivity
                |       case)
                |      Note: Calculation Model filters MUST only be supplied through their IDs.
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
                |         S_OK if all OK E_INVALIDARG if incorrect input format

        :param str i_filters:
        :rtype: None
        """
        return self.mhi_load_parameters.SetFilters(i_filters)

    def set_process_tree_id(self, i_process_tree_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProcessTreeID(CATBSTR iProcessTreeID)
                | 
                |     Sets the "subcompitem" ID (oid) of process tree selected for the load For
                |     the topmost node in the tree, since no "subcompitem" ID is available, the
                |     "ergocompbase" ID has to be supplied
                | 
                |     Parameters:
                | 
                |         iProcessTreeID
                |             [in] ID of the process tree 
                | 
                |     Returns:
                |         S_OK in all cases

        :param str i_process_tree_id:
        :rtype: None
        """
        return self.mhi_load_parameters.SetProcessTreeID(i_process_tree_id)

    def set_product_bomid(self, i_product_bomid: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProductBOMID(CATBSTR iProductBOMID)
                | 
                |     Sets the "subcompitem" ID (oid) of product BOM selected for the load For
                |     the topmost node in the tree, since no "subcompitem" ID is available, the
                |     "ergocompbase" ID has to be supplied
                | 
                |     Parameters:
                | 
                |         iProductBOMID
                |             [in] ID of the product BOM 
                | 
                |     Returns:
                |         S_OK in all cases

        :param str i_product_bomid:
        :rtype: None
        """
        return self.mhi_load_parameters.SetProductBOMID(i_product_bomid)

    def set_resource_tree_id(self, i_resource_tree_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetResourceTreeID(CATBSTR iResourceTreeID)
                | 
                |     Sets the "subcompitem" ID (oid) of resource tree selected for the load For
                |     the topmost node in the tree, since no "subcompitem" ID is available, the
                |     "ergocompbase" ID has to be supplied
                | 
                |     Parameters:
                | 
                |         iResourceTreeID
                |             [in] ID of the resource tree 
                | 
                |     Returns:
                |         S_OK in all cases

        :param str i_resource_tree_id:
        :rtype: None
        """
        return self.mhi_load_parameters.SetResourceTreeID(i_resource_tree_id)

    def set_selected_object_id(self, i_selected_object_id: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSelectedObjectID(CATBSTR iSelectedObjectID)
                | 
                |     Sets the "ergocompbase" ID (oid) of selected object (object use to start
                |     the load).
                | 
                |     Parameters:
                | 
                |         iSelectedObjectID
                |             [in] ID of the selected object 
                | 
                |     Returns:
                |         S_OK in all cases

        :param str i_selected_object_id:
        :rtype: None
        """
        return self.mhi_load_parameters.SetSelectedObjectID(i_selected_object_id)

    def __repr__(self):
        return f'MHILoadParameters(name="{self.name}")'
