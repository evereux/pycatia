from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument

document_type = {
    "CATPart": PartDocument,
    "CATProduct": ProductDocument,
    "CATDrawing": DrawingDocument,
    "CATMaterial": MaterialDocument,
    "CATSystem": FunctionalDocument
}
