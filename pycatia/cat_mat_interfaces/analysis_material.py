#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class AnalysisMaterial(AnyObject):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     AnalysisMaterial
            |
            | Represents an AnalysisMaterial object.
            | This object is used to manage the Analysis properties of a
            | material.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_material = com_object

    def get_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetType() As CATBSTR
                |
                |     Returns the analysis type (Ex: MATERIAL_ORTHOTROPIC, MATERIAL_ISOTROPIC).

        :rtype: str
        """
        return self.analysis_material.GetType()

    def get_value(self, i_label: str) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetValue(CATBSTR iLabel) As CATVariant
                |
                |     Returns an analysis value of the material. The name of the parameter is
                |     needed

        :param str i_label:
        :rtype: cat_variant
        """
        return self.analysis_material.GetValue(i_label)

    def put_value(self, i_label: str, i_value: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutValue(CATBSTR iLabel,
                | CATVariant iValue)
                |
                |     Sets an analysis value of the material. The name of the
                |     parameter is needed

        :param str i_label:
        :param cat_variant i_value:
        :rtype: None
        """
        return self.analysis_material.PutValue(i_label, i_value)

    def __repr__(self):
        return f'AnalysisMaterial(name="{self.name}")'
