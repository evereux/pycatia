#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.fix_together import FixTogether
from pycatia.system_interfaces.collection import Collection


class FixTogethers(Collection):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FixTogethers
                | 
                | A collection of all the FixTogether objects contained in the
                | product.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fix_togethers = com_object

    def add(self) -> FixTogether:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As FixTogether
                | 
                |     Creates a new FixTogether and adds it to the FixTogethers
                |     collection.
                | 
                |     Returns:
                |         The created FixTogether 
                |     Example:
                |         The following example creates a FixTogether newFixTogether in the
                |         FixTogether collection.
                | 
                |          Set newFixTogether = fixTogethers.Add

        :return: FixTogether
        :rtype: FixTogether
        """
        return FixTogether(self.fix_togethers.Add())

    def item(self, i_index: CATVariant) -> FixTogether:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As FixTogether
                | 
                |     Returns a FixTogether using its index or its name from the FixTogethers
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the FixTogether to retrieve from the
                |             collection of FixTogether. As a numerics, this index is the rank of the
                |             FixTogether in the collection. The index of the first FixTogether in the
                |             collection is 1, and the index of the last FixTogether is Count. As a string,
                |             it is the name you assigned to the FixTogether using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved FixTogether 
                |     Example:
                |         This example retrieves in thisFixTogether the fifth FixTogether in the
                |         collection and in thatFixTogether the FixTogether named MyFixTogether in the
                |         FixTogether collection of the product product.
                | 
                |          Set fixTogetherColl = product.FixTogethers
                |          Set thisFixTogether = fixTogetherColl.Item(5)
                |          Set thatFixTogether = fixTogetherColl.Item("MyFixTogether")

        :param CATVariant i_index:
        :return: FixTogether
        :rtype: FixTogether
        """
        return FixTogether(self.fix_togethers.Item(i_index.com_object))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a FixTogether from the FixTogethers collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the FixTogether to remove from the
                |             FixTogethers collection. As a numerics, this index is the rank of the
                |             FixTogether in the collection. The index of the first FixTogether in the
                |             collection is 1, and the index of the last FixTogether is Count. As a string,
                |             it is the name you assigned to the FixTogether using the
                |             
                | 
                |         AnyObject.Name property. 
                | 
                | Example:
                |     This example removes the last FixTogether in the
                |     collection.
                | 
                |      fixTogetherColl.Remove(fixTogetherColl.Count)

        :param CATVariant i_index:
        :return: None
        :rtype: None
        """
        return self.fix_togethers.Remove(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(fix_togethers)
        # #     Dim iIndex (2)
        # #     fix_togethers.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'FixTogethers(name="{self.name}")'
