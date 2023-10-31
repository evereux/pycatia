#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_fastener_interfaces.fastener import Fastener
from pycatia.system_interfaces.collection import Collection


class FastenerSet(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FastenerSet
                | 
                | Interface DELMIAFasteners DELMIAFasteners represent collection of fasteners of
                | both types point and curve.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Fastener)
        self.fastener_set = com_object

    def get_fastener(self, index: int) -> Fastener:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFastener(short index) As Fastener
                | 
                |     Get a specified DELMIAFastener from the collection of Fasteners. The
                |     specification is through the Index or the location of fastener in the list.
                |     Index starts at 1.
                | 
                |     Parameters:
                | 
                |         index
                |             Integer for the index in the list. It is an input parameter.
                |             
                |         opiFastener
                |             Returned instance of DELMIAFastener. It contains the return
                |             DELMIAFastener at the specifed index. It is an output
                |             parameter.

        :param int index:
        :rtype: Fastener
        """
        return Fastener(self.fastener_set.GetFastener(index))

    def __repr__(self):
        return f'FastenerSet(name="{self.name}")'
