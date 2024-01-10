#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.cat_smarteam_integ_interfaces.sti_db_children import StiDBChildren


class StiDBItem(AnyObject):
    """

    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     StiDBItem
            |
            | Represents the SmarTeam Integration Object, that is to say the Document coming
            | from SmarTeam database.
            | Role: It retrieves SmarTeam Document information. It is managed by
            | StiEngine.
            |
            | See also:
            |     StiEngine
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sti_db_item = com_object

    def get_children(self) -> 'StiDBChildren':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetChildren() As StiDBChildren
                | 
                |     Returns both all the Children of the CATIA Document -associated to the
                |     CATIAStiDBItem- and their corresponding Link Types with their Father CATIA
                |     Document.
                | 
                |     See also:
                |         StiDBChildren 
                |     Returns:
                |         This ouptut corresponds to the retrieved CATIAStiDBChildren from the
                |         Father CATIAStiDBItem. 
                |     Example:
                | 
                |           The following example returns in ochildrenList both all the Children
                |           
                |          and their Link Types with their CATIAStiDBItem Father
                |          oStiDBItem.
                |
                |          Dim oStiDBItem As StiDBItem
                |          Dim ochildrenList As StiDBChildren
                |          Set ochildrenList = oStiDBItem.GetChildren
                |          Dim lChildrenNumber As long
                |          lChildrenNumber = ochildrenList.Count
                |          For i = 1 To lChildrenNumber
                |             Dim oChildStiDBItem As StiDBItem
                |             Set oChildStiDBItem = ochildrenList.Item(i)
                |             Dim sChildLinkType As CATBSTR
                |             sChildLinkType = ochildrenList.LinkType(i)
                |          Next

        :rtype: StiDBChildren
        """

        from pycatia.cat_smarteam_integ_interfaces.sti_db_children import StiDBChildren
        return StiDBChildren(self.sti_db_item.GetChildren())

    def get_document(self) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDocument() As Document
                | 
                |     Returns the CATIA Document associated to the CATIAStiDBItem -the SmarTeam
                |     Integration Object.
                | 
                |     Returns:
                |         This ouptut corresponds to the retrieved CATIA Document.
                |         
                |     Example:
                | 
                |           The following example returns in oDocument the CATIA Document
                |           corresponding to 
                |          the CATIAStiDBItem oStiDBItem.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiEngine.GetStiDBItemFromCATBSTR("E:/CATIAFiles/Engine.CATProduct")
                |          Dim oDocument As Document
                |          Set oDocument = oStiDBItem.GetDocument

        :rtype: Document
        """
        return Document(self.sti_db_item.GetDocument())

    def get_document_full_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDocumentFullPath() As CATBSTR
                | 
                |     Returns the Full Path of the CATIA Document associated to the
                |     CATIAStiDBItem.
                | 
                |     Returns:
                |         This ouptut corresponds to the retrieved Full Path of the
                |         CATIAStiDBItem. 
                |     Example:
                | 
                |           The following example returns in oFullPath the full path
                |           corresponding to 
                |          the CATIAStiDBItem oStiDBItem.
                |
                |          Dim oStiDBItem As StiDBItem
                |          Dim oFullPath As string
                |          oFullPath = oStiDBItem.GetDocumentFullPath

        :rtype: str
        """
        return self.sti_db_item.GetDocumentFullPath()

    def is_cfo_type(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsCFOType() As boolean
                | 
                |     Returns if the CATIA Document -associated to the CATIAStiDBItem- is a
                |     Component File or not.
                | 
                |     Returns:
                |         This ouptut corresponds to the boolean 'oIsCFOType'. 'oIsCFOType' is
                |         True when the CATIAStiDBItem is a Component File, False otherwise.
                |         
                |     Example:
                | 
                |           The following example tests if the CATIAStiDBItem is a Component
                |           File.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          (...)
                |          Dim oIsCFOType As boolean
                |          oIsCFOType = oStiEngine.IsCFOType

        :rtype: bool
        """
        return self.sti_db_item.IsCFOType()

    def is_root(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsRoot() As boolean
                | 
                |     Returns if the CATIA Document -associated to the CATIAStiDBItem- is a Root.
                |     This method returns True if the Document is a Root, False
                |     otherwise.
                | 
                |     Returns:
                |         This ouptut corresponds to the boolean 'oIsRootCFO'. 
                |     Example:
                | 
                |           The following example tests if the CATIAStiDBItem is a Root component
                |           file.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          (...)
                |          Dim oIsRootCFO As boolean
                |          oIsRootCFO = oStiEngine.IsRoot

        :rtype: bool
        """
        return self.sti_db_item.IsRoot()

    def __repr__(self):
        return f'StiDBItem(name="{self.name}")'
