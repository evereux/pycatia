#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_property import ABQProperty
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQProperties(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQProperties
                | 
                | The collection of Abaqus property objects (ABQProperty) attached to
                | an
                | ABQAnalysisModel object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQProperty)
        self.abq_properties = com_object

    def add(self, i_property_type: str) -> ABQProperty:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iPropertyType) As ABQProperty
                | 
                |     Creates a new Abaqus Property and adds it to the collection of Abaqus
                |     Properties.
                | 
                |     Parameters:
                | 
                |         iPropertyType
                |             The type of the Property to create.
                | 
                |             Legal values:
                | 
                |             "ABQTabularAmplitude"
                |             "ABQSmoothStepAmplitude"
                |             "ABQMechConnBehavior"
                |             "ABQThermalConnBehavior"
                |             "ABQPreTensionProperty"
                |             "ABQGasketProperty"
                | 
                |     Returns:
                |         oProperty The Abaqus Property object that was created.
                |         
                |     Example:
                |         The following example creates a Tabular Amplitude Property in the
                |         ABQProperties collection:
                | 
                |          Dim abaqusproperties As ABQPropertiess
                |          Dim abqtabularAmpl As ABQTabularAmplitude
                |          Set abqtabularAmpl =  abaqusproperties.Add("ABQTabularAmplitude")

        :param str i_property_type:
        :rtype: ABQProperty
        """
        return ABQProperty(self.abq_properties.Add(i_property_type))

    def item(self, i_index: cat_variant) -> ABQProperty:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQProperty
                | 
                |     Returns an Abaqus property using its index or its name from the
                |     ABQProperties collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus property to retrieve from the
                |             collection of Abaqus properties. If the index is a number, it specifies the
                |             rank of the Abaqus property in the collection. The index of the first Abaqus
                |             property in the collection is 1, and the index of the last property is Count.
                |             If the index is a string, it specifies the name you assigned to the property
                |             using the CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQProperty.

        :param cat_variant i_index:
        :rtype: ABQProperty
        """
        return ABQProperty(self.abq_properties.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Abaqus property using its index or its name from the property
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus property to retrieve from the
                |             collection of Abaqus Properties. If the index is a number, it specifies the
                |             rank of the Abaqus property in the collection. The index of the first Abaqus
                |             property in the collection is 1, and the index of the last property is Count.
                |             If the index is a string, it specifies the name you assigned to the property
                |             using the CATIABase::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_properties.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_properties)
        # #     Dim iIndex (2)
        # #     abq_properties.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQProperties(name="{self.name}")'
