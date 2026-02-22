#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2026-02-21 14:49:57.443389

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam


class HybridShapePlaneBetween(Plane):
    """

    Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneBetween


    """

    def __init__(self, com_object):
        super().__init__(com_object)

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.com_object = com_object

    @property
    def first_element(self) -> Reference:
        """

        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)
                | Property FirstElement() As Reference
                |     Returns or sets the first reference Plane.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                |
                |     Example:
                |         This example retrieves in RefPlane1 the first reference Plane for the
                |         PlaneBetween hybrid shape feature.
                |
                |          Dim RefPlane1 As Reference
                |          Set RefPlane1 = PlaneBetween.FirstPlane

        :rtype: Reference
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return Reference(self.com_object.FirstElement)

    @first_element.setter
    def first_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.com_object.FirstElement = value

    @property
    def orientation(self) -> int:
        """
        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)
                | Property Orientation() As long
                |     Returns or sets the orientation. Role:
                |     Orientation = 1 means that distance is measured from the second Plane
                |
                |     Example:
                |         This example retrieves in Orient the orientation for the PlaneBetween
                |         hybrid shape feature.
                |
                |          Dim Orient As long
                |          Set Orient = PlaneBetween.Orientation

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.com_object.Orientation = value

    @property
    def ratio(self) -> RealParam:
        """
        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)
                | Property Ratio() As RealParam (Read Only)
                |     Get the ratio. Role:
                |     if d1 is the distance between the first Plane and the created Plane, and d2 is the distance between the first Plane and the second Plane, then ratio = d1/d2.
                |
                |     Example:
                |         This example retrieves in ratio the orientation for the PlaneBetween
                |         hybrid shape feature.
                |
                |          Dim ratio  As CATIARealParam
                |          Get ratio = PlaneBetween.Ratio

        :rtype: RealParam
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return RealParam(self.com_object.Ratio)

    @property
    def second_element(self) -> Reference:
        """

        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)
                | Property SecondElement() As Reference
                |     Returns or sets the second reference Plane.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                |
                |     Example:
                |         This example retrieves in RefPlane2 the second reference Plane for the
                |         PlaneBetween hybrid shape feature.
                |
                |          Dim RefPlane2 As Reference
                |          Set RefPlane2 = PlaneBetween.SecondPlane

        :rtype: Reference
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return Reference(self.com_object.SecondElement)

    @second_element.setter
    def second_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.com_object.SecondElement = value

    def __repr__(self):
        return f'HybridShapePlaneBetween(name="{self.name}")'
