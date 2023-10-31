#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class OriginElements(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OriginElements
                | 
                | Represents the part's 3D reference axis system.
                | It allows an easy access to 3D reference axis system of a Part object thru the
                | three planes XY, YZ, and ZX.
                | See Part for parent object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.origin_elements = com_object

    @property
    def plane_xy(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PlaneXY() As AnyObject (Read Only)
                | 
                |     Returns the XY plane of the part 3D reference axis system.
                | 
                |     Example:
                |         The following example returns in plnXY the XY plane of the partRoot
                |         part from the partDoc part document:
                | 
                |          Set partRoot = partDoc.Part
                |          Set plnXY = partRoot.originElements.PlaneXY

        :rtype: AnyObject
        """

        return AnyObject(self.origin_elements.PlaneXY)

    @property
    def plane_yz(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PlaneYZ() As AnyObject (Read Only)
                | 
                |     Returns the YZ plane of the part 3D reference axis system.
                | 
                |     Example:
                |         The following example returns in plnYZ the YZ plane of the partRoot
                |         part from the partDoc part document:
                | 
                |          Set partRoot = partDoc.Part
                |          Set plnYZ = partRoot.originElements.PlaneYZ

        :rtype: AnyObject
        """

        return AnyObject(self.origin_elements.PlaneYZ)

    @property
    def plane_zx(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PlaneZX() As AnyObject (Read Only)
                | 
                |     Returns the ZX plane of the part 3D reference axis system.
                | 
                |     Example:
                |         The following example returns in plnZX the ZX plane of the partRoot
                |         part from the partDoc part document:
                | 
                |          Set partRoot = partDoc.Part
                |          Set plnZX = partRoot.originElements.PlaneZX

        :rtype: AnyObject
        """

        return AnyObject(self.origin_elements.PlaneZX)

    def __repr__(self):
        return f'OriginElements(name="{ self.name }")'
