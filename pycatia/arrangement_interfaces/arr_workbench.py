#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arr_nomenclature_tree import ArrNomenclatureTree
from pycatia.arrangement_interfaces.arrangement_product import ArrangementProduct
from pycatia.in_interfaces.workbench import Workbench
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class ArrWorkbench(Workbench):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         ArrWorkbench
                | 
                | Returns the Arrangement Workbench.
                | Role: Use this interface to manage the ArrNomenclatureTree object, create
                | Arrangement objects (such as ArrangementArea, ArrangementRun
                | etc).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arr_workbench = com_object

    @property
    def arr_nomenclature_tree(self) -> ArrNomenclatureTree:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrNomenclatureTree() As ArrNomenclatureTree (Read
                | Only)
                | 
                |     Returns the ArrNomenclatureTree.

        :rtype: ArrNomenclatureTree
        """

        return ArrNomenclatureTree(self.arr_workbench.ArrNomenclatureTree)

    def add_nomenclature_tree(self) -> ArrNomenclatureTree:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddNomenclatureTree() As ArrNomenclatureTree
                | 
                |     This method allows the user to add a nomenclature tree if the
                |     get_ArrNomenclatureTree returns a Return code of E_FAIL. Basically, the
                |     workbench could not locate the startup instance to generate the necessary
                |     NomenclatureTree information.

        :rtype: ArrNomenclatureTree
        """
        return ArrNomenclatureTree(self.arr_workbench.AddNomenclatureTree())

    def convert_arrangement_product_to_product(self, i_arr_product: ArrangementProduct) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ConvertArrangementProductToProduct(ArrangementProduct iArrProduct) As
                | Product
                | 
                |     This method converts an ArrangementProduct back to a
                |     Product.
                | 
                |     Parameters:
                | 
                |         iArrProduct
                |             Input ArrangementProduct to be converted. 
                | 
                |     Returns:
                |         oProduct As CATIAProduct Converted Product. 
                |     See also:
                |         Product

        :param ArrangementProduct i_arr_product:
        :rtype: Product
        """
        return Product(self.arr_workbench.ConvertArrangementProductToProduct(i_arr_product.com_object))

    def convert_product_to_arrangement_product(self, i_product: Product) -> ArrangementProduct:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ConvertProductToArrangementProduct(Product iProduct) As
                | ArrangementProduct
                | 
                |     This method converts a Product to an ArrangementProduct.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             Input Product to be converted. 
                | 
                |     Returns:
                |         oArrProduct Converted ArrangementProduct. 
                |     See also:
                |         Product

        :param Product i_product:
        :rtype: ArrangementProduct
        """
        return ArrangementProduct(self.arr_workbench.ConvertProductToArrangementProduct(i_product.com_object))

    def find_interface(self, i_interface_name: str, i_object: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FindInterface(CATBSTR iInterfaceName,
                | CATBaseDispatch iObject) As CATBaseDispatch
                | 
                |     This method returns a interface handle as specified by the input interface
                |     name and the input interface handle.
                | 
                |      Dim interfaceFound As AnyObject
                |      Set interfaceFound = CATIAArrWorkbench.FindInterface("InterfaceNameToFind",CATIAProduct_iObject)
                |      
                | 
                |     Parameters:
                | 
                |         iInterfaceName
                |             interface name to search for ("CATIAxxxx") 
                |         iObject
                |             The object to search for the required interface. 
                | 
                |     Returns:
                |         oInterfaceFound interface handle found

        :param str i_interface_name:
        :param AnyObject i_object:
        :rtype: AnyObject
        """
        return self.arr_workbench.FindInterface(i_interface_name, i_object.com_object)

    def __repr__(self):
        return f'ArrWorkbench(name="{self.name}")'
