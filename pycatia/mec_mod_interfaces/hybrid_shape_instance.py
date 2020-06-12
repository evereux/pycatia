#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25


class HybridShapeInstance:
    """
        .. note::
            CAA V5 Visual Basic help

                | The interface to access a CATIAHybridShapeInstance.

    """

    def __init__(self, catia):
        self.hybridshapeinstance = catia.HybridShapeInstance     

    @property
    def inputs_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | InputsCount
                | o Property InputsCount() As long
                | 
                | Returns the number of Inputs.  Example:The following example retrieves
                | in inputsCount the number of Inputs of hybridShapeInstance:
                | inputsCount = hybridShapeInstance.InputsCount


                | Parameters:


        """
        return self.hybridshapeinstance.InputsCount

    @property
    def outputs_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OutputsCount
                | o Property OutputsCount() As long
                | 
                | Returns the number of Outputs.  Example:The following example
                | retrieves in outputsCount the number of Outputs of
                | hybridShapeInstance:  outputsCount = hybridShapeInstance.OutputsCount


                | Parameters:


        """
        return self.hybridshapeinstance.OutputsCount

    @property
    def parameters_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParametersCount
                | o Property ParametersCount() As long
                | 
                | Returns the number of Parameters.  Example:The following example
                | retrieves in parametersCount the number of parameters of
                | hybridShapeInstance:  parametersCount =
                | hybridShapeInstance.ParametersCount


                | Parameters:


        """
        return self.hybridshapeinstance.ParametersCount

    def get_input(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInput
                | o Func GetInput(    CATBSTR    iIndex) As AnyObject
                | 
                | Gets an input of a hybrid shape instance by its name.


                | Parameters:
                | iName
                |    The name of the input of the hybrid shape instance
                |  
                | 
                |  Returns:
                |      The input, if found


                | Examples:
                | 
                | The following example tests if the input was found:
                | 
                | Set input = hybridShapeInstance.GetInput("Input1")
                | If TypeName(input)="Nothing" Then
                | MsgBox "Input not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetInput(i_index)

    def get_input_data(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInputData
                | o Func GetInputData(    CATBSTR    iName) As CATBaseDispatch
                | 
                | Gets an input of a shape instance by its name. Use this method if you
                | want to retrieve a Reference.


                | Parameters:
                | iName
                |    The name of the input of the shape instance
                |  
                | 
                |  Returns:
                |      The input, if found


                | Examples:
                | 
                | The following example tests if the input was found:
                | 
                | Set input = shapeInstance.GetInput("Input1")
                | If TypeName(input)="Nothing" Then
                | MsgBox "Input not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetInputData(i_name)

    def get_input_data_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInputDataFromPosition
                | o Func GetInputDataFromPosition(    long    iPosition) As CATBaseDispatch
                | 
                | Gets an input of a hybrid shape instance from its position. Use this
                | method if you want to retrieve a Reference.


                | Parameters:
                | iPosition
                |    The position 
                |  
                | 
                |  Returns:
                |      The input, if found


                | Examples:
                | 
                | The following example tests if the input was found:
                | 
                | Set input = hybridShapeInstance.GetInputFromPosition(2)
                | If TypeName(input)="Nothing" Then
                | MsgBox "Input not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetInputDataFromPosition(i_position)

    def get_input_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInputFromPosition
                | o Func GetInputFromPosition(    long    iPosition) As AnyObject
                | 
                | Gets an input of a hybrid shape instance from its position.


                | Parameters:
                | iPosition
                |    The position 
                |  
                | 
                |  Returns:
                |      The input, if found


                | Examples:
                | 
                | The following example tests if the input was found:
                | 
                | Set input = hybridShapeInstance.GetInputFromPosition(2)
                | If TypeName(input)="Nothing" Then
                | MsgBox "Input not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetInputFromPosition(i_position)

    def get_output(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOutput
                | o Func GetOutput(    CATBSTR    iName) As AnyObject
                | 
                | Gets a Ouput by its name.


                | Parameters:
                | iName
                |    The name of the output of the shape instance
                |  
                | 
                |  Returns:
                |   	 The output, if found


                | Examples:
                | 
                | The following example tests if the output was found:
                | 
                | Set output = shapeInstance.GetOuput("Output1")
                | If TypeName(output)="Nothing" Then
                | MsgBox "Output not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetOutput(i_name)

    def get_output_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOutputFromPosition
                | o Func GetOutputFromPosition(    long    iPosition) As AnyObject
                | 
                | Gets a Ouput from its position.


                | Parameters:
                | iPosition
                |    The position 
                |  
                | 
                |  Returns:
                |   	 The output, if found


                | Examples:
                | 
                | The following example tests if the output was found:
                | 
                | Set output = shapeInstance.GetOuputFromPosition(2)
                | If TypeName(output)="Nothing" Then
                | MsgBox "Output not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetOutputFromPosition(i_position)

    def get_parameter(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParameter
                | o Func GetParameter(    CATBSTR    iName) As AnyObject
                | 
                | Gets a parameter of a hybrid shape instance by its name.


                | Parameters:
                | iName
                |    The name of the parameter of the hybrid shape instance
                |  
                | 
                |  Returns:
                |   	 The parameter, if found


                | Examples:
                | 
                | The following example tests if the parameter was found:
                | 
                | Set parameter = hybridShapeInstance.GetParameter("Parameter1")
                | If TypeName(parameter)="Nothing" Then
                | MsgBox "Parameter not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetParameter(i_name)

    def get_parameter_from_position(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParameterFromPosition
                | o Func GetParameterFromPosition(    long    iPosition) As AnyObject
                | 
                | Gets a parameter of a hybrid shape instance from its position.


                | Parameters:
                | iPosition
                |    The position 
                |  
                | 
                |  Returns:
                |      The parameter, if found


                | Examples:
                | 
                | The following example tests if the parameter was found:
                | 
                | Set parameter = hybridShapeInstance.GetParameterFromPosition(2)
                | If TypeName(input)="Nothing" Then
                | MsgBox "Parameter not found"
                | End If
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.GetParameterFromPosition(i_position)

    def put_input(self, i_index, i_input):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutInput
                | o Sub PutInput(    CATBSTR    iIndex,
                |                    AnyObject    iInput)
                | 
                | Defines an input of a hybrid shape instance.


                | Parameters:
                | iName
                |    The input name
                |  
                |  iInput
                |    The element wich will be input of the hybrid shape instance
                |    All types of 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object are possibly supported.


                | Examples:
                | 
                | The following example defines the input of a hybrid shape instance
                | The input will be a point and its name will be Input1.
                | 
                | hybridShapeInstance.PutInput "Input1",point
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.PutInput(i_index, i_input)

    def put_input_data(self, i_name, i_input):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutInputData
                | o Sub PutInputData(    CATBSTR    iName,
                |                        CATBaseDispatch    iInput)
                | 
                | Defines an input of a shape instance. Use this method if you want to
                | set as input a Reference.


                | Parameters:
                | iName
                |    The input name
                |  
                |  iInput
                |    The element wich will be input of the shape instance
                |    All types of 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object are possibly supported.


                | Examples:
                | 
                | The following example defines the input of a shape instance
                | The input will be a point and its name will be Input1.
                | 
                | shapeInstance.PutInput "Input1",point
                | 
                | 
                | 
        """
        return self.hybridshapeinstance.PutInputData(i_name, i_input)

