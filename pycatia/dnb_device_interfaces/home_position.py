#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class HomePosition(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HomePosition
                | 
                | Interface representing a device's Home Position.
                | 
                | Role: This interface is used to interact with a device's home positions. This
                | includes devices created in using V5 mechanisms or imported from DENEB
                | D5.
                | A home position is a list of values, each value being associated to each
                | Degrees Of Freedom(DOF) of the device, defining a state for the device (The
                | list size matches the number of commands that can be
                | simulated).
                | 
                | With home positions, it is possible to define Tool tips. A Tool tip is a
                | specific device part meant to be in contact with product(s). User may define
                | some device parts as tool tips so that, when they are in collision, the clash
                | is ignored. Tool tips are excluded from clash analysis in tools like DPM
                | Body-in-White's weldgun search.
                | 
                | The following code snippet can be used to obtain a home position from a
                | device.
                | 
                |    Dim objDevice As BasicDevice
                |    set objDevice = CATIA.ActiveDocument.Product.GetTechnologicalObject("BasicDevice")
                |    Dim ListOfHomePositions()
                |    objDevice.GetHomePositions ListOfHomePositions
                |    Dim homePos as HomePosition
                |    For Each homePos In ListOfHomePositions
                |       ...
                |    Next
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.home_position = com_object

    def get_associated_tool_tip(self, o_tip_list: tuple) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAssociatedToolTip(CATSafeArrayVariant oTipList)
                | 
                |     Get the tooltips associated with the home position.
                | 
                |     Parameters:
                | 
                |         oTipList
                |             This out parameter contains list of tooltips associated with the
                |             home position. The list contains a set of device parts.
                |
                |     Example:
                |
                |            ' declaration of 1 list of products and 1 home
                |            position
                |            Dim MyToolTips() As Product
                |            Dim MyHomePosition As HomePosition
                | 
                |            ' valuation of variables
                |            Set MyHomePosition = ...
                | 
                |            ' retrieval of tool tips as part of product array
                |            MyHomePosition.GetAssociatedToolTip( MyToolTips )
                | 
                |            ' start a loop displaying the name of each tool tip
                |            For Each toolTip In toolTips
                |                'warning: MsgBox is a modal dialog: it requires user
                |                interactions!!
                |                MsgBox toolTip.PartNumber = ...
                |            Next

        :param tuple o_tip_list:
        :return: Product
        :rtype: Product
        """
        return Product(self.home_position.GetAssociatedToolTip(o_tip_list))
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_associated_tool_tip'
        # # vba_code = """
        # # Public Function get_associated_tool_tip(home_position)
        # #     Dim oTipList (2)
        # #     home_position.GetAssociatedToolTip oTipList
        # #     get_associated_tool_tip = oTipList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_dof_values(self, o_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDOFValues(CATSafeArrayVariant oValues)
                | 
                |     Get the DOF values for the home position.
                | 
                |     Parameters:
                | 
                |         oValues
                |             This contains a list of the current DOF values. Please note that
                |             values are expressed as:
                | 
                |                 meters for length values
                |                 radians for angle values
                | 
                |             angles in radians. 
                | 
                |     Example:
                |
                |            Dim objDevice As BasicDevice
                |            set objDevice = CATIA.ActiveDocument.Product.GetTechnologicalObject("BasicDevice")
                |            Dim ListOfHomePositions() 
                |            objDevice.GetHomePositions ListOfHomePositions
                |            Dim homePos as HomePosition  
                |            'define an empty array to store the values
                |            Dim DOFValues ()
                |            For Each homePos In ListOfHomePositions
                |               homePos.GetDOFValues DOFValues 
                |               For i = 0 to ubound (DOFValues)
                |                  ...
                |               Next
                |            Next

        :param tuple o_values:
        :return: None
        :rtype: None
        """
        return self.home_position.GetDOFValues(o_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_dof_values'
        # # vba_code = """
        # # Public Function get_dof_values(home_position)
        # #     Dim oValues (2)
        # #     home_position.GetDOFValues oValues
        # #     get_dof_values = oValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_associated_tool_tip(self, i_tip_list: tuple) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAssociatedToolTip(CATSafeArrayVariant iTipList)
                | 
                |     Set the tool tip associated with the home position.
                | 
                |     Parameters:
                | 
                |         iTipList
                |             This parameter contains list of associated tooltips (device parts
                |             meant to be ignored during clash analysis). 
                | 
                |     Example:
                |
                |            ' declaration of 2 products and 1 home position
                |            Dim MyPart1 As Product
                |            Dim MyPart2 As Product
                |            Dim MyHomePosition As HomePosition
                | 
                |            ' valuation of variables
                |            Set MyPart1 = ...
                |            Set MyPart2 = ...
                |            Set MyHomePosition = ...
                | 
                |            ' defining the tool tips through an array
                |            Dim MyToolTips(1) As Product
                |            Set MyToolTips(0) = MyPart1
                |            Set MyToolTips(1) = MyPart2
                |            MyHomePosition.SetAssociatedToolTip( MyToolTips )

        :param tuple i_tip_list:
        :return: Product
        :rtype: Product
        """
        return Product(self.home_position.SetAssociatedToolTip(i_tip_list))
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_associated_tool_tip'
        # # vba_code = """
        # # Public Function set_associated_tool_tip(home_position)
        # #     Dim iTipList (2)
        # #     home_position.SetAssociatedToolTip iTipList
        # #     set_associated_tool_tip = iTipList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dof_values(self, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDOFValues(CATSafeArrayVariant iValues)
                | 
                |     Set the DOF values for the home position.
                | 
                |     Parameters:
                | 
                |         oValues
                |             This contains a list of the current DOF values. Please note that
                |             values are expressed as:
                | 
                |                 meters for length values
                |                 radians for angle values
                | 
                |     Example:
                |
                |            Dim DOFValues (6)
                |            For i = 0 to 5
                |               'Store value in radians
                |               DOFValues(i) = 10 * i * (pi / 180.0)
                |            next
                |            'Note: to obtain homePos, please refer to example in
                |            GetDOFValues
                |            homePos.SetDOFValues DOFValues

        :param tuple i_values:
        :return: None
        :rtype: None
        """
        return self.home_position.SetDOFValues(i_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dof_values'
        # # vba_code = """
        # # Public Function set_dof_values(home_position)
        # #     Dim iValues (2)
        # #     home_position.SetDOFValues iValues
        # #     set_dof_values = iValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HomePosition(name="{self.name}")'