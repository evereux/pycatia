#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.functional_facet_mgr import FunctionalFacetMgr
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class FunctFacetManagers(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FunctFacetManagers
                | 
                | Represents the Functional Facet's Managers.
    
    """

    def __init__(self, com_object, child_object=FunctionalFacetMgr):
        super().__init__(com_object, child_object=FunctionalFacetMgr)
        self.funct_facet_managers = com_object
        self.child_object = FunctionalFacetMgr

    def elem(self, i_index: cat_variant) -> FunctionalFacetMgr:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Elem(CATVariant iIndex) As FunctionalFacetMgr
                | 
                |     Returns a facet manager using its index or its name from the facet managers
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the facet manager to retrieve from the
                |             collection of facet managers. As a numerics, this index is the rank of the
                |             facet manager in the collection. The index of the first facet manager in the
                |             collection is 1, and the index of the last facet manager is Count. As a string,
                |             it is the name you assigned to the facet manager using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved action 
                |     Example:
                |         This example retrieves in Obj1 the fifth facet manager in the
                |         collection and in Obj2 the facet manager named IMC.
                | 
                |          Dim Obj1 As FunctFacetManager
                |          Set Obj1 = Desc.FacetManagers.Elem(5)
                |          Dim Obj2 As FunctFacetManager
                |          Set Obj2 = Desc.FacetManagers.Elem("IMC")

        :param cat_variant i_index:
        :rtype: FunctionalFacetMgr
        """
        return FunctionalFacetMgr(self.funct_facet_managers.Elem(i_index))

    def __repr__(self):
        return f'FunctFacetManagers(name="{self.name}")'
