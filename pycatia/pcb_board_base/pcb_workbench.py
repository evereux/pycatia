#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.workbench import Workbench
from pycatia.system_interfaces.any_object import AnyObject


class PCBWorkbench(Workbench):
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
                |                         PCBWorkbench
                | 
                | Interface to access Circuit Board Design workbench object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcb_workbench = com_object

    def create_board(self, i_root: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateBoard(CATBaseDispatch iRoot) As CATBaseDispatch
                | 
                |     Allows to create a Board.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             Root product of the Part to extend 
                |         oBoard
                |             The board created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_root:
        :rtype: AnyObject
        """
        return self.pcb_workbench.CreateBoard(i_root.com_object)

    def create_component(
            self,
            i_root: AnyObject,
            i_elec_package_number: str,
            i_elec_part_number: str,
            i_elec_type: str
    ) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateComponent(CATBaseDispatch iRoot,
                | CATBSTR iElecPackageNumber,
                | CATBSTR iElecPartNumber,
                | CATBSTR iElecType) As CATBaseDispatch
                | 
                |     Allows to create a Component.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             Root product of the Part to extend 
                |         iElecPackageNumber
                |             The package number used to valuate the component attribute
                |             
                |         iElecPartNumber
                |             The part number used to valuate the part number of the component
                |             
                |         iElecType
                |             The Type of the component to create : ELECTRICAL or MECHANICAL 
                |         oComponent
                |             The Component created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_root:
        :param str i_elec_package_number:
        :param str i_elec_part_number:
        :param str i_elec_type:
        :rtype: AnyObject
        """
        return self.pcb_workbench.CreateComponent(
            i_root.com_object,
            i_elec_package_number,
            i_elec_part_number,
            i_elec_type
        )

    def create_panel(self, i_root: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreatePanel(CATBaseDispatch iRoot) As CATBaseDispatch
                | 
                |     Allows to create a panel.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             Root product of the Part to extend 
                |         oPanel
                |             The panel created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_root:
        :rtype: AnyObject
        """
        return self.pcb_workbench.CreatePanel(i_root.com_object)

    def get_root_product(self, doc: Document) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRootProduct(Document doc) As CATBaseDispatch
                | 
                |     Allows to get the root product of a document.
                | 
                |     Parameters:
                | 
                |         doc
                |             The document to scan 
                |         oRoot
                |             The root product of the document scanned 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Document doc:
        :rtype: AnyObject
        """
        return self.pcb_workbench.GetRootProduct(doc.com_object)

    def __repr__(self):
        return f'PCBWorkbench(name="{self.name}")'
