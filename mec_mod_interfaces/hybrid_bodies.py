#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.system_interfaces.collection import Collection


class HybridBodies(Collection):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     HybridBodies
                | 
                | A collection of the HybridBody objects.
    
    """

    def __init__(self, com_object, child_object=HybridBody):
        super().__init__(com_object, child_object=HybridBody)
        self.hybrid_bodies = com_object
        self.child_object = child_object

    def add(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add() As HybridBody
                | 
                |     Creates a new hybrid body and adds it to the HybridBodies collection. This
                |     body becomes the current one
                | 
                |     Returns:
                |         The created body 
                |     Example:
                |         The following example creates a body named newHybridBody in the hybrid
                |         body collection of the rootPart part in the partDoc part document. NewPartBody
                |         becomes the current body in partDoc.
                | 
                |          Set NewPartBody = rootPart.Bodies.AddPartBody()

        :return: HybridBody
        """
        return HybridBody(self.hybrid_bodies.Add())

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As HybridBody
                | 
                |     Returns a body using its index or its name from the Bodies
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the hybrid body to retrieve from the
                |             collection of hybrid bodies. As a numerics, this index is the rank of the
                |             hybrid body in the collection. The index of the first hybrid body in the
                |             collection is 1, and the index of the last hybrid body is Count. As a string,
                |             it is the name you assigned to the hybrid body using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved hybrid body 
                |     Example:
                |         This example retrieves in ThisHybridBody the fifth hybrid body in the
                |         collection and in ThatHybridBody the hybrid body named MyHybridBody in the
                |         hybrid body collection of the partDoc part document.
                | 
                |          Set hybridBodyColl = partDoc.Part.HybridBodies
                |          Set ThisHybridBody = hybridBodyColl.Item(5)
                |          Set ThatHybridBody = hybridBodyColl.Item("MyHybridBody")

        :param CATVariant i_index:
        :return: HybridBody
        """
        return HybridBody(self.hybrid_bodies.Item(i_index))

    def __repr__(self):
        return f'HybridBodies(name="{self.name}")'
