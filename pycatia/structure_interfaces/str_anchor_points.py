#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.structure_interfaces.str_anchor_point import StrAnchorPoint
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class StrAnchorPoints(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrAnchorPoints
                | 
                | A collection of the anchor points of a section object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrAnchorPoint)
        self.str_anchor_points = com_object

    def item(self, i_index: cat_variant) -> StrAnchorPoint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As StrAnchorPoint
                | 
                |     Returns an anchor point from its index in the anchor points
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the anchor point to retrieve in the collection of
                |             anchor points. This index can either be the rank of the anchor point in the
                |             collection or the name you assign to the anchor point. As a numerics, this
                |             index is the rank of the anchor point in the collection. The index of the first
                |             anchor point in the collection is 1, and the index of the last anchor point is
                |             Count. As a string, it is the name you assigned to the member using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved anchor point

        :param cat_variant i_index:
        :rtype: StrAnchorPoint
        """
        return StrAnchorPoint(self.str_anchor_points.Item(i_index))

    def __repr__(self):
        return f'StrAnchorPoints(name="{self.name}")'
