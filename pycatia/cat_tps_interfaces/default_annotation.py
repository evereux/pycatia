#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DefaultAnnotation(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DefaultAnnotation
                | 
                | This interface is used to get information about default
                | annotation.
                | Ther is two kinds of default annotation : - with a manual selection - with a selection automatic
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.default_annotation = com_object

    @property
    def link_wi_geom_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LinkWiGeomType() As CATBSTR (Read Only)
                | 
                |     Get the type of link between the default annotation and the geometry.
                |     Return E_FAIL if the annotation is not a default one.
                | 
                |     Parameters:
                | 
                |         oLinkWiGeom
                |             Type of link.

        :rtype: str
        """

        return self.default_annotation.LinkWiGeomType

    @property
    def search_algo_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SearchAlgoType() As CATBSTR (Read Only)
                | 
                |     Get the type of search algo to find geometry on which the annotation apply
                |     to. Return E_FAIL if the annotation is not a default one.
                | 
                |     Parameters:
                | 
                |         oAlgo
                |             Type of algo.

        :rtype: str
        """

        return self.default_annotation.SearchAlgoType

    def is_in_automatic_search_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsInAutomaticSearchMode() As boolean
                | 
                |     Get the type of search algo Return E_FAIL if the annotation is not a
                |     default one.
                | 
                |     Parameters:
                | 
                |         oIsAutoMode
                |             oIsAutoMode = TRUE if Automatic mode

        :rtype: bool
        """
        return self.default_annotation.IsInAutomaticSearchMode()

    def __repr__(self):
        return f'DefaultAnnotation(name="{ self.name }")'
