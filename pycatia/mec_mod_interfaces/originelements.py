#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from pycatia.system_interfaces.base_object import AnyObject


class OriginElements(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the part's 3D reference axis system.It allows an easy
                | access to 3D reference axis system of a Part object thru the three
                | planes XY, YZ, and ZX.SeeactivateLinkAnchor('Part','','Part')for
                | parent object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.origin_elements = com_object

    @property
    def plane_xy(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PlaneXY
                | o Property PlaneXY(    ) As AnyObject  (Read Only)
                | 
                | Returns the XY plane of the part 3D reference axis system.
                |
                | Example:
                | The following example returns in plnXY the XY plane of the partRoot part
                | from the partDoc part document:
                | Set partRoot = partDoc.Part
                | Set plnXY = partRoot.originElements.PlaneXY

        :return: AnyObject()
        """
        return AnyObject(self.origin_elements.PlaneXY)

    @property
    def plane_yz(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PlaneYZ
                | o Property PlaneYZ(    ) As AnyObject  (Read Only)
                | 
                | Returns the YZ plane of the part 3D reference axis system.
                |
                | Example:
                | The following example returns in plnYZ the YZ plane of the partRoot part
                | from the partDoc part document:
                | Set partRoot = partDoc.Part
                | Set plnYZ = partRoot.originElements.PlaneYZ

        :return: AnyObject()
        """
        return AnyObject(self.origin_elements.PlaneYZ)

    @property
    def plane_zx(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PlaneZX
                | o Property PlaneZX(    ) As AnyObject (Read Only)
                | 
                | Returns the ZX plane of the part 3D reference axis system. Example:The
                | following example returns in plnZX the ZX plane of the partRoot part
                | from the partDoc part document:  Set partRoot = partDoc.Part Set plnZX
                | = partRoot.originElements.PlaneZX

        :return: AnyObject()
        """
        return AnyObject(self.origin_elements.PlaneZX)

    def __repr__(self):
        return f'OriginElements()'
