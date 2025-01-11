#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject


class NonSemanticDatumTarget(AnyObject):
    """

    Introduced in V5-6R2017.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NonSemanticDatumTarget
                | 
                | Interface Managing Non Semantic Datum Target.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_datum_target = com_object

    @property
    def low_label(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LowLabel() As CATBSTR
                | 
                |     Retrieves or sets Lower Label.

        :rtype: str
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return self.non_semantic_datum_target.LowLabel

    @low_label.setter
    def low_label(self, value: str):
        """
        :param str value:
        """

        self.non_semantic_datum_target.LowLabel = value

    @property
    def type_specifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TypeSpecifier() As CATBSTR
                | 
                |     Retrieves or sets the type of specifier.
                |     Legal values:
                | 
                |         None
                |         Square
                |         Diameter

        :rtype: str
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return self.non_semantic_datum_target.TypeSpecifier

    @type_specifier.setter
    def type_specifier(self, value: str):
        """
        :param str value:
        """

        self.non_semantic_datum_target.TypeSpecifier = value

    @property
    def up_label(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UpLabel() As CATBSTR
                | 
                |     Retrieves or sets Upper Label.

        :rtype: str
        """
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return self.non_semantic_datum_target.UpLabel

    @up_label.setter
    def up_label(self, value: str):
        """
        :param str value:
        """

        self.non_semantic_datum_target.UpLabel = value

    def __repr__(self):
        return f'NonSemanticDatumTarget(name="{self.name}")'
