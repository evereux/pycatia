#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_data_output_request import ABQDataOutputRequest
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQDataOutputRequests(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQDataOutputRequests
                | 
                | The collection of Abaqus data output request (ABQDataOutputRequest) objects
                | attached to an
                | ABQGeneralStaticStep, an ABQFrequencyStep, or an ABQHeatTransferStep
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQDataOutputRequest)
        self.abq_data_output_requests = com_object

    def add(self) -> ABQDataOutputRequest:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As ABQDataOutputRequest
                | 
                |     Creates a new Abaqus data output request and adds it to the collection of
                |     Abaqus data output requests.
                | 
                |     Returns:
                |         oDataOutputRequest The Abaqus data output request object that was
                |         created. 
                |     Example:
                |         The following example creates a data output request in the
                |         ABQDataOutputRequests collection:
                | 
                |          Dim abqDataOutputRequests As ABQDataOutputRequests
                |          Set abqDataOutputRequests = generalstaticstep.DataOutputRequests
                |          Dim abqDataOutputRequest As ABQDataOutputRequest
                |          Set abqDataOutputRequest =  abqDataOutputRequests.Add()

        :rtype: ABQDataOutputRequest
        """
        return ABQDataOutputRequest(self.abq_data_output_requests.Add())

    def item(self, i_index: cat_variant) -> ABQDataOutputRequest:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ABQDataOutputRequest
                | 
                |     Returns an Abaqus data output request using its index or its name from the
                |     ABQDataOutputRequests collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus data output request to retrieve
                |             from the collection of Abaqus data output requests. If the index is a number,
                |             it specifies the rank of the Abaqus data output request in the collection. The
                |             index of the first Abaqus data output request in the collection is 1, and the
                |             index of the last data output request is Count. If the index is a string, it
                |             specifies the name you assigned to the data output request using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQDataOutputRequest.

        :param cat_variant i_index:
        :rtype: ABQDataOutputRequest
        """
        return ABQDataOutputRequest(self.abq_data_output_requests.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Abaqus data output request using its index or its name from the
                |     data output requests collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the data output request to retrieve from
                |             the collection of data output requests. As a numeric, this index is the rank of
                |             the data output request in the collection. The index of the first data output
                |             request in the collection is 1, and the index of the last data output request
                |             is Count. As a string, it is the name you assigned to the data output request
                |             using the CATIABase::Name property.

        :param cat_variant i_index:
        :rtype: None
        """
        return self.abq_data_output_requests.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_data_output_requests)
        # #     Dim iIndex (2)
        # #     abq_data_output_requests.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQDataOutputRequests(name="{self.name}")'
