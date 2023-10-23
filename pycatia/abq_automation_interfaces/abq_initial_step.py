#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_fields import ABQFields
from pycatia.abq_automation_interfaces.abq_mass_scalings import ABQMassScalings
from pycatia.abq_automation_interfaces.abq_step import ABQStep


class ABQInitialStep(ABQStep):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQStep
                |                         ABQInitialStep
                | 
                | Represents an Abaqus initial step (ABQInitialStep) object.
                | Role: Access an Abaqus initial step object or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_initial_step = com_object

    @property
    def fields(self) -> ABQFields:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Fields() As ABQFields (Read Only)
                | 
                |     Returns the ABQFields container associated with the step.
                | 
                |     Example:
                |         This example retrieves the ABQFields container
                |         abqFields.
                | 
                |          Dim abqInitialStep As ABQInitialStep 
                |          Dim abqFields As ABQFields
                |          Set abqFields = abqInitialStep.Fields

        :rtype: ABQFields
        """

        return ABQFields(self.abq_initial_step.Fields)

    @property
    def mass_scalings(self) -> ABQMassScalings:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MassScalings() As ABQMassScalings (Read Only)
                | 
                |     Returns the ABQMassScalings container associated with the
                |     step.
                | 
                |     Example:
                |         The following example retrieves the ABQMassScalings container
                |         abqScalings:
                | 
                |          Dim abqInitialStep As ABQInitialStep 
                |          Dim abqScalings As ABQMassScalings
                |          Set abqScalings = abqInitialStep.MassScalings

        :rtype: ABQMassScalings
        """

        return ABQMassScalings(self.abq_initial_step.MassScalings)

    def __repr__(self):
        return f'ABQInitialStep(name="{self.name}")'
