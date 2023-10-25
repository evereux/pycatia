#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.viewer_2d import Viewer2D


class SpecsViewer(Viewer2D):
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
                |                         InfInterfaces.Viewer2D
                |                             SpecsViewer
                | 
                | Represents the specification tree viewer.
                | This viewer displays the document's specification tree according to the chosen
                | layout, and can only be included in a SpecsAndGeomWindow
                | object.
                | 
                | See also:
                |     CatSpecsLayout, SpecsAndGeomWindow
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.specs_viewer = com_object

    @property
    def layout(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Layout() As CatSpecsLayout
                | 
                |     Returns or sets the specification tree layout.
                | 
                |     Example:
                |         This example sets the specification tree layout for the SpecsTreeViewer
                |         specification tree viewer to
                |         catSpecsViewerHorizontalCentered.
                | 
                |          SpecsTreeViewer.Layout = catSpecsViewerHorizontalCentered

        :return: enum cat_specs_layout
        :rtype: int
        """

        return self.specs_viewer.Layout

    @layout.setter
    def layout(self, value: int):
        """
        :param int value: enum cat_specs_layout
        """

        self.specs_viewer.Layout = value

    def __repr__(self):
        return f'SpecsViewer(name="{self.name}")'
