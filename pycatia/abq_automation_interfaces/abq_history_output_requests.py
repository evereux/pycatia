#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_history_output_request import ABQHistoryOutputRequest
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQHistoryOutputRequests(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQHistoryOutputRequests
                | 
                | The collection of Abaqus history output request (ABQHistoryOutputRequest)
                | objects attached to an
                | ABQGeneralStaticStep, an ABQHeatTransferStep, or an ABQExplicitDynamicsStep
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQHistoryOutputRequest)
        self.abq_history_output_requests = com_object

    def add(self) -> ABQHistoryOutputRequest:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As ABQHistoryOutputRequest
                | 
                |     Creates a new Abaqus history output request and adds it to the collection
                |     of Abaqus history output requests.
                | 
                |     Returns:
                |         oHistoryOutputRequest The Abaqus history output request object that was
                |         created. 
                |     Example:
                |         The following example creates a history output request in the
                |         ABQHistoryOutputRequests collection:
                | 
                |          Dim abqHistoryOutputRequests As
                |          ABQHistoryOutputRequests
                |          Set abqHistoryOutputRequests = generalstaticstep.HistoryOutputRequests
                |          Dim abqHistoryOutputRequest As
                |          ABQHistoryOutputRequest
                |          Set abqHistoryOutputRequest =  abqHistoryOutputRequests.Add()

        :rtype: ABQHistoryOutputRequest
        """
        return ABQHistoryOutputRequest(self.abq_history_output_requests.Add())

    def item(self, i_index: cat_variant) -> ABQHistoryOutputRequest:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQHistoryOutputRequest
                | 
                |     Returns an Abaqus history output request using its index or its name from
                |     the ABQHistoryOutputRequests collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus history output request to
                |             retrieve from the collection of Abaqus history output requests. If the index is
                |             a number, it specifies the rank of the Abaqus history output request in the
                |             collection. The index of the first Abaqus history output request in the
                |             collection is 1, and the index of the last history output request is Count. If
                |             the index is a string, it specifies the name you assigned to the history output
                |             request using the CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQHistoryOutputRequest.

        :param cat_variant i_index:
        :rtype: ABQHistoryOutputRequest
        """
        return ABQHistoryOutputRequest(self.abq_history_output_requests.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus history output request using its index or its name from
                |     the history output requests collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the history output request to retrieve
                |             from the collection of history output requests. As a numeric, this index is the
                |             rank of the history output request in the collection. The index of the first
                |             history output request in the collection is 1, and the index of the last
                |             history output request is Count. As a string, it is the name you assigned to
                |             the history output request using the CATIABase::Name
                |             property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_history_output_requests.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_history_output_requests)
        # #     Dim iIndex (2)
        # #     abq_history_output_requests.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQHistoryOutputRequests(name="{self.name}")'
