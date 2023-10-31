#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.manufacturing_interfaces.manufacturing_feature import ManufacturingFeature
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingPattern(ManufacturingFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                         ManufacturingPattern
                | 
                | The Manufacturing Pattern is a specialized feature used to machine the same
                | item several times at several positions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_pattern = com_object

    @property
    def tool_axis_strategy(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ToolAxisStrategy() As CATBSTR
                | 
                |     Returns or sets the Tool Axis Strategy of a Manufacturing
                |     Pattern.
                |     Legal values: The parameter name can be
                | 
                |     Fixed
                |     Variable
                |     NormalToPS
                | 
                | Examples:
                |     The following example returns the Tool Axis Strategy ThisToolAxisStrategy
                |     of the manufacturing pattern CurrentMfgPattern
                | 
                |      Dim ThisToolAxisStrategy As CATBSTR
                |      ThisToolAxisStrategy = CurrentMfgPattern.ToolAxisStrategy
                |      
                | 
                |     The next example sets the Tool Axis Strategy of the manufacturing pattern
                |     CurrentMfgPattern
                | 
                |      CurrentMfgPattern.ToolAxisStrategy = "Fixed"

        :rtype: str
        """

        return self.manufacturing_pattern.ToolAxisStrategy

    @tool_axis_strategy.setter
    def tool_axis_strategy(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_pattern.ToolAxisStrategy = value

    def activate_point(self, i_point_number: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ActivatePoint(short iPointNumber)
                | 
                |     Activates a point of a Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         iPointNumber
                |             The number of the point to activate.
                | 
                |             Example:
                |                 The following example activates the point number 2 of the
                |                 manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.ActivatePoint(2)

        :param int i_point_number:
        :rtype: None
        """
        return self.manufacturing_pattern.ActivatePoint(i_point_number)

    def add_part_surface(self, i_part_surface: AnyObject, i_product: Product, i_notify: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPartSurface(AnyObject iPartSurface,
                | Product iProduct,
                | short iNotify)
                | 
                |     Adds a Part Surface to the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         iPartSurface
                |             The part surface to be added. 
                |         iProduct
                |             The product containing the part surface to add. 
                |         iNotify
                |             The flag to specify if a refresh of the visualization is needed.
                |             Usually, this parameter is set to 1. In the case of a loop, it should be set to
                |             1 only on the last call of the method.
                |             Legal values: The parameter can be
                | 
                |             0
                |                 no notification is sent 
                |             1
                |                 a notification is sent 
                | 
                |             Example:
                |                 The following example adds the part surface 'TopPlane' to the
                |                 manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.AddPartSurface(TopPlane,Product1,1)

        :param AnyObject i_part_surface:
        :param Product i_product:
        :param int i_notify:
        :rtype: None
        """
        return self.manufacturing_pattern.AddPartSurface(i_part_surface.com_object, i_product.com_object, i_notify)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_part_surface'
        # # vba_code = """
        # # Public Function add_part_surface(manufacturing_pattern)
        # #     Dim iPartSurface (2)
        # #     manufacturing_pattern.AddPartSurface iPartSurface
        # #     add_part_surface = iPartSurface
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_position(self, i_position: AnyObject, i_product: Product, i_notify: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPosition(AnyObject iPosition,
                | Product iProduct,
                | short iNotify)
                | 
                |     Adds a position to the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position to be added.
                |             Legal values: The position can be a
                | 
                |             Design Hole
                |                 the point is the origin point of the hole 
                |             Design Pattern
                |                 points are retrieved from the design pattern 
                |             Point
                |                 the point coordinates are retrieved from the added point
                |                 
                |             Circle
                |                 the point is the center of the circle 
                | 
                |         iProduct
                |             The product containing the position to add. 
                |         iNotify
                |             The flag to specify if a refresh of the visualization is needed.
                |             Usually, this parameter is set to 1. In the case of a loop, it should be set to
                |             1 only on the last call of the method.
                |             Legal values: The parameter can be
                | 
                |             0
                |                 no notification is sent 
                |             1
                |                 a notification is sent 
                | 
                |             Example:
                |                 The following example adds the position 'DesignPattern1' to the
                |                 manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.AddPosition(DesignPattern1,Product1,1)

        :param AnyObject i_position:
        :param Product i_product:
        :param int i_notify:
        :rtype: None
        """
        return self.manufacturing_pattern.AddPosition(i_position.com_object, i_product.com_object, i_notify)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_position'
        # # vba_code = """
        # # Public Function add_position(manufacturing_pattern)
        # #     Dim iPosition (2)
        # #     manufacturing_pattern.AddPosition iPosition
        # #     add_position = iPosition
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def deactivate_point(self, i_point_number: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DeactivatePoint(short iPointNumber)
                | 
                |     Deactivates a point of a Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         iPointNumber
                |             The number of the point to deactivate.
                | 
                |             Example:
                |                 The following example deactivates the point number 2 of the
                |                 manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.DeactivatePoint(2)

        :param int i_point_number:
        :rtype: None
        """
        return self.manufacturing_pattern.DeactivatePoint(i_point_number)

    def get_an_attribute(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnAttribute(CATBSTR iAttribut) As Parameter
                | 
                |     Retreive the attribute of Manufacturing Pattern from its
                |     name.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The identifier of the attribute to be read.
                |             Legal values: The identifier can be
                | 
                |             JumpDistance
                |                 the jump distance of the pattern 
                |             TopMode
                |                 the Top Mode of the pattern 
                | 
                |             Example:
                |                 The following example retrieves the attribute 'JumpDistance' of
                |                 the manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.GetAnAttribute(JumpDistance,JumpParm)

        :param str i_attribute:
        :rtype: Parameter
        """
        return Parameter(self.manufacturing_pattern.GetAnAttribute(i_attribute))

    def get_local_tool_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLocalToolAxis(short iPointNumber,
                | double oX,
                | double oY,
                | double oZ)
                | 
                |     Retrieve the local tool axis of a point of a Manufacturing
                |     Pattern.
                | 
                |     Parameters:
                | 
                |         iPointNumber
                |             The number of the point on which the tool axis is set.
                |             
                |         oX
                |             The first coordinate of the tool axis. 
                |         oY
                |             The second coordinate of the tool axis. 
                |         oZ
                |             The third coordinate of the tool axis.
                | 
                |             Example:
                |                 The following example retrieves the tool axis of the point
                |                 number 3 of manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.GetLocalToolAxis(3,oX,oY,oZ)

        :rtype: tuple
        """
        return self.manufacturing_pattern.GetLocalToolAxis()

    def get_numbers(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetNumbers(CATSafeArrayVariant oNumbers)
                | 
                |     Retrieve the number of the points of a Manufacturing
                |     Pattern.
                | 
                |     Parameters:
                | 
                |         oNumbers
                |             The numbers of the points of the pattern.
                | 
                |             Example:
                |                 The following example retrieves the numbers of the points of
                |                 the manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.GetNumbers(oNumbers)

        :param tuple o_numbers:
        :rtype: None
        """
        return self.manufacturing_pattern.GetNumbers()
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_numbers'
        # # vba_code = """
        # # Public Function get_numbers(manufacturing_pattern)
        # #     Dim oNumbers (2)
        # #     manufacturing_pattern.GetNumbers oNumbers
        # #     get_numbers = oNumbers
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_part_surfaces(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePartSurfaces()
                | 
                |     Remove the Part Surfaces of the Manufacturing Pattern.
                | 
                |     Example:
                |         The following example removes the part surfaces of the manufacturing
                |         pattern mfgPattern:
                | 
                |          call mfgPattern.RemovePartSurfaces()

        :rtype: None
        """
        return self.manufacturing_pattern.RemovePartSurfaces()

    def reverse(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Reverse()
                | 
                |     Reverses the numbering of a Manufacturing Pattern.
                | 
                |     Example:
                |         The following example reverses the numbering of the manufacturing
                |         pattern mfgPattern:
                | 
                |          call mfgPattern.Reverse()

        :rtype: None
        """
        return self.manufacturing_pattern.Reverse()

    def set_item_to_copy(self, i_item: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetItemToCopy(AnyObject iItem)
                | 
                |     Sets the feature to be copied.
                | 
                |     Parameters:
                | 
                |         iItemToCopy
                |             The feature to be copied. It may be a Design Hole or a
                |             Manufacturing Hole.
                |             Legal values: The parameter name can be
                | 
                |             Diameter
                |                 The hole diameter 
                | 
                |         oParameter
                |             The value of the parameter
                | 
                |             Example:
                |                 The following example sets the item to copy 'Hole1' to the
                |                 manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.SetItemToCopy(Hole1)

        :param AnyObject i_item:
        :rtype: None
        """
        return self.manufacturing_pattern.SetItemToCopy(i_item.com_object)

    def set_local_tool_axis(self, i_point_number: int, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLocalToolAxis(short iPointNumber,
                | double iX,
                | double iY,
                | double iZ)
                | 
                |     Sets a local tool axis to a point of a Manufacturing
                |     Pattern.
                | 
                |     Parameters:
                | 
                |         iPointNumber
                |             The number of the point on which the tool axis is set .
                |             
                |         iX
                |             The first coordinate of the tool axis. 
                |         iY
                |             The second coordinate of the tool axis. 
                |         iZ
                |             The third coordinate of the tool axis.
                | 
                |             Example:
                |                 The following example sets the Z axis as tool axis of the point
                |                 number 3 of manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.SetLocalToolAxis(3,0,0,1)

        :param int i_point_number:
        :param float i_x:
        :param float i_y:
        :param float i_z:
        :rtype: None
        """
        return self.manufacturing_pattern.SetLocalToolAxis(i_point_number, i_x, i_y, i_z)

    def start_point(self, i_point_number: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub StartPoint(short iPointNumber)
                | 
                |     Sets a point of a Manufacturing Pattern as the start
                |     point.
                | 
                |     Parameters:
                | 
                |         iPointNumber
                |             The number of the point to set as start point.
                | 
                |             Example:
                |                 The following example sets the point number 2 as the start
                |                 point of the manufacturing pattern mfgPattern:
                | 
                |                  call mfgPattern.StartPoint(2)

        :param int i_point_number:
        :rtype: None
        """
        return self.manufacturing_pattern.StartPoint(i_point_number)

    def __repr__(self):
        return f'ManufacturingPattern(name="{self.name}")'
