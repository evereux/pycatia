from pycatia.mec_mod_interfaces.hybrid_bodies import HybridBodies
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody


def create_geometrical_set(parent: HybridBodies, name: str) -> HybridBody:
    """
    Creates a new HybridBody (Geometrical Set) adding it to the parents
    HybridBodies collection.

    :param parent:
    :param name:
    :return: -> HybridBody
    """

    geometrical_set = parent.add()
    geometrical_set.name = name

    return geometrical_set
