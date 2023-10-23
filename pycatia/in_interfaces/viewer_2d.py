#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.viewer import Viewer
from pycatia.in_interfaces.viewpoint_2d import Viewpoint2D


class Viewer2D(Viewer):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Viewer
                |                         Viewer2D
                | 
                | Represents a 2D viewer.
                | The 2D viewer aggregates a 2D viewpoint to display a 2D scene.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewer_2d = com_object

    @property
    def viewpoint_2d(self) -> Viewpoint2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viewpoint2D() As Viewpoint2D
                | 
                |     Returns or sets the 2D viewpoint of a 2D viewer.
                | 
                |     Example:
                |         This example retrieves the Nice2DViewpoint 2D viewpoint from the
                |         My2DViewer 2D viewer.
                | 
                |          Dim Nice2DViewpoint As Viewpoint2D
                |          Set Nice2DViewpoint = My2DViewer.Viewpoint2D

        :rtype: Viewpoint2D
        """

        return Viewpoint2D(self.viewer_2d.Viewpoint2D)

    @viewpoint_2d.setter
    def viewpoint_2d(self, value: Viewpoint2D):
        """
        :param Viewpoint2D value:
        """

        self.viewer_2d.Viewpoint2D = value

    def __repr__(self):
        return f'Viewer2D(name="{self.name}")'
