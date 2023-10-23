#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.system_interfaces.any_object import AnyObject


class InstanceFactory(Factory):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         InstanceFactory
                | 
                | Represents the CATIAInstanceFactory.
                | Role: This interface is used to create a new instance of a shape reference
                | (ShapeInstance ) or a hybrid shape reference ( HybridShapeInstance ) in case of
                | the instantiation of a User Feature.
                | It is also used to instantiate a Power Copy reference.
                | 
                | This interface contains two protocols of instantiation:
                | 
                |     The first protocol is dedicated to User Feature instantiation
                |     only.
                |     It is defined by a single method: AddInstance . It creates a shape or
                |     hybrid shape instance depending on the result of the User
                |     Feature.
                |     Use this method when you want to perform only one instantiation of the
                |     reference. Read the document containing the User Feature reference and
                |     instantiate it.
                |     As the document containing the reference is released from the session at
                |     the end of the instantiation, it is not recommmended to use this method if you
                |     want to perform several instantiations of the same reference in a
                |     loop.
                |     In that case, prefer the second protocol of instantiation.
                |     The second protocol is dedicated to both User Feature and Power Copy
                |     instantiations.
                |     It is defined by several methods that must be called in
                |     order.
                |         For User Feature instantiation, these methods are an alternative way of
                |         the AddInstance method.
                |         It is recommended to use the second protocol to perform several
                |         instantiations of the same reference in a loop.
                |         For Power Copy instantiation, it is the only way of instantiating a
                |         reference.
                |     The instantiation process is composed of three major
                |     steps:
                |         The first step BeginInstanceFactory consists in initializing the
                |         InstanceFactory with the reference and the document where it is
                |         stored.
                |         This step must be called once at the beginning whatever the number of
                |         instantiations are done.
                |         Optional step InstantiationMode allow the user to specify the mode of
                |         the instantiation, that is to say "After" or "Inside".
                |         If this method is not called, the instantiation mode will be chosen
                |         according to the BeginInstantiate method.
                |         The second step is the instantiation itself: it is composed of five
                |         methods that must be called in the order.
                |         This set of five methods can be called in a loop in order to make
                |         several instantiations.
                |             The method BeginInstantiate is used to initialize all data of the
                |             reference.
                |             The method PutInputData is used to set a value to any input of the
                |             reference.
                |             The method GetParameter is used to retrieve any parameter of the
                |             reference in order to modify its value.
                |             The method Instantiate is used to duplicate the reference. It
                |             returns the created instance when it does exist.
                |             The method EndInstantiate is used to indicate that the
                |             instantiation is done.
                |         The third step EndInstanceFactory consists in ending the instantiation
                |         and cleaning the InstanceFactory.
                |         When doing several instantiations in a loop, this step must be called
                |         just once at the end of all instantiations.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.instance_factory = com_object

    @property
    def instantiation_mode(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InstantiationMode(CATBSTR iInstantiationModeBSTR) (Write
                | Only)
                | 
                |     Sets the mode of instantiation to "Inside" or "After".
                |     Role: This method should be called BEFORE the method BeginInstantiate to
                |     take into account the desired instantiation mode.
                |     It is used to set the destination path of insertion of the template
                |     reference.
                | 
                |     Example:
                |         The following example shows how to determine the instantiation mode
                |         (Mode's value is "Inside" or "After"):
                | 
                |          InstanceFactory.InstantationMode = Mode

        :rtype: str
        """

        return self.instance_factory.InstantiationMode

    @instantiation_mode.setter
    def instantiation_mode(self, value: str):
        """
        :param str value:
        """

        self.instance_factory.InstantiationMode = value

    def add_instance(self, i_reference: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddInstance(AnyObject iReference) As AnyObject
                | 
                |     Creates a new instance of a shape or hybrid shape.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference shape or hybrid shape. 
                | 
                |     Example:
                |         This example creates the instance NewInstance in the
                |         part.
                | 
                |          Set NewInstance = instanceFactory.AddInstance(reference)

        :param AnyObject i_reference:
        :rtype: AnyObject
        """
        return AnyObject(self.instance_factory.AddInstance(i_reference.com_object))

    def begin_instance_factory(self, i_name_of_reference: str, i_name_of_document: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub BeginInstanceFactory(CATBSTR iNameOfReference,
                | CATBSTR iNameOfDocument)
                | 
                |     Initializes the instantiation process with the document containing the
                |     reference.
                |     Role: Use this method to start instantiating a reference in the current
                |     document.
                |     In that method, the document containing the reference is locked in
                |     session.
                |     It will be unlocked in the last step EndInstanceFactory .
                | 
                |     Parameters:
                | 
                |         iNameOfReference
                |             The name of the reference to be instantiated. 
                |         iDocumentFileName
                |             The name of the file containing the document where to find the
                |             reference to be instantiated. 
                | 
                |     Example:
                |         The following example initializes the factory with a document and a
                |         reference:
                | 
                |         InstanceFactory.BeginInstanceFactory"NameOfReference","c:\\tmp\\NameOfDocument.CATPart"

        :param str i_name_of_reference:
        :param str i_name_of_document:
        :rtype: None
        """
        return self.instance_factory.BeginInstanceFactory(i_name_of_reference, i_name_of_document)

    def begin_instantiate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub BeginInstantiate()
                | 
                |     Initializes the data of the reference.
                |     Role: This is the first method of the second step of
                |     instantiation.
                |     It is used to initialize all data of the reference in the
                |     factory.
                | 
                |     Example:
                |         The following example shows how to initialize the
                |         factory:
                | 
                |          InstanceFactory.BeginInstantiate

        :rtype: None
        """
        return self.instance_factory.BeginInstantiate()

    def end_instance_factory(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub EndInstanceFactory()
                | 
                |     Ends the instantiation process.
                |     Role: Use this method to end the instantiation process.
                |     In that method the document containing the reference is unlocked and
                |     released from the session.
                | 
                |     Example:
                |         The following example shows how to end the
                |         instantiation:
                | 
                |          InstanceFactory.EndInstanceFactory

        :rtype: None
        """
        return self.instance_factory.EndInstanceFactory()

    def end_instantiate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub EndInstantiate()
                | 
                |     Ends the instantiation of the reference.
                |     Role: This is the fifth and last method of the second step of
                |     instantiation.
                |     It is used to end the instantiation: after this step, all the links to the
                |     reference are broken.
                | 
                |     Example:
                |         The following example shows how to end the
                |         instantiation:
                | 
                |          InstanceFactory.EndInstantiate

        :rtype: None
        """
        return self.instance_factory.EndInstantiate()

    def get_parameter(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetParameter(CATBSTR iName) As AnyObject
                | 
                |     Retrieves a parameter of the reference by its name.
                |     Role: This is the third method of the second step of
                |     instantiation.
                |     This step is optional.
                |     It is used to retrieve a parameter of the reference in order to change its
                |     value, using the ValuateFromString method of the Parameter
                |     interface.
                |     It has to be called on each parameter whose value has to be
                |     changed.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter. 
                | 
                |     Example:
                |         The following example retrieves a parameter on the
                |         reference:
                | 
                |          Set parameter = InstanceFactory.GetParameter("Parameter1")

        :param str i_name:
        :rtype: AnyObject
        """
        return AnyObject(self.instance_factory.GetParameter(i_name))

    def instantiate(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Instantiate() As AnyObject
                | 
                |     Instantiates the reference in the current document.
                |     Role: This is the fourth method of the second step of
                |     instantiation.
                |     It is used to duplicate or instantiate the data of the
                |     reference.
                | 
                |         In case of Power Copy instantiation, the data are duplicated and there
                |         is no created instance.
                |         In case of User Feature instantiation, the data are instantiated and an
                |         instance is created and returned.
                | 
                |     Example:
                |         The following example instantiates the reference:
                | 
                |          Set Instance = InstanceFactory.Instantiate

        :rtype: AnyObject
        """
        return AnyObject(self.instance_factory.Instantiate())

    def put_input_data(self, i_name: str, i_input: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutInputData(CATBSTR iName,
                | CATBaseDispatch iInput)
                | 
                |     Sets a value to an input of the reference.
                |     Role: This is the second method of the second step of
                |     instantiation.
                |     It is used to set a value to any input of the reference.
                |     It has to be called on each input of the reference.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the input. 
                |         iInput
                |             The element to set as the new value of the input.
                |             All types of 
                | 
                |         Boundary object are possibly supported. 
                | 
                | Example:
                |     The following example sets a value to an input of the reference: The input
                |     is a point and its name is Input1.
                | 
                |      InstanceFactory.PutInputData "Input1",point1

        :param str i_name:
        :param AnyObject i_input:
        :rtype: None
        """
        return self.instance_factory.PutInputData(i_name, i_input.com_object)

    def __repr__(self):
        return f'InstanceFactory(name="{self.name}")'
