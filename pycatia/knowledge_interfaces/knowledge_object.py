#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class KnowledgeObject(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeObject
                | 
                | Interface to access a CATIAKnowledgeObject.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.knowledge_object = com_object

    @property
    def hidden(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Hidden() As boolean
                | 
                |     Returns or sets wether the relation is hidden or should be hidden. or not.

        :rtype: bool
        """

        return self.knowledge_object.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        """
        :param bool value:
        """

        self.knowledge_object.Hidden = value

    @property
    def is_const(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property IsConst() As boolean
                | 
                |     Returns or sets wether the relation is Const or should be Const. or not.

        :rtype: bool
        """

        return self.knowledge_object.IsConst

    @is_const.setter
    def is_const(self, value: bool):
        """
        :param bool value:
        """

        self.knowledge_object.IsConst = value

    def __repr__(self):
        return f'KnowledgeObject(name="{ self.name }")'
