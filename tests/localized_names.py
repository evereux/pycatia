#! /usr/bin/python3.9

FIRST_LENGTH_PARAMETER_NAMES = [
    r"cat_part_measurable\PartBody\Pad.1\FirstLimit\Length",
    r"cat_part_measurable\Hauptkörper\Block.1\Begrenzung1\Länge",
    r"cat_part_measurable\零件几何体\凸台.1\第一限制\长度",
]

PART_BODY_NAMES = [
    "PartBody",
    "Hauptkörper",
    "零件几何体",
]

PAD_NAMES = [
    "Pad.1",
    "Block.1",
    "凸台.1",
]

SHEET_1_NAMES = [
    "Sheet.1",
    "Blatt.1",
    "图纸.1",
]

SHEET_2_NAMES = [
    "Sheet.2",
    "Blatt.2",
    "图纸.2",
]

PARAMETER_SET_1_REPRS = [
    'ParameterSet(name="Parameters.1")',
    'ParameterSet(name="Parameter.1")',
    'ParameterSet(name="参数.1")',
]


def get_item_by_localized_name(collection, names):
    for name in names:
        item = collection.get_item_by_name(name)
        if item is not None:
            return item

    return None
