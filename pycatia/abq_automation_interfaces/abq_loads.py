#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_load import ABQLoad
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQLoads(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQLoads
                | 
                | The collection of Abaqus load (ABQLoad) objects attached to an
                | ABQGeneralStaticStep, ABQHeatTransferStep, or an ABQExplicitDynamicsStep
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQLoad)
        self.abq_loads = com_object

    def add(self, i_load_type: str) -> ABQLoad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iLoadType) As ABQLoad
                | 
                |     Creates a new Abaqus load and adds it to the collection of Abaqus
                |     loads.
                | 
                |     Parameters:
                | 
                |         iLoadType
                |             The type of the load to create.
                | 
                |             Legal values:
                | 
                |             "ABQPressure"
                |             "ABQConcentratedForce"
                |             "ABQGravity"
                |             "ABQFilmCondition"
                | 
                |     Returns:
                |         oLoad The Abaqus load object that was created. 
                |     Example:
                |         The following example creates a pressure load in the ABQLoads
                |         collection:
                | 
                |          Dim abaqusLoads As ABQLoads
                |          Dim abqPressure As ABQPressure
                |          Set abaqusLoads = generalstaticstep.Loads
                |          Set abqPressure =  abaqusLoads.Add("ABQPressure")

        :param str i_load_type:
        :rtype: ABQLoad
        """
        return ABQLoad(self.abq_loads.Add(i_load_type))

    def item(self, i_index: cat_variant) -> ABQLoad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQLoad
                | 
                |     Returns an Abaqus load using its index or its name from the ABQLoads
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus load to retrieve from the
                |             collection of Abaqus loads. If the index is a number, it specifies the rank of
                |             the Abaqus load in the collection. The index of the first Abaqus load in the
                |             collection is 1, and the index of the last load is Count. If the index is a
                |             string, it specifies the name you assigned to the load using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQLoad.

        :param cat_variant i_index:
        :rtype: ABQLoad
        """
        return ABQLoad(self.abq_loads.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Abaqus load using its index or its name from the collection od
                |     loads.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus load n to retrieve from the
                |             collection of Abaqus loads. If the index is a number, it specifies the rank of
                |             the Abaqus load in the collection. The index of the first Abaqus load in the
                |             collection is 1, and the index of the last load is Count. If the index is a
                |             string, it specifies the name you assigned to the load using the
                |             CATIACollection::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_loads.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_loads)
        # #     Dim iIndex (2)
        # #     abq_loads.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQLoads(name="{self.name}")'
