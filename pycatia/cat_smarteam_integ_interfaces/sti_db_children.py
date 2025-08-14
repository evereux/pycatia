#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_smarteam_integ_interfaces.sti_db_item import StiDBItem
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class StiDBChildren(AnyObject):
    """

    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     StiDBChildren
            |
            | Represents all the Children of a CATIAStiDBItem.
            |
            | For each Child, we are able to retrieve its associated CATIAStiDBItem and the
            | Link Type (between itself and its father).
            | It should be represented as the following Correspondance Table { Child Number /
            | CATIAStiDBItem / Link Type}.
            |
            | Example:
            |
            |       The following example presents an Assembly structure and the associated
            |       Correspondance Tables for each element.
            |
            |      +-----------+
            |      \|  Product  \|<-----------------+
            |      +-----------+                  \|
            |         \|                           \|
            |         \|                           \|
            |         \|                           \|
            |        \|                           \|
            |         \|                           \|
            |         \|   +-----------------+     \|
            |         +-->\| Reference Part  \|     \|Contextual Link
            |         \|   +-----------------+     \|
            |         \|            ^              \|
            |         \|            \|              \|
            |         \|            \| Design Link  \|
            |         \|            \|              \|
            |         \|            \|              \|
            |         \|   +-----------------+     \|
            |         +-->\| Contextual Part \|-----+
            |             +-----------------+
            |
            |
            |     CATIAStiDBChildren for Product Child Number 	CATIAStiDBItem 	Link
            |     Type
            |     Child n°1 	Reference Part 	Product Link
            |     Child n°2 	Contextual Part 	Product Link
            |
            |     CATIAStiDBChildren for Contextual Part Child Number 	CATIAStiDBItem 	Link
            |     Type
            |     Child n°1 	Reference Part 	Design Link
            |     Child n°2 	Product 	Contextual Link
            |
            |     CATIAStiDBChildren for Reference Part Child Number 	CATIAStiDBItem 	Link
            |     Type
            |
            |     Here is the List of all CATIA Link Types :
            |
            |     CATIA Link Behavior 	Description
            |     CATIA Product Link 	Defines the basic Product Structure Link -i.e.: the
            |     link between either a Product and its Sub-Products or a Product and its
            |     Representation
            |     CATIA Design Link 	Defines Design Link -i.e.: Part to Part Link created
            |     with 'Copy/Paste ... with link' or as Contextual Link It can also be used for
            |     Link to external Parameters
            |     CATIA Design Table Link 	Defines the Link to a Design
            |     Table
            |     CATIA Rule Base Link 	Defines the Link to Document defining Rule
            |     Base
            |     CATIA Downstream Application Link 	Defines for instance the Link between a
            |     Drawing or an Analysis Document and a Part Document
            |     CATIA Contextual Link 	Defines the Link from a Part Document to its
            |     Context
            |     CATIA Result Link 	Defines the Link to "Result" document, like Analysis
            |     Reports, ...
            |     CATIA Is Composed Of Link 	Defines a simple "Composed Of" Link, like a
            |     Catalog Document Composed Of Sub-Catalog Documents
            |     CATIA Reference Link 	Defines any kind of Link that does not belong to one
            |     type described above including for instance OLE links, Link from a Catalog
            |     Document to a Part, Link to Material Document, ...
            |
            | See also:
            |     StiDBItem
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sti_db_children = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the Number of Children currently gathered in
                |     CATIAStiDBChildren.
                | 
                |     Returns:
                |         This output corresponds to the Children Number of a CATIAStiDBItem.
                |         
                |     Example:
                | 
                |               This example retrieves in  lChildrenNumber the Number of children
                |               currently gathered in oStiDBChildren.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiEngine.GetStiDBItemFromCATBSTR("E:/CATIAFiles/Assembly.CATProduct")
                |          Dim oStiDBChildren As StiDBChildren
                |          Set oStiDBChildren = oStiDBItem.GetChildren()
                |          (...)
                |          Dim oNbChildren As long
                |          oNbChildren = oStiDBChildren.Count

        :rtype: int
        """

        return self.sti_db_children.Count

    def item(self, i_index: cat_variant) -> StiDBItem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As StiDBItem
                | 
                |     Returns the CATIAStiDBItem from its index in the
                |     CATIAStiDBChildren.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             This input corresponds to the Index of the CATIAStiDBItem to
                |             retrieve from the CATIAStiDBChildren. This index is the rank of the
                |             CATIAStiDBItem in the CATIAStiDBChildren -list of all the Children of a
                |             CATIAStiDBItem. The index of the first CATIAStiDBItem is '1' and the index of
                |             the last CATIAStiDBItem is 'Count'. 
                | 
                |     Returns:
                |         This ouptut corresponds to the retrieved CATIAStiDBItem from its index.
                |         
                |     Example:
                | 
                |           The following example returns in oChildStiDBItem the third
                |           CATIAStiDBItem
                |          gathered in oStiDBChildren.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim oFatherStiDBItem As StiDBItem
                |          Set oFatherStiDBItem = oStiEngine.GetStiDBItemFromCATBSTR("E:\\CATIAFiles\\Assembly.CATProduct")
                |          Dim oStiDBChildren As StiDBChildren
                |          Set oStiDBChildren = oFatherStiDBItem.GetChildren()
                |          (...)
                |          Dim oStiDBItem As StiDBItem
                |          Set oStiDBItem = oStiDBChildren.Item(3)

        :param cat_variant i_index:
        :rtype: StiDBItem
        """
        return StiDBItem(self.sti_db_children.Item(i_index))

    def link_type(self, i_index: cat_variant) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func LinkType(CATVariant iIndex) As CATBSTR
                | 
                |     Returns the Link Type from its index in the
                |     CATIAStiDBChildren.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             This input corresponds to the index of the Link Type to retrieve
                |             from the CATIAStiDBChildren. This index is the rank of the Link Type in the
                |             CATIAStiDBChildren. The index of the first Link Type is '1' and the index of
                |             the last Link Type is 'Count'. 
                | 
                |     Returns:
                |         This ouptut corresponds to the retrieved Link Type from its index.
                |         
                |     Example:
                | 
                |           The following example returns in oLinkType the third Link Type
                |           
                |          gathered in oStiDBChildren.
                |
                |          Dim oStiEngine As StiEngine
                |          Set oStiEngine = CATIA.GetItem("CAIEngine")
                |          Dim oFatherStiDBItem As StiDBItem
                |          Set oFatherStiDBItem = oStiEngine.GetStiDBItemFromCATBSTR("E:\\CATIAFiles\\Assembly.CATProduct")
                |          Dim oStiDBChildren As StiDBChildren
                |          Set oStiDBChildren = oFatherStiDBItem.GetChildren()
                |          (...)
                |          Dim oLinkType As CATBSTR
                |          oLinkType = oStiDBChildren.LinkType(3)

        :param cat_variant i_index:
        :rtype: str
        """
        return self.sti_db_children.LinkType(i_index)

    def __repr__(self):
        return f'StiDBChildren(name="{self.name}")'
