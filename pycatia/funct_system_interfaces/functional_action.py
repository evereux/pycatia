#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.funct_system_interfaces.functional_element import FunctionalElement
from pycatia.funct_system_interfaces.functional_facet import FunctionalFacet
from pycatia.funct_system_interfaces.functional_facet_mgr import FunctionalFacetMgr
from pycatia.funct_system_interfaces.functional_position import FunctionalPosition

if TYPE_CHECKING:
    from pycatia.funct_system_interfaces.funct_actions_group import FunctActionsGroup


class FunctionalAction(FunctionalElement):
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
                |                         FunctionalAction
                | 
                | The interface to access a Functional Action.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_action = com_object

    @property
    def from_(self) -> FunctionalPosition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property From() As FunctionalPosition
                | 
                |     Get the From object.

        :rtype: FunctionalPosition
        """

        return FunctionalPosition(self.functional_action.From)

    @from_.setter
    def from_(self, value: FunctionalPosition):
        """
        :param FunctionalPosition value:
        """

        self.functional_action.From = value

    @property
    def group(self) -> 'FunctActionsGroup':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Group() As FunctActionsGroup (Read Only)
                | 
                |     Get the Group property.
                | 
                |     Vary when adding/removing the action to/from a group.

        :rtype: FunctActionsGroup
        """

        return FunctActionsGroup(self.functional_action.Group)

    @property
    def orientation_direction(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OrientationDirection() As
                | CATFunctOrientationDirection
                | 
                |     Get the OrientationDirection property.
                | 
                |     See also:
                |         CATFunctOrientationDirection

        :return: enum cat_funct_orientation_direction
        :rtype: int
        """

        return self.functional_action.OrientationDirection

    @orientation_direction.setter
    def orientation_direction(self, value: int):
        """
        :param int value: enum cat_funct_orientation_direction
        """

        self.functional_action.OrientationDirection = value

    @property
    def to(self) -> FunctionalPosition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property To() As FunctionalPosition
                | 
                |     Get the To object.

        :rtype: FunctionalPosition
        """

        return FunctionalPosition(self.functional_action.To)

    @to.setter
    def to(self, value: FunctionalPosition):
        """
        :param FunctionalPosition value:
        """

        self.functional_action.To = value

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
        return FunctionalFacet(self.functional_action.GetFacet(i_fm.com_object))

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
        return FunctionalFacet(self.functional_action.GetFacetByName(i_fm))

    def invert_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InvertDirection()
                | 
                |     Invert the action's Direction.
                | 
                |     Fails if the action is included in a group.

        :rtype: None
        """
        return self.functional_action.InvertDirection()

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
        return FunctionalFacet(self.functional_action.SearchFacet(i_fm.com_object, i_create_if_necessary))

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
        return FunctionalFacet(self.functional_action.SearchFacetByName(i_fm, i_create_if_necessary))

    def __repr__(self):
        return f'FunctionalAction(name="{self.name}")'
