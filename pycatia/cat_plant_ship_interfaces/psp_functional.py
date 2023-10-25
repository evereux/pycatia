#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.cat_plant_ship_interfaces.psp_list_of_objects import PSPListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class PSPFunctional(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspFunctional
                | 
                | Represents Plant Ship functional object.
                | Role: To access Plant Ship Functional object information.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_functional = com_object

    @property
    def catalog_part_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CatalogPartName() As CATBSTR (Read Only)
                | 
                |     Returns catalog part name of physical object that realizes this
                |     function.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim strVar1 As CATBSTR
                |           ...
                |          Set strVar1 = objThisIntf.CatalogPartName

        :rtype: str
        """

        return self.psp_functional.CatalogPartName

    @property
    def function_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FunctionStatus() As CatPspIDLFunctionStatus (Read
                | Only)
                | 
                |     Returns function object status.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPhysical
                |          Dim objArg1 As CatPspIDLFunctionStatus
                |           ...
                |          objArg1 = objThisIntf.FunctionStatus

        :return: enum cat_psp_idl_function_status
        :rtype: int
        """

        return self.psp_functional.FunctionStatus

    @property
    def part_catalog_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PartCatalogName() As CATBSTR (Read Only)
                | 
                |     Returns Part catalog name of physical object that realizes this
                |     function.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim strVar1 As CATBSTR
                |           ...
                |          strVar1 = objThisIntf.PartCatalogName

        :rtype: str
        """

        return self.psp_functional.PartCatalogName

    @property
    def part_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PartNumber() As CATBSTR (Read Only)
                | 
                |     Returns part number of physical object that realizes this
                |     function.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim strVar1 As CATBSTR
                |           ...
                |          strVar1 = objThisIntf.PartNumber

        :rtype: str
        """

        return self.psp_functional.PartNumber

    @property
    def part_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PartType() As CATBSTR (Read Only)
                | 
                |     Returns the part type of physical object that realizes this
                |     function.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim strVar1 As CATBSTR
                |           ...
                |          strVar1 = objThisIntf.PartType

        :rtype: str
        """

        return self.psp_functional.PartType

    @property
    def physicals(self) -> PSPListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Physicals() As PspListOfObjects (Read Only)
                | 
                |     Returns a list of all associated physical objects.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim objArg1 As PspListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.Physicals

        :rtype: PSPListOfObjects
        """

        return PSPListOfObjects(self.psp_functional.Physicals)

    @property
    def standard(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Standard() As CATBSTR (Read Only)
                | 
                |     Return Standard.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim strVar1 As CATBSTR
                |           ...
                |          strVar1 = objThisIntf.Standard

        :rtype: str
        """

        return self.psp_functional.Standard

    def get_compatible_part_types(self, iu_standard: str) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCompatiblePartTypes(CATBSTR iuStandard) As
                | PspListOfBSTRs
                | 
                |     Retrieves a list of all physical part types that are compatible with this
                |     function.
                | 
                |     Parameters:
                | 
                |         iuStandard
                |             Standard name 
                | 
                |     Returns:
                |         List of Compatible Part Types.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional  
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As PspListOfBSTRs
                |          
                |           ...
                |          Set objArg1 = objThisIntf.GetCompatiblePartTypes   (strVar1)

        :param str iu_standard:
        :rtype: PSPListOfBSTRs
        """
        return PSPListOfBSTRs(self.psp_functional.GetCompatiblePartTypes(iu_standard))

    def is_ok_to_integrate(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsOKToIntegrate() As boolean
                | 
                |     Check it is OK to integrate (realize) this function with a physical
                |     part.
                | 
                |     Returns:
                |         TRUE if ok to be integrated
                |
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional  
                |          Dim objArg1 As boolean  
                |           ...
                |          objArg1 = objThisIntf.IsOKToIntegrate

        :rtype: bool
        """
        return self.psp_functional.IsOKToIntegrate()

    def is_realized(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsRealized() As boolean
                | 
                |     Checks if the Function object is realized or not.
                | 
                |     Returns:
                |         TRUE if the object is Realized
                |
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional  
                |          Dim objArg1 As boolean  
                |           ...
                |          objArg1 = objThisIntf.IsRealized

        :rtype: bool
        """
        return self.psp_functional.IsRealized()

    def is_spec_driven(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsSpecDriven() As boolean
                | 
                |     Checks if the functional object is specification driven or
                |     not.
                | 
                |     Returns:
                |         TRUE if this object is specification driven.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional  
                |          Dim objArg1 As boolean  
                |           ...
                |          objArg1 = objThisIntf.IsSpecDriven

        :rtype: bool
        """
        return self.psp_functional.IsSpecDriven()

    def list_compatible_part_numbers(
            self,
            iu_part_type: str,
            iu_standard: str,
            iu_catalog_name: str,
            o_l_part_types: PSPListOfBSTRs,
            o_l_catalog_part_names: PSPListOfBSTRs
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListCompatiblePartNumbers(CATBSTR iuPartType,
                | CATBSTR iuStandard,
                | CATBSTR iuCatalogName,
                | PspListOfBSTRs oLPartTypes,
                | PspListOfBSTRs oLCatalogPartNames)
                | 
                |     Retrieves a list of compatible Part numbers and part
                |     types.
                | 
                |     Parameters:
                | 
                |         iuPartType
                |             part type 
                |         iuStandard
                |             Standard name 
                |         iuCatalogName
                |             catalog name 
                |         oLPartTypes
                |             a list of part types 
                |         oLCatalogPartNames
                |             List of catalog part names 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspFunctional
                |          Dim strVar1 As CATBSTR
                |          Dim strVar2 As CATBSTR
                |          Dim strVar3 As CATBSTR
                |          Dim objArg4 As PspListOfBSTRs
                |          Dim objArg5 As PspListOfBSTRs
                |          
                |          ..
                |          ..
                |          objThisIntf.ListCompatiblePartNumbers
                |          strVar1,strVar2,strVar3,objArg4,objArg5

        :param str iu_part_type:
        :param str iu_standard:
        :param str iu_catalog_name:
        :param PSPListOfBSTRs o_l_part_types:
        :param PSPListOfBSTRs o_l_catalog_part_names:
        :rtype: None
        """
        return self.psp_functional.ListCompatiblePartNumbers(
            iu_part_type,
            iu_standard,
            iu_catalog_name,
            o_l_part_types.com_object,
            o_l_catalog_part_names.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_compatible_part_numbers'
        # # vba_code = """
        # # Public Function list_compatible_part_numbers(psp_functional)
        # #     Dim iuPartType (2)
        # #     psp_functional.ListCompatiblePartNumbers iuPartType
        # #     list_compatible_part_numbers = iuPartType
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PSPFunctional(name="{self.name}")'
