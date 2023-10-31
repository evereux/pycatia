#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.assembly_interfaces.assembly_feature import AssemblyFeature
from pycatia.knowledge_interfaces.parameter import Parameter


class StrCutback(AssemblyFeature):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATAssemblyInterfaces.AssemblyFeature
                |                         StrCutback
                | 
                | Represents the cutback object.
                | It is aggregated to an extremity of a member. It can be retrieved using the
                | StrMemberExtremity object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_cutback = com_object

    @property
    def offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Offset() As Parameter (Read Only)
                | 
                |     Returns the parameter defining the offset.

        :rtype: Parameter
        """

        return Parameter(self.str_cutback.Offset)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CatStrCutbackType (Read Only)
                | 
                |     Returns the type of the cutback object.
                | 
                |     Example:
                |         This example retrieves the type for the StrMember
                |         object.
                | 
                |          Type = Member.Type

        :return: enum cat_str_cutback_type
        :rtype: int
        """

        return self.str_cutback.Type

    def __repr__(self):
        return f'StrCutback(name="{self.name}")'
