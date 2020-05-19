#! /usr/bin/python3.6

from pywintypes import com_error
from pycatia.exception_handling import CATIAApplicationException
from pycatia.knowledge_interfaces.boolparam import BoolParam
from pycatia.knowledge_interfaces.dimension import Dimension
from pycatia.knowledge_interfaces.intparam import IntParam
from pycatia.knowledge_interfaces.listparameter import ListParameter
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.knowledge_interfaces.parameterset import ParameterSet
from pycatia.knowledge_interfaces.realparam import RealParam
from pycatia.knowledge_interfaces.strparam import StrParam
from pycatia.system_interfaces.collection import Collection


class Parameters(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the Parameters collection of the part or the product.

                | Examples:
                | The following example shows how to retrieve it:
                |
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim part1 As Document
                | Set part1 = CATDocs.Add("CATPart")
                | Dim parameterList As Parameters
                | Set parameterList = part1.Part.Parameters
    """

    def __init__(self, parameters_com_object):
        super().__init__(parameters_com_object)
        self.parameters = parameters_com_object

    @property
    def name(self):
        """
        :return: str - parameterset name
        """
        return self.parameters.Name

    @property
    def root_parameter_set(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RootParameterSet
                | o Property RootParameterSet(    ) As ParameterSet
                |
                | Returns the root parameter set of a document. If it doesn't exist, it
                | is created.
        """
        return ParameterSet(self.parameters.RootParameterSet)

    def all_parameters(self):
        """

        :return: list(Parameter())
        """

        parameters = []

        if self.has_parameters():
            for i in range(self.parameters.Count):
                para = Parameter(self.parameters.Item(i + 1))
                parameters.append(para)

        return parameters

    def create_boolean(self, name, value):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateBoolean
                | o Func CreateBoolean(    CATBSTR    iName,
                |                          boolean    iValue) As BoolParam
                |
                | Creates a boolean parameter and adds it to the part's collection of
                | parameters.

                | Parameters:
                | iName
                |     The parameter name
                |
                |  iValue
                |     The parameter value

                | Examples:
                | This example creates the checked boolean parameter
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim part1 As Document
                | Set part1 = CATDocs.Add("CATPart")
                | Dim chk As BooleanParam
                | Set chk = part1.Part.Parameters.CreateBoolean("checked", False)

        :param str name:
        :param boolean value:
        """
        return BoolParam(self.parameters.CreateBoolean(name, value))

    def create_dimension(self, name, unit_type, value):
        """

        .. warning::
            The documentation below isn't quite right. There are many more dimension
            types available other than "LENGTH" and "ANGLE".

        .. note::
            CAA V5 Visual Basic help

                | CreateDimension
                | o Func CreateDimension(    CATBSTR    iName,
                |                            CATBSTR    iMagnitude,
                |                            double    iValue) As Dimension
                |
                | Creates a user dimension and adds it to the part's collection of
                | parameters.

                | Parameters:
                | iName
                |     The dimension name
                |
                |  iMagnitude
                |     The dimension magnitude. Units are those of the IS system. Valid magnitudes
                |     are:
                |        "LENGTH": the unit is the meter.
                |        "ANGLE": the unit is the radian.
                |
                |     The activateLinkAnchor('Dimension','','Dimension')  object provides the
                |     activateLinkAnchor('Dimension','ValuateFromString','Dimension.ValuateFromStrin
                |      g') method with which you may express the value in any unit for a given
                |      dimension.
                |
                | iValue
                |     The dimension value provided as a real number

                | Examples:
                | This example creates a LENGTH dimension
                | and adds it to the newly created part. The initial value
                | is expressed in meters. The new value is expressed in
                | millimeters.
                |
                | Dim depth As Dimension
                | Set depth = parameters.CreateDimension("depth", "LENGTH", 20)
                | depth.ValuateFromString("300mm")


        """
        try:
            return Dimension(self.parameters.CreateDimension(name, unit_type, value))
        except com_error:
            raise ValueError(f'Dimension type not allowed.')

    def create_integer(self, name, value):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateInteger
                | o Func CreateInteger(    CATBSTR    iName,
                |                          long    iValue) As IntParam
                |
                | Creates an integer parameter and adds it to the part's collection of
                | parameters.

                | Parameters:
                | iName
                |     The parameter name
                |
                |  iValue
                |     The parameter value

                | Examples:
                | This example creates the RevisionNumber integer parameter
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim part1 As Document
                | Set part1   = CATDocs.Add("CATPart")
                | Dim revision As IntParam
                | Set revision = part1.Part.Parameters.CreateInteger ("RevisionRumber", 17)

            :param str name:
            :param int value:
        """

        if not isinstance(value, int):
            raise ValueError(f'Value "{value}" must be int.')

        return IntParam(self.parameters.CreateInteger(name, value))

    def create_list(self, name):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateList
                | o Func CreateList(    CATBSTR    iName) As ListParameter
                |
                | Creates a list parameter and adds it to the part's collection of
                | parameters.

                | Parameters:
                | iName
                |     The parameter name

                | Examples:
                | This example creates the ListName list parameter
                | and adds it to the newly created part:
                |
                | Set CATDocs = CATIA.Documents
                | Set part1   = CATDocs.Add("CATPart")
                | Set list1 = part1.Part.Parameters.CreateList ("ListName")
        """
        return ListParameter(self.parameters.CreateList(name))

    def count_parameters(self):
        """
        :return: int
        """
        return self.parameters.Count

    def create_real(self, name, value):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateReal
                | o Func CreateReal(    CATBSTR    iName,
                |                       double    iValue) As RealParam
                |
                | Creates a real parameter and adds it to the part's collection of
                | parameters.

                | Parameters:
                | iName
                |     The parameter name
                |
                |  iValue
                |     The parameter value

                | Examples:
                | This example creates the ReliabilityRate real parameter
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim part1 As Document
                | Set part1   = CATDocs.Add("CATPart")
                | Dim rate As RealParam
                | Set rate = part1.Part.Parameters.CreateReal ("ReliabilityRate", 2.5 )

        :param str name:
        :param float value:
        """

        if not any([isinstance(value, float), isinstance(value, int)]):
            raise ValueError(f'Value "{value}" should be float.')
        return RealParam(self.parameters.CreateReal(name, value))

    def create_set_of_parameters(self, parent):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateSetOfParameters
                | o Sub CreateSetOfParameters(    AnyObject    iFather)
                |
                | Creates a set of parameters and appends it to argument iFather.
        """
        self.parameters.CreateSetOfParameters(parent.parameterset)

    def create_string(self, name, text):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateString
                | o Func CreateString(    CATBSTR    iName,
                |                         CATBSTR    iValue) As StrParam
                |
                | Creates a string parameter and adds it to the part's collection of
                | parameters.

                | Parameters:
                | iName
                |     The parameter name
                |
                |  iValue
                |     The parameter value

                | Examples:
                | This example creates the responsible string parameter
                | and adds it to the newly created part:
                |
                | Set CATDocs = CATIA.Documents
                | Set part1   = CATDocs.Add("CATPart")
                | Set density = part1.Part.Parameters.CreateString ("responsible", "The Boss")

        :param str name:
        :param str text:
        """
        if not isinstance(text, str):
            raise ValueError(f'Text "{text}" must be a string.')

        return StrParam(self.parameters.CreateString(name, text))

    def get_name_to_use_in_relation(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNameToUseInRelation
                | o Func GetNameToUseInRelation(    AnyObject    iObject) As CATBSTR
                |
                | Returns a correct name of a feature to use it in a relation.
        """
        return self.parameters.GetNameToUseInRelation(i_object.parameter)

    def has_parameters(self):
        """
        :return: bool
        """
        if self.parameters.Count > 0:
            return True

        return False

    def is_parameter(self, index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        :param str or int index: parameter name or parameter number
        :return: bool
        """

        if isinstance(index, int):
            index += 1

        try:
            if self.parameters.Item(index):
                return True
        except com_error:
            return False

    def item(self, index):
        """

        .. warning::

            The index when not a string must be it's python index (indexs in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As Parameter
                |
                | Retrieves a parameter  using its index or its name from the from the
                | Parameters collection.

                | Parameters:
                | iIndex
                |    The index or the name of the parameter to retrieve from
                |    the collection of parameters.
                |    As a numerics, this index is the rank of the parameter
                |    in the collection.
                |    The index of the first parameter in the collection is 1, and
                |    the index of the last parameter is Count.
                |    As a string, it is the name you assigned to the parameter using
                |    the
                |
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property or when
                |  creating the parameter.

                | Examples:
                | This example retrieves the last parameter in the parameters
                | collection:
                |
                | Set lastParameter = parameters.Item(parameters.Count)

        """

        if isinstance(index, int):
            index += 1

        parameter = None

        if not self.is_parameter(index):
            raise CATIAApplicationException(f'Could not find parameter name "{index}".')

        if isinstance(self.parameters.Item(index).value, bool):
            parameter = BoolParam(self.parameters.Item(index))

        elif isinstance(self.parameters.Item(index).value, int):
            parameter = IntParam(self.parameters.Item(index))

        elif isinstance(self.parameters.Item(index).value, str):
            parameter = StrParam(self.parameters.Item(index))

        elif isinstance(self.parameters.Item(index).value, float):
            parameter = RealParam(self.parameters.Item(index))

        return parameter

    def sub_list(self, i_object, recursively):
        """
        .. note::
            CAA V5 Visual Basic help

                | SubList
                | o Func SubList(    AnyObject    iObject,
                |                    boolean    iRecursively) As Parameters
                |
                | Returns a sub-collection of parameters aggregated to an object.

                | Parameters:
                | iObject
                |  The object used to filter the whole parameter
                |  collection to get the resulting sub-collection.
                |
                |  iRecursively
                |  A flag to specify if children parameters are to be searched for in the returned
                |  collection

                | Examples:
                | This example shows how to retrieve a collection of parameters that are
                | associated to a Pad.
                |
                | Dim Parameters1 As Parameters
                | Set Parameters1 = CATIA.ActiveDocument.Part.Parameters
                | Dim Body0 As AnyObject
                | Set Body0 = CATIA.ActiveDocument.Part.Bodies.Item("MechanicalTool.1")
                | Dim Pad1 As AnyObject
                | Set Pad1 = Body0.Shapes.Item("Pad.1")
                | Dim Parameters2 As Parameters
                | # gets the collection of parameters that are under the pad Pad.1
                | Set Parameters2 = Parameters1.SubList(Pad1,TRUE)

            :param i_object:
            :param bool recursively:
        """
        return Parameters(self.parameters.SubList(i_object.com_object, recursively))

    def remove_item(self, index):

        """

        .. warning::

            The index when not a string must be it's python index (indexs in python start from 0).
            collection. The COM interface index starts at 1.


        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(CATVariant iIndex)
                |
                | Removes a parameter from the Parameters collection.

                | Parameters:
                | iIndex
                |    The index or the name of the parameter to remove from
                |    the collection of parameters.
                |    As a numerics, this index is the rank of the parameter
                |    in the collection.
                |    The index of the first parameter in the collection is 1, and
                |    the index of the last parameter is Count.
                |    As a string, it is the name you assigned to the parameter using
                |    the
                |
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property or when
                |  creating the parameter.

                | Examples:
                | This example removes the "depth" parameter from the parameters
                | collection.
                |
                | parameters.Remove("depth")
        """

        if isinstance(index, int):
            index += 1

        return self.parameters.Remove(index)

    def __repr__(self):
        return 'Parameters()'
