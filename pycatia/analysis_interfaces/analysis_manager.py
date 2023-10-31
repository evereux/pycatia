#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_linked_documents import AnalysisLinkedDocuments
from pycatia.analysis_interfaces.analysis_models import AnalysisModels
from pycatia.analysis_interfaces.analysis_sets import AnalysisSets
from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.relations import Relations
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class AnalysisManager(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisManager
                | 
                | Represents the root object inside an analysis document.
                | It aggregates all the objects making up an analysis document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_manager = com_object

    @property
    def analysis_models(self) -> AnalysisModels:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisModels() As AnalysisModels (Read Only)
                | 
                |     Returns the analysis model collection from the current analysis
                |     manager.
                | 
                |     Example:
                |         The following example returns from RootAnalysis the root analysis
                |         object of the active document, assumed to be an Analysis document, the
                |         collection of analysis models.
                | 
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          Dim analysisModels As AnalysisModels
                |          Set analysisModels = RootAnalysis.AnalysisModels

        :rtype: AnalysisModels
        """

        return AnalysisModels(self.analysis_manager.AnalysisModels)

    @property
    def analysis_sets(self) -> AnalysisSets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisSets() As AnalysisSets (Read Only)
                | 
                |     Returns the analysis sets collection associated with an analysis manager.
                |     This collection allows to access the Analysis Connection Manager that
                |     aggregates the Analysis Connection features.
                | 
                |     Returns:
                |         a collection of CATIAAnalysisSets.

        :rtype: AnalysisSets
        """

        return AnalysisSets(self.analysis_manager.AnalysisSets)

    @property
    def linked_documents(self) -> AnalysisLinkedDocuments:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LinkedDocuments() As AnalysisLinkedDocuments (Read
                | Only)
                | 
                |     Returns the collection containing the documents linked to analysis
                |     document. All the CATIA documents that are linked to the different objects
                |     (like AnalysisMeshPart of Analysis Entity) might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in documents the linked documents of the
                |         AnalysisDocument :
                | 
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          Dim Documents As AnalysisLinkedDocuments
                |          Set Documents = RootAnalysis.LinkedDocuments

        :rtype: AnalysisLinkedDocuments
        """

        return AnalysisLinkedDocuments(self.analysis_manager.LinkedDocuments)

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Parameters() As Parameters (Read Only)
                | 
                |     Returns the collection object containing the analysis parameters. All the
                |     parameters that are defined in analysis objects might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in params the parameters of the
                |         RootAnalysis from the AnalysisDocument document:
                | 
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          Dim params As CATIAParameters
                |          Set params = RootAnalysis.Parameters

        :rtype: Parameters
        """

        return Parameters(self.analysis_manager.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Relations() As Relations (Read Only)
                | 
                |     Returns the collection object containing the analysis relations. All the
                |     relations that are defined in analysis objects might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in relation the relations of the
                |         RootAnalysis from the AnalysisDocument document:
                | 
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          Dim relation As CATIARelations
                |          Set relation = RootAnalysis.Relations

        :rtype: Relations
        """

        return Relations(self.analysis_manager.Relations)

    def create_reference_from_geometry(self, i_product: Product, i_geometry: Reference) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateReferenceFromGeometry(Product iProduct,
                | Reference iGeometry) As Reference
                | 
                |     Creates a reference from a geometry. This geometry must in defined in a
                |     document rerecened in the CATIAAnalysisLinkedDocuments
                |     collection.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product of the geometry to be referenced that defines the
                |             instance of the geometry. 
                |         iGeometry
                |             The geometry to be referenced. As a reference, it can be an
                |             CATIABoundary object of a mechanical feature. 
                | 
                |     Returns:
                |         a reference of the couple (iProduct, iGeometry).

        :param Product i_product:
        :param Reference i_geometry:
        :rtype: Reference
        """
        return Reference(self.analysis_manager.CreateReferenceFromGeometry(i_product.com_object, i_geometry.com_object))

    def create_reference_from_object(self, i_object: AnyObject) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateReferenceFromObject(AnyObject iObject) As
                | Reference
                | 
                |     Creates a reference from an analysis object. Use of reference allows a
                |     uniform handling of anay objects.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The analysis object to be referenced. It can be an AnalysisEntity
                |             or an AnalysisSet 
                | 
                |     Returns:
                |         The reference to the object.

        :param AnyObject i_object:
        :rtype: Reference
        """
        return Reference(self.analysis_manager.CreateReferenceFromObject(i_object.com_object))

    def import_(self, i_document_to_import: Document) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Import(Document iDocumentToImport)
                | 
                |     Import an existing document in an analysis document . This document can of
                |     any type that implement the CATIADocument interface. This is implemented for
                |     internal document formats. (like Part or Product
                |     documents).
                | 
                |     Example:
                |         The following example imports an opened CATPart
                |         document
                | 
                |          Dim AnalysisDocument As Document
                |          Dim PartDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          RootAnalysis.Import(PartDocument)

        :param Document i_document_to_import:
        :rtype: None
        """
        return self.analysis_manager.Import(i_document_to_import.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'import'
        # # vba_code = """
        # # Public Function import(analysis_manager)
        # #     Dim iDocumentToImport (2)
        # #     analysis_manager.Import iDocumentToImport
        # #     import = iDocumentToImport
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_define_file(self, i_document_path: str, i_type_late: str, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportDefineFile(CATBSTR iDocumentPath,
                | CATBSTR iTypeLate,
                | CATSafeArrayVariant iValues)
                | 
                |     Import an existing document in an analysis document. This document can of
                |     any type that is managed by the CATISamImportDefine
                |     interface.
                | 
                |     Example:
                |         The following example imports an CATPart document stored as FileToOpen
                |         file. This example is also use the CATAnalysisImport Object. This object allow
                |         to import Part, Product or Analysis documents. As of today no parameters are
                |         mandatory for this object.
                | 
                |          Dim arrayOfVariant(0)
                |          FileToOpen = "e:/users/Parts/ThisIsANicePart.CATPart"
                |          ObjectForImport = "CATAnalysisImport"
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          RootAnalysis.ImportDefineFile(FileToOpen,CATAnalysisImport,arrayOfVariant)

        :param str i_document_path:
        :param str i_type_late:
        :param tuple i_values:
        :rtype: None
        """
        return self.analysis_manager.ImportDefineFile(i_document_path, i_type_late, i_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'import_define_file'
        # # vba_code = """
        # # Public Function import_define_file(analysis_manager)
        # #     Dim iDocumentPath (2)
        # #     analysis_manager.ImportDefineFile iDocumentPath
        # #     import_define_file = iDocumentPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_file(self, i_document_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportFile(CATBSTR iDocumentPath)
                | 
                |     Import an existing document in an analysis document.
                | 
                |     Deprecated:
                |         V5R15 use ImportDefineFile instead. This document can of any type that
                |         implement the CATISamImportDefine interface.
                | 
                |         Example:
                |             The following example imports an CATPart document stored as
                |             FileToOpen file.
                | 
                |              FileToOpen = "e:/users/Parts/ThisIsANicePart.CATPart"
                |              Dim AnalysisDocument As Document
                |              Set AnalysisDocument = CATIA.ActiveDocument
                |              Dim RootAnalysis As AnalysisManager
                |              Set RootAnalysis = AnalysisDocument.Analysis
                |              RootAnalysis.ImportFile(FileToOpen)

        :param str i_document_path:
        :rtype: None
        """
        return self.analysis_manager.ImportFile(i_document_path)

    def __repr__(self):
        return f'AnalysisManager(name="{self.name}")'
