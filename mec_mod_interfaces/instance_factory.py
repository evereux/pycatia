#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from .factory import Factory


class InstanceFactory(Factory):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the CATIAInstanceFactory.Role: This interface is used to
                | create a new instance of a shape reference
                | (activateLinkAnchor('ShapeInstance','','ShapeInstance')) or a hybrid
                | shape reference
                | (activateLinkAnchor('HybridShapeInstance','','HybridShapeInstance'))
                | in case of the instantiation of aUser Feature.It is also used to
                | instantiate aPower Copyreference.This interface contains two protocols
                | of instantiation:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.instance_factory = com_object

    def instantiation_mode(self, i_instantiation_mode_bstr):
        """
        .. note::
            CAA V5 Visual Basic help

                | InstantiationMode
                | o Property InstantiationMode(iInstantiationModeBSTR) (Write Only)
                | 
                | Sets the mode of instantiation to "Inside" or "After". Role:
                | This method should be called BEFORE the method
                | BeginInstantiate to take into account the desired
                | instantiation mode. It is used to set the destination path
                | of insertion of the template reference. Example: The
                | following example shows how to determine the instantiation
                | mode (Mode's value is "Inside" or "After"):
                | InstanceFactory.InstantationMode = Mode
                |

        :param i_instantiation_mode_bstr:
        :return:
        """
        self.instance_factory.InstantiationMode = i_instantiation_mode_bstr

    def add_instance(self, i_reference):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddInstance
                | o Func AddInstance(iReference) As
                | 
                | Creates a new instance of a shape or hybrid shape.
                |
                | Parameters:
                | iReference
                |    The reference shape or hybrid shape.

                |                | Examples:
                | This example creates the instance NewInstance in the part.
                | Set NewInstance = instanceFactory.AddInstance(reference)

        :param i_reference:
        :return:
        """
        return self.instance_factory.AddInstance(i_reference)

    def begin_instance_factory(self, i_name_of_reference, i_name_of_document):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginInstanceFactory
                | o Sub BeginInstanceFactory(iNameOfReference,
                |                                    iNameOfDocument)
                | 
                | Initializes the instantiation process with the document
                | containing the reference. Role: Use this method to start
                | instantiating a reference in the current document. In that
                | method, the document containing the reference is locked in
                | session. It will be unlocked in the last step .
                |
                | Parameters:
                | iNameOfReference
                | 	The name of the reference to be instantiated.
                |  
                |  iDocumentFileName
                |   The name of the file containing the document where to find the reference to be instantiated.

                |                | Examples:
                | The following example initializes the factory with a
                | document and a reference: InstanceFactory.BeginInstanceFacto
                | ry"NameOfReference","c:/tmp/NameOfDocument.CATPart"

        :param i_name_of_reference:
        :param i_name_of_document:
        :return:
        """
        return self.instance_factory.BeginInstanceFactory(i_name_of_reference, i_name_of_document)

    def begin_instantiate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BeginInstantiate
                | o Sub BeginInstantiate()
                | 
                | Initializes the data of the reference. Role: This is the
                | first method of the second step of instantiation. It is used
                | to initialize all data of the reference in the factory.
                | Example: The following example shows how to initialize the
                | factory: InstanceFactory.BeginInstantiate
                |
                | Parameters:

                |
        :return:
        """
        return self.instance_factory.BeginInstantiate()

    def end_instance_factory(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndInstanceFactory
                | o Sub EndInstanceFactory()
                | 
                | Ends the instantiation process. Role: Use this method to end
                | the instantiation process. In that method the document
                | containing the reference is unlocked and released from the
                | session. Example: The following example shows how to end the
                | instantiation: InstanceFactory.EndInstanceFactory
                |
                | Parameters:

                |
        :return:
        """
        return self.instance_factory.EndInstanceFactory()

    def end_instantiate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndInstantiate
                | o Sub EndInstantiate()
                | 
                | Ends the instantiation of the reference. Role: This is the
                | fifth and last method of the second step of instantiation.
                | It is used to end the instantiation: after this step, all
                | the links to the reference are broken. Example: The
                | following example shows how to end the instantiation:
                | InstanceFactory.EndInstantiate
                |
                | Parameters:

                |
        :return:
        """
        return self.instance_factory.EndInstantiate()

    def get_parameter(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParameter
                | o Func GetParameter(iName) As
                | 
                | Retrieves a parameter of the reference by its name. Role:
                | This is the third method of the second step of
                | instantiation. This step is optional. It is used to retrieve
                | a parameter of the reference in order to change its value,
                | using the ValuateFromString method of the Parameter
                | interface. It has to be called on each parameter whose value
                | has to be changed.
                |
                | Parameters:
                | iName
                |    The name of the parameter.

                |                | Examples:
                | The following example retrieves a parameter on the
                | reference: Set parameter =
                | InstanceFactory.GetParameter("Parameter1")

        :param i_name:
        :return:
        """
        return self.instance_factory.GetParameter(i_name)

    def instantiate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Instantiate
                | o Func Instantiate() As
                | 
                | Instantiates the reference in the current document. Role:
                | This is the fourth method of the second step of
                | instantiation. It is used to duplicate or instantiate the
                | data of the reference. In case of Power Copy instantiation,
                | the data are duplicated and there is no created instance. In
                | case of User Feature instantiation, the data are
                | instantiated and an instance is created and returned.
                | Example: The following example instantiates the reference:
                | Set Instance = InstanceFactory.Instantiate
                |
                | Parameters:

                |
        :return:
        """
        return self.instance_factory.Instantiate()

    def put_input_data(self, i_name, i_input):
        """
        .. note::
            CAA V5 Visual Basic help

                | PutInputData
                | o Sub PutInputData(iName,
                |                            iInput)
                | 
                | Sets a value to an input of the reference. Role: This is the
                | second method of the second step of instantiation. It is
                | used to set a value to any input of the reference. It has to
                | be called on each input of the reference.
                |
                | Parameters:
                | iName
                |    The name of the input.
                |  
                |  iInput
                |    The element to set as the new value of the input.
                |    All types of 
                | 
                |  object are possibly supported.

                |                | Examples:
                | The following example sets a value to an input of the
                | reference: The input is a point and its name is Input1.
                | InstanceFactory.PutInputData "Input1",point1

        :param i_name:
        :param i_input:
        :return:
        """
        return self.instance_factory.PutInputData(i_name, i_input)

    def __repr__(self):
        return f'InstanceFactory(name="{self.name}")'
