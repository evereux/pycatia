#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_boundary_condition import ABQBoundaryCondition
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQBoundaryConditions(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQBoundaryConditions
                | 
                | The collection of Abaqus boundary condition objects attached
                | to
                | ABQGeneralStaticStep, ABQHeatTransferStep, and ABQExplicitDynamicsStep
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQBoundaryCondition)
        self.abq_boundary_conditions = com_object

    def add(self, i_boundary_type: str) -> ABQBoundaryCondition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iBoundaryType) As ABQBoundaryCondition
                | 
                |     Creates a new Abaqus boundary condition and adds it to the collection of
                |     Abaqus boundary conditions.
                | 
                |     Parameters:
                | 
                |         iBoundaryType
                |             The type of the boundary condition to create.
                | 
                |             Legal values:
                | 
                |             "ABQClamp"
                |             "ABQDisplacementBC"
                |             "ABQTemperatureBC"
                | 
                |     Returns:
                |         oBoundaryCondition The Abaqus boundary condition object that was
                |         created. 
                |     Example:
                |         The following example creates a clamp boundary condition in the
                |         ABQBoundaryConditions collection:
                | 
                |          Dim abaqusBCs As ABQBoundaryConditions
                |          Dim abqClampBC As ABQClampBC
                |          Set abqClampBC =  abaqusBCs.Add("ABQClamp")

        :param str i_boundary_type:
        :rtype: ABQBoundaryCondition
        """
        return ABQBoundaryCondition(self.abq_boundary_conditions.Add(i_boundary_type))

    def item(self, i_index: cat_variant) -> ABQBoundaryCondition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQBoundaryCondition
                | 
                |     Returns an Abaqus boundary condition using its index or its name from the
                |     ABQBoundaryConditions collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus boundary condition to retrieve
                |             from the collection of Abaqus boundary conditions. If the index is a number, it
                |             specifies the rank of the Abaqus boundary condition in the collection. The
                |             index of the first Abaqus boundary condition in the collection is 1, and the
                |             index of the last boundary condition is Count. If the index is a string, it
                |             specifies the name you assigned to the boundary condition using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQBoundaryCondition.

        :param cat_variant i_index:
        :rtype: ABQBoundaryCondition
        """
        return ABQBoundaryCondition(self.abq_boundary_conditions.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus boundary condition using its index or its name from the
                |     collection of boundary conditions.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus boundary condition to retrieve
                |             from the collection of Abaqus boundary conditions. If the index is a number, it
                |             specifies the rank of the Abaqus boundary condition in the collection. The
                |             index of the first Abaqus boundary condition in the collection is 1, and the
                |             index of the last boundary condition is Count. If the index is a string, it
                |             specifies the name you assigned to the boundary condition using the
                |             CATIACollection::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_boundary_conditions.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_boundary_conditions)
        # #     Dim iIndex (2)
        # #     abq_boundary_conditions.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQBoundaryConditions(name="{self.name}")'
