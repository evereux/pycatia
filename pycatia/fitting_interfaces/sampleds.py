#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.fitting_interfaces.sampled import Sampled
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Sampleds(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Sampleds
                | 
                | The collection of all the Sampled objects currently contained in the current
                | document.
                | A Sampled object is the base type for Track objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Sampled)
        self.sampleds = com_object

    def add(self) -> Sampled:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As Sampled
                | 
                |     Creates a new Sampled object and adds it to the Sampleds
                |     collection.
                | 
                |     Returns:
                |         The created Sampled 
                |     Example:
                |         The following example creates a Sampled (called newSampled) with in the
                |         Sampleds collection.
                | 
                |          Set newSampled = Sampleds.Add

        :rtype: Sampled
        """
        return Sampled(self.sampleds.Add())

    def add_from_sel(self) -> Sampled:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddFromSel() As Sampled
                | 
                |     Creates a new Sampled from the selection and adds it to the Sampleds
                |     collection.
                | 
                |     Returns:
                |         The created Sampled 
                |     Example:
                |         The following example creates a Sampled (called newSampled) with in the
                |         Sampleds collection.
                | 
                |          Set newSampled = Sampleds.Add

        :rtype: Sampled
        """
        return Sampled(self.sampleds.AddFromSel())

    def item(self, i_index: cat_variant) -> Sampled:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Sampled
                | 
                |     Returns a CATIASampled object using its index from the CATIASampled
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the sampled to retrieve from the collection of
                |             sampleds. Numerically, the index value corresponds to the rank of the sampled
                |             in the collection (ie. the first is 1, second is 2, ...).
                |             
                | 
                |     Returns:
                |         The retrieved Sampled 
                |     Example:
                |         The following example retrieves the second Sampled from the Sampleds
                |         collection of the active document.
                | 
                |          Dim newSampled as Sampled
                |          Set newSampled = Sampleds.Item (2)

        :param cat_variant i_index:
        :rtype: Sampled
        """
        return Sampled(self.sampleds.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a CATIASampled object from the CATIASampled
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the sampled to remove from the collection of sampleds.
                |             Numerically, the index value corresponds to the rank of the sampled in the
                |             collection (ie. the first is 1, second is 2, ...).
                |             
                |         Example:
                |             The following example removes the third Sampled from the Sampleds
                |             collection of the active document.
                | 
                |              Sampleds.Remove (3)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.sampleds.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(sampleds)
        # #     Dim iIndex (2)
        # #     sampleds.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Sampleds(name="{self.name}")'
