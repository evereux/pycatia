#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.part import Part
from pycatia.system_interfaces.any_object import AnyObject


class SDDProduct(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddProduct
                | 
                | Interface to create a SDD Design Unit under a Product.
                | Role: Allows creating Design Unit under a Product.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sdd_product = com_object

    def create_design_unit(self) -> Part:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateDesignUnit() As Part
                | 
                |     Creates the Design Unit inside a Product.
                | 
                |     Example:
                |
                |              This Example creates a Design Unit inside a Product from
                |              scratch.
                |
                |              ' Create a New Product Document
                |              Dim NewProdDoc As ProductDocument
                |              Set NewProdDoc = CATIA.Documents.Add("Product")
                |              ' Get the Product from the Product Document
                |              Dim RootPrd As Product
                |              Set RootPrd = NewProdDoc.Product
                |              ' Select the Product Document and Add the product to this
                |              selection
                |              Dim SelectionObj As Selection
                |              Set SelectionObj = NewProdDoc.Selection
                |              SelectionObj.Add RootPrd
                |              ' Create a SDD product from above Product
                |              Dim SddProductObj As SddProduct
                |              Set SddProductObj = SelectionObj.FindObject("CATIASddProduct")
                |              ' Create a Design Unit under this Product
                |              Dim SddDesignUnit As Part
                |              Set SddDesignUnit = SddProductObj.CreateDesignUnit
                |              ' Using this Part get the CustomerFactory
                |              Dim FactoryObj As SfmFactory
                |              Set FactoryObj = SddDesignUnit.GetCustomerFactory("SfmFactory")

        :rtype: Part
        """
        return Part(self.sdd_product.CreateDesignUnit())

    def __repr__(self):
        return f'SDDProduct(name="{self.name}")'
