from pycatia import CATIADocHandler
from pycatia import Product

cat_product = r'tests/CF_TopLevelAssy.CATProduct'

with CATIADocHandler(cat_product) as handler:
    catia = handler.catia
    product = handler.document.product()

    product.apply_work_mode("DESIGN_MODE")

    Product.activate_terminal_node(product.get_products())

    assert 0 == product.analyze.mass
    assert 0 == product.analyze.volume
    assert 0 == product.analyze.wet_area
    assert (0.0, 0.0, 0.0) == product.analyze.get_gravity_center(catia)
    assert (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) == product.analyze.get_inertia(catia)
