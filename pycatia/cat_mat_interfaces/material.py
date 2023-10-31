#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.cat_mat_interfaces.analysis_material import AnalysisMaterial
from pycatia.cat_rma_interfaces.rendering_material import RenderingMaterial
from pycatia.system_interfaces.any_object import AnyObject


class Material(AnyObject):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     Material
            |
            | Represents a Material object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.material = com_object

    @property
    def analysis_material(self) -> AnalysisMaterial:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisMaterial() As AnalysisMaterial (Read Only)
                |
                |     Returns the analysis material object from the current
                |     material.

        :rtype: AnalysisMaterial
        """
        return AnalysisMaterial(self.material.AnalysisMaterial)

    @property
    def rendering_material(self) -> RenderingMaterial:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RenderingMaterial() As RenderingMaterial (Read
                | Only)
                |
                |     Returns the rendering material object from the current
                |     material.

        :rtype: RenderingMaterial
        """
        return RenderingMaterial(self.material.RenderingMaterial)

    def copy_rendering_data_from(self, i_rendering_material: RenderingMaterial) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CopyRenderingDataFrom(RenderingMaterial
                | iRenderingMaterial)
                |
                |     Copy rendering data from a material to the current
                |     material.

        :param RenderingMaterial i_rendering_material:
        :rtype: None
        """
        return self.material.CopyRenderingDataFrom(i_rendering_material.com_object)

    def create_analysis_data(self, i_label: str) -> AnalysisMaterial:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateAnalysisData(CATBSTR iLabel) As
                | AnalysisMaterial
                |
                |     Create a default analysis material on the current
                |     material.

        :param str i_label:
        :rtype: AnalysisMaterial
        """
        return AnalysisMaterial(self.material.CreateAnalysisData(i_label))

    def create_rendering_data(self) -> RenderingMaterial:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateRenderingData() As RenderingMaterial
                |
                |     Create a default rendering material on the current
                |     material.

        :rtype: RenderingMaterial
        """
        return RenderingMaterial(self.material.CreateRenderingData())

    def exist_analysis_data(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ExistAnalysisData() As short
                |
                |     Returns true if a analysis material exists on the current
                |     material.

        :rtype: int
        """
        return self.material.ExistAnalysisData()

    def exist_rendering_data(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ExistRenderingData() As short
                |
                |     Returns true if a rendering material exists on the current
                |     material.

        :rtype: int
        """
        return self.material.ExistRenderingData()

    def get_icon(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetIcon(CATBSTR iPath)
                | 
                |     Write the icon of a material to disc. The parameter is the
                |     path of the folder where the JPEG is going to be written
                |     Ex : E:\\folder\\

        :param str i_path:
        :rtype: None
        """
        return self.material.GetIcon(i_path)

    def put_icon(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutIcon(CATBSTR iPath)
                | 
                |     Read the icon of a material from JPEG file. The parameter
                |     is the path of the folder where the JPEG is going to be
                |     read Ex : E:\\folder\\

        :param str i_path:
        :rtype: None
        """
        return self.material.PutIcon(i_path)

    def __repr__(self):
        return f'Material(name="{self.name}")'
