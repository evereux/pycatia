#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.funct_system_interfaces.funct_actions_groups import FunctActionsGroups
from pycatia.funct_system_interfaces.functional_actions import FunctionalActions
from pycatia.funct_system_interfaces.functional_element import FunctionalElement
from pycatia.funct_system_interfaces.functional_facet import FunctionalFacet
from pycatia.funct_system_interfaces.functional_facet_mgr import FunctionalFacetMgr
from pycatia.funct_system_interfaces.functional_objects import FunctionalObjects
from pycatia.funct_system_interfaces.functional_position import FunctionalPosition

if TYPE_CHECKING:
    from pycatia.funct_system_interfaces.functional_variants import FunctionalVariants


class FunctionalDescription(FunctionalElement):
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
                |                         FunctionalDescription
                | 
                | The interface to access a Functional Description.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_description = com_object

    @property
    def actions(self) -> FunctionalActions:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Actions() As FunctionalActions (Read Only)
                | 
                |     Get the Actions collection.

        :rtype: FunctionalActions
        """

        return FunctionalActions(self.functional_description.Actions)

    @property
    def actions_groups(self) -> FunctActionsGroups:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActionsGroups() As FunctActionsGroups (Read Only)
                | 
                |     Get the ActionsGroups collection.

        :rtype: FunctActionsGroups
        """

        return FunctActionsGroups(self.functional_description.ActionsGroups)

    @property
    def objects(self) -> FunctionalObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Objects() As FunctionalObjects (Read Only)
                | 
                |     Get the Objects collection.

        :rtype: FunctionalObjects
        """

        return FunctionalObjects(self.functional_description.Objects)

    @property
    def variants(self) -> 'FunctionalVariants':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Variants() As FunctionalVariants (Read Only)
                | 
                |     Get the Variants collection.
                | 
                |     (gives a NULL pointer if the description is a itself variant)

        :rtype: FunctionalVariants
        """

        return FunctionalVariants(self.functional_description.Variants)

    def create_position(self, i_x: float, i_y: float) -> FunctionalPosition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreatePosition(double iX,
                | double iY) As FunctionalPosition
                | 
                |     Create a Position.
                | 
                |     To create actions pointing to NULL

        :param float i_x:
        :param float i_y:
        :rtype: FunctionalPosition
        """
        return FunctionalPosition(self.functional_description.CreatePosition(i_x, i_y))

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
        return FunctionalFacet(self.functional_description.GetFacet(i_fm.com_object))

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
        return FunctionalFacet(self.functional_description.GetFacetByName(i_fm))

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
        return FunctionalFacet(self.functional_description.SearchFacet(i_fm.com_object, i_create_if_necessary))

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
        return FunctionalFacet(self.functional_description.SearchFacetByName(i_fm, i_create_if_necessary))

    def unlock(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Unlock()
                | 
                |     Unlock.
                | 
                |     To remove the protection against modifications.

        :rtype: None
        """
        return self.functional_description.Unlock()

    def __repr__(self):
        return f'FunctionalDescription(name="{self.name}")'
