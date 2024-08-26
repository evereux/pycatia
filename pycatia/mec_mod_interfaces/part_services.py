#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.in_interfaces.references import References
from pycatia.system_interfaces.any_object import AnyObject


class PartServices(AnyObject):
    """

    Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PartServices
                |
                | The object exposes services for the part.
                |
                | This object is available thanks to Part Set myPart = CATIA.ActiveDocument.Part ' Get Service Object by querying on part - extension of CATIA Base Set partServices = myPart.GetItem("CATPartServices")
                |
                | Example:
                |
                |    Set part1 = CATIA.ActiveDocument.Part
                |    Set partServices1 = myPart.GetItem("CATPartServices")

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.part_services = com_object

    def get_near_sub_elements(
            self,
            i_object: AnyObject,
            i_sub_element_dimension: int,
            i_near_object: AnyObject
    ) -> References:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetNearSubElements(AnyObject iObject,long iSubElementDimension,AnyObject
                | iNearObject) As References
                |     Get the sub elements of a geometric object or a body that are the closest
                |     to a geometric object or a body.
                |
                |     Parameters:
                |
                |         iObject
                |             A geometric object or a body
                |         iSubElementDimension
                |             The dimension of sub elements wanted: 0 for vertex, 1 for edge, 2
                |             for face.
                |         iNearObject
                |             A geometric object or a body to be close to
                |         oSubElements
                |             List of the sub elements of iObject (without duplicates) closest to
                |             iNearObject.
                |
                |             Example:
                |                 The following example returns the vertices of a pad that are
                |                 the closest to a point.
                |
                |                   Set part1 = CATIA.ActiveDocument.Part
                |                   Set bodies1 = part1.Bodies
                |                   Set body1 = bodies1.Item("PartBody")
                |                   Set shapes1 = body1.Shapes
                |                   Set pad1 = shapes1.Item("Pad.1")
                |                   Set point1 = shapes1.Item("Point.1")
                |                   Set partServices1 = myPart.GetItem("CATPartServices")
                |                   Set references1 = partServices1.GetSubNearElements(pad1, 0, point1)

        :param AnyObject i_object:
        :param int i_sub_element_dimension:
        :param AnyObject i_near_object:
        :rtype: References
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return References(
            self.part_services.GetNearSubElements(
                i_object.com_object,
                i_sub_element_dimension,
                i_near_object.com_object
            )
        )

    def get_sub_elements(self, i_object: AnyObject, i_sub_element_dimension: int, i_duplicates: bool) -> References:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetSubElements(AnyObject iObject,long iSubElementDimension,boolean
                | iDuplicates) As References
                |     Get the sub elements of a geometric object or a body.
                |
                |     Parameters:
                |
                |         iObject
                |             A geometric object or a body
                |         iSubElementDimension
                |             The dimension of sub elements wanted: 0 for vertex, 1 for edge, 2
                |             for face.
                |         iDuplicates
                |             Allow duplicate sub elements in the list. FALSE will remove
                |             duplicates (same label and selecting feature).
                |         oSubElements
                |             List of the sub elements
                |
                |             Example:
                |                 The following example returns the vertices of a
                |                 pad
                |
                |                   Set part1 = CATIA.ActiveDocument.Part
                |                   Set bodies1 = part1.Bodies
                |                   Set body1 = bodies1.Item("PartBody")
                |                   Set shapes1 = body1.Shapes
                |                   Set pad1 = shapes1.Item("Pad.1")
                |                   Set partServices1 = myPart.GetItem("CATPartServices")
                |                   Set references1 = partServices1.GetSubElements(pad1, 0, True)

        :param AnyObject i_object:
        :param int i_sub_element_dimension:
        :param bool i_duplicates:
        :rtype: References
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return References(self.part_services.GetSubElements(i_object.com_object, i_sub_element_dimension, i_duplicates))

    def __repr__(self):
        return f'PartServices(name="{self.name}")'
