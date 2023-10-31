#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pathlib import Path

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.product_structure_interfaces.product import Product


class AssemblyConvertor(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AssemblyConvertor
                | 
                | Product conversion object.
                | The AssemblyConvertor is the object that allows saving an
                | assembly to a specified format. Two objects exist from now on
                | : BillOfMaterial, which creates a bill of material (every
                | sub-assembly is represented, with all the one level depth
                | components), and ListingReport, which creates a listing report
                | (shows the product structure as it appears in the graph)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_convertor = com_object

    def print(self, i_file_type: str, i_file: Path, i_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Print(CATBSTR iFileType,
                | CATBSTR iFile,
                | Product iProduct)
                | 
                |     Extracts the product's contents as a specified format. Saves it in a txt,
                |     html or xls file (depends of the object).
                | 
                |     Parameters:
                | 
                |         iFileType
                |             Type of the resulting file : TXT (for text file),
                |             HTML (for html file), XLS (for xls file) or MOTIF
                |             (do not use).
                |         iFile
                |             Path of the resulting file 
                |         iProduct
                |             Product that will be converted

        :param str i_file_type:
        :param Path i_file:
        :param Product i_product:
        :rtype: None
        """

        vba_function_name = 'print'
        vba_code = """
        Public Function print(assembly_convertor, i_file_type, i_file, i_product)
            assembly_convertor.Print i_file_type, i_file, i_product
            print = iFileType
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object, i_file_type, str(i_file), i_product.com_object])

    def set_current_format(self, ilist_props: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetCurrentFormat(CATSafeArrayVariant ilistProps)
                | 
                |     Defines the properties that will be used in the print
                |     method.
                | 
                |     Parameters:
                | 
                |         ilistProps
                |             list of properties to display

        :param tuple ilist_props:
        :rtype: None
        """
        return self.assembly_convertor.SetCurrentFormat(ilist_props)

    def set_secondary_format(self, ilist_props: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSecondaryFormat(CATSafeArrayVariant ilistProps)
                | 
                |     Defines the secondary properties that will be used in the print
                |     method.
                | 
                |     Parameters:
                | 
                |         ilistProps
                |             secondary list of properties to display

        :param tuple ilist_props:
        :rtype: None
        """
        return self.assembly_convertor.SetSecondaryFormat(ilist_props)

    def __repr__(self):
        return f'AssemblyConvertor(name="{self.name}")'
