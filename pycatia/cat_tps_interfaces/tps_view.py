#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.cat_tps_interfaces.annotations import Annotations
from pycatia.system_interfaces.any_object import AnyObject


class TPSView(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSView


    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_view = com_object

    @property
    def annotation_plane(self) -> tuple:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AnnotationPlane() As CATSafeArrayVariant (Read Only)
                |     Reads view annoation plane.
                |
                |     Parameters:
                |
                |         oMathPlane
                |             Mathematical plane definition of the View.

        :rtype: tuple
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.tps_view.AnnotationPlane

    @property
    def annotation_sketch(self) -> False:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AnnotationSketch(AnyObject Layout2DLView)
                |     Gets / Sets the annotation Sketch associated under the current
                |     View.
                |
                |     Parameters:
                |
                |         Layout2DLView
                |             2D Layout View used by current View as annotation sketch

        :rtype: False
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return None

    @annotation_sketch.setter
    def annotation_sketch(self, value: False):
        """
        :param False value:
        """

        self.tps_view.AnnotationSketch = value

    @property
    def annotations(self) -> Annotations:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Annotations() As Annotations (Read Only)
                |     Retrieves the TPS components of the View.
                |
                |     Parameters:
                |
                |         oAnnots
                |             Collection of returned component.

        :rtype: Annotations
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return Annotations(self.tps_view.Annotations)

    @property
    def display_ratio(self) -> False:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisplayRatio(double RatioValue)
                |     Sets / Gets the ratio of current View.
                |
                |     Parameters:
                |
                |         RatioValue
                |             Ratio applied to the View.

        :rtype: False
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return None

    @display_ratio.setter
    def display_ratio(self, value: False):
        """
        :param False value:
        """

        self.tps_view.DisplayRatio = value

    @property
    def view_type(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property ViewType() As long (Read Only)
                |     Gets view type.
                |
                |     Parameters:
                |
                |         oViewType
                |             The view type
                |             Legal values:
                |
                |                 1: Front View
                |                 2: Section View
                |                 3: Cut View

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.tps_view.ViewType

    def __repr__(self):
        return f'TpsView(name="{self.name}")'
