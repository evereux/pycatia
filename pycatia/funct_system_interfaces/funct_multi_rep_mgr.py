#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.funct_associations import FunctAssociations
from pycatia.funct_system_interfaces.functional_facet import FunctionalFacet


class FunctMultiRepMgr(FunctionalFacet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATFunctSystemItf.FunctionalFacet
                |                         FunctMultiRepMgr
                | 
                | The interface to access a Functional Multi-Rep manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.funct_multi_rep_mgr = com_object

    @property
    def associations(self) -> FunctAssociations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Associations() As FunctAssociations (Read Only)
                | 
                |     Get the Associations collection.

        :rtype: FunctAssociations
        """

        return FunctAssociations(self.funct_multi_rep_mgr.Associations)

    @property
    def current_assoc(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CurrentAssoc() As long
                | 
                |     Get the CurrentAssoc.

        :rtype: int
        """

        return self.funct_multi_rep_mgr.CurrentAssoc

    @current_assoc.setter
    def current_assoc(self, value: int):
        """
        :param int value:
        """

        self.funct_multi_rep_mgr.CurrentAssoc = value

    def __repr__(self):
        return f'FunctMultiRepMgr(name="{self.name}")'
