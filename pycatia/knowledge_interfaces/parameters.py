#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator
from typing import TYPE_CHECKING
from typing import Optional

from pywintypes import com_error

from pycatia.exception_handling import CATIAApplicationException
from pycatia.knowledge_interfaces.bool_param import BoolParam
from pycatia.knowledge_interfaces.dimension import Dimension
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.knowledge_interfaces.list_parameter import ListParameter
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.knowledge_interfaces.units import Units
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant
from pycatia.types.general import any_parameter

if TYPE_CHECKING:
    from pycatia.knowledge_interfaces.parameter_set import ParameterSet


class Parameters(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Parameters
                | 
                | Represents the Parameters collection of the part or the
                | product.
                | The following example shows how to retrieve it:
                | 
                | 	Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim parameterList As Parameters
                |   Set parameterList = part1.Part.Parameters

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Parameter)
        self.parameters = com_object

    @property
    def root_parameter_set(self) -> 'ParameterSet':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RootParameterSet() As ParameterSet (Read Only)
                | 
                |     Returns the root parameter set of a document. If it doesn't exist, it is
                |     created.

        :return: ParameterSet
        :rtype: ParameterSet
        """
        from pycatia.knowledge_interfaces.parameter_set import ParameterSet
        return ParameterSet(self.parameters.RootParameterSet)

    @property
    def units(self) -> Units:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Units() As Units (Read Only)
                | 
                |     Returns the collection of units.

        :return: Units
        :rtype: Units
        """

        return Units(self.parameters.Units)

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

    def create_boolean(self, i_name: str, i_value: bool) -> BoolParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateBoolean(CATBSTR iName,
                | boolean iValue) As BoolParam
                | 
                |     Creates a boolean parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Example:
                |         This example creates the checked boolean parameter and adds it to the
                |         newly created part:
                | 
                |         Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim part1 As Document
                |          Set part1   = CATDocs.Add("CATPart")
                |          Dim chk As BooleanParam
                |           Set chk = part1.Part.Parameters.CreateBoolean ("checked", False)

        :param str i_name:
        :param bool i_value:
        :return: BoolParam
        :rtype: BoolParam
        """
        return BoolParam(self.parameters.CreateBoolean(i_name, i_value))

    def create_dimension(self, i_name: str, i_magnitude: str, i_value: float) -> Dimension:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateDimension(CATBSTR iName,
                | CATBSTR iMagnitude,
                | double iValue) As Dimension
                | 
                |     Creates a user dimension and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The dimension name 
                |         iMagnitude
                |             The dimension magnitude. Units are those of the IS system. Valid
                |             magnitudes are:
                | 
                |                 "LENGTH": the unit is the meter.
                |                 "ANGLE": the unit is the radian. 
                | 
                |             The 
                | 
                |         Dimension object provides the Dimension.ValuateFromString method with
                |         which you may express the value in any unit for a given dimension (see the
                |         example below). 
                |     iValue
                |         The dimension value provided as a real number 
                |     Example:
                |         This example creates a LENGTH dimension and adds it to the newly
                |         created part. The initial value is expressed in meters. The new value is
                |         expressed in millimeters.
                | 
                |          Dim depth As Dimension
                |          Set depth = parameters.CreateDimension("depth", "LENGTH", 20)
                |          depth.ValuateFromString("300mm");

        :param str i_name:
        :param str i_magnitude:
        :param float i_value:
        :return: Dimension
        :rtype: Dimension
        """
        return Dimension(self.parameters.CreateDimension(i_name, i_magnitude, i_value))

    def create_integer(self, i_name: str, i_value: int) -> IntParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateInteger(CATBSTR iName,
                | long iValue) As IntParam
                | 
                |     Creates an integer parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Example:
                |         This example creates the RevisionNumber integer parameter and adds it
                |         to the newly created part:
                | 
                |         Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim part1 As Document
                |          Set part1   = CATDocs.Add("CATPart")
                |          Dim revision As IntParam
                |           Set revision = part1.Part.Parameters.CreateInteger ("RevisionRumber", 17)

        :param str i_name:
        :param int i_value:
        :return: IntParam
        :rtype: IntParam
        """
        return IntParam(self.parameters.CreateInteger(i_name, i_value))

    def create_list(self, i_name: str) -> ListParameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateList(CATBSTR iName) As ListParameter
                | 
                |     Creates a list parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                | 
                |     Example:
                |         This example creates the ListName list parameter and adds it to the
                |         newly created part:
                | 
                |           Set CATDocs = CATIA.Documents
                |           Set part1   = CATDocs.Add("CATPart")
                |           Set list1 = part1.Part.Parameters.CreateList ("ListName")

        :param str i_name:
        :return: ListParameter
        :rtype: ListParameter
        """
        return ListParameter(self.parameters.CreateList(i_name))

    def create_real(self, i_name: str, i_value: float) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateReal(CATBSTR iName,
                | double iValue) As RealParam
                | 
                |     Creates a real parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Example:
                |         This example creates the ReliabilityRate real parameter and adds it to
                |         the newly created part:
                | 
                |         Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim part1 As Document
                |          Set part1   = CATDocs.Add("CATPart")
                |          Dim rate As RealParam
                |           Set rate = part1.Part.Parameters.CreateReal ("ReliabilityRate", 2.5 )

        :param str i_name:
        :param float i_value:
        :return: RealParam
        :rtype: RealParam
        """
        return RealParam(self.parameters.CreateReal(i_name, i_value))

    def create_set_of_parameters(self, i_father: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub CreateSetOfParameters(AnyObject iFather)
                | 
                |     Creates a set of parameters and appends it to argument iFather.

        :param AnyObject i_father:
        :return: None
        :rtype: None
        """
        return self.parameters.CreateSetOfParameters(i_father.com_object)

    def create_string(self, i_name: str, i_value: str) -> StrParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateString(CATBSTR iName,
                | CATBSTR iValue) As StrParam
                | 
                |     Creates a string parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Example:
                |         This example creates the responsible string parameter and adds it to
                |         the newly created part:
                | 
                |           Set CATDocs = CATIA.Documents
                |           Set part1   = CATDocs.Add("CATPart")
                |           Set density = part1.Part.Parameters.CreateString ("responsible", "The Boss")

        :param str i_name:
        :param str i_value:
        :return: StrParam
        :rtype: StrParam
        """
        return StrParam(self.parameters.CreateString(i_name, i_value))

    def get_name_to_use_in_relation(self, i_object: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetNameToUseInRelation(AnyObject iObject) As CATBSTR
                | 
                |     Returns a correct name of a feature to use it in a relation.

        :param AnyObject i_object:
        :return: str
        :rtype: str
        """
        return self.parameters.GetNameToUseInRelation(i_object.com_object)

    def has_parameters(self):
        """
        :return: bool
        """
        if self.parameters.Count > 0:
            return True

        return False

    def is_parameter(self, index: cat_variant):
        """
        :param cat_variant index: parameter name or parameter number
        :return: bool
        :rtype: bool
        """
        try:
            if self.parameters.Item(index):
                return True
        except com_error:
            return False

    def item(self, index: cat_variant) -> any_parameter:
        """
        .. note::
            :class: toggle

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
                |    As a numeric, this index is the rank of the parameter
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


        :param cat_variant index:
        :return: any_parameter
        :rtype: any_parameter
        """

        p: any_parameter

        if not self.is_parameter(index):
            raise CATIAApplicationException(f'Could not find parameter name "{index}".')

        if isinstance(self.parameters.Item(index).value, bool):
            p = BoolParam(self.parameters.Item(index))

        elif isinstance(self.parameters.Item(index).value, int):
            p = IntParam(self.parameters.Item(index))

        elif isinstance(self.parameters.Item(index).value, str):
            p = StrParam(self.parameters.Item(index))

        elif isinstance(self.parameters.Item(index).value, float):
            p = RealParam(self.parameters.Item(index))

        else:

            raise CATIAApplicationException(f'Could not assign parameter name "{index}".')

        return p

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a parameter from the Parameters collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the parameter to remove from the
                |             collection of parameters. As a numerics, this index is the rank of the
                |             parameter in the collection. The index of the first parameter in the collection
                |             is 1, and the index of the last parameter is Count. As a string, it is the name
                |             you assigned to the parameter using the 
                | 
                |         AnyObject.Name property or when creating the parameter.
                |         
                |     Example:
                |         This example removes the "depth" parameter from the parameters
                |         collection.
                | 
                |          parameters.Remove("depth")

        :param cat_variant i_index:
        :return: None
        :rtype: None
        """
        return self.parameters.Remove(i_index)

    def sub_list(self, i_object: AnyObject, i_recursively: bool) -> 'Parameters':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func SubList(AnyObject iObject,
                | boolean iRecursively) As Parameters
                | 
                |     Returns a sub-collection of parameters aggregated to an
                |     object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object used to filter the whole parameter collection to get the
                |             resulting sub-collection. 
                |         iRecursively
                |             A flag to specify if children parameters are to be searched for in
                |             the returned collection 
                |         Example:
                |             This example shows how to retrieve a collection of parameters that
                |             are associated to a Pad.
                | 
                |              Dim Parameters1 As Parameters
                |              Set Parameters1 = CATIA.ActiveDocument.Part.Parameters gets the collection of parameters
                |                  in the part
                |              Dim Body0 As AnyObject
                |              Set Body0 = CATIA.ActiveDocument.Part.Bodies.Item  ( "MechanicalTool.1" ) 
                |              Dim Pad1 As AnyObject
                |              Set Pad1 = Body0.Shapes.Item  ( "Pad.1" ) gets the pad Pad.1
                |              Dim Parameters2 As Parameters
                |              Set Parameters2 = Parameters1.SubList(Pad1,TRUE) gets the collection of parameters that
                |                  are under the pad Pad.1

        :param AnyObject i_object:
        :param bool i_recursively:
        :return: Parameters
        :rtype: Parameters
        """
        return Parameters(self.parameters.SubList(i_object.com_object, i_recursively))

    def __getitem__(self, n: int) -> Parameter:
        if (n + 1) > self.count:
            raise StopIteration

        return Parameter(self.parameters.item(n + 1))

    def __iter__(self) -> Iterator[Parameter]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Parameters(name="{self.name}")'
