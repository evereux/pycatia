#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_object_factory import SchAppObjectFactory
from pycatia.cat_sch_platform_interfaces.sch_base_factory import SchBaseFactory
from pycatia.cat_sch_platform_interfaces.sch_component import SchComponent
from pycatia.cat_sch_platform_interfaces.sch_grr import SchGRR
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.cat_sch_platform_interfaces.sch_session import SchSession
from pycatia.cat_sch_platform_interfaces.sch_temp_list_factory import SchTempListFactory
from pycatia.drafting_interfaces.drawing_root import DrawingRoot
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class SchematicRoot(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchematicRoot
                | 
                | Represents the top node of the schematic object tree.
                | From this node all the queries for lists of schematic objects can be made.
                | Furthermore, all the factories handles can be obtained through this
                | interface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.schematic_root = com_object

    def get_appl_obj_fact_from_virtual_type(self, i_application_id: str) -> SchAppObjectFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetApplObjFactFromVirtualType(CATBSTR iApplicationID) As
                | SchAppObjectFactory
                | 
                |     Returns the object factory for specific schematic
                |     application.
                | 
                |     Example:
                | 
                |           This example illustrates how to get the object factory of user
                |           defined virtual type. 
                |          User provides implementation to this type.
                |          
                | 
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchObjFact As SchAppObjectFactory
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchObjFact = objSchPlatformRoot.GetApplObjFactFromVirtualType("UserDefined")(

        :param str i_application_id:
        :rtype: SchAppObjectFactory
        """
        return SchAppObjectFactory(self.schematic_root.GetApplObjFactFromVirtualType(i_application_id))

    def get_application_object_factory(self, i_application_id: int) -> SchAppObjectFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetApplicationObjectFactory(CatSchIDLApplicationID iApplicationID) As
                | SchAppObjectFactory
                | 
                |     Returns the object factory for specific schematic
                |     application.
                | 
                |     Example:
                | 
                |           This example illustrates how to get the object factory of Piping
                |          and Instrumentation Diagram application.
                |          
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchObjFact As SchAppObjectFactory
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchObjFact = objSchPlatformRoot.GetApplicationObjectFactory("CatSchIDLCATPID")(

        :param int i_application_id: enum cat_sch_idl_application_id
        :rtype: SchAppObjectFactory
        """
        return SchAppObjectFactory(self.schematic_root.GetApplicationObjectFactory(i_application_id))

    def get_comp_group_from_catalog(self, i_catalog_entry_name: str, i_ctlg_doc: Document) -> SchComponent:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCompGroupFromCatalog(CATBSTR iCatalogEntryName,
                | Document iCtlgDoc) As SchComponent
                | 
                |     Returns specific component group entry in a schematic component catalog
                |     document.
                | 
                |     Example:
                | 
                |           This example illustrates how to get a specific component group entry
                |           in a schematic component catalog document.
                |          
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchComponent As SchComponent
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Dim objCtlgDoc As Document
                |          Set objCtlgDoc = CATIA.Documents.Open ("Electrical_ANSI_PartFunctions.catalog")
                |          Set objSchComponent = objSchPlatformRoot.GetCompGroupFromCatalog ("JuncBox-TermBoard",objCtlgDoc)

        :param str i_catalog_entry_name:
        :param Document i_ctlg_doc:
        :rtype: SchComponent
        """
        return SchComponent(self.schematic_root.GetCompGroupFromCatalog(i_catalog_entry_name, i_ctlg_doc.com_object))

    def get_comp_symbol_from_catalog(self, i_catalog_entry_name: str, i_ctlg_doc: Document) -> SchGRR:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCompSymbolFromCatalog(CATBSTR iCatalogEntryName,
                | Document iCtlgDoc) As SchGRR
                | 
                |     Returns specific entry in a schematic component catalog
                |     document.
                | 
                |     Example:
                | 
                |           This example illustrates how to get a specific entry in a schematic
                |           component catalog document.
                |          
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchGRRComp As SchGRRComp
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Dim objCtlgDoc As Document
                |          Set objCtlgDoc = CATIA.Documents.Open ("PID_ANSI_Equipment.catalog")
                |          Set objSchGRRComp = objSchPlatformRoot.GetCompSymbolFromCatalog ("Blower",objCtlgDoc)

        :param str i_catalog_entry_name:
        :param Document i_ctlg_doc:
        :rtype: SchGRR
        """
        return SchGRR(self.schematic_root.GetCompSymbolFromCatalog(i_catalog_entry_name, i_ctlg_doc.com_object))

    def get_components(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetComponents() As SchListOfObjects
                | 
                |     Returns a list of schematic component instances under the
                |     root.
                | 
                |     Example:
                | 
                |           This example illustrates how to get the list of component instances
                |           from a schematic product document.
                |          
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchListComps As SchListOfObjects
                |          Set objoSchListComps = objSchPlatformRoot.GetComponents

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.schematic_root.GetComponents())

    def get_drawing(self) -> DrawingRoot:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDrawing() As DrawingRoot
                | 
                |     Retrieves the drawing root in the schematic document.
                | 
                |     Example:
                | 
                |           This example illustrates how to get the drawing of a schematic
                |           document.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Dim objDrawRoot As DrawingRoot
                |          Set objDrawRoot = objSchPlatformRoot.GetDrawing

        :rtype: DrawingRoot
        """
        return DrawingRoot(self.schematic_root.GetDrawing())

    def get_drawing_standard(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDrawingStandard() As CatDrawingStandard
                |
                |     Get the drawing standard.
                |
                |     Example:
                |
                |           This example illustrates how to get the drafting standard of a
                |           schematic document.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchLSymbols As SchListOfObjects
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          oDrwStd = objSchPlatformRoot.GetDrawingStandard

        :return: enum cat_drawing_standard
        :rtype: int
        """
        return self.schematic_root.GetDrawingStandard()

    def get_interface(self, i_interface_name: str, i_object: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInterface(CATBSTR iInterfaceName,
                | AnyObject iObject) As AnyObject
                |
                |     Returns specific interface handle on a given object.
                |
                |     Example:
                |
                |           This example illustrates how to get a specific interface handle from
                |           a given object.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchObjFact As SchAppObjectFactory
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchObjFact = SchPlatformRoot.GetApplicationObjectFactory("CatSchIDLCATPID")
                |          Set objSchObjFact2 = objSchPlatformRoot.GetInterface ("CATIASchAppObjectFactory2",SchObjFact)

        :param str i_interface_name:
        :param AnyObject i_object:
        :rtype: AnyObject
        """
        return AnyObject(self.schematic_root.GetInterface(i_interface_name, i_object.com_object))

    def get_ref_components(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRefComponents() As SchListOfObjects
                |
                |     Returns a list of schematic component references under the
                |     root.
                |
                |     Example:
                |
                |           This example illustrates how to get the list of component references
                |           from a schematic product document.
                |
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchListComps As SchListOfObjects
                |          Set objSchListComps = objSchPlatformRoot.GetRefComponents

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.schematic_root.GetRefComponents())

    def get_routes(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRoutes() As SchListOfObjects
                |
                |     Returns a list of schematic routes under the root.
                |
                |     Example:
                |
                |           This example illustrates how to get the list of routes from a
                |           schematic product document.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchListRoutes As SchListOfObjects
                |          Set objSchListRoutes = objSchPlatformRoot.GetRoutes

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.schematic_root.GetRoutes())

    def get_sch_base_factory(self) -> SchBaseFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSchBaseFactory() As SchBaseFactory
                |
                |     Returns schematic base object factory.
                |
                |     Example:
                |
                |           This example illustrates how to get the schematic base
                |           factory.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchBaseFact As SchBaseFactory
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchBaseFact = objSchPlatformRoot.GetBaseFactory

        :rtype: SchBaseFactory
        """
        return SchBaseFactory(self.schematic_root.GetSchBaseFactory())

    def get_schematic_session(self) -> SchSession:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSchematicSession() As SchSession
                |
                |     Returns the schematic session the document containing the root is
                |     associated with.
                |
                |     Example:
                |
                |           This example illustrates how to get the schematic
                |           session.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchSession As SchSession
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchSession = objSchPlatformRoot.GetSession

        :rtype: SchSession
        """
        return SchSession(self.schematic_root.GetSchematicSession())

    def get_temporary_list_factory(self) -> SchTempListFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTemporaryListFactory() As SchTempListFactory
                |
                |     Returns the factory to create lists of various types. These lists will not
                |     be saved with the model.
                |
                |     Example:
                |
                |           This example illustrates how to get the list factory from a schematic
                |           product document.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchList As SchTempListFactory
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchList = objSchPlatformRoot.GetTemporaryListFactory

        :rtype: SchTempListFactory
        """
        return SchTempListFactory(self.schematic_root.GetTemporaryListFactory())

    def get_unassociated_symbols(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUnassociatedSymbols() As SchListOfObjects
                |
                |     Returns a list of unassociated symbol.
                |
                |     Example:
                |
                |           This example illustrates how to get a list of unassociated
                |           symbol.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchLSymbols As SchListOfObjects
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          Set objSchLSymbols = objSchPlatformRoot.GetUnassociatedSymbols

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.schematic_root.GetUnassociatedSymbols())

    def set_drawing_standard(self, i_drw_std: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDrawingStandard(CatDrawingStandard iDrwStd)
                |
                |     Set the drawing standard.
                |
                |     Example:
                |
                |           This example illustrates how to set the drafting standard of a
                |           schematic document.
                |
                |          Dim objSchPlatformRoot As SchematicRoot
                |          Dim objSchLSymbols As SchListOfObjects
                |          Dim objProductRoot As Product
                |          Set objProductRoot = CATIA.ActiveDocument.Product
                |          Set objSchPlatformRoot = objProductRoot.GetTechnologicalObject ("SchematicRoot")
                |          objSchPlatformRoot.SetDrawingStandard catISO

        :param int i_drw_std: enum cat_drawing_standard
        :rtype: None
        """
        return self.schematic_root.SetDrawingStandard(i_drw_std)

    def __repr__(self):
        return f'SchematicRoot(name="{self.name}")'
