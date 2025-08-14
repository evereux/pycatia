#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_step import ABQStep
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQSteps(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQSteps
                | 
                | The collection of Abaqus analysis step (ABQStep) objects contained in
                | an
                | ABQAnalysisCase object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQStep)
        self.abq_steps = com_object

    def add(self, i_step_type: str) -> ABQStep:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(CATBSTR iStepType) As ABQStep
                | 
                |     Creates a new Abaqus Step and adds it to the collection of Abaqus
                |     steps.
                | 
                |     Parameters:
                | 
                |         iStepType
                |             The type of the step to create.
                | 
                |             Legal values: "ABQGeneralStaticStep", "ABQFrequencyStep",
                |             "ABQExplicitDynamicsStep", "ABQHeatTransferStep" "ABQLinearDynamicStepModal"
                |             "ABQLinearDynamicStepSubspace" 
                | 
                |     Returns:
                |         oStep The Abaqus step object that was created. 
                |     Example:
                |         The following example creates a general static step in the ABQSteps
                |         collection:
                | 
                |          Dim abqCase As ABQAnalysisCase
                |          Dim abaqusSteps As ABQSteps
                |          Dim generalstaticstep As ABQGeneralStaticStep
                |          Set abaqusSteps = abqCase.Steps
                |          Set generalstaticstep =  abaqusSteps.Add("ABQGeneralStaticStep")

        :param str i_step_type:
        :rtype: ABQStep
        """
        return ABQStep(self.abq_steps.Add(i_step_type))

    def insert(self, i_step_type: str, i_index: cat_variant) -> ABQStep:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Insert(CATBSTR iStepType,
                | CATVariant iIndex) As ABQStep
                | 
                |     Creates a new Abaqus Step and inserts it to the collection of Abaqus
                |     steps.
                | 
                |     Parameters:
                | 
                |         iStepType
                |             The type of the step to create.
                | 
                |             Legal values: "ABQGeneralStaticStep", "ABQFrequencyStep",
                |             "ABQExplicitDynamicsStep", "ABQHeatTransferStep" 
                |         iIndex
                |             Index of Abaqus step after which the new step is to be inserted.
                |             for initialization step iIndex is 1
                | 
                |     Returns:
                |         oStep The Abaqus step object that was inserted. 
                |     Example:
                |         The following example creates a general static step in the ABQSteps
                |         collection:
                | 
                |          Dim abqCase As ABQAnalysisCase
                |          Dim abaqusSteps As ABQSteps
                |          Dim generalstaticstep As ABQGeneralStaticStep
                |          Set abaqusSteps = abqCase.Steps
                |          Set generalstaticstep =  abaqusSteps.Insert("ABQGeneralStaticStep", 1)

        :param str i_step_type:
        :param cat_variant i_index:
        :rtype: ABQStep
        """
        return ABQStep(self.abq_steps.Insert(i_step_type, i_index))

    def item(self, i_index: cat_variant) -> ABQStep:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQStep
                | 
                |     Returns an Abaqus step using its index or its name from the ABQSteps
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus step to retrieve from the
                |             collection of Abaqus steps. If the index is a number, it specifies the rank of
                |             the Abaqus step in the collection. The index of the first Abaqus step in the
                |             collection is 1, and the index of the last step is Count. If the index is a
                |             string, it specifies the name you assigned to the step using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQStep. 
                |     Example:
                |         This example retrieves the fifth Abaqus step in the collection and
                |         saves it in a variable called FirstStep. The example also retrieves the Abaqus
                |         step named "MyStep" in the collection and saves it in a variable called
                |         SecondStep.
                | 
                |          Set CaseColl = AnalysisDoc.ABQAnalysisModel.Cases
                |          Set ThisCase = CaseColl.Item(5)
                |          Set StepColl = ThisCase.Steps
                |          Set FirstStaticStep = StepColl.Item(5)
                |          Set SecondStaticStep = StepColl.Item("MyStep")

        :param cat_variant i_index:
        :rtype: ABQStep
        """
        return ABQStep(self.abq_steps.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus step using its index or its name from the Step
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus step to retrieve from the
                |             collection of Abaqus Steps. If the index is a number, it specifies the rank of
                |             the Abaqus step in the collection. The index of the first Abaqus step in the
                |             collection is 1, and the index of the last step is Count. If the index is a
                |             string, it specifies the name you assigned to the step using the
                |             CATIABase::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_steps.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_steps)
        # #     Dim iIndex (2)
        # #     abq_steps.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQSteps(name="{self.name}")'
