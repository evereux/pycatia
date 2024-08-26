#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.cat_tps_interfaces.semantic_gdt_common_zone import SemanticGDTCommonZone
from pycatia.system_interfaces.any_object import AnyObject


class SemanticGDTNxDisplay(AnyObject):
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
                |                     SemanticGDTNxDisplay
                |
                | Interface to distinguish Collection of features from Separate features
                | GDT.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.semantic_gdt_nx_display = com_object

    @property
    def instance_count(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property InstanceCount() As long (Read Only)
                |     Gets count of instances.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt_nx_display.InstanceCount

    def common_zone(self) -> SemanticGDTCommonZone:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func CommonZone() As SemanticGDTCommonZone
                |     Gets the GDT on the Common Zone interface to access CZ modifier
                |     information. Method is only returning a valid object if ISO Standard is
                |     applied.
                |
                |     Parameters:
                |
                |         oCommonZone
                |             Common Zone related information.

        :rtype: SemanticGDTCommonZone
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return SemanticGDTCommonZone(self.semantic_gdt_nx_display.CommonZone())

    def is_a_collection(self) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func IsACollection() As boolean
                |     Checks if GDT is Collection of Features. In ISO Standard, GDT may have a CZ
                |     modifier on tolerance value.
                |
                |     Parameters:
                |
                |         oIsColl
                |
                |                 TRUE: The GDT is applied on several elements considered as a
                |                 collection
                |                 FALSE: The GDT is not applied with a collection consideration.
                |                 It must be a separate.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt_nx_display.IsACollection()

    def is_a_separate(self) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func IsASeparate() As boolean
                |     Checks if GDT is Separate Features. In ASME Standard this is indicated with
                |     the "INDIVIDUALLY" text linked to the GDT.
                |
                |     Parameters:
                |
                |         oIsSeparate
                |
                |                 TRUE: The GDT is applied on several elements as many separate
                |                 specifications.
                |                 FALSE: The GDT is not applied with a separate consideration. It
                |                 must be a collection.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt_nx_display.IsASeparate()

    def __repr__(self):
        return f'SemanticGdtNxDisplay(name="{self.name}")'
