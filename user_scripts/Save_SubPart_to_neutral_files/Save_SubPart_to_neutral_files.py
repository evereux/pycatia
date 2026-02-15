#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert_2_sep_stp
Script for convert part in product to separate stp files
Warning:
    - CATIA must be running with an active Product document
    - Product must have part files
    - Part files must be saved
"""

from pycatia.in_interfaces.application import Application
from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.exception_handling.exceptions import CATIAApplicationException

from pycatia import catia
import os
import sys
from pathlib import Path
from dataclasses import dataclass


__author__ = '[ptm] by plm-forum.ru'
__status__ = 'beta'



# Adding project path for development
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_project_root, 'pycatia'))

@dataclass
class Export_constants:
    THIS_SCRIPT:str="--- ProductToStepExport V1.0 ---"
    #use \\ for path
    EXPORT_DIR:str="c:\\temp"
    EXPORT_FILE_EXT:str=".stp"
    EXPORT_FILE_FORMAT:str="stp"


@dataclass
class Cat_pointer:
    """
    Class to carry caa application and main opened document
    """
    App:Application
    Doc:Document



def initialize_catia(visible=True) -> Cat_pointer:
    """
    Initializes CATIA and returns the active PartDocument.

    Args:
        visible: Make CATIA visible (default True)

    Returns:
        PartDocument: Active CATIA document

    Raises:
        SystemExit: If CATIA is not running or no open document
    """
    try:
        caa = catia()
        caa.application.visible = visible

        if not caa.active_document:
            raise CATIAApplicationException("No active document")

        document = ProductDocument(caa.active_document.com_object)

        if not document.is_product:
            raise CATIAApplicationException(
                "Active document is not a product")

        print(f"Opened document: {caa.active_document.full_name}")

        return Cat_pointer(App=caa,Doc=document)

    except CATIAApplicationException as e:
        print(f"CATIA initialization error: {e.message}")
        print("Ensure that:")
        print("1. CATIA is running")
        print("2. A part document (*.CATPart) is open")
        print("3. Multiple CATIA sessions are not running")
        


def validate_part_document(document: ProductDocument):
    """
    Validates that the part document contains no errors.

    Args:
        document: Document to validate

    Raises:
        SystemExit: If document contains errors
    """
    try:
        prod = document.product
        prod.update()
    except CATIAApplicationException as e:
        print(f"Error updating part: {e.message}")
        print("Part document must be error-free!")
        sys.exit(1)


class Convert_2_sep_stp:
    
    """
    constants
    Poitn to right place.
    Folder must exist
    
    """
    CONSTANT=Export_constants()
    def __init__(self, refs:Cat_pointer):
        try:
            self.caa =catia
            self.caa = refs.App
            self.Doc=Document
            self.Doc=refs.Doc
            self.product = refs.Doc.product
            self.tree=refs.Doc.product.products
        except CATIAApplicationException as e:
            print(f"Error initialize convert class: {e.message}")
            print("Product must be open. ")
            print("Product must have some child")
            sys.exit(1)
            
    



    def convert(self):
        print(self.CONSTANT.THIS_SCRIPT)
        #walk to sub tree and select only parts and ignore subproduct
        sel=self.Doc.selection
        sel.clear()
        
        
        prt=sel.search("'Product Structure'.Part + FreeStyle.Part + 'Systems Routing'.Part + 'HVAC Design'.Part + 'Assembly Design'.Part + 'Waveguide Diagrams'.Part + 'HVAC Diagrams'.Part + 'Part Design'.Part + 'Systems Space Reservation'.Part + 'Generative Shape Design'.Part + 'Functional Molded Part'.Part + 'Process Applications'.Part + 'Tubing Diagrams'.Part + 'Plant Layout'.Part + 'Piping and Instrumentation Diagrams'.Part;all")
        print("sel=",prt)
        list_part=[]
        for i in sel.items():
            #select only part
            if i.type=="Part":
                doc=Document(i.value.parent.com_object)
                item=Path(doc.full_name).resolve()
                if item not in list_part:
                    if item.exists():
                        list_part.append(item)
                    else:
                        raise CATIAApplicationException(
                "Save all parts before run script")
            
                        
        
        for i in list_part:
            try:
                cur_doc = self.caa.documents.open(i)
                print("i=",i)
                print("Path_i=",Path(i).stem)
                fn_export =Path(self.CONSTANT.EXPORT_DIR+"\\"+Path(i).stem+self.CONSTANT.EXPORT_FILE_EXT).resolve()
                print("fn=",fn_export)
                cur_doc.export_data(fn_export, self.CONSTANT.EXPORT_FILE_FORMAT, True)
                print("Save file:")
                print("-->",fn_export)
                cur_doc.close()
            except:
                raise CATIAApplicationException(
                "See class Export_constants: PATHs must exists! ")
                return 
               
# Main initialization
if __name__ == "__main__":
    # CATIA initialization
    try:
        cat_refs = initialize_catia(visible=True)

        # Document validation
        validate_part_document(cat_refs.Doc)

        print("CATIA successfully initialized")
        # =============================================================================
        # User code should be placed below
        # =============================================================================
        cat_refs.Doc.product.apply_work_mode(2)
        start_convert=Convert_2_sep_stp(cat_refs)
        start_convert.convert()
        print("Export successful!")
        # =============================================================================
        # End user code
        # =============================================================================

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)
