#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_engine_v6_r2014x import CD5EngineV6R2014x
from pycatia.eno_cd5_interfaces.cd5_id import CD5ID
from pycatia.eno_cd5_interfaces.cd5_ids import CD5IDs
from pycatia.eno_cd5_interfaces.cd5_properties import CD5Properties
from pycatia.eno_cd5_interfaces.cd5_template import CD5Template
from pycatia.eno_cd5_interfaces.cd5_template_types import CD5TemplateTypes
from pycatia.in_interfaces.document import Document


class CD5EngineV6R2015(CD5EngineV6R2014x):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ENOCD5Interfaces.CD5Engine
                |                         ENOCD5Interfaces.CD5EngineV6R2014x
                |                             CD5EngineV6R2015
                | 
                | Represents the ENOVIA V6 Integration Engine, that is to say the entry point to
                | the CATIA/ENOVIA V6 Integration.
                | 
                | It allows end user to realize the various operations like ENOVIA
                | New
                | Note that all operations performed from this interface are the same as
                | operations available in the ENOVIA V6 menu in CATIA, unless most of them are
                | executed without panel.
                | 
                | Example:
                | 
                |       The following example indicates how to retrieve the ENOVIA V6 Integration
                |       Engine.
                |      
                | 
                |      Dim oCD5Engine As CD5EngineV6R2015
                |      Set oCD5Engine = CATIA.GetItem("CD5EngineV6R2015")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_engine_v6_r2015 = com_object

    @property
    def template_types(self) -> CD5TemplateTypes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TemplateTypes() As CD5TemplateTypes (Read Only)
                | 
                |     Returns (gets) the list of all "Template Types".
                | 
                |     Example:
                | 
                |           The following example gets the list of Template Types. 
                |
                |          Dim oTemplateTypes As ENOIACD5TemplateTypes
                |          Set oTemplateTypes = oCD5Engine.TemplateTypes

        :rtype: CD5TemplateTypes
        """

        return CD5TemplateTypes(self.cd5_engine_v6_r2015.TemplateTypes)

    def get_id_from_physical_id(self, i_physical_id: str) -> CD5ID:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIDFromPhysicalID(CATBSTR iPhysicalID) As CD5ID
                | 
                |     Returns CD5ID of the object for the given PhysicalID.
                | 
                |     Parameters:
                | 
                |         iPhysicalID
                |             Physical ID of the object 
                | 
                |     Returns:
                |         The created CD5ID of the object 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                | 
                |     Example:
                | 
                |           The following example returns the ENOIACD5ID of the
                |           object:
                |
                |          iPhysicalID : "6EFB8D2E00008A445257E36100000DF7".
                |
                |          Dim ID As CD5ID
                |          Set ID = oCD5Engine.GetIDFromPhysicalID("6EFB8D2E00008A445257E36100000DF7")

        :param str i_physical_id:
        :rtype: CD5ID
        """
        return CD5ID(self.cd5_engine_v6_r2015.GetIDFromPhysicalID(i_physical_id))

    def get_i_ds_from_physical_i_ds(self, i_physical_i_ds: tuple) -> CD5IDs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIDsFromPhysicalIDs(CATSafeArrayVariant iPhysicalIDs) As
                | CD5IDs
                | 
                |     Returns CD5IDs of the objects for the given PhysicalIDs.
                | 
                |     Parameters:
                | 
                |         iPhysicalIDs
                |             Physical IDs of the objects 
                | 
                |     Returns:
                |         The created CD5ID array of the objects 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                | 
                |     Example:
                | 
                |           The following example returns the ENOIACD5IDs of the
                |           object:
                |
                |             iPhysicalIDs : "6EFB8D2E00008A445257E36100000DF7,6EFB8D2E00008A445257E3610000090".
                |
                |          Dim IDs As CD5IDs
                |          Set IDs = oCD5Engine.GetIDsFromPhysicalIDs(iPhysicalIDs)

        :param tuple i_physical_i_ds:
        :rtype: CD5IDs
        """
        return CD5IDs(self.cd5_engine_v6_r2015.GetIDsFromPhysicalIDs(i_physical_i_ds))

    def get_properties(self, i_enoiacd5_id: CD5ID) -> CD5Properties:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProperties(CD5ID iENOIACD5ID) As CD5Properties
                | 
                |     Returns a collection of all the ENOVIA V6 properties for a given Object
                |     defined by Type, Name, Revision & Version.
                | 
                |     Parameters:
                | 
                |         iENOIACD5ID
                |             The ENOIACD5ID object id representing ENOVIA V6 Object which is to
                |             be explored. 
                | 
                |     Returns:
                |         The collection of properties of the ENOVIA object passes as iENOIACD5ID
                |         
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |         -1691273589 : Invalid object type
                |         -1857112104 : Name or Type Empty
                | 
                |     Example:
                | 
                |           The following example retrieves all the ENOVIA V6 properties from a
                |           given ENOIACD5ID.
                |
                |          Dim ObjID As CD5ID
                |          Set ObjID = oCD5Engine.GetIDFromTNRV("Versioned CATPart", "Part_Name", "A", "0")
                |          Dim oCD5Properties As CD5Properties
                |          Set oCD5Properties = oCD5Engine.GetProperties(ObjID)

        :param CD5ID i_enoiacd5_id:
        :rtype: CD5Properties
        """
        return CD5Properties(self.cd5_engine_v6_r2015.GetProperties(i_enoiacd5_id.com_object))

    def get_properties_of_document(self, i_catia_document: Document) -> CD5Properties:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPropertiesOfDocument(Document iCATIADocument) As
                | CD5Properties
                | 
                |     Returns a collection of all the ENOVIA V6 properties for a given ENOVIA
                |     object.
                | 
                |     Parameters:
                | 
                |         iCATIADocument
                |             The document representing ENOVIA V6 Object which is to be explored.
                |
                |     Returns:
                |         The collection of properties of the ENOVIA object passes as
                |         iCATIADocument 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                | 
                |     Example:
                | 
                |           The following example retrieves all the ENOVIA V6 properties for a
                |           given ENOVIA object.
                |
                |          Dim docCD5ID As CD5ID
                |          Set docCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "MyProduct", "---")
                |          Dim objDocument As Document
                |          Set objDocument = oCD5Engine.Open(docCD5ID)
                |          Dim oCD5Properties As CD5Properties
                |          Set oCD5Properties = oCD5Engine.GetPropertiesOfDocument(objDocument)

        :param Document i_catia_document:
        :rtype: CD5Properties
        """
        return CD5Properties(self.cd5_engine_v6_r2015.GetPropertiesOfDocument(i_catia_document.com_object))

    def get_properties_of_embedded_component(
            self,
            i_catia_document: Document,
            i_embedded_component_name: str
    ) -> CD5Properties:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPropertiesOfEmbeddedComponent(Document
                | iCATIADocument,
                | CATBSTR iEmbeddedComponentName) As CD5Properties
                | 
                |     Returns a collection of all the ENOVIA V6 properties for a given Embedded
                |     Component.
                | 
                |     Parameters:
                | 
                |         iCATIADocument
                |             The document representing ENOVIA V6 Object in which the target
                |             embedded component resides. 
                |         iEmbeddedComponentName
                |             Name of the embedded component to be explored. 
                | 
                |     Returns:
                |         The collection of properties of the embedded component passed as input
                |         
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                | 
                |     Example:
                | 
                |           The following example retrieves all the ENOVIA V6 properties for a
                |           given Embedded Component.
                |
                |          Dim docCD5ID As CD5ID
                |          Set docCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "MyProduct", "---")
                |          Dim objDocument As Document
                |          Set objDocument = oCD5Engine.Open(docCD5ID)
                |          Dim oCD5Properties As CD5Properties
                |          Set oCD5Properties = oCD5Engine.GetPropertiesOfEmbeddedComponent(objDocument,
                |                                                                           "Embedded_Component_Name")

        :param Document i_catia_document:
        :param str i_embedded_component_name:
        :rtype: CD5Properties
        """
        return CD5Properties(
            self.cd5_engine_v6_r2015.GetPropertiesOfEmbeddedComponent(
                i_catia_document.com_object,
                i_embedded_component_name
            )
        )

    def new_from(self, i_cd5_template: CD5Template, i_name: str, i_type: str) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NewFrom(CD5Template iCD5Template,
                | CATBSTR iName,
                | CATBSTR iType) As Document
                | 
                |     Creates a new object from given template.
                | 
                |     Parameters:
                | 
                |         iCD5Template
                |             The Template object from which we want to create a new object.
                |             
                |         iName
                |             The name for the new object. 
                |         iType
                |             The ENOVIA type for the new object. 
                | 
                |     Returns:
                |         The created Document. 
                |     Throws:
                | 
                |         -1697450280 : CATIA is not connected to ENOVIA V6.
                |         -1782306828 : Template object is assigned more than one file.
                |         -1774688310 : Template object is not assigned any file.
                |         -1866082326 : File of same name as that of file attached to Template object is present on checkout directory.
                |         -1739257732 : The name for the new object contains unsupported characters.
                |         -1706631745 : An object with the same name as that of new object is already present in ENOVIA.
                |         -1844336441 : File of same name as that of new object is already present on checkout directory.
                | 
                |     Example:
                | 
                |           The following example creates a new object to be loaded in the CATIA
                |           session:
                |
                |             iCD5Template : template.
                |
                |             iName : "NewPart".
                |
                |          Dim types As Array
                |          types = oTemplateType.PossibleTypes
                |          Dim document As CATIADocument
                |          Set document = oCD5Engine.NewFrom(template, "NewPart", types(0))

        :param CD5Template i_cd5_template:
        :param str i_name:
        :param str i_type:
        :rtype: Document
        """
        return Document(self.cd5_engine_v6_r2015.NewFrom(i_cd5_template.com_object, i_name, i_type))

    def __repr__(self):
        return f'CD5EngineV6R2015(name="{self.name}")'
