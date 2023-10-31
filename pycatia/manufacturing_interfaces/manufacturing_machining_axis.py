#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_feature import ManufacturingFeature
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingMachiningAxis(ManufacturingFeature):
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
                |                         ManufacturingMachiningAxis
                | 
                | ManufacturingMachiningAxis defines a set of methods to manage a Machining Axis
                | System or an Origin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_machining_axis = com_object

    @property
    def origin(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Origin() As short
                | 
                |     This property returns the interface which manages if instruction os used as
                |     an Origin or as a Machining Axis System. If instruction is an Origin, Origin is
                |     set to 1, 0 otherwise.
                | 
                |     Example:
                |         The following example returns in origin the attribute to provide if
                |         instruction is used as a Machining Axis System or an Origin
                |         :
                | 
                |          ...
                |          Set myInstruction  = ... 
                |          Set MyOrigin = myInstruction.Origin

        :rtype: int
        """

        return self.manufacturing_machining_axis.Origin

    @origin.setter
    def origin(self, value: int):
        """
        :param int value:
        """

        self.manufacturing_machining_axis.Origin = value

    @property
    def origin_group(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OriginGroup() As short
                | 
                |     This property returns the interface which determines the origin group of
                |     the instruction if used a an Origin.
                | 
                |     Example:
                |         The following example set the Origin Group to 5.
                | 
                |          ...
                |          Set myInstruction  = ... 
                |          Set myInstruction.OriginGroup = 3

        :rtype: int
        """

        return self.manufacturing_machining_axis.OriginGroup

    @origin_group.setter
    def origin_group(self, value: int):
        """
        :param int value:
        """

        self.manufacturing_machining_axis.OriginGroup = value

    @property
    def origin_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OriginNumber() As short
                | 
                |     This property returns the interface which manages the origin number of the
                |     instruction if used a an Origin.
                | 
                |     Example:
                |         The following example set the Origin Number to 3.
                | 
                |          ...
                |          Set myInstruction  = ... 
                |          Set myInstruction.OriginNumber = 3

        :rtype: int
        """

        return self.manufacturing_machining_axis.OriginNumber

    @origin_number.setter
    def origin_number(self, value: int):
        """
        :param int value:
        """

        self.manufacturing_machining_axis.OriginNumber = value

    def get_origin_point(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOriginPoint(double x,
                | double y,
                | double z)
                | 
                |     Gets the Origin of a Manufacturing Machining Axis System used as
                |     Origin.
                | 
                |     Example:
                |         The following example gets MfgAxisSystem with PointOrigin as an Origin
                |         Point and with ProductOrigin a belonging product.
                | 
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          Dim PointOrigin As CATSafeArrayVariant
                |          Dim ProductOrigin As Product
                |          MfgAxisSystem.GetOriginPoint (PointOrigin)

        :rtype: tuple
        """
        return self.manufacturing_machining_axis.GetOriginPoint()

    def get_origin_x_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOriginXDirection(double x,
                | double y,
                | double z)
                | 
                |     Gets the Origin X direction of a Manufacturing Machining Axis System used
                |     as Origin.
                | 
                |     Example:
                |         The following example gets MfgAxisSystem with origin X direction in
                |         DblMathDirection.
                | 
                |          Dim DlbMathDirection As Double(3)
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          MfgAxisSystem.GetOriginXDirection (DblMathDirection)

        :rtype: tuple
        """
        return self.manufacturing_machining_axis.GetOriginXDirection()

    def get_origin_y_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOriginYDirection(double x,
                | double y,
                | double z)
                | 
                |     Gets the Origin Y direction of a Manufacturing Machining Axis System used
                |     as Origin.
                | 
                |     Example:
                |         The following example gets MfgAxisSystem with origin Y direction in
                |         DblMathDirection.
                | 
                |          Dim DlbMathDirection As Double(3)
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          MfgAxisSystem.GetOriginYDirection (DblMathDirection)

        :rtype: tuple
        """
        return self.manufacturing_machining_axis.GetOriginYDirection()

    def get_origin_z_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOriginZDirection(double x,
                | double y,
                | double z)
                | 
                |     Gets the Origin Z direction of a Manufacturing Machining Axis System used
                |     as Origin.
                | 
                |     Example:
                |         The following example gets MfgAxisSystem with origin Z direction in
                |         DblMathDirection.
                | 
                |          Dim x,y,z As Double
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          MfgAxisSystem.GetOriginZDirection (x,y,z)

        :rtype: tuple
        """
        return self.manufacturing_machining_axis.GetOriginZDirection()

    def set_origin_point(self, i_point: AnyObject, i_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOriginPoint(AnyObject iPoint,
                | AnyObject iProduct)
                | 
                |     Sets the Origin of a Manufacturing Machining Axis System used as
                |     Origin.
                | 
                |     Example:
                |         The following example sets MfgAxisSystem with PointOrigin as an Origin
                |         Point and with ProductOrigin a belonging product.
                | 
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          Dim PointOrigin As AnyObject
                |          Dim ProductOrigin As Product
                |          MfgAxisSystem.SetOriginPoint
                |          (PointOrigin,ProductOrigin)

        :param AnyObject i_point:
        :param AnyObject i_product:
        :rtype: None
        """
        return self.manufacturing_machining_axis.SetOriginPoint(i_point.com_object, i_product.com_object)

    def set_origin_point_by_coordinates(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOriginPointByCoordinates(double x,
                | double y,
                | double z)
                | 
                |     Sets the Origin of a Manufacturing Machining Axis System used as Origin by
                |     coordinates.
                | 
                |     Example:
                |         The following example sets the Origin MfgAxisSystem at coordinates
                |         x,y,z.
                | 
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          MfgAxisSystem.SetOriginPointByCoordinates(x,y,z)

        :param float x:
        :param float y:
        :param float z:
        :rtype: None
        """
        return self.manufacturing_machining_axis.SetOriginPointByCoordinates(x, y, z)

    def set_origin_x_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOriginXDirection(double x,
                | double y,
                | double z)
                | 
                |     Sets the Origin X direction of a Manufacturing Machining Axis System used
                |     as Origin.
                | 
                |     Example:
                |         The following example sets MfgAxisSystem with origin X direction in
                |         DblMathDirection.
                | 
                |          Dim DlbMathDirection As Double(3)
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          MfgAxisSystem.SetOriginXDirection (DblMathDirection)

        :param float x:
        :param float y:
        :param float z:
        :rtype: None
        """
        return self.manufacturing_machining_axis.SetOriginXDirection(x, y, z)

    def set_origin_z_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOriginZDirection(double x,
                | double y,
                | double z)
                | 
                |     Sets the Origin Z direction of a Manufacturing Machining Axis System used
                |     as Origin.
                | 
                |     Example:
                |         The following example sets MfgAxisSystem with origin Y direction in
                |         DblMathDirection.
                | 
                |          Dim x,y,z As Double
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          MfgAxisSystem.SetOriginZDirection (x,y,z)

        :param float x:
        :param float y:
        :param float z:
        :rtype: None
        """
        return self.manufacturing_machining_axis.SetOriginZDirection(x, y, z)

    def set_part_axis_system(self, i_pas: AnyObject, i_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPartAxisSystem(AnyObject iPAS,
                | AnyObject iProduct)
                | 
                |     Sets the Part Axis System of a Manufacturing Machining Axis
                |     System.
                | 
                |     Example:
                |         The following example sets MfgAxisSystem with PAS as a Part Axis System
                |         and with ProductPAS a belonging product.
                | 
                |          Dim MfgAxisSystem As ManufacturingMachiningAxis
                |          Set MfgAxisSystem = ...
                |          Dim PAS As AxisSystem
                |          Dim PASProduct As Product
                |          MfgAxisSystem.SetMachiningAxisSystem (PAS,PASProduct)

        :param AnyObject i_pas:
        :param AnyObject i_product:
        :rtype: None
        """
        return self.manufacturing_machining_axis.SetPartAxisSystem(i_pas.com_object, i_product.com_object)

    def __repr__(self):
        return f'ManufacturingMachiningAxis(name="{self.name}")'
