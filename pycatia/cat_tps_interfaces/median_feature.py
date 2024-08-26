#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject


class MedianFeature(AnyObject):
    """

    Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MedianFeature
                |
                | Interface for accessing Median Feature modifier on a Semantic GDT (ISO Standard
                | only).

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.median_feature = com_object

    @property
    def modifier(self) -> str:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Modifier() As CATBSTR (Read Only)
                |     Retrieves Median Feature modifier display.
                |     Empty string is returned if modifier not applied; this could suggest that
                |     either:
                |     _ Median Feature modifier display has been formally switched
                |     off,
                |     _ Median Feature is not displayed if Dimension of Visualization is existing
                |     for given GDT.

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.median_feature.Modifier

    def __repr__(self):
        return f'MedianFeature(name="{self.name}")'
