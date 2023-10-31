#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class Export3DXmlSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         Export3DXmlSettingAtt
                | 
                | Represents a setting controller for the 3D XML export
                | settings.
                | Role: This interface is implemented by a component which represents the
                | controller of the 3D XML export settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.export_3d_xml_setting_att = com_object

    @property
    def alternate_view(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AlternateView() As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.get_DesignReview Returns or sets the alternate view
                |         activation flag.
                | 
                |         Example:
                |             This example activates the alternate view export.
                | 
                |               
                |               export3DXmlSettingAtt.AlternateView = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.AlternateView

    @alternate_view.setter
    def alternate_view(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.AlternateView = value

    @property
    def animation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Animation() As boolean
                | 
                |     Returns or sets the animation activation flag.
                | 
                |     Example:
                |         This example activates the animation export.
                | 
                |           
                |           export3DXmlSettingAtt.Animation = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.Animation

    @animation.setter
    def animation(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.Animation = value

    @property
    def annotated_view(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotatedView() As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.get_DesignReview Returns or sets the annotated view
                |         activation flag.
                | 
                |         Example:
                |             This example activates the annotated view export.
                | 
                |               
                |               export3DXmlSettingAtt.AnnotatedView = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.AnnotatedView

    @annotated_view.setter
    def annotated_view(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.AnnotatedView = value

    @property
    def annotation_3d(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Annotation3D() As boolean
                | 
                |     Returns or sets the 3D annotation activation flag.
                | 
                |     Example:
                |         This example activates the 3D annotation export.
                | 
                |           
                |           export3DXmlSettingAtt.Annotation3D = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.Annotation3D

    @annotation_3d.setter
    def annotation_3d(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.Annotation3D = value

    @property
    def design_review(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DesignReview() As boolean
                | 
                |     Returns or sets the Design Review activation flag.
                | 
                |     Example:
                |         This example activates the Design Review export.
                | 
                |           
                |           export3DXmlSettingAtt.DesignReview = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.DesignReview

    @design_review.setter
    def design_review(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.DesignReview = value

    @property
    def geometry_representation_format(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GeometryRepresentationFormat() As
                | Cat3DXmlGeomRepresentationType
                | 
                |     Returns or sets the format of geometry representation.
                | 
                |     Example:
                |         This example sets the representation format to the exact
                |         mode.
                | 
                |           
                |           export3DXmlSettingAtt.GeometryRepresentationFormat = cat3DXmlExact

        :return: enum cat_3d_xml_geom_representation_type
        :rtype: int
        """

        return self.export_3d_xml_setting_att.GeometryRepresentationFormat

    @geometry_representation_format.setter
    def geometry_representation_format(self, value: int):
        """
        :param int value:
        """

        self.export_3d_xml_setting_att.GeometryRepresentationFormat = value

    @property
    def measure(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Measure() As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.get_DesignReview Returns or sets the measure activation
                |         flag.
                | 
                |         Example:
                |             This example activates the measure export.
                | 
                |               
                |               export3DXmlSettingAtt.Measure = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.Measure

    @measure.setter
    def measure(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.Measure = value

    @property
    def ppr_save_config(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PPRSaveConfig() As Cat3DXmlPPRSaveConfig
                | 
                |     Returns or sets the PPR config.
                | 
                |     Example:
                |         This example sets the PPR config. Product And resources export is
                |         acivated.
                | 
                |           
                |           export3DXmlSettingAtt.PPRSaveConfig = cat3DXmlProductAndResourceList

        :return: enum cat_3d_xml_ppr_save_config
        :rtype: int
        """

        return self.export_3d_xml_setting_att.PPRSaveConfig

    @ppr_save_config.setter
    def ppr_save_config(self, value: int):
        """
        :param int value: enum cat_3d_xml_ppr_save_config
        """

        self.export_3d_xml_setting_att.PPRSaveConfig = value

    @property
    def presentation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Presentation() As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.get_DesignReview Returns or sets the presentation
                |         activation flag.
                | 
                |         Example:
                |             This example activates the presentation export.
                | 
                |               
                |               export3DXmlSettingAtt.Presentation = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.Presentation

    @presentation.setter
    def presentation(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.Presentation = value

    @property
    def section(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Section() As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.get_DesignReview Returns or sets the section activation
                |         flag.
                | 
                |         Example:
                |             This example activates the section export.
                | 
                |               
                |               export3DXmlSettingAtt.Section = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.Section

    @section.setter
    def section(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.Section = value

    @property
    def surface_accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SurfaceAccuracy() As float
                | 
                |     Returns or sets the surface accuracy.
                | 
                |     Example:
                |         This example sets the surface accuracy used by the exact
                |         mode.
                | 
                |           
                |           export3DXmlSettingAtt.SurfaceAccuracy = 0.01

        :rtype: float
        """

        return self.export_3d_xml_setting_att.SurfaceAccuracy

    @surface_accuracy.setter
    def surface_accuracy(self, value: float):
        """
        :param float value:
        """

        self.export_3d_xml_setting_att.SurfaceAccuracy = value

    @property
    def work_instructions(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WorkInstructions() As boolean
                | 
                |     Returns or sets the Work Instructions activation flag.
                | 
                |     Example:
                |         This example activates the Work Instructions export.
                | 
                |           
                |           export3DXmlSettingAtt.DesignReview = True

        :rtype: bool
        """

        return self.export_3d_xml_setting_att.WorkInstructions

    @work_instructions.setter
    def work_instructions(self, value: bool):
        """
        :param bool value:
        """

        self.export_3d_xml_setting_att.WorkInstructions = value

    def get_alternate_view_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAlternateViewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.GetDesignReviewInfo Retrieves environment informations
                |         for the alternate view setting.
                |         Role:Retrieves the state of the alternate view setting in the current
                |         environment. 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetAlternateViewInfo(io_admin_level, io_locked)

    def get_animation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnimationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the animation
                |     setting.
                |     Role:Retrieves the state of the animation setting in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetAnimationInfo(io_admin_level, io_locked)

    def get_annotated_view_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnnotatedViewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.GetDesignReviewInfo Retrieves environment informations
                |         for the annotated view setting.
                |         Role:Retrieves the state of the annotated view setting in the current
                |         environment. 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetAnnotatedViewInfo(io_admin_level, io_locked)

    def get_annotation_3d_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnnotation3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 3D annotation
                |     setting.
                |     Role:Retrieves the state of the 3D annotation setting in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetAnnotation3DInfo(io_admin_level, io_locked)

    def get_design_review_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDesignReviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Design Review
                |     setting.
                |     Role:Retrieves the state of the Design Review setting in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetDesignReviewInfo(io_admin_level, io_locked)

    def get_geometry_representation_format_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGeometryRepresentationFormatInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the geometry representation format
                |     setting.
                |     Role:Retrieves the state of the parameter geometry representation format
                |     setting in the current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetGeometryRepresentationFormatInfo(io_admin_level, io_locked)

    def get_measure_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMeasureInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.GetDesignReviewInfo Retrieves environment informations
                |         for the measure setting.
                |         Role:Retrieves the state of the measure setting in the current
                |         environment. 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetMeasureInfo(io_admin_level, io_locked)

    def get_ppr_save_config_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPPRSaveConfigInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PPRSaveConfig
                |     setting.
                |     Role:Retrieves the state of the PPRSaveConfig setting in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetPPRSaveConfigInfo(io_admin_level, io_locked)

    def get_presentation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPresentationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.GetDesignReviewInfo Retrieves environment informations
                |         for the presentation setting.
                |         Role:Retrieves the state of the presentation setting in the current
                |         environment. 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetPresentationInfo(io_admin_level, io_locked)

    def get_section_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSectionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.GetDesignReviewInfo Retrieves environment informations
                |         for the section setting.
                |         Role:Retrieves the state of the section setting in the current
                |         environment. 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetSectionInfo(io_admin_level, io_locked)

    def get_surface_accuracy_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSurfaceAccuracyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the surface accuracy
                |     setting.
                |     Role:Retrieves the state of the surface accuracy setting in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetSurfaceAccuracyInfo(io_admin_level, io_locked)

    def get_work_instructions_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWorkInstructionsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Work Instructions
                |     setting.
                |     Role:Retrieves the state of the Work Instructions setting in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.export_3d_xml_setting_att.GetWorkInstructionsInfo(io_admin_level, io_locked)

    def set_alternate_view_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAlternateViewLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.SetDesignReviewLock Locks or unlocks the
                |         flag.
                |         Role:Locks or unlocks the parameter if it is possible in the current
                |         administrated. In user mode this method will always return E_FAIL.
                |         
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetAlternateViewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_alternate_view_lock'
        # # vba_code = """
        # # Public Function set_alternate_view_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetAlternateViewLock iLocked
        # #     set_alternate_view_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_animation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnimationLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetAnimationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_animation_lock'
        # # vba_code = """
        # # Public Function set_animation_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetAnimationLock iLocked
        # #     set_animation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annotated_view_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnnotatedViewLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.SetDesignReviewLock Locks or unlocks the
                |         flag.
                |         Role:Locks or unlocks the parameter if it is possible in the current
                |         administrated. In user mode this method will always return E_FAIL.
                |         
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetAnnotatedViewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annotated_view_lock'
        # # vba_code = """
        # # Public Function set_annotated_view_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetAnnotatedViewLock iLocked
        # #     set_annotated_view_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_annotation_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnnotation3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetAnnotation3DLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annotation3_d_lock'
        # # vba_code = """
        # # Public Function set_annotation3_d_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetAnnotation3DLock iLocked
        # #     set_annotation3_d_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_design_review_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDesignReviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetDesignReviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_design_review_lock'
        # # vba_code = """
        # # Public Function set_design_review_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetDesignReviewLock iLocked
        # #     set_design_review_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_geometry_representation_format_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGeometryRepresentationFormatLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetGeometryRepresentationFormatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_geometry_representation_format_lock'
        # # vba_code = """
        # # Public Function set_geometry_representation_format_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetGeometryRepresentationFormatLock iLocked
        # #     set_geometry_representation_format_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_measure_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMeasureLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.SetDesignReviewLock Locks or unlocks the
                |         flag.
                |         Role:Locks or unlocks the parameter if it is possible in the current
                |         administrated. In user mode this method will always return E_FAIL.
                |         
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetMeasureLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_measure_lock'
        # # vba_code = """
        # # Public Function set_measure_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetMeasureLock iLocked
        # #     set_measure_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ppr_save_config_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPPRSaveConfigLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetPPRSaveConfigLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ppr_save_config_lock'
        # # vba_code = """
        # # Public Function set_ppr_save_config_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetPPRSaveConfigLock iLocked
        # #     set_ppr_save_config_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_presentation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPresentationLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.SetDesignReviewLock Locks or unlocks the
                |         flag.
                |         Role:Locks or unlocks the parameter if it is possible in the current
                |         administrated. In user mode this method will always return E_FAIL.
                |         
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetPresentationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_presentation_lock'
        # # vba_code = """
        # # Public Function set_presentation_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetPresentationLock iLocked
        # #     set_presentation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_section_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSectionLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R19 This method will be replaced by
                |         Export3DXmlSettingAtt.SetDesignReviewLock Locks or unlocks the
                |         flag.
                |         Role:Locks or unlocks the parameter if it is possible in the current
                |         administrated. In user mode this method will always return E_FAIL.
                |         
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetSectionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_section_lock'
        # # vba_code = """
        # # Public Function set_section_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetSectionLock iLocked
        # #     set_section_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_surface_accuracy_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSurfaceAccuracyLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetSurfaceAccuracyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_surface_accuracy_lock'
        # # vba_code = """
        # # Public Function set_surface_accuracy_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetSurfaceAccuracyLock iLocked
        # #     set_surface_accuracy_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_work_instructions_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWorkInstructionsLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.export_3d_xml_setting_att.SetWorkInstructionsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_work_instructions_lock'
        # # vba_code = """
        # # Public Function set_work_instructions_lock(export3_d_xml_setting_att)
        # #     Dim iLocked (2)
        # #     export3_d_xml_setting_att.SetWorkInstructionsLock iLocked
        # #     set_work_instructions_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Export3DXmlSettingAtt(name="{self.name}")'
