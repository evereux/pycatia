#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Fillet(DressUpShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Fillet
                | 
                | Represents the fillet shape.
                | It is the base object for face fillets and edge fillets.
                | 
                | See also:
                |     FaceFillet, EdgeFillet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fillet = com_object

    @property
    def fillet_boundary_relimitation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FilletBoundaryRelimitation() As
                | CatFilletBoundaryRelimitation
                | 
                |     Returns or sets the fillet boundary relimitation mode. This boundary
                |     relimitation mode is used when computing the fillet.
                | 
                |     Example:
                |         The following example returns in mode the fillet boundary relimitation
                |         mode of the firstFillet fillet, and then sets it to
                |         catMinimumFilletBoundaryRelimitation, so that the fillet expands up to the
                |         limits of the smallest shell:
                | 
                |          Set mode = firstFillet.FilletBoundaryRelimitation
                |          Set FirstFillet.FilletBoundaryRelimitation = catMinimumFilletBoundaryRelimitation

        :return: enum cat_fillet_boundary_relimitation
        :rtype: int
        """

        return self.fillet.FilletBoundaryRelimitation

    @fillet_boundary_relimitation.setter
    def fillet_boundary_relimitation(self, value: int):
        """
        :param int value: enum cat_fillet_boundary_relimitation
        """

        self.fillet.FilletBoundaryRelimitation = value

    @property
    def fillet_trim_support(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FilletTrimSupport() As CatFilletTrimSupport
                | 
                |     Returns or sets the fillet Trim Support mode. This Trim Support mode is
                |     used when computing the fillet.
                | 
                |     Example:
                |         The following example returns in mode the fillet Trim Support mode of
                |         the firstFillet fillet, and then sets it to catMinimumFilletTrimSupport, so
                |         that the fillet expands up to the limits of the smallest
                |         shell:
                | 
                |          Set mode = firstFillet.FilletTrimSupport
                |          Set FirstFillet.FilletTrimSupport = catNoTrimFilletSupport

        :return: enum cat_fillet_trim_support
        :rtype: int
        """

        return self.fillet.FilletTrimSupport

    @fillet_trim_support.setter
    def fillet_trim_support(self, value: int):
        """
        :param int value: enum cat_fillet_trim_support
        """

        self.fillet.FilletTrimSupport = value

    def __repr__(self):
        return f'Fillet(name="{self.name}")'
