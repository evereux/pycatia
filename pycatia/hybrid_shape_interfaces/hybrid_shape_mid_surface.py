#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeMidSurface(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeMidSurface
                | 
                | Represents the hybrid shape MidSurface feature object.
                | Role: To access the data of the hybrid shape MidSurface feature
                | object.
                | This data includes:
                | 
                |     Support Body
                |     Creation Mode
                |     Threshold Thickness
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeMidSurface
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_mid_surface = com_object

    @property
    def auto_thickness_threshold(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AutoThicknessThreshold() As long
                | 
                |     Returns or sets AutoThicknessThreshold. Automatic Thickmess Threshold Check Button ON :1,
                |     OFF : 0 (Only Automatic Creation Mode Available for Automation)

        :rtype: int
        """

        return self.hybrid_shape_mid_surface.AutoThicknessThreshold

    @auto_thickness_threshold.setter
    def auto_thickness_threshold(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_mid_surface.AutoThicknessThreshold = value

    @property
    def creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CreationMode() As long
                | 
                |     Returns or sets CreationMode. Face Pairs : 0, Faces To Offset : 1, Automatic :
                |     2 (Only Automatic Creation Mode Available for Automation)

        :rtype: int
        """

        return self.hybrid_shape_mid_surface.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_mid_surface.CreationMode = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets Support Body. Reference.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_mid_surface.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_mid_surface.Support = reference_support.com_object

    @property
    def threshold(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Threshold() As Length
                | 
                |     Returns or sets Threshold Thickness. Length.

        :rtype: Length
        """

        return Length(self.hybrid_shape_mid_surface.Threshold)

    @threshold.setter
    def threshold(self, value: Length):
        """
        :param Length value:
        """

        self.hybrid_shape_mid_surface.Threshold = value

    def __repr__(self):
        return f'HybridShapeMidSurface(name="{self.name}")'
