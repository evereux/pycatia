#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_mat_interfaces.material import Material


class PositionedMaterial(AnyObject):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     PositionedMaterial
            |
            | Represents a Positioned Material object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.positioned_material = com_object

    @property
    def application_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplicationMode() As short (Read Only)
                |
                |     Returns the application mode of the material.
                |
                |         Possible mode values are:
                |         0: Material has been applied as a copy on the
                |         geometrical object
                |         1: Material has been applied as a link on the
                |         geometrical object

        :rtype: int
        """

        return self.positioned_material.ApplicationMode

    @property
    def inheritance_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InheritanceMode() As short
                |
                |     Returns or sets the inheritance mode of an applied
                |     material.
                |
                |         Possible inheritance mode values are:
                |         0: The material is propagated towards its children
                |         1: The material is not propagated towards its children
                |         2: The material do not accept material propagated by
                |            its father (forced mode)

        :rtype: int
        """

        return self.positioned_material.InheritanceMode

    @inheritance_mode.setter
    def inheritance_mode(self, value: int):
        """
        :param int value:
        """

        self.positioned_material.InheritanceMode = value

    @property
    def material(self) -> Material:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Material() As Material (Read Only)
                |
                |     Returns the material object from the current positioned
                |     material.

        :rtype: Material
        """

        return Material(self.positioned_material.Material)

    def __repr__(self):
        return f'PositionedMaterial(name="{self.name}")'
