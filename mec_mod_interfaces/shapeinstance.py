#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from .shape import Shape


class ShapeInstance(Shape):
    """
        .. note::
            CAA V5 Visual Basic help

                | The interface to access a CATIAShapeInstance.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape_instance = com_object

    @property
    def inputs_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InputsCount
                | o Property InputsCount(    ) As   (Read Only)
                | 
                | Returns the number of Inputs. 
                |
                | Example:
                | The following example
                | retrieves in inputsCount the number of Inputs of
                | hybridShapeInstance: inputsCount =
                | hybridShapeInstance.InputsCount

        :return: int
        """
        return self.shape_instance.InputsCount

    @property
    def outputs_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OutputsCount
                | o Property OutputsCount(    ) As   (Read Only)
                | 
                | Returns the number of Outputs. 
                |
                | Example:
                | The following
                | example retrieves in outputsCount the number of Outputs of
                | hybridShapeInstance: outputsCount =
                | hybridShapeInstance.OutputsCount

        :return: int
        """
        return self.shape_instance.OutputsCount

    @property
    def parameters_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParametersCount
                | o Property ParametersCount(    ) As   (Read Only)
                | 
                | Returns the number of Parameters. 
                |
                | Example:
                | The following
                | example retrieves in parametersCount the number of
                | parameters of hybridShapeInstance: parametersCount =
                | hybridShapeInstance.ParametersCount

        :return: int
        """
        return self.shape_instance.ParametersCount

    def get_input(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInput
                | o Func GetInput(        iName) As
                | 
                | Gets an input of a shape instance by its name.
                |
                | Parameters:
                | iName
                |    The name of the input of the shape instance
                |  
                |  Returns:
                |      The input, if found
                |
                | Examples:
                | The following example tests if the input was found: Set
                | input = shapeInstance.GetInput("Input1") If
                | TypeName(input)="Nothing" Then MsgBox "Input not found" End
                | If

        :param str i_name:
        :return: AnyObject()
        """
        return self.shape_instance.GetInput(i_name)

    def get_input_data(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInputData
                | o Func GetInputData(        iName) As
                | 
                | Gets an input of a shape instance by its name. Use this
                | method if you want to retrieve a Reference.
                |
                | Parameters:
                | iName
                |    The name of the input of the shape instance
                |  
                |  Returns:
                |      The input, if found
                |
                | Examples:
                | The following example tests if the input was found: Set
                | input = shapeInstance.GetInput("Input1")
                | If TypeName(input)="Nothing"
                |   Then MsgBox "Input not found"
                | End If

        :param str i_name:
        :return:
        """
        return self.shape_instance.GetInputData(i_name)

    def get_input_data_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInputDataFromPosition
                | o Func GetInputDataFromPosition(        iPosition) As
                | 
                | Gets an input of a hybrid shape instance from its position.
                | Use this method if you want to retrieve a Reference.
                |
                | Parameters:
                | iPosition
                |    The position 
                |  
                |  Returns:
                |      The input, if found
                |
                | Examples:
                | The following example tests if the input was found:
                | Set input = hybridShapeInstance.GetInputFromPosition(2)
                | If TypeName(input)="Nothing"
                |   Then MsgBox "Input not found"
                | End If

        :param str i_position:
        :return:
        """
        return self.shape_instance.GetInputDataFromPosition(i_position)

    def get_input_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInputFromPosition
                | o Func GetInputFromPosition(        iPosition) As
                | 
                | Gets an input of a hybrid shape instance from its position.
                |
                | Parameters:
                | iPosition
                |    The position 
                |  
                |  Returns:
                |      The input, if found
                |
                | Examples:
                | The following example tests if the input was found:
                | Set input = hybridShapeInstance.GetInputFromPosition(2)
                | If TypeName(input)="Nothing"
                |   Then MsgBox "Input not found"
                | End If

        :param str i_position:
        :return:
        """
        return self.shape_instance.GetInputFromPosition(i_position)

    def get_output(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOutput
                | o Func GetOutput(        iName) As
                | 
                | Gets a Ouput by its name.
                |
                | Parameters:
                | iName
                |    The name of the output of the shape instance
                |  
                |  Returns:
                |   	 The output, if found
                |
                | Examples:
                | The following example tests if the output was found: Set
                | output = shapeInstance.GetOuput("Output1") If
                | TypeName(output)="Nothing" Then MsgBox "Output not found"
                | End If

        :param str i_name:
        :return:
        """
        return self.shape_instance.GetOutput(i_name)

    def get_output_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOutputFromPosition
                | o Func GetOutputFromPosition(        iPosition) As
                | 
                | Gets a Ouput from its position.
                |
                | Parameters:
                | iPosition
                |    The position 
                |  
                |  Returns:
                |   	 The output, if found
                |
                | Examples:
                | The following example tests if the output was found: 
                | Set output = shapeInstance.GetOuputFromPosition(2) 
                | If TypeName(output)="Nothing" 
                |   Then MsgBox "Output not found"
                | End If

        :param str i_position:
        :return:
        """
        return self.shape_instance.GetOutputFromPosition(i_position)

    def get_parameter(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParameter
                | o Func GetParameter(        iName) As
                | 
                | Gets a parameter of a shape instance by its name.
                |
                | Parameters:
                | iName
                |    The name of the parameter of the shape instance
                |  
                |  Returns:
                |   	 The parameter, if found
                |
                | Examples:
                | The following example tests if the parameter was found: 
                | Set parameter = shapeInstance.GetParameter("Parameter1") 
                | If TypeName(parameter)="Nothing" 
                |   Then MsgBox "Parameter not found" 
                | End If

        :param str i_name:
        :return:
        """
        return self.shape_instance.GetParameter(i_name)

    def get_parameter_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParameterFromPosition
                | o Func GetParameterFromPosition(        iPosition) As
                |
                | Gets a parameter of a hybrid shape instance from its
                | position.
                |
                | Parameters:
                | iPosition
                |    The position
                |
                |  Returns:
                |      The parameter, if found
                |
                | Examples:
                | The following example tests if the parameter was found:
                | Set parameter = hybridShapeInstance.GetParameterFromPosition(2)
                | If TypeName(input)="Nothing"
                | Then MsgBox "Parameter not found"
                | End If

        :param str i_position:
        :return:
        """
        return self.shape_instance.GetParameterFromPosition(i_position)

    def put_input(self, i_name, i_input):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutInput
                | o Sub PutInput(        iName,
                |                        iInput)
                |
                | Defines an input of a shape instance.
                |
                | Parameters:
                | iName
                |    The input name
                |
                |  iInput
                |    The element wich will be input of the shape instance
                |    All types of
                |
                |  object are possibly supported.
                |
                | Examples:
                | The following example defines the input of a shape instance
                | The input will be a point and its name will be Input1.
                | shapeInstance.PutInput "Input1",point

        :param str i_name:
        :param i_input:
        :return:
        """
        return self.shape_instance.PutInput(i_name, i_input)

    def put_input_data(self, i_name, i_input):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutInputData
                | o Sub PutInputData(        iName,
                |                            iInput)
                |
                | Defines an input of a shape instance. Use this method if you
                | want to set as input a Reference.
                |
                | Parameters:
                | iName
                |    The input name
                |
                |  iInput
                |    The element wich will be input of the shape instance
                |    All types of
                |
                |  object are possibly supported.
                |
                | Examples:
                | The following example defines the input of a shape instance
                | The input will be a point and its name will be Input1.
                | shapeInstance.PutInput "Input1",point

        :param str i_name:
        :param i_input:
        :return:
        """
        return self.shape_instance.PutInputData(i_name, i_input)

    def __repr__(self):
        return f'ShapeInstance()'
