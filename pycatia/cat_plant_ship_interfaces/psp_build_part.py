#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class PSPBuildPart(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspBuildPart
                | 
                | Represents Interface to create and modify a part.
                | Role: To build and define a part.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_build_part = com_object

    def change_part_type(self, i_ref_part: Product, iu_part_type: str, u_part_number: str) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ChangePartType(Product iRefPart,
                | CATBSTR iuPartType,
                | CATBSTR uPartNumber) As Product
                | 
                |     Returns the part after changing the part type of an existing
                |     part.
                | 
                |     Parameters:
                | 
                |         iReferencePart
                |             Reference Product in CATPart document to modify. 
                |         iPartType
                |             New part class type. 
                |         iPartNumber
                |             New Part number. 
                | 
                |     Returns:
                |         New reference Product in CATPart document
                |
                |     Example:
                |
                |          Dim objThisIntf As PspBuildPart
                |          Dim iRefPart As   Product
                |          Dim iuPartType As CATBSTR
                |          Dim uPartNumber As CATBSTR
                |          Dim oNewRefPart As Product
                |           ...
                |          Set oNewRefPart= objThisIntf.ChagePartType (iRefPart, iuPartType,
                |          uPartNumber )

        :param Product i_ref_part:
        :param str iu_part_type:
        :param str u_part_number:
        :rtype: Product
        """
        return Product(self.psp_build_part.ChangePartType(i_ref_part.com_object, iu_part_type, u_part_number))

    def list_part_parametric_attributes(self, i_ref_part: Product) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListPartParametricAttributes(Product iRefPart) As
                | PspListOfBSTRs
                | 
                |     Returns the part parametric attribute names.
                | 
                |     Parameters:
                | 
                |         iRefPart
                |             Reference Product in new CATPart document. 
                | 
                |     Returns:
                |         List of parametric attribute names.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspBuildPart
                |          Dim iRefPart As Product
                |          Dim oLAttributeNames As PspListOfBSTRs
                |           ...
                |          Set oLAttributeNames = objThisIntf.ListPartParametricAttributes (iRefPart)

        :param Product i_ref_part:
        :rtype: PSPListOfBSTRs
        """
        return PSPListOfBSTRs(self.psp_build_part.ListPartParametricAttributes(i_ref_part.com_object))

    def new_part(self, iu_part_type: str, u_part_number: str) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NewPart(CATBSTR iuPartType,
                | CATBSTR uPartNumber) As Product
                | 
                |     Create a new part.
                | 
                |     Parameters:
                | 
                |         iPartType
                |             Part class type. 
                |         iPartNumber
                |             Part number. 
                | 
                |     Returns:
                |         Retruns Reference Product pointer in new CATPart document.
                |         
                |     Example:
                |
                |          Dim objThisIntf As PspBuildPart
                |          Dim iuPartType As CATBSTR
                |          Dim uPartNumber As CATBSTR
                |          Dim oNewRefPart As Product
                |           ...
                |          Set oNewRefPart = objThisIntf.NewPart (iuPartType, uPartNumber)

        :param str iu_part_type:
        :param str u_part_number:
        :rtype: Product
        """
        return Product(self.psp_build_part.NewPart(iu_part_type, u_part_number))

    def set_part_parametric_attributes(self, i_ref_part: Product, i_l_attribute_names: PSPListOfBSTRs) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPartParametricAttributes(Product iRefPart,
                | PspListOfBSTRs iLAttributeNames)
                | 
                |     Sets the part parametric attribute names.
                | 
                |     Parameters:
                | 
                |         iRefPart
                |             Reference Product in new CATPart document. 
                |         iLAttributeNames
                |             List of parametric attribute names. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspBuildPart
                |          Dim iRefPart As Product
                |          Dim iLAttributeNames As PspListOfBSTRs
                |           ...
                |          objThisIntf.SetPartParametricAttributes iRefPart,
                |          iLAttributeNames

        :param Product i_ref_part:
        :param PSPListOfBSTRs i_l_attribute_names:
        :rtype: None
        """
        return self.psp_build_part.SetPartParametricAttributes(i_ref_part.com_object, i_l_attribute_names.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_part_parametric_attributes'
        # # vba_code = """
        # # Public Function set_part_parametric_attributes(psp_build_part)
        # #     Dim iRefPart (2)
        # #     psp_build_part.SetPartParametricAttributes iRefPart
        # #     set_part_parametric_attributes = iRefPart
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PSPBuildPart(name="{self.name}")'
