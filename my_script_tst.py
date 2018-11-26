#! /usr/bin/python3.6

from catia_python import create_reference
from catia_python import get_document_part_object


document, part = get_document_part_object()
annotation_sets = part.get_annotation_sets()
density = part.density
geomtric_elements = part.get_geometric_elements()
print(part.part.HybridShapeFactory)

for i in range(0, geomtric_elements.Count):

    reference_object = create_reference(part.part, geomtric_elements.Item(i+1))
    print(geomtric_elements.Item(i+1).name)
    print(part.part.HybridShapeFactory.GetGeometricalFeatureType(reference_object))



