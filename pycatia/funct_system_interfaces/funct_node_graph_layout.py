#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.functional_facet import FunctionalFacet


class FunctNodeGraphLayout(FunctionalFacet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATFunctSystemItf.FunctionalFacet
                |                         FunctNodeGraphLayout
                | 
                | Represents a CATIAFunctNodeGraphLayout.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.funct_node_graph_layout = com_object

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Height() As double (Read Only)
                | 
                |     Returns the Height coordinate.

        :rtype: float
        """

        return self.funct_node_graph_layout.Height

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Width() As double (Read Only)
                | 
                |     Returns the Width coordinate.

        :rtype: float
        """

        return self.funct_node_graph_layout.Width

    def set_height_and_width(self, i_height: float, i_width: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetHeightAndWidth(double iHeight,
                | double iWidth)
                | 
                |     Sets the height and width.
                | 
                |     Parameters:
                | 
                |         iHeight
                |             the height value. 
                |         iWidth
                |             the width value.

        :param float i_height:
        :param float i_width:
        :rtype: None
        """
        return self.funct_node_graph_layout.SetHeightAndWidth(i_height, i_width)

    def __repr__(self):
        return f'FunctNodeGraphLayout(name="{self.name}")'
