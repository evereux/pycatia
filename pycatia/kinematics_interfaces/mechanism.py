#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.kinematics_interfaces.joint import Joint
from pycatia.kinematics_interfaces.joints import Joints
from pycatia.kinematics_interfaces.mechanism_command import MechanismCommand
from pycatia.kinematics_interfaces.mechanism_commands import MechanismCommands
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class Mechanism(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Mechanism
                | 
                | Interface to access the Mechanism object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mechanism = com_object

    @property
    def commands(self) -> MechanismCommands:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Commands() As MechanismCommands (Read Only)
                | 
                |     Returns the collection of commands in the mechanism.
                | 
                |     Parameters:
                | 
                |         oCommands
                |             The collection of commands. This property is read only because
                |             because list is aggregated in the Mechanism

        :rtype: MechanismCommands
        """

        return MechanismCommands(self.mechanism.Commands)

    @property
    def fixed_part(self) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FixedPart() As Product
                | 
                |     Returns or sets the fixed part of the mechanism.
                | 
                |     Parameters:
                | 
                |         oFixedPart
                |             The fixed part.

        :rtype: Product
        """

        return Product(self.mechanism.FixedPart)

    @fixed_part.setter
    def fixed_part(self, value: Product):
        """
        :param Product value:
        """

        self.mechanism.FixedPart = value

    @property
    def joints(self) -> Joints:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Joints() As Joints (Read Only)
                | 
                |     Returns the collection of joints in the mechanism.
                | 
                |     Parameters:
                | 
                |         oJoints
                |             The collection of joints. This property is read only because
                |             because list is aggregated in the Mechanism

        :rtype: Joints
        """

        return Joints(self.mechanism.Joints)

    @property
    def nb_commands(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbCommands() As long (Read Only)
                | 
                |     Returns the number of commands in the mechanism.
                | 
                |     Parameters:
                | 
                |         oNbCommands
                |             The number of commands. This property is read only because number
                |             depends on commands creation/destruction

        :rtype: int
        """

        return self.mechanism.NbCommands

    @property
    def nb_dof(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbDof() As long (Read Only)
                | 
                |     Returns the degree of freedom of the mechanism.
                | 
                |     Parameters:
                | 
                |         oNbDof
                |             The degree of freedom. This property is read only because because
                |             it depends on joints and commands

        :rtype: int
        """

        return self.mechanism.NbDof

    @property
    def nb_joints(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbJoints() As long (Read Only)
                | 
                |     Returns the number of joints in the mechanism.
                | 
                |     Parameters:
                | 
                |         oNbJoints
                |             The number of joints. This property is read only because number
                |             depends on joints creation/destruction

        :rtype: int
        """

        return self.mechanism.NbJoints

    @property
    def nb_products(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property NbProducts() As long (Read Only)
                | 
                |     Returns the number of products (i.e. bodies) involved in the
                |     mechanism.
                | 
                |     Parameters:
                | 
                |         oNbProducts
                |             The number of products. This property is read only because number
                |             depends on joints creation/destruction

        :rtype: int
        """

        return self.mechanism.NbProducts

    def add_command(self, i_cmd_type: str, i_joint: Joint) -> MechanismCommand:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddCommand(CATBSTR iCmdType,
                | Joint iJoint) As MechanismCommand
                | 
                |     Adds a command in the mechanism, on a joint.
                | 
                |     Parameters:
                | 
                |         iCmdType
                |             The command type. 
                |         iJoint
                |             The joint to be driven. 
                |         oNewCommand
                |             The newly created command.

        :param str i_cmd_type:
        :param Joint i_joint:
        :rtype: MechanismCommand
        """
        return MechanismCommand(self.mechanism.AddCommand(i_cmd_type, i_joint.com_object))

    def add_joint(self, i_joint_type: str, i_list_elem: tuple) -> Joint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddJoint(CATBSTR iJointType,
                | CATSafeArrayVariant iListElem) As Joint
                | 
                |     Adds a joint in the mechanism.
                | 
                |     Parameters:
                | 
                |         iJointType
                |             The joint type. 
                |         iListElem
                |             The list of elements expected to locate the joint, depending on the
                |             type. 
                |         oNewJoint
                |             The newly created joint.

        :param str i_joint_type:
        :param tuple i_list_elem:
        :rtype: Joint
        """
        return Joint(self.mechanism.AddJoint(i_joint_type, i_list_elem))

    def get_command_values(self, io_cmd_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCommandValues(CATSafeArrayVariant ioCmdValues)
                | 
                |     Allows to retrieve current state of the mechanism.
                | 
                |     Parameters:
                | 
                |         ioCmdValues
                |             current command values

        :param tuple io_cmd_values:
        :rtype: None
        """
        return self.mechanism.GetCommandValues(io_cmd_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_command_values'
        # # vba_code = """
        # # Public Function get_command_values(mechanism)
        # #     Dim ioCmdValues (2)
        # #     mechanism.GetCommandValues ioCmdValues
        # #     get_command_values = ioCmdValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_product(self, i_index: int) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProduct(long iIndex) As Product
                | 
                |     Returns an item from the list of the products involved in the
                |     mechanism.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index for the product. 
                |         oProduct
                |             The product at that index. 
                | 
                |     Returns:
                |         HRESULT

        :param int i_index:
        :rtype: Product
        """
        return Product(self.mechanism.GetProduct(i_index))

    def get_product_motion(self, i_product: Product, io_motion: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProductMotion(Product iProduct,
                | CATSafeArrayVariant ioMotion)
                | 
                |     Retrieves motion from initial state to current state for a part of the
                |     mechanism.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The moving product 
                |         ioMotion
                |             The motion matrix (12 real values, compatible with the Move object)
                |             
                | 
                |     See also:
                |         Move

        :param Product i_product:
        :param tuple io_motion:
        :rtype: None
        """
        return self.mechanism.GetProductMotion(i_product.com_object, io_motion)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_product_motion'
        # # vba_code = """
        # # Public Function get_product_motion(mechanism)
        # #     Dim iProduct (2)
        # #     mechanism.GetProductMotion iProduct
        # #     get_product_motion = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_command_values(self, i_cmd_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutCommandValues(CATSafeArrayVariant iCmdValues)
                | 
                |     Triggers immediate mechanism solving (motion is NOT applied to the
                |     model).
                | 
                |     Parameters:
                | 
                |         iCmdValues
                |             command values to be solved for

        :param tuple i_cmd_values:
        :rtype: None
        """
        return self.mechanism.PutCommandValues(i_cmd_values)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_command_values'
        # # vba_code = """
        # # Public Function put_command_values(mechanism)
        # #     Dim iCmdValues (2)
        # #     mechanism.PutCommandValues iCmdValues
        # #     put_command_values = iCmdValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_command_values_with_multi_steps(self, i_cmd_values: tuple, i_nb_steps: int, o_step_reached: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutCommandValuesWithMultiSteps(CATSafeArrayVariant
                | iCmdValues,
                | long iNbSteps,
                | long oStepReached)
                | 
                |     Puts command values in given number of steps. Visualization is updated
                |     after every step.
                | 
                |     Parameters:
                | 
                |         iCmdValues
                |             Array of target command values (position to achieve)
                |             
                |         inbSteps
                |             Number of steps in witch the target command value is to be
                |             reached.
                |             Legal values
                | 
                |             inbSteps greater than 0
                |                 Number of step must be greater than zero. 
                |             oStepReached
                |                 Number of steps reached successfully.

        :param tuple i_cmd_values:
        :param int i_nb_steps:
        :param int o_step_reached:
        :rtype: None
        """
        return self.mechanism.PutCommandValuesWithMultiSteps(i_cmd_values, i_nb_steps, o_step_reached)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_command_values_with_multi_steps'
        # # vba_code = """
        # # Public Function put_command_values_with_multi_steps(mechanism)
        # #     Dim iCmdValues (2)
        # #     mechanism.PutCommandValuesWithMultiSteps iCmdValues
        # #     put_command_values_with_multi_steps = iCmdValues
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reset_cmd_value_to_zero(self, i_command: MechanismCommand) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetCmdValueToZero(MechanismCommand iCommand)
                | 
                |     Sets the command value to zero for the given command without disturbing
                |     part positions.
                | 
                |     Parameters:
                | 
                |         iCommand
                |             The command to reset to zero

        :param MechanismCommand i_command:
        :rtype: None
        """
        return self.mechanism.ResetCmdValueToZero(i_command.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'reset_cmd_value_to_zero'
        # # vba_code = """
        # # Public Function reset_cmd_value_to_zero(mechanism)
        # #     Dim iCommand (2)
        # #     mechanism.ResetCmdValueToZero iCommand
        # #     reset_cmd_value_to_zero = iCommand
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Update()
                | 
                |     Reassembles the mechanism after dimension changes in the parts.

        :rtype: None
        """
        return self.mechanism.Update()

    def __repr__(self):
        return f'Mechanism(name="{self.name}")'
