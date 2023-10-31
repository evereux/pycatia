#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relation import Relation


class Law(Relation):

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
                |                             KnowledgeInterfaces.Relation
                |                                 Law
                | 
                | Represents the Law object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.law = com_object

    def add_formal_parameter(self, i_name: str, i_magnitude: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddFormalParameter(CATBSTR iName,
                | CATBSTR iMagnitude)
                | 
                |     Creates a formal parameter for the law.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the formal parameter. 
                |         iType
                |             The type name of the formal parameter.

        :param str i_name:
        :param str i_magnitude:
        :rtype: None
        """
        return self.law.AddFormalParameter(i_name, i_magnitude)

    def remove_formal_parameter(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveFormalParameter(CATBSTR iName)
                | 
                |     Removes a formal parameter of the law.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the formal parameter.

        :param str i_name:
        :rtype: None
        """
        return self.law.RemoveFormalParameter(i_name)

    def __repr__(self):
        return f'Law(name="{ self.name }")'
