#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_output_request import ABQOutputRequest
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ABQOutputRequests(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ABQOutputRequests
                | 
                | The collection of Abaqus output request (ABQOutputRequest) objects attached to
                | an
                | ABQGeneralStaticStep, an ABQFrequencyStep, ABQHeatTransferStep, or an
                | ABQExplicitDynamicsStep object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ABQOutputRequest)
        self.abq_output_requests = com_object

    def add(self, i_output_request_type: int) -> ABQOutputRequest:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(ABQOutputRequestType iOutputRequestType) As
                | ABQOutputRequest
                | 
                |     Creates a new Abaqus output request and adds it to the collection of Abaqus
                |     output requests.
                | 
                |     Parameters:
                | 
                |         iOutputRequestType
                |             The type of the output request to create.
                | 
                |             Legal values:
                | 
                |             "ABQFIELD"
                |             "ABQHISTORY"
                |             "ABQDATA
                | 
                |     Returns:
                |         oOutputRequest The Abaqus output request object that was created.
                |         
                |     Example:
                |         The following example creates a field output request in the
                |         ABQOutputRequests collection:
                | 
                |          Dim abaqusOutputRequests As ABQOutputRequests
                |          Set abaqusOutputRequests = generalstaticstep.GetItem ("ABQVBOutputRequests")
                |          Dim abqFieldOutputRequest As ABQFieldOutputRequest
                |          Set abqFieldOutputRequest =  abaqusOutputRequests.Add("ABQFIELD")

        :param int i_output_request_type: enum abq_output_request_type
        :rtype: ABQOutputRequest
        """
        return ABQOutputRequest(self.abq_output_requests.Add(i_output_request_type))

    def item(self, i_index: cat_variant, i_output_request_type: int) -> ABQOutputRequest:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex,
                | ABQOutputRequestType iOutputRequestType) As ABQOutputRequest
                | 
                |     Returns an Abaqus output request using its index or its name and output
                |     request type from the ABQOutputRequests collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus output request to retrieve from
                |             the collection of Abaqus output requests. 
                |         iOutputRequestType
                |             The type of the output request.
                | 
                |             Legal values:
                | 
                |             "ABQFIELD"
                |             "ABQHISTORY"
                |             "ABQDATA
                | 
                |             If the index is a number, it specifies the rank of the Abaqus
                |             output request corresponding to the specified output request type in the
                |             collection. The index of the first Abaqus output request in the collection is 1
                |             and the index of the last output request is Count. If the index is a string, it
                |             specifies the name you assigned to the output request using the
                |             CATIACollection::Name property. 
                | 
                |     Returns:
                |         The specified ABQOutputRequest.

        :param cat_variant i_index:
        :param int i_output_request_type: enum abq_output_request_type
        :rtype: ABQOutputRequest
        """
        return ABQOutputRequest(self.abq_output_requests.Item(i_index, i_output_request_type))

    def remove(self, i_index: cat_variant, i_output_request_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex,
                | ABQOutputRequestType iOutputRequestType)
                | 
                |     Removes a Abaqus output request using its index or its name and output
                |     request type from the collection output requests.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Abaqus output request to retrieve from
                |             the collection of Abaqus output requests. 
                |         iOutputRequestType
                |             The type of the output request.
                | 
                |             Legal values:
                | 
                |             "ABQFIELD"
                |             "ABQHISTORY"
                |             "ABQDATA
                | 
                |             If the index is a number, it specifies the rank of the Abaqus
                |             output request corresponding to the specified output request type in the
                |             collection. The index of the first Abaqus output request in the collection is 1
                |             and the index of the last output request is Count. If the index is a string, it
                |             specifies the name you assigned to the output request using the
                |             CATIACollection::Name property.

        :param cat_variant i_index:
        :param int i_output_request_type: enum abq_output_request_type
        :rtype: None
        """
        return self.abq_output_requests.Remove(i_index, i_output_request_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(abq_output_requests)
        # #     Dim iIndex (2)
        # #     abq_output_requests.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQOutputRequests(name="{self.name}")'
