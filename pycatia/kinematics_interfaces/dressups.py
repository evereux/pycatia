#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.kinematics_interfaces.dressup import Dressup
from pycatia.kinematics_interfaces.mechanism import Mechanism
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Dressups(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Dressups
                | 
                | A collection of all Dressup entities currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dressups = com_object

    def add(self, i_mechanism: Mechanism, i_context: Product) -> Dressup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Mechanism iMechanism,
                | Product iContext) As Dressup
                | 
                |     Creates a new Dressup and adds it to the Dressups
                |     collection.
                | 
                |     Parameters:
                | 
                |         iMechanism
                |             The mechanism on which the dressup will apply. 
                |         iContext
                |             The Context product on which the mechanism is defined
                |
                |     Returns:
                |         The created Dressup 
                |     Example:
                |         This example creates a new Dressup in the TheDressups
                |         collection.
                | 
                |             Dim NewDressup As Dressup
                |             Set NewDressup = TheDressups.Add(Mechanism)

        :param Mechanism i_mechanism:
        :param Product i_context:
        :rtype: Dressup
        """
        return Dressup(self.dressups.Add(i_mechanism.com_object, i_context.com_object))

    def item(self, i_index: cat_variant) -> Dressup:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Dressup
                | 
                |     Returns a Dressup using its index or its name from the Dressups
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Dressup to retrieve from the
                |             collection of Dressups. As a numerics, this index is the rank of the Dressup in
                |             the collection. The index of the first Dressup in the collection is 1, and the
                |             index of the last Dressup is Count. As a string, it is the name you assigned to
                |             the Dressup using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Dressup 
                |     Example:
                |         This example returns in ThisDressup the third Dressup in the
                |         collection, and in ThatDressup the Dressup named
                |         MyDressup.
                | 
                |          Dim ThisDressup As Dressup
                |          Set ThisDressup = TheDressups.Item(3)
                |          Dim ThatDressup As Dressup
                |          Set ThatDressup = CATIA.Dressups.Item("MyDressup")

        :param cat_variant i_index:
        :rtype: Dressup
        """
        return Dressup(self.dressups.Item(i_index))

    def list_mechanisms_context(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListMechanismsContext() As CATSafeArrayVariant
                | 
                |     Each mechanism of the list given by ListPossibleMechanisms has a context
                |     product on which it is defined.
                | 
                |     Parameters:
                | 
                |         Nothing
                | 
                |     Returns:
                |         The list of mechanisms' contexts on which a dressup can be created. The
                |         context of oMechanismList(i) is oContextList(i). 
                |     Example:
                |         The following example returns the first and the last element of the
                |         list of mechanisms' contexts. We assume that this list contains at least two
                |         values.
                | 
                |             Dim ContextList As Product
                |             ContextList = MyDressups.ListMechanismsContext()
                |             Dim FirstContext As Product
                |             Set FirstContext = ContextList(0) 
                |             Dim LastContext As Product
                |             Set LastContext = ContextList(ubound(ContextList))

        :rtype: tuple
        """
        return self.dressups.ListMechanismsContext()

    def list_possible_mechanisms(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListPossibleMechanisms() As CATSafeArrayVariant
                | 
                |     Returns information about all possible mechanisms on which a dressup can be
                |     created.
                | 
                |     Parameters:
                | 
                |         Nothing
                | 
                |     Returns:
                |         The list of possible mechanisms on which a dressup can be created.
                |         
                |     Example:
                |         The following example returns the first and the last element of the
                |         list of possible mechanisms. We assume that this list contains at least two
                |         values.
                | 
                |             Dim PossibleMecList As Mechanism
                |             PossibleMecList = MyDressups.ListPossibleMechanisms()
                |             Dim FirstMeca As Mechanism
                |             Set Meca  = PossibleMecList(0) 
                |             Dim LastMeca As Mechanism
                |             Set Meca  = PossibleMecList(ubound(PossibleMecList))

        :rtype: tuple
        """
        return self.dressups.ListPossibleMechanisms()

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Dressup from the Dressups collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Dressup to retrieve from the
                |             collection of Dressups. As a numerics, this index is the rank of the Dressup in
                |             the collection. The index of the first Dressup in the collection is 1, and the
                |             index of the last Dressup is Count. As a string, it is the name you assigned to
                |             the Dressup. 
                | 
                |     Returns:
                |         Nothing 
                |     Example:
                |         The following example removes the tenth Dressup and the Dressup named
                |         DressupTwo from the TheDressups collection.
                | 
                |             TheDressups.Remove(10)
                |             TheDressups.Remove("DressupTwo")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.dressups.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(dressups)
        # #     Dim iIndex (2)
        # #     dressups.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Dressups(name="{self.name}")'
