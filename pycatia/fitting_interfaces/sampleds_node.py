#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SampledsNode(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SampledsNode
                | 
                | The interface to access a CATIASampledsNode.
                | Role: The SampledsNode interface can be used to obtain different types of
                | Sampled based collections from within the current action
                | document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sampleds_node = com_object

    def get_sampleds(self, i_collection_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSampleds(CATBSTR iCollectionName) As
                | CATBaseDispatch
                | 
                |     Retrieves a sampleds based collection of objects
                | 
                |     Parameters:
                | 
                |         iCollectionName
                |             The name of the collection to retrieve. 
                | 
                |     Returns:
                |         The requested collection 
                |     Example:
                |         The following example retrieves the collection of Track objects (called
                |         CATIATracks) from within the current document.
                | 
                |          Dim myTracks as Tracks
                |          Set myTracks = SampledsNode.GetSampleds ("Tracks")

        :param str i_collection_name:
        :rtype: AnyObject
        """
        return self.sampleds_node.GetSampleds(i_collection_name)

    def __repr__(self):
        return f'SampledsNode(name="{ self.name }")'
