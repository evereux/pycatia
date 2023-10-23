#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_doubles import PSPListOfDoubles
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class PSPLightConnector(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspLightConnector
                | 
                | Represents the light connector.
                | Role: To access light connector data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_light_connector = com_object

    def get_alignment_vector(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAlignmentVector(Product iRelAxis) As
                | PspListOfDoubles
                | 
                |     Returns the position of the connector.
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
                |          Dim objThisIntf As PspLightConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetAlignmentVector (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_light_connector.GetAlignmentVector(i_rel_axis.com_object))

    def get_orientation_vector(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOrientationVector(Product iRelAxis) As
                | PspListOfDoubles
                | 
                |     Returns the Orientation Direction of the connector.
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
                |          Dim objThisIntf As PspLightConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetOrientationVector (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_light_connector.GetOrientationVector(i_rel_axis.com_object))

    def get_origin(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOrigin(Product iRelAxis) As PspListOfDoubles
                | 
                |     Returns the position of the connector.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             the relative axis object (Nothing means relative to parent)
                |             
                |         oOrigin
                |             Origin point position-three double values stand for x,y,z
                |
                |     Example:
                |
                |          Dim objThisIntf As PspLightConnector
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.GetOrigin (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_light_connector.GetOrigin(i_rel_axis.com_object))

    def set_alignment_vector(self, i_rel_axis: Product, i_alignment_direction: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAlignmentVector(Product iRelAxis,
                | CATSafeArrayVariant iAlignmentDirection)
                | 
                |     Sets the alignment direction of the connector.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             the relative axis object (Nothing means relative to parent)
                |             
                |         iAlignmentDirection
                |             Three double values stand for X,Y,Z component of the Alignment
                |             vector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspLightConnector
                |          Dim objArg1 As  Product
                |          Dim dbVar2(2) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetAlignmentVector objArg1, dbVar2

        :param Product i_rel_axis:
        :param tuple i_alignment_direction:
        :rtype: tuple
        """
        return self.psp_light_connector.SetAlignmentVector(i_rel_axis.com_object, i_alignment_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_alignment_vector'
        # # vba_code = """
        # # Public Function set_alignment_vector(psp_light_connector)
        # #     Dim iRelAxis (2)
        # #     psp_light_connector.SetAlignmentVector iRelAxis
        # #     set_alignment_vector = iRelAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_orientation_vector(self, i_rel_axis: Product, i_orientation_direction: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOrientationVector(Product iRelAxis,
                | CATSafeArrayVariant iOrientationDirection)
                | 
                |     Sets the Orientation Direction of the connector.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             the relative axis object (Nothing means relative to parent)
                |             
                |         iAlignmentDirection
                |             Three double values stand for X,Y,Z component of the Alignment
                |             vector 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspLightConnector
                |          Dim objArg1 As  Product
                |          Dim dbVar2(2) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetAlignmentVector objArg1, dbVar2

        :param Product i_rel_axis:
        :param tuple i_orientation_direction:
        :rtype: tuple
        """
        return self.psp_light_connector.SetOrientationVector(i_rel_axis.com_object, i_orientation_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_orientation_vector'
        # # vba_code = """
        # # Public Function set_orientation_vector(psp_light_connector)
        # #     Dim iRelAxis (2)
        # #     psp_light_connector.SetOrientationVector iRelAxis
        # #     set_orientation_vector = iRelAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_origin(self, i_rel_axis: Product, i_db3_position: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOrigin(Product iRelAxis,
                | CATSafeArrayVariant iDb3Position)
                | 
                |     Sets the position of the connector.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             the relative axis object (Nothing means relative to parent)
                |             
                |         iDb3Position
                |             absolute X-Y-Z coordinates of the current position of the connector
                |             to be set 
                | 
                |     Example:
                |
                |          Dim objThisIntf As PspLightConnector
                |          Dim objArg1 As  Product
                |          Dim dbVar2(3) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetOrigin objArg1, dbVar2

        :param Product i_rel_axis:
        :param tuple i_db3_position:
        :rtype: tuple
        """
        return self.psp_light_connector.SetOrigin(i_rel_axis.com_object, i_db3_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_origin'
        # # vba_code = """
        # # Public Function set_origin(psp_light_connector)
        # #     Dim iRelAxis (2)
        # #     psp_light_connector.SetOrigin iRelAxis
        # #     set_origin = iRelAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PSPLightConnector(name="{self.name}")'
