#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_solution_step import ABQSolutionStep
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQSolutionSteps(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQSolutionSteps
                | 
                | The collection of Abaqus solution step (ABQSolutionStep) objects contained
                | in
                | ABQSolutionCase objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQSolutionStep)
        self.abq_solution_steps = com_object

    def item(self, i_index: cat_variant) -> ABQSolutionStep:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQSolutionStep
                | 
                |     Returns an Abaqus solution step using its index or its name from the
                |     ABQSolutionSteps collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus solution step to retrieve from
                |             the collection of Abaqus solution steps. If the index is a number, it specifies
                |             the rank of the Abaqus solution step in the collection. The index of the first
                |             Abaqus solution step in the collection is 1, and the index of the last solution
                |             step is Count. If the index is a string, it specifies the name you assigned to
                |             the solution step using the CATIACollection::Name property.
                |             
                | 
                |     Returns:
                |         The specified ABQSolutionStep.

        :param cat_variant i_index:
        :rtype: ABQSolutionStep
        """
        return ABQSolutionStep(self.abq_solution_steps.Item(i_index))

    def __repr__(self):
        return f'ABQSolutionSteps(name="{self.name}")'
