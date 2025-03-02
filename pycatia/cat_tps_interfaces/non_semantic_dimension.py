#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.drafting_interfaces.drawing_dimension import DrawingDimension
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.dimension_limit import DimensionLimit


class NonSemanticDimension(AnyObject):
    """

    Introduced in V5-6R2017.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NonSemanticDimension
                | 
                | Interface Managing Non Semantic Dimension.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_dimension = com_object

    def dimension_limit(self) -> DimensionLimit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DimensionLimit() As DimensionLimit
                | 
                |     Gets the Dimension on the DimensionLimit interface.
                | 
                |     Parameters:
                | 
                |         oDimLim
                |             The Dimension Limits.

        :rtype: DimensionLimit
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return DimensionLimit(self.non_semantic_dimension.DimensionLimit())

    def get_2d_annot(self) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Get2dAnnot() As DrawingDimension
                | 
                |     Retrieves Drafting Dimension.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The Drafting Dimension.

        :rtype: DrawingDimension
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return DrawingDimension(self.non_semantic_dimension.Get2dAnnot())

    def has_dimension_limit(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasDimensionLimit() As boolean
                | 
                |     Checks if the Dimension has a Dimension Limit.
                | 
                |     Parameters:
                | 
                |         oHasDimLim
                | 
                |                 TRUE: Dimension Limit exists
                |                 FALSE: Dimension Limit does not exist

        :rtype: bool
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return self.non_semantic_dimension.HasDimensionLimit()

    def __repr__(self):
        return f'NonSemanticDimension(name="{self.name}")'
