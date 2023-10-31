#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_objects import PSPListOfObjects
from pycatia.cat_plant_ship_interfaces.psp_part_connector import PSPPartConnector
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject


class PSPPhsyicalProduct(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspPhsyicalProduct
                | 
                | Represents the interface to manage the technological connectors on physical
                | objects.
                | Role: To manage connectors on physical objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_phsyical_product = com_object

    @property
    def connectors(self) -> PSPListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Connectors() As PspListOfObjects (Read Only)
                | 
                |     Returns a list of Part connectors of the object.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPhsyicalProduct  
                |          Dim objArg1 As PspListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.Connectors

        :rtype: PSPListOfObjects
        """

        return PSPListOfObjects(self.psp_phsyical_product.Connectors)

    def add_connector(
            self,
            i_class_filter: str,
            i_face_cntr: Reference,
            ie_face_type: int,
            i_alignment_cntr: Reference,
            ie_align_type: int,
            i_clock_cntr: Reference,
            ie_clock_type: int
    ) -> PSPPartConnector:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddConnector(CATBSTR iClassFilter,
                | Reference iFaceCntr,
                | CatPspIDLPartConnectorType ieFaceType,
                | Reference iAlignmentCntr,
                | CatPspIDLPartConnectorType ieAlignType,
                | Reference iClockCntr,
                | CatPspIDLPartConnectorType ieClockType) As PspPartConnector
                | 
                |     Returns the added connector on the object.
                | 
                |     Parameters:
                | 
                |         iuClassFilter
                |             Connector class type. If null string application default connector
                |             class will be used. 
                |         iFaceCntr
                |             A face connector 
                |         ieFaceType
                |             Face connector type 
                |         iAlignmentCntr
                |             An alignment connector 
                |         ieAlignType
                |             Alignment connector type 
                |         iClockCntr
                |             A clock connector 
                |         ieClockType
                |             A clock connector type 
                | 
                |     Returns:
                |         Part connector added
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPhsyicalProduct
                |          Dim strVar1 As CATBSTR
                |          Dim objArg2 As Reference
                |          Dim objArg3 As catPspIDLPartConnectorType
                |          Dim objArg4 As Reference
                |          Dim objArg5 As catPspIDLPartConnectorType
                |          Dim objArg6 As Reference
                |          Dim objArg7 As catPspIDLPartConnectorType
                |          Dim objArg8 As PspPartConnector
                |           ...
                |          objArg8 = objThisIntf.AddConnector (strVar1, objArg2,objArg3,objArg4, objArg5,objArg6,objArg7 )

        :param str i_class_filter:
        :param Reference i_face_cntr:
        :param int ie_face_type: enum cat_psp_idl_part_connector_type
        :param Reference i_alignment_cntr:
        :param int ie_align_type: enum cat_psp_idl_part_connector_type
        :param Reference i_clock_cntr:
        :param int ie_clock_type: enum cat_psp_idl_part_connector_type
        :rtype: PSPPartConnector
        """
        return PSPPartConnector(
            self.psp_phsyical_product.AddConnector(
                i_class_filter,
                i_face_cntr.com_object,
                ie_face_type,
                i_alignment_cntr.com_object,
                ie_align_type,
                i_clock_cntr.com_object,
                ie_clock_type
            )
        )

    def remove_connector(self, i_cntr_to_remove: PSPPartConnector) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveConnector(PspPartConnector iCntrToRemove)
                | 
                |     Removes part connector.
                | 
                |     Parameters:
                | 
                |         iCntrToRemove
                |             Part connector to be removed 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPhsyicalProduct
                |          Dim objArg1 As PspPartConnector
                |           ...
                |          objThisIntf.RemoveConnector objArg1

        :param PSPPartConnector i_cntr_to_remove:
        :rtype: None
        """
        return self.psp_phsyical_product.RemoveConnector(i_cntr_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_connector'
        # # vba_code = """
        # # Public Function remove_connector(psp_phsyical_product)
        # #     Dim iCntrToRemove (2)
        # #     psp_phsyical_product.RemoveConnector iCntrToRemove
        # #     remove_connector = iCntrToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PSPPhsyicalProduct(name="{self.name}")'
