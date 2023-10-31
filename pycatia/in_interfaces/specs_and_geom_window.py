#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.specs_viewer import SpecsViewer
from pycatia.in_interfaces.window import Window


class SpecsAndGeomWindow(Window):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Window
                |                         SpecsAndGeomWindow
                | 
                | Represents a window featuring a specification viewer and a geometry
                | viewer.
                | The specification viewer is located in the left part of the window and displays
                | the document's specification tree. The geometry viewer is located in the right
                | part of the window and displays the document's geometry, and can thus be a
                | Viewer2D or a Viewer3D, according to the document type. Even if generally the
                | two viewers are simultaneously displayed, one viewer or the other can be hidden
                | thanks to the CatSpecsAndGeomWindowLayout enumeration.
                | 
                | See also:
                |     CatSpecsAndGeomWindowLayout
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.specs_and_geom_window = com_object

    @property
    def layout(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Layout() As CatSpecsAndGeomWindowLayout
                | 
                |     Returns or sets the specification and geometry window
                |     layout.
                | 
                |     Example:
                |         This example sets the specification and geometry window layout for the
                |         MyCADWindow window to catWindowGeomOnly.
                | 
                |          MyCADWindow.Layout = catWindowGeomOnly

        :return: enum cat_specs_and_geom_window_layout
        :rtype: int
        """

        return self.specs_and_geom_window.Layout

    @layout.setter
    def layout(self, value: int):
        """
        :param int value: enum cat_specs_and_geom_window_layout
        """

        self.specs_and_geom_window.Layout = value

    @property
    def specs_viewer(self) -> SpecsViewer:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SpecsViewer() As SpecsViewer (Read Only)
                | 
                |     Returns the specifications viewer.
                | 
                |     Example:
                |         This example retrieves the specification viewer for the MyCADWindow
                |         window.
                | 
                |          Dim MyViewer As Viewer
                |          Set MyViewer = MyCADWindow.SpecsViewer

        :rtype: SpecsViewer
        """

        return SpecsViewer(self.specs_and_geom_window.SpecsViewer)

    def __repr__(self):
        return f'SpecsAndGeomWindow(name="{self.name}")'
