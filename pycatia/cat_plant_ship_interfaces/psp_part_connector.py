#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_bstrs import PSPListOfBSTRs
from pycatia.cat_plant_ship_interfaces.psp_list_of_doubles import PSPListOfDoubles
from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class PSPPartConnector(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspPartConnector
                | 
                | Represent the Part Connector to manage the technological data on
                | connectors.
                | Role: To access the technological data on connectors.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_part_connector = com_object

    @property
    def align_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AlignType() As CatPspIDLPartConnectorType (Read
                | Only)
                | 
                |     Returns the alignment type for this connector.
                | 
                |     See also:
                |         CatPspIDLPartConnectorType
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As CatPspIDLPartConnectorType
                |           ...
                |          objArg1 = objThisIntf.AlignType

        :return: enum cat_psp_idl_part_connector_type
        :rtype: int
        """

        return self.psp_part_connector.AlignType

    @property
    def attribute_names(self) -> PSPListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttributeNames() As PspListOfBSTRs
                | 
                |     Returns or sets a list of attribute names associated with this
                |     connector.
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim ojArg1 As PspListOfBSTRs
                |           ...
                |          Set ojArg1 = objThisIntf.AttributeNames

        :rtype: PSPListOfBSTRs
        """

        return PSPListOfBSTRs(self.psp_part_connector.AttributeNames)

    @attribute_names.setter
    def attribute_names(self, value: PSPListOfBSTRs):
        """
        :param PSPListOfBSTRs value:
        """

        self.psp_part_connector.AttributeNames = value

    @property
    def clock_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClockType() As CatPspIDLPartConnectorType (Read
                | Only)
                | 
                |     Returns the clocking type (how symmetric this end is) for this
                |     connector.
                | 
                |     See also:
                |         CatPspIDLPartConnectorType
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As CatPspIDLPartConnectorType
                |           ...
                |          objArg1 = objThisIntf.ClockType

        :return: enum cat_psp_idl_part_connector_type
        :rtype: int
        """

        return self.psp_part_connector.ClockType

    @property
    def face_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FaceType() As CatPspIDLPartConnectorType (Read
                | Only)
                | 
                |     Returns the face type (normal or "transparent" support) for this
                |     connector.
                | 
                |     Parameters:
                | 
                |         oFaceType
                |             The face type. 
                | 
                |     See also:
                |         CatPspIDLPartConnectorType
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As CatPspIDLPartConnectorType
                |           ...
                |          Set objArg1 = objThisIntf.FaceType

        :return: enum cat_psp_idl_part_connector_type
        :rtype: int
        """

        return self.psp_part_connector.FaceType

    def get_alignment_connector(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAlignmentConnector() As Reference
                | 
                |     Returns the Alignmnet connector.
                | 
                |     Parameters:
                | 
                |         oCntr
                |             Alignment connector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |           ...
                |          Set objArg1 = objThisIntf.GetAlignmentConnector

        :rtype: Reference
        """
        return Reference(self.psp_part_connector.GetAlignmentConnector())

    def get_alignment_direction(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAlignmentDirection(Product iRelAxis) As
                | PspListOfDoubles
                | 
                |     Retrieves the alignment direction outward normal to the face place
                |     position.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             the relative axis object (Nothing means relative to parent)
                |             
                |         oAlignmentDirection
                |             Three double values stand for X,Y,Z components of the alignment
                |             vector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetAlignmentVector (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_part_connector.GetAlignmentDirection(i_rel_axis.com_object))

    def get_connector_math_plane(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConnectorMathPlane(Product iRelAxis) As
                | PspListOfDoubles
                | 
                |     Returns the 9 doubles values for plane contains the connector position
                |     (plane origin), alignment direction (plane z-axis), and the up direction (plane
                |     y-axis). Nine double values stand for plane origin, and the two normalized
                |     vectors
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             The relative axis object (Nothing means relative to parent).
                |
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetConnectorMathPlane (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_part_connector.GetConnectorMathPlane(i_rel_axis.com_object))

    def get_datum_connector(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDatumConnector() As Reference
                | 
                |     Returns the Datum connector.
                | 
                |     Parameters:
                | 
                |         oCntr
                |             Orientation connector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |           ...
                |          Set objArg1 = objThisIntf.GetDatumConnector

        :rtype: Reference
        """
        return Reference(self.psp_part_connector.GetDatumConnector())

    def get_face_connector(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFaceConnector() As Reference
                | 
                |     Returns the face connector.
                | 
                |     Parameters:
                | 
                |         oCntr
                |             Face connector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |           ...
                |          Set objArg1 = objThisIntf.GetFaceConnector

        :rtype: Reference
        """
        return Reference(self.psp_part_connector.GetFaceConnector())

    def get_orientation_connector(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOrientationConnector() As Reference
                | 
                |     Get Orientation connector.
                | 
                |     Parameters:
                | 
                |         oCntr
                |             Orientation connector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |           ...
                |          Set objArg1 = objThisIntf.GetOrientationConnector

        :rtype: Reference
        """
        return Reference(self.psp_part_connector.GetOrientationConnector())

    def get_position(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPosition(Product iRelAxis) As PspListOfDoubles
                | 
                |     Returns the Position of the connector.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             The relative axis object (NULL means relative to parent).
                |             
                |         oPosition
                |             X-Y-Z coordinates of the part connector Three double values stand
                |             for x,y,z coordinates 
                | 
                |     Example:
                | 
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetPosition (objArg1 )

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_part_connector.GetPosition(i_rel_axis.com_object))

    def get_up_direction(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUpDirection(Product iRelAxis) As PspListOfDoubles
                | 
                |     Returns the UP direction of the connector.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             The relative axis object (Nothing means relative to parent).
                |             
                |         oUpDirection
                |             The connector face plane. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetUpDirection (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_part_connector.GetUpDirection(i_rel_axis.com_object))

    def set_alignment_connector(self, i_align_cntr: Reference, ie_align_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAlignmentConnector(Reference iAlignCntr,
                | CatPspIDLPartConnectorType ieAlignType)
                | 
                |     Sets the Face connector.
                | 
                |     Parameters:
                | 
                |         iAlignCntr
                |             Alignment connector 
                |         ieAlignType
                |             Alignment connector Type 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |          Dim objArg2 As CatPspIDLPartConnectorType
                |           ...
                |          objThisIntf.SetFaceConnector objArg1, objArg2

        :param Reference i_align_cntr:
        :param int ie_align_type: enum cat_psp_idl_part_connector_type
        :rtype: None
        """
        return self.psp_part_connector.SetAlignmentConnector(i_align_cntr.com_object, ie_align_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_alignment_connector'
        # # vba_code = """
        # # Public Function set_alignment_connector(psp_part_connector)
        # #     Dim iAlignCntr (2)
        # #     psp_part_connector.SetAlignmentConnector iAlignCntr
        # #     set_alignment_connector = iAlignCntr
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_datum_connector(self, i_datum_cntr: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDatumConnector(Reference iDatumCntr)
                | 
                |     Sets the Datum connector.
                | 
                |     Parameters:
                | 
                |         iDatumCntr
                |             Datum connector. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |           ...
                |          objThisIntf.SetDatumConnector objArg1

        :param Reference i_datum_cntr:
        :rtype: None
        """
        return self.psp_part_connector.SetDatumConnector(i_datum_cntr.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_datum_connector'
        # # vba_code = """
        # # Public Function set_datum_connector(psp_part_connector)
        # #     Dim iDatumCntr (2)
        # #     psp_part_connector.SetDatumConnector iDatumCntr
        # #     set_datum_connector = iDatumCntr
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_face_connector(self, i_face_cntr: Reference, ie_face_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFaceConnector(Reference iFaceCntr,
                | CatPspIDLPartConnectorType ieFaceType)
                | 
                |     Sets Face connector.
                | 
                |     Parameters:
                | 
                |         iFaceCntr
                |             Face connector 
                |         ieFaceType
                |             Face connector Type 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |          Dim objArg2 As CatPspIDLPartConnectorType
                |           ...
                |          objThisIntf.SetFaceConnector objArg1, objArg2

        :param Reference i_face_cntr:
        :param int ie_face_type: enum cat_psp_idl_part_connector_type
        :rtype: None
        """
        return self.psp_part_connector.SetFaceConnector(i_face_cntr.com_object, ie_face_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_face_connector'
        # # vba_code = """
        # # Public Function set_face_connector(psp_part_connector)
        # #     Dim iFaceCntr (2)
        # #     psp_part_connector.SetFaceConnector iFaceCntr
        # #     set_face_connector = iFaceCntr
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_orientation_connector(self, i_orient_cntr: Reference, ie_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOrientationConnector(Reference iOrientCntr,
                | CatPspIDLPartConnectorType ieOrientation)
                | 
                |     Sets Face connector.
                | 
                |     Parameters:
                | 
                |         iOrientCntr
                |             Alignment connector 
                |         ieOrientation
                |             Orientation connector Type 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspPartConnector
                |          Dim objArg1 As Reference
                |          Dim objArg2 As CatPspIDLPartConnectorType
                |           ...
                |          objThisIntf.SetOrientationConnector objArg1, objArg2

        :param Reference i_orient_cntr:
        :param int ie_orientation: enum cat_psp_idl_part_connector_type
        :rtype: None
        """
        return self.psp_part_connector.SetOrientationConnector(i_orient_cntr.com_object, ie_orientation)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_orientation_connector'
        # # vba_code = """
        # # Public Function set_orientation_connector(psp_part_connector)
        # #     Dim iOrientCntr (2)
        # #     psp_part_connector.SetOrientationConnector iOrientCntr
        # #     set_orientation_connector = iOrientCntr
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PSPPartConnector(name="{self.name}")'
