#! /usr/bin/python3.6
"""
    Enumerated Types Index

    The key values in this module are taken straight from the V5Automation handbook and are therefor not pythonic.
    Don't PEP 8 me.

    When used the pycatia method will expect the key value.

"""

cat_file_types = {
    "catFileTypeText": 0,
    "catFileTypeMotif": 1,
    "catFileTypeHTML": 2,
}

cat_product_source = {
    "catProductSourceUnknown": 0,
    "catProductMade": 0,
    "catProductBought": 0,
}

cat_work_mode_types = {
    "DEFAULT_MODE": 0,
    "VISUALIZATION_MODE": 1,
    "DESIGN_MODE": 2,
}

cat_rep_types = {
    "catRep3D": 0,
    "catRep2D": 1,
    "catRepText": 2,
}
