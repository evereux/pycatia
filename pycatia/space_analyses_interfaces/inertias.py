#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.space_analyses_interfaces.inertia import Inertia
from pycatia.system_interfaces.collection import Collection


class Inertias(Collection):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Inertias
                | 
                | A collection of all inertia objects currently managed by the
                | application.
                | 
                | WARNING: this collection will be DEPRECATED in the next release. It is
                | recommended to use the method GetTechnologicalObject("Inertia") on the product
                | to analyze, to retrieve an Inertia object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.inertias = com_object

    def add(self, i_object=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(AnyObject iObject) As Inertia
                | 
                |     Creates an Inertia object from an object and adds it to the Inertias
                |     collection.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The Object 
                | 
                |     Returns:
                |         The created Inertia 
                |     Example:
                | 
                |              This example creates a new Inertia from a product
                |              TheProduct
                |             in the TheInertias collection.
                |             
                | 
                |             Dim NewInertia As Inertia
                |             Set NewInertia = TheInertias.Add(TheProduct)

        :param AnyObject i_object:
        :return: Inertia
        """
        return Inertia(self.inertias.Add(i_object.com_object))

    def item(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Inertia
                | 
                |     Returns an Inertia object using its index or its name from the Inertias
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Inertia to retrieve from the
                |             collection of inertias. As a numerics, this index is the rank of the Inertia in
                |             the collection. The index of the first Inertia in the collection is 1, and the
                |             index of the last Inertia is Count. As a string, it is the name you assigned to
                |             the Inertia. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisInertia the ninth
                |              Inertia,
                |             and in ThatInertia the Inertia named
                |             Inertia Of MyProduct from the TheInertias collection.
                |             
                |             
                | 
                |             Dim ThisInertia As Inertia
                |             Set ThisInertia = TheInertias.Item(9)
                |             Dim ThatInertia As Inertia
                |             Set ThatInertia = TheInertias.Item("Inertia Of MyProduct")

        :param CATVariant i_index:
        :return: Inertia
        """
        return Inertia(self.inertias.Item(i_index.com_object))

    def remove(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Inertia object from the Inertias collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Inertia to remove from the collection
                |             of inertias. As a numerics, this index is the rank of the Inertia in the
                |             collection. The index of the first Inertia in the collection is 1, and the
                |             index of the last Inertia is Count. As a string, it is the name you assigned to
                |             the Inertia. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth Inertia and the Inertia
                |              named
                |             Inertia Of MyProduct from the TheInertias
                |             collection.
                |             
                | 
                |             TheInertias.Remove(10)
                |             TheInertias.Remove("Inertia Of MyProduct")

        :param CATVariant i_index:
        :return: None
        """
        return self.inertias.Remove(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(inertias)
        # #     Dim iIndex (2)
        # #     inertias.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Inertias(name="{ self.name }")'
