from pycatia.analysis_interfaces.analysis_document import AnalysisDocument
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.dmaps_interfaces.process_document import ProcessDocument
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument

document_type = {
    # "CATImmNavDoc": Document,
    "CATAnalysis": AnalysisDocument,
    "CATPart": PartDocument,
    "CATProduct": ProductDocument,
    "CATDrawing": DrawingDocument,
    "CATMaterial": MaterialDocument,
    "CATSystem": FunctionalDocument,
    "CATProcess": ProcessDocument,
    "cgm": Document,
    "FeatureDictionary": Document,
    "gl": Document,
    "gl2": Document,
    "hpgl": Document,
    "ProcessLibrary": Document,
}
