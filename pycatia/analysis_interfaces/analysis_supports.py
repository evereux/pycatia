#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection


class AnalysisSupports(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisSupports
                | 
                | The collection of analysis case making an Analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_supports = com_object

    def item(self, i_index: int, o_positionning: AnyObject, o_pointed: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Item(long iIndex,
                | AnyObject oPositionning,
                | AnyObject oPointed)
                | 
                |     Returns analysis support object information using its index in the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The numeric index is the rank in the collection. The index of the
                |             first case in the collection is 1, and the index of the last is Count.
                |             
                |         oPositionning
                |             The positionning feature is exists. 
                |         oPointed
                |             The pointed object.

        :param int i_index:
        :param AnyObject o_positionning:
        :param AnyObject o_pointed:
        :rtype: None
        """
        return self.analysis_supports.Item(i_index, o_positionning.com_object, o_pointed.com_object)

    def __repr__(self):
        return f'AnalysisSupports(name="{self.name}")'
