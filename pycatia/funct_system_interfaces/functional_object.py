#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.functional_facet import FunctionalFacet
from pycatia.funct_system_interfaces.functional_facet_mgr import FunctionalFacetMgr
from pycatia.funct_system_interfaces.functional_position import FunctionalPosition


class FunctionalObject(FunctionalPosition):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATFunctSystemItf.FunctionalElement
                |                         CATFunctSystemItf.FunctionalPosition
                |                             FunctionalObject
                | 
                | The interface to access a Functional Object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_object = com_object

    def get_facet(self, i_fm: FunctionalFacetMgr) -> FunctionalFacet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFacet(FunctionalFacetMgr iFM) As FunctionalFacet
                | 
                |     Returns the Facet.

        :param FunctionalFacetMgr i_fm:
        :rtype: FunctionalFacet
        """
        return FunctionalFacet(self.functional_object.GetFacet(i_fm.com_object))

    def get_facet_by_name(self, i_fm: str) -> FunctionalFacet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFacetByName(CATBSTR iFM) As FunctionalFacet
                | 
                |     Returns the Facet.

        :param str i_fm:
        :rtype: FunctionalFacet
        """
        return FunctionalFacet(self.functional_object.GetFacetByName(i_fm))

    def search_facet(self, i_fm: FunctionalFacetMgr, i_create_if_necessary: bool) -> FunctionalFacet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SearchFacet(FunctionalFacetMgr iFM,
                | boolean iCreateIfNecessary) As FunctionalFacet
                | 
                |     Searches the Facet.

        :param FunctionalFacetMgr i_fm:
        :param bool i_create_if_necessary:
        :rtype: FunctionalFacet
        """
        return FunctionalFacet(self.functional_object.SearchFacet(i_fm.com_object, i_create_if_necessary))

    def search_facet_by_name(self, i_fm: str, i_create_if_necessary: bool) -> FunctionalFacet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SearchFacetByName(CATBSTR iFM,
                | boolean iCreateIfNecessary) As FunctionalFacet
                | 
                |     Searches the Facet.

        :param str i_fm:
        :param bool i_create_if_necessary:
        :rtype: FunctionalFacet
        """
        return FunctionalFacet(self.functional_object.SearchFacetByName(i_fm, i_create_if_necessary))

    def __repr__(self):
        return f'FunctionalObject(name="{self.name}")'
