#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import TYPE_CHECKING

from pycatia.knowledge_interfaces.knowledge_activate_object import KnowledgeActivateObject
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.knowledge_interfaces.parameter import Parameter

class Relation(KnowledgeActivateObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             Relation
                | 
                | Represents the relation object.
                | It is an abstract object which is not intended to be created as such, but from
                | which the check, design table, formula, rule, objects derive.
                | 
                | See also:
                |     Check, DesignTable, Formula, Rule
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.relation = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Comment() As CATBSTR
                | 
                |     Returns or sets the comment associated with the relation. The comment
                |     explains the relation's purpose. It is passed as the second input argument of
                |     the relation creation methods of the Relations collection.
                | 
                |     Example:
                |         This example retrieves the maximummass relation comment and displays it
                |         in a message box:
                | 
                |          relcomment = maximummass.Comment
                |          MsgBox "maximummass comment : " & relcomment

        :rtype: str
        """

        return self.relation.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.relation.Comment = value

    @property
    def context(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Context() As AnyObject (Read Only)
                | 
                |     Returns the context of the parameter.
                |     The context of a parameter can be a part, a product, a drafting, or a
                |     process document, depending where the parameter is.
                | 
                |     Returns:
                |         The context 
                |     See also:
                |         Part, Product, CATIADrawing, CATIAProcess

        :rtype: AnyObject
        """

        return AnyObject(self.relation.Context)

    @property
    def nb_in_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property NbInParameters() As long (Read Only)
                | 
                |     Returns the number of input parameters of the relation.

        :rtype: int
        """

        return self.relation.NbInParameters

    @property
    def nb_out_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property NbOutParameters() As long (Read Only)
                | 
                |     Returns the number of output parameters of the relation.
                |     The output parameters of the relation are those constrained by the
                |     relation.

        :rtype: int
        """

        return self.relation.NbOutParameters

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Value() As CATBSTR (Read Only)
                | 
                |     Returns the definition of the relation. It returns an empty string if the
                |     relation is not an expressional one (for example for a design table). The
                |     definition is the body to be executed to compute one or several parameters. It
                |     is passed as the last input argument of the relation creation methods of the
                |     Relations collection.
                | 
                |     Example:
                |         This example retrieves the maximummass relation definition and displays
                |         it in a message box:
                | 
                |          reldef = maximummass.Value
                |          MsgBox "maximummass relation is defined as " & reldef

        :rtype: str
        """

        return self.relation.Value

    def get_in_parameter(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetInParameter(long iIndex) As AnyObject
                | 
                |     Returns an input parameter of the relation.
                |     This method can return an object that is not a parameter, that is, you
                |     cannot handle it as a Parameter object. For example, in a relation
                |     like
                | 
                |     Area.1 = area(PartBody/Pad.1/Sketch.1)
                | 
                |     the object PartBody/Pad.1/Sketch.1 is a sketch and not a
                |     parameter.
                |     To use such an object, call the Visual Basic TypeName function to retrieve
                |     its real type.
                | 
                |     Dim objectType
                |      objectType = TypeName(oParameter)
                |      If objectType = "Parameter" Then
                |      ...
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The searched input parameter index in the
                |             relation.
                |             Legal values: 1 ≤ iIndex ≤ 
                | 
                |         NbInParameters

        :param int i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.relation.GetInParameter(i_index))

    def get_out_parameter(self, i_index: int) -> 'Parameter':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetOutParameter(long iIndex) As Parameter
                | 
                |     Returns an output parameter of the relation. Use TypeName method on the
                |     returned parameter to get the real type of the parameter.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The searched input parameter index in the
                |             relation.
                |             Legal values: 1 ≤ iIndex ≤ 
                | 
                |         NbOutParameters

        :param int i_index:
        :rtype: Parameter
        """
        from pycatia.knowledge_interfaces.parameter import Parameter
        return Parameter(self.relation.GetOutParameter(i_index))

    def modify(self, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Modify(CATBSTR iValue)
                | 
                |     Modifies the relation.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The new relation value

        :param str i_value:
        :rtype: None
        """
        return self.relation.Modify(i_value)

    def rename(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Rename(CATBSTR iName)
                | 
                |     Renames the relation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The new relation name

        :param str i_name:
        :rtype: None
        """
        return self.relation.Rename(i_name)

    def __repr__(self):
        return f'Relation(name="{self.name}")'
