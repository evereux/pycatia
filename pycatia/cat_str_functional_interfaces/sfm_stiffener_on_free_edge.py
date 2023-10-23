#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_profile import SFMProfile
from pycatia.cat_str_functional_interfaces.sfm_welds import SFMWelds
from pycatia.in_interfaces.reference import Reference


class SFMStiffenerOnFreeEdge(SFMProfile):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrFunctionalInterfaces.SfmObject
                |                         CATStrFunctionalInterfaces.SfmProfile
                |                             SfmStiffenerOnFreeEdge
                | 
                | Interface to manage different attributes of Stiffener on free
                | edge.
                | Role: Provides access to Structural Functional Modeler's Stiffener on free
                | edge.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_stiffener_on_free_edge = com_object

    @property
    def free_edge_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FreeEdgeOffset() As double
                | 
                |     Returns or sets the SFE's Free Edge offset.
                | 
                |     Parameters:
                | 
                |         oOffset
                |             [out] The retrieved Free Edge offset. 
                |         iOffset
                |             [in] The input Free Edge offset. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves in Offset the Free Edge offset of the
                |             SfmStiffenerOnFreeEdge feature.
                | 
                |              Dim Offset As Double
                |              Set Offset = SfmStiffenerOnFreeEdge.FreeEdgeOffset

        :rtype: float
        """

        return self.sfm_stiffener_on_free_edge.FreeEdgeOffset

    @free_edge_offset.setter
    def free_edge_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_stiffener_on_free_edge.FreeEdgeOffset = value

    @property
    def section_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SectionAngle() As double
                | 
                |     Returns or sets the SFE's section angle.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             [out] The retrieved angle of the section of SFE. 
                |         iAngle
                |             [in] The retrieved angle of the section of SFE. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves in Angle the angle of the section of
                |             SfmStiffenerOnFreeEdge feature.
                | 
                |              Dim Angle As Double
                |              Set Angle = SfmStiffenerOnFreeEdge.SectionAngle

        :rtype: float
        """

        return self.sfm_stiffener_on_free_edge.SectionAngle

    @section_angle.setter
    def section_angle(self, value: float):
        """
        :param float value:
        """

        self.sfm_stiffener_on_free_edge.SectionAngle = value

    @property
    def side_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SideOrientation() As long
                | 
                |     Returns or sets the side orientation.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             [out] The retrieved Side Orientation of SFE. 
                |         iOrientation
                |             [in] The input Side Orientation of SFE. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves side orientation of the
                |             Stiffener.
                | 
                |              Dim Orient As Long
                |              Orient = SfmStiffenerOnFreeEdge.SideOrientation

        :rtype: int
        """

        return self.sfm_stiffener_on_free_edge.SideOrientation

    @side_orientation.setter
    def side_orientation(self, value: int):
        """
        :param int value:
        """

        self.sfm_stiffener_on_free_edge.SideOrientation = value

    def get_free_edge(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFreeEdge() As Reference
                | 
                |     Returns the Free Edge.
                | 
                |     Parameters:
                | 
                |         oFreeEdge
                |             [out] The retrieved Free Edge. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves in FreeEdge the Free Edge of the
                |             SfmStiffenerOnFreeEdge feature.
                | 
                |              Dim FreeEdge As Reference
                |              Set FreeEdge = SfmStiffenerOnFreeEdge.GetFreeEdge

        :rtype: Reference
        """
        return Reference(self.sfm_stiffener_on_free_edge.GetFreeEdge())

    def get_molded_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMoldedSurface() As Reference
                | 
                |     Returns the molded surface.
                | 
                |     Parameters:
                | 
                |         oMoldedSurface
                |             [out] The retrieved Molded Surface. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example retrieves MoldedSurface the molded surface of the
                |             SfmStiffenerOnFreeEdge feature.
                | 
                |              Dim MoldedSurface As Reference
                |              Set MoldedSurface = SfmStiffenerOnFreeEdge.GetMoldedSurface

        :rtype: Reference
        """
        return Reference(self.sfm_stiffener_on_free_edge.GetMoldedSurface())

    def get_welds(self, i_operating_ele: Reference) -> SFMWelds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWelds(Reference iOperatingEle) As SfmWelds
                | 
                |     Gets Welds feature on operated SFE.
                | 
                |     Parameters:
                | 
                |         iOperatingEle
                |             [in] Operating element of the weld features. 
                |         oWelds
                |             [out] The retrieved Weld features. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example gets welds features of Split SFE.
                | 
                |              Dim Welds As SfmWelds
                |              Set Welds = SplitSFE.GetWelds(Nothing)

        :param Reference i_operating_ele:
        :rtype: SFMWelds
        """
        return SFMWelds(self.sfm_stiffener_on_free_edge.GetWelds(i_operating_ele.com_object))

    def set_free_edge(self, i_free_edge: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFreeEdge(Reference iFreeEdge)
                | 
                |     Sets the Free Edge.
                | 
                |     Parameters:
                | 
                |         iFreeEdge
                |             [in] The input Free Edge. 
                | 
                |     Returns:
                |         S_OK if everything ran ok.
                | 
                |         Example:
                |             This example sets FreeEdge the Free Edge of the
                |             SfmStiffenerOnFreeEdge feature.
                | 
                |              Dim FreeEdge As Reference
                |              Set FreeEdge = SfmStiffenerOnFreeEdge.SetFreeEdge

        :param Reference i_free_edge:
        :rtype: None
        """
        return self.sfm_stiffener_on_free_edge.SetFreeEdge(i_free_edge.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_free_edge'
        # # vba_code = """
        # # Public Function set_free_edge(sfm_stiffener_on_free_edge)
        # #     Dim iFreeEdge (2)
        # #     sfm_stiffener_on_free_edge.SetFreeEdge iFreeEdge
        # #     set_free_edge = iFreeEdge
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMStiffenerOnFreeEdge(name="{self.name}")'
