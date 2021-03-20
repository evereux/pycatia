from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument

document_type = {
    'CATPart': PartDocument,
    'CATProduct': ProductDocument,
    'CATDrawing': DrawingDocument,
}
