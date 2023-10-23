#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relation import Relation
from pycatia.system_interfaces.any_object import AnyObject


class Parameter(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Parameter
                | 
                | Represents the parameter.
                | It can be computed from a relation: formula, program, or check. It is an
                | abstract object which is not intended to be created as such, but from which the
                | integer, bolean, real, and string parameters derive. Here is an example to
                | create one:
                | 
                | 	Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim density As RealParam
                |  Set density = part1.Part.Parameters.CreateReal("density", 2.5)
                |  
                | 
                | See also:
                |     IntParam, BoolParam, RealParam, StrParam, Formula, Rule, Check
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameter = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Comment() As CATBSTR
                | 
                |     Returns or sets the parameter object comment.

        :rtype: str
        """

        return self.parameter.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.parameter.Comment = value

    @property
    def context(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Context() As AnyObject (Read Only)
                | 
                |     Returns the context of the parameter : a part, a product, a drafting, a process, depending where
                |     the parameter is.

        :rtype: AnyObject
        """

        return AnyObject(self.parameter.Context)

    @property
    def hidden(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Hidden() As boolean
                | 
                |     Returns or sets whether the parameter is hidden or should be hidden or not.

        :rtype: bool
        """

        return self.parameter.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        """
        :param bool value:
        """

        self.parameter.Hidden = value

    @property
    def is_true_parameter(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property IsTrueParameter() As boolean (Read Only)
                | 
                |     Returns a boolean saying if the parameter is a true one (real, dimension,
                |     string, etc.) or a geometrical one (isolated points, curves, surfaces).

        :rtype: bool
        """

        return self.parameter.IsTrueParameter

    @property
    def optional_relation(self) -> Relation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property OptionalRelation() As Relation (Read Only)
                | 
                |     Returns the relation that can be used to compute the parameter. As this
                |     relation might not exist, NULL may be returned, so a test is
                |     required.
                | 
                |     Example:
                |         This example checks if there is a relation to compute the param1
                |         parameter, and if no relation exists, displays a message
                |         box:
                | 
                |          Set param1_rel = param1.OptionalRelation
                |          If param1_rel is Nothing Then
                |               MsgBox "No relation to compute param1"
                |          End If

        :rtype: Relation
        """

        return Relation(self.parameter.OptionalRelation)

    @property
    def read_only(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ReadOnly() As boolean (Read Only)
                | 
                |     Returns whether the parameter can be modified.
                | 
                |     Example:
                |         This example checks if the param1 parameter can be modified, and if it
                |         cannot, displays a message box:
                | 
                |          If ( param1.ReadOnly ) Then
                |               MsgBox "No way to change param1"
                |          End If

        :rtype: bool
        """

        return self.parameter.ReadOnly

    @property
    def renamed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Renamed() As boolean (Read Only)
                | 
                |     Returns a boolean saying if the parameter is a renamed parameter or not.

        :rtype: bool
        """

        return self.parameter.Renamed

    @property
    def user_access_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UserAccessMode() As long (Read Only)
                | 
                |     Returns the user access mode of the parameter. 
                | 
                | 0
                |     Read only parameter (cannot be destroyed). 
                | 1
                |     Read/write parameter (cannot be destroyed). 
                | 2
                |     User parameter (can be read, written and destroyed).
                |     Methods
                | 
                | o Sub Rename(CATBSTR iName)
                | 
                |     Renames the parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             The new name of the parameter. If iName contains "Local:" prefix
                |             the rename will affect the local name. If not, it will affect the global name.
                |             
                | 
                |     Example:
                |         This example renames the param1 parameter to
                |         PartSeatbodyMinimumThickness:
                | 
                |          Call param1.Rename("PartSeatbodyMinimumThickness")
                |          
                | 
                | o Sub ValuateFromString(CATBSTR iValue)
                | 
                |     Valuates a parameter using a string as input. The string depends on
                |     parameter nature :
                | 
                |     "True" or "False" for Boolean
                | 
                |     a numerical value for Integer or Real
                | 
                |     a numerical value with or without a unit for Dimension
                | 
                |     Parameters:
                | 
                |         iValue
                |             The value to assign to the dimension parameter 
                | 
                |     Example:
                |         This example sets the value of the existing dimension parameter to a
                |         new value:
                | 
                |          dimension.ValuateFromString("300mm");
                |          
                | 
                | o Func ValueAsString() As CATBSTR
                | 
                |     Returns the value of the parameter as a string.
                | 
                | Example:
                |     This example gets the value of the existing dimension parameter and shows
                |     it in a message box
                | 
                |      Dim str
                |      str = dimension.ValueAsString;
                |      MessageBox str
                |      
                | 
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :rtype: int
        """

        return self.parameter.UserAccessMode

    def rename(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Rename(CATBSTR iName)
                |
                |     Renames the parameter.
                |
                |     Parameters:
                |
                |         iName
                |             The new name of the parameter. If iName contains "Local:" prefix
                |             the rename will affect the local name. If not, it will affect the global name.
                |
                |
                |     Example:
                |         This example renames the param1 parameter to
                |         PartSeatbodyMinimumThickness:
                |
                |          Call param1.Rename("PartSeatbodyMinimumThickness")

        :param str i_name:
        :rtype: None
        """
        return self.parameter.Rename(i_name)

    def valuate_from_string(self, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ValuateFromString(CATBSTR iValue)
                |
                |     Valuates a parameter using a string as input. The string depends on
                |     parameter nature :
                |
                |     "True" or "False" for Boolean
                |
                |     a numerical value for Integer or Real
                |
                |     a numerical value with or without a unit for Dimension
                |
                |     Parameters:
                |
                |         iValue
                |             The value to assign to the dimension parameter
                |
                |     Example:
                |         This example sets the value of the existing dimension parameter to a
                |         new value:
                |
                |          dimension.ValuateFromString("300mm");

        :param str i_value:
        :rtype: None
        """
        return self.parameter.ValuateFromString(i_value)

    def value_as_string(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ValueAsString() As CATBSTR
                |
                |     Returns the value of the parameter as a string.
                |
                | Example:
                |     This example gets the value of the existing dimension parameter and shows
                |     it in a message box
                |
                |      Dim str
                |      str = dimension.ValueAsString;
                |      MessageBox str
                |
                |
                |     Copyright © 1999-2011, Dassault Systèmes. All rights
                |     reserved.

        :rtype: str
        """
        return self.parameter.ValueAsString()

    def __repr__(self):
        return f'Parameter(name="{self.name}")'
