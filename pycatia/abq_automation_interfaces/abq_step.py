#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_data_output_requests import ABQDataOutputRequests
from pycatia.abq_automation_interfaces.abq_field_output_requests import ABQFieldOutputRequests
from pycatia.abq_automation_interfaces.abq_history_output_requests import ABQHistoryOutputRequests
from pycatia.abq_automation_interfaces.abq_interactions import ABQInteractions
from pycatia.system_interfaces.any_object import AnyObject


class ABQStep(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQStep
                | 
                | Represents a Abaqus analysis step (ABQStep) object.
                | Role: Access an Abaqus analysis step or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_step = com_object

    @property
    def data_output_requests(self) -> ABQDataOutputRequests:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DataOutputRequests() As ABQDataOutputRequests (Read
                | Only)
                | 
                |     Returns the ABQDataOutputRequests container associated with the
                |     step.
                | 
                |     Example:
                |         The following example retrieves the ABQDataOutputRequests container
                |         abqOutputRequests:
                | 
                |          Dim abqStep As ABQGeneralStaticStep 
                |          Dim abqDataOutputRequests As ABQDataOutputRequests
                |          Set abqDataOutputRequests = abqStep.OutputRequests

        :rtype: ABQDataOutputRequests
        """

        return ABQDataOutputRequests(self.abq_step.DataOutputRequests)

    @property
    def field_output_requests(self) -> ABQFieldOutputRequests:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FieldOutputRequests() As ABQFieldOutputRequests (Read
                | Only)
                | 
                |     Returns the ABQFieldOutputRequests container associated with the
                |     step.
                | 
                |     Example:
                |         The following example retrieves the ABQFieldOutputRequests container
                |         abqOutputRequests:
                | 
                |          Dim abqStep As ABQGeneralStaticStep 
                |          Dim abqFieldOutputRequests As ABQFieldOutputRequests
                |          Set abqFieldOutputRequests = abqStep.OutputRequests

        :rtype: ABQFieldOutputRequests
        """

        return ABQFieldOutputRequests(self.abq_step.FieldOutputRequests)

    @property
    def history_output_requests(self) -> ABQHistoryOutputRequests:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HistoryOutputRequests() As ABQHistoryOutputRequests (Read
                | Only)
                | 
                |     Returns the ABQHistoryOutputRequests container associated with the
                |     step.
                | 
                |     Example:
                |         The following example retrieves the ABQHistoryOutputRequests container
                |         abqOutputRequests:
                | 
                |          Dim abqStep As ABQGeneralStaticStep 
                |          Dim abqHistoryOutputRequests As
                |          ABQHistoryOutputRequests
                |          Set abqHistoryOutputRequests = abqStep.OutputRequests

        :rtype: ABQHistoryOutputRequests
        """

        return ABQHistoryOutputRequests(self.abq_step.HistoryOutputRequests)

    @property
    def interactions(self) -> ABQInteractions:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Interactions() As ABQInteractions (Read Only)
                | 
                |     Returns the ABQInteractions container associated with the
                |     step.
                | 
                |     Example:
                |         The following example retrieves the ABQInteractions container
                |         abqInteractions:
                | 
                |          Dim abqStep As ABQGeneralStaticStep 
                |          Dim abqInteractions As ABQInteractions
                |          Set abqInteractions = abqStep.Interactions

        :rtype: ABQInteractions
        """

        return ABQInteractions(self.abq_step.Interactions)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the step.
                | 
                |     Returns:
                |         The string representing the type of the step.

        :rtype: str
        """

        return self.abq_step.Type

    def __repr__(self):
        return f'ABQStep(name="{self.name}")'
