#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_temperature import ABQTemperature
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQFields(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQFields
                | 
                | The collection of Abaqus field (ABQTemperature) objects contained
                | in
                | ABQInitialStep and ABQGeneralStaticStep and ABQExplicitDynamicsStep
                | objects.
    
    """

    def __init__(self, com_object):
        """
        Please note: The child object was guessed here as I'm unfamiliar with this module.
        """
        super().__init__(com_object, child_object=ABQTemperature)
        self.abq_fields = com_object

    def add(self, i_field_type: str) -> ABQTemperature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iFieldType) As ABQTemperature
                | 
                |     Creates a new Abaqus field and adds it to the collection of Abaqus fields.
                |     The ABQInitialTemperature object can be created only in an ABQFields collection
                |     obtained from ABQInitialStep. Similarly the ABQTemperatureHistory object can be
                |     created only in an ABQFields collection obtained from
                |     ABQGeneralStaticStep.
                | 
                |     Parameters:
                | 
                |         iFieldType
                |             The type of the field to create.
                | 
                |             Legal values:
                | 
                |             "ABQInitialTemperature"
                |             "ABQTemperatureHistory"
                | 
                |     Returns:
                |         oTemperature The Abaqus field object that was created.
                |         
                |     Example:
                |         The following example creates an initial temperature in the ABQFields
                |         collection obtained from the ABQInitialStep type
                |         object:
                | 
                |          Dim abqInitialStep As ABQInitialStep
                |          Dim abqFields As ABQIAABQFields
                |          Dim abqInitalTemp As ABQTemperature
                |          Set abqFields = abqInitialStep.Fields
                |          Set abqInitalTemp =  abqFields.Add("ABQInitialTemperature")

        :param str i_field_type:
        :rtype: ABQTemperature
        """
        return ABQTemperature(self.abq_fields.Add(i_field_type))

    def item(self, i_index: cat_variant) -> ABQTemperature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQTemperature
                | 
                |     Returns an Abaqus field using its index or its name from the ABQFields
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus field to retrieve from the
                |             collection of Abaqus fields. If the index is a number, it specifies the rank of
                |             the Abaqus field in the collection. The index of the first Abaqus field in the
                |             collection is 1, and the index of the last field is Count. If the index is a
                |             string, it specifies the name you assigned to the field using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQTemperature.

        :param cat_variant i_index:
        :rtype: ABQTemperature
        """
        return ABQTemperature(self.abq_fields.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus field using its index or its name from the field
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus field to retrieve from the
                |             collection of Abaqus Fields. If the index is a number, it specifies the rank of
                |             the Abaqus field in the collection. The index of the first Abaqus field in the
                |             collection is 1, and the index of the last field is Count. If the index is a
                |             string, it specifies the name you assigned to the field using the
                |             CATIABase::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_fields.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_fields)
        # #     Dim iIndex (2)
        # #     abq_fields.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQFields(name="{self.name}")'
