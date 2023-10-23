#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_interaction import ABQInteraction
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQInteractions(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQInteractions
                | 
                | The collection of Abaqus interactions (ABQInteraction) objects attached to
                | an
                | ABQInitialStep object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQInteraction)
        self.abq_interactions = com_object

    def add(self, i_interaction_type: str) -> ABQInteraction:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iInteractionType) As ABQInteraction
                | 
                |     Creates a new Abaqus interaction and adds it to the collection of Abaqus
                |     Interactions.
                | 
                |     Parameters:
                | 
                |         iInteractionType
                |             The type of the interaction to create.
                | 
                |             Legal values:
                | 
                |             "ABQSurfaceToSurfaceContact"
                |             "ABQFastenedPair"
                |             "ABQRigidBodyConstraint"
                |             "ABQRigidCoupling"
                |             "ABQSmoothCoupling"
                |             "ABQARSurf"
                | 
                |     Returns:
                |         oInteraction The Abaqus interaction object that was created.
                |         
                |     Example:
                |         The following example creates a Contact pair interaction in the
                |         ABQInteractions collection:
                | 
                |          Dim abaqusInteractions As ABQInteractions
                |          Dim abqFPair As ABQFastenedPair
                |          Set abqFPair =  abaqusInteractions..Add("ABQFastenedPair")

        :param str i_interaction_type:
        :rtype: ABQInteraction
        """
        return ABQInteraction(self.abq_interactions.Add(i_interaction_type))

    def item(self, i_index: cat_variant) -> ABQInteraction:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQInteraction
                | 
                |     Returns an Abaqus interaction using its index or its name from the
                |     ABQInteractions collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus interaction to retrieve from
                |             the collection of Abaqus Interactions. If the index is a number, it specifies
                |             the rank of the Abaqus interaction in the collection. The index of the first
                |             Abaqus interaction in the collection is 1, and the index of the last
                |             interaction is Count. If the index is a string, it specifies the name you
                |             assigned to the interaction using the CATIACollection::Name property.
                |             
                | 
                |     Returns:
                |         The specified ABQInteraction.

        :param cat_variant i_index:
        :rtype: ABQInteraction
        """
        return ABQInteraction(self.abq_interactions.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus interaction using its index or its name from the
                |     Interaction collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus interaction to retrieve from
                |             the collection of Abaqus Interactions. If the index is a number, it specifies
                |             the rank of the Abaqus interaction in the collection. The index of the first
                |             Abaqus interaction in the collection is 1, and the index of the last
                |             interaction is Count. If the index is a string, it specifies the name you
                |             assigned to the interaction using the CATIABase::Name
                |             property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_interactions.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_interactions)
        # #     Dim iIndex (2)
        # #     abq_interactions.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQInteractions(name="{self.name}")'
