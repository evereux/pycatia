#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.system_interfaces.any_object import AnyObject


class HybridShapeInstance(HybridShape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeInstance
                | 
                | The interface to access a CATIAHybridShapeInstance.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_instance = com_object

    @property
    def inputs_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InputsCount() As long (Read Only)
                | 
                |     Returns the number of Inputs.
                | 
                |     Example:
                |         The following example retrieves in inputsCount the number of Inputs of
                |         hybridShapeInstance:
                | 
                |          inputsCount = hybridShapeInstance.InputsCount

        :rtype: int
        """

        return self.hybrid_shape_instance.InputsCount

    @property
    def outputs_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OutputsCount() As long (Read Only)
                | 
                |     Returns the number of Outputs.
                | 
                |     Example:
                |         The following example retrieves in outputsCount the number of Outputs
                |         of hybridShapeInstance:
                | 
                |          outputsCount = hybridShapeInstance.OutputsCount

        :rtype: int
        """

        return self.hybrid_shape_instance.OutputsCount

    @property
    def parameters_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ParametersCount() As long (Read Only)
                | 
                |     Returns the number of Parameters.
                | 
                |     Example:
                |         The following example retrieves in parametersCount the number of
                |         parameters of hybridShapeInstance:
                | 
                |          parametersCount = hybridShapeInstance.ParametersCount

        :rtype: int
        """

        return self.hybrid_shape_instance.ParametersCount

    def get_input(self, i_index: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetInput(CATBSTR iIndex) As AnyObject
                | 
                |     Gets an input of a hybrid shape instance by its name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the input of the hybrid shape instance
                |             
                | 
                |     Returns:
                |         The input, if found 
                |     Example:
                |         The following example tests if the input was found:
                | 
                |          Set input = hybridShapeInstance.GetInput("Input1")
                |          If TypeName(input)="Nothing" Then
                |               MsgBox "Input not found"
                |          End If

        :param str i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.hybrid_shape_instance.GetInput(i_index))

    def get_input_data(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetInputData(CATBSTR iName) As CATBaseDispatch
                | 
                |     Gets an input of a shape instance by its name. Use this method if you want
                |     to retrieve a Reference.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the input of the shape instance 
                | 
                |     Returns:
                |         The input, if found 
                |     Example:
                |         The following example tests if the input was found:
                | 
                |          Set input = shapeInstance.GetInput("Input1")
                |          If TypeName(input)="Nothing" Then
                |               MsgBox "Input not found"
                |          End If

        :param str i_name:
        :rtype: AnyObject
        """
        return self.hybrid_shape_instance.GetInputData(i_name)

    def get_input_data_from_position(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetInputDataFromPosition(long iPosition) As
                | CATBaseDispatch
                | 
                |     Gets an input of a hybrid shape instance from its position. Use this method
                |     if you want to retrieve a Reference.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position 
                | 
                |     Returns:
                |         The input, if found 
                |     Example:
                |         The following example tests if the input was found:
                | 
                |          Set input = hybridShapeInstance.GetInputFromPosition(2)
                |          If TypeName(input)="Nothing" Then
                |               MsgBox "Input not found"
                |          End If

        :param int i_position:
        :rtype: AnyObject
        """
        return self.hybrid_shape_instance.GetInputDataFromPosition(i_position)

    def get_input_from_position(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetInputFromPosition(long iPosition) As AnyObject
                | 
                |     Gets an input of a hybrid shape instance from its
                |     position.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position 
                | 
                |     Returns:
                |         The input, if found 
                |     Example:
                |         The following example tests if the input was found:
                | 
                |          Set input = hybridShapeInstance.GetInputFromPosition(2)
                |          If TypeName(input)="Nothing" Then
                |               MsgBox "Input not found"
                |          End If

        :param int i_position:
        :rtype: AnyObject
        """
        return AnyObject(self.hybrid_shape_instance.GetInputFromPosition(i_position))

    def get_output(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOutput(CATBSTR iName) As AnyObject
                | 
                |     Gets a Ouput by its name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the output of the shape instance 
                | 
                |     Returns:
                |         The output, if found 
                |     Example:
                |         The following example tests if the output was found:
                | 
                |          Set output = shapeInstance.GetOuput("Output1")
                |          If TypeName(output)="Nothing" Then
                |               MsgBox "Output not found"
                |          End If

        :param str i_name:
        :rtype: AnyObject
        """
        return AnyObject(self.hybrid_shape_instance.GetOutput(i_name))

    def get_output_from_position(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOutputFromPosition(long iPosition) As AnyObject
                | 
                |     Gets a Ouput from its position.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position 
                | 
                |     Returns:
                |         The output, if found 
                |     Example:
                |         The following example tests if the output was found:
                | 
                |          Set output = shapeInstance.GetOuputFromPosition(2)
                |          If TypeName(output)="Nothing" Then
                |               MsgBox "Output not found"
                |          End If

        :param int i_position:
        :rtype: AnyObject
        """
        return AnyObject(self.hybrid_shape_instance.GetOutputFromPosition(i_position))

    def get_parameter(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetParameter(CATBSTR iName) As AnyObject
                | 
                |     Gets a parameter of a hybrid shape instance by its name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter of the hybrid shape instance
                |             
                | 
                |     Returns:
                |         The parameter, if found 
                |     Example:
                |         The following example tests if the parameter was
                |         found:
                | 
                |          Set parameter = hybridShapeInstance.GetParameter("Parameter1")
                |          If TypeName(parameter)="Nothing" Then
                |               MsgBox "Parameter not found"
                |          End If

        :param str i_name:
        :rtype: AnyObject
        """
        return AnyObject(self.hybrid_shape_instance.GetParameter(i_name))

    def get_parameter_from_position(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetParameterFromPosition(long iPosition) As AnyObject
                | 
                |     Gets a parameter of a hybrid shape instance from its
                |     position.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position 
                | 
                |     Returns:
                |         The parameter, if found 
                |     Example:
                |         The following example tests if the parameter was
                |         found:
                | 
                |          Set parameter = hybridShapeInstance.GetParameterFromPosition(2)
                |          If TypeName(input)="Nothing" Then
                |                MsgBox "Parameter not found"
                |          End If

        :param int i_position:
        :rtype: AnyObject
        """
        return AnyObject(self.hybrid_shape_instance.GetParameterFromPosition(i_position))

    def put_input(self, i_index: str, i_input: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutInput(CATBSTR iIndex,
                | AnyObject iInput)
                | 
                |     Defines an input of a hybrid shape instance.
                | 
                |     Parameters:
                | 
                |         iName
                |             The input name 
                |         iInput
                |             The element wich will be input of the hybrid shape
                |             instance
                |             All types of 
                | 
                |         Boundary object are possibly supported. 
                |     Example:
                |         The following example defines the input of a hybrid shape instance The
                |         input will be a point and its name will be Input1.
                | 
                |          hybridShapeInstance.PutInput "Input1",point

        :param str i_index:
        :param AnyObject i_input:
        :rtype: None
        """
        return self.hybrid_shape_instance.PutInput(i_index, i_input.com_object)

    def put_input_data(self, i_name: str, i_input: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutInputData(CATBSTR iName,
                | CATBaseDispatch iInput)
                | 
                |     Defines an input of a shape instance. Use this method if you want to set as
                |     input a Reference.
                | 
                |     Parameters:
                | 
                |         iName
                |             The input name 
                |         iInput
                |             The element wich will be input of the shape
                |             instance
                |             All types of 
                | 
                |         Boundary object are possibly supported. 
                |     Example:
                |         The following example defines the input of a shape instance The input
                |         will be a point and its name will be Input1.
                | 
                |          shapeInstance.PutInput "Input1",point

        :param str i_name:
        :param AnyObject i_input:
        :rtype: None
        """
        return self.hybrid_shape_instance.PutInputData(i_name, i_input.com_object)

    def __repr__(self):
        return f'HybridShapeInstance(name="{ self.name }")'
