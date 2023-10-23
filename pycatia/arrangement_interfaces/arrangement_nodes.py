#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_node import ArrangementNode
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ArrangementNodes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArrangementNodes
                | 
                | A Collection object for ArrangementNode objects.
                | Use this object to access individual ArrangementNode objects of an
                | ArrangementRun, ArrangementPathway and ArrangementBoundary.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArrangementNode)
        self.arrangement_nodes = com_object

    def item(self, i_index: cat_variant) -> ArrangementNode:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ArrangementNode
                | 
                |     Returns the specified ArrangementNode item of the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ArrangementNode to retrieve from this
                |             collection.
                | 
                |             To retrieve a specific object by number, use the rank of the
                |             ArrangementNode in that collection.
                |                 Note that the index of the first element in the collection is
                |                 1, and the index of the last element is Count. To retrieve a specific
                |                 ArrangementNode by name, use name that you assigned using the
                |                 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved ArrangementNode object.

        :param cat_variant i_index:
        :rtype: ArrangementNode
        """
        return ArrangementNode(self.arrangement_nodes.Item(i_index))

    def __repr__(self):
        return f'ArrangementNodes(name="{self.name}")'
