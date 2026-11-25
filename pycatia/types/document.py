from typing import Union

from pycatia.analysis_interfaces.analysis_document import AnalysisDocument
from pycatia.components_catalogs_interfaces.catalog_document import CatalogDocument
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.dmaps_interfaces.process_document import ProcessDocument
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument

AnyDocument = Union[
    AnalysisDocument,
    MaterialDocument,
    ProcessDocument,
    Document,
    DrawingDocument,
    FunctionalDocument,
    PartDocument,
    ProductDocument,
    ProcessDocument,
]

document_types = {
    'AnalysisDocument': AnalysisDocument,
    'CatalogDocument': CatalogDocument,
    'DrawingDocument': DrawingDocument,
    'FunctionalDocument': FunctionalDocument,
    'MaterialDocument': MaterialDocument,
    'PartDocument': PartDocument,
    'ProcessDocument': ProcessDocument,
    'ProductDocument': ProductDocument,
    'Document': Document,
}
