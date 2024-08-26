#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.system_interfaces.setting_controller import SettingController


class StepSettingAtt(SettingController):
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
                |                         StepSettingAtt
                | 
                | The interface to access a CATIAStepSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.step_setting_att = com_object

    @property
    def att_ap(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttAP() As short
                | 
                |     Returns or sets the AttAP parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttAP

    @att_ap.setter
    def att_ap(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttAP = value

    @property
    def att_asm(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttASM() As short
                | 
                |     Returns or sets the AttASM parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttASM

    @att_asm.setter
    def att_asm(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttASM = value

    @property
    def att_asmgvp(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttASMGVP() As short
                | 
                |     Returns or sets the AttASMGVP parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttASMGVP

    @att_asmgvp.setter
    def att_asmgvp(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttASMGVP = value

    @property
    def att_angle_def_fitting(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttAngleDefFiting() As float
                | 
                |     Returns or sets the AttAngleDefFiting parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.step_setting_att.AttAngleDefFiting

    @att_angle_def_fitting.setter
    def att_angle_def_fitting(self, value: float):
        """
        :param float value:
        """

        self.step_setting_att.AttAngleDefFiting = value

    @property
    def att_annotation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttAnnotation() As short
                | 
                |     Returns or sets the AttAnnotation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttAnnotation

    @att_annotation.setter
    def att_annotation(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttAnnotation = value

    @property
    def att_annotation_export(self) -> int:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AttAnnotationExport() As short
                |     Returns or sets the AttAnnotationExport parameter.
                |
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.step_setting_att.AttAnnotationExport

    @att_annotation_export.setter
    def att_annotation_export(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttAnnotationExport = value

    @property
    def att_composites(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttComposites() As short
                | 
                |     Returns or sets the AttComposites parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttComposites

    @att_composites.setter
    def att_composites(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttComposites = value

    @property
    def att_export_rep_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttExportRepMode() As short
                | 
                |     Returns or sets the AttExportRepMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttExportRepMode

    @att_export_rep_mode.setter
    def att_export_rep_mode(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttExportRepMode = value

    @property
    def att_fitting(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttFitting() As short
                | 
                |     Returns or sets the AttFitting parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttFitting

    @att_fitting.setter
    def att_fitting(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttFitting = value

    @property
    def att_gvp(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGVP() As short
                | 
                |     Returns or sets the AttGVP parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttGVP

    @att_gvp.setter
    def att_gvp(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttGVP = value

    @property
    def att_gvpcops(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGVPCOPS() As short
                | 
                |     Returns or sets the AttGVPCOPS parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttGVPCOPS

    @att_gvpcops.setter
    def att_gvpcops(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttGVPCOPS = value

    @property
    def att_gvpcopssag(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGVPCOPSSAG() As double
                | 
                |     Returns or sets the AttGVPCOPSSAG parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.step_setting_att.AttGVPCOPSSAG

    @att_gvpcopssag.setter
    def att_gvpcopssag(self, value: float):
        """
        :param float value:
        """

        self.step_setting_att.AttGVPCOPSSAG = value

    @property
    def att_gvpcops_tol(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGVPCOPSTol() As double
                | 
                |     Returns or sets the AttGVPCOPSSAG parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.step_setting_att.AttGVPCOPSTol

    @att_gvpcops_tol.setter
    def att_gvpcops_tol(self, value: float):
        """
        :param float value:
        """

        self.step_setting_att.AttGVPCOPSTol = value

    @property
    def att_gvpcdg(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGVPCdG() As double
                | 
                |     Returns or sets the AttGVPCdG parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.step_setting_att.AttGVPCdG

    @att_gvpcdg.setter
    def att_gvpcdg(self, value: float):
        """
        :param float value:
        """

        self.step_setting_att.AttGVPCdG = value

    @property
    def att_gvpva(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGVPVA() As double
                | 
                |     Returns or sets the AttGVPVA parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.step_setting_att.AttGVPVA

    @att_gvpva.setter
    def att_gvpva(self, value: float):
        """
        :param float value:
        """

        self.step_setting_att.AttGVPVA = value

    @property
    def att_group_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttGroupMode() As short
                | 
                |     Returns or sets the AttGroupMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttGroupMode

    @att_group_mode.setter
    def att_group_mode(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttGroupMode = value

    @property
    def att_header_author(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttHeaderAuthor() As CATBSTR
                | 
                |     Returns or sets the AttHeaderAuthor parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.step_setting_att.AttHeaderAuthor

    @att_header_author.setter
    def att_header_author(self, value: str):
        """
        :param str value:
        """

        self.step_setting_att.AttHeaderAuthor = value

    @property
    def att_header_authorisation(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttHeaderAuthorisation() As CATBSTR
                | 
                |     Returns or sets the AttHeaderAuthorisation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.step_setting_att.AttHeaderAuthorisation

    @att_header_authorisation.setter
    def att_header_authorisation(self, value: str):
        """
        :param str value:
        """

        self.step_setting_att.AttHeaderAuthorisation = value

    @property
    def att_header_description(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttHeaderDescription() As CATBSTR
                | 
                |     Returns or sets the AttHeaderDescription parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.step_setting_att.AttHeaderDescription

    @att_header_description.setter
    def att_header_description(self, value: str):
        """
        :param str value:
        """

        self.step_setting_att.AttHeaderDescription = value

    @property
    def att_header_organisation(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttHeaderOrganisation() As CATBSTR
                | 
                |     Returns or sets the AttHeaderOrganisation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.step_setting_att.AttHeaderOrganisation

    @att_header_organisation.setter
    def att_header_organisation(self, value: str):
        """
        :param str value:
        """

        self.step_setting_att.AttHeaderOrganisation = value

    @property
    def att_iasm(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttIASM() As short
                | 
                |     Returns or sets the AttIASM parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttIASM

    @att_iasm.setter
    def att_iasm(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttIASM = value

    @property
    def att_layers_filters(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttLayersFilters() As short
                | 
                |     Returns or sets the AttLayersFilters parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttLayersFilters

    @att_layers_filters.setter
    def att_layers_filters(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttLayersFilters = value

    @property
    def att_multi_cad(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttMultiCAD() As short
                | 
                |     Returns or sets the AttMultiCAD parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttMultiCAD

    @att_multi_cad.setter
    def att_multi_cad(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttMultiCAD = value

    @property
    def att_optimize_c2(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttOptimizeC2() As short
                | 
                |     Returns or sets the AttOptimizeC2 parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttOptimizeC2

    @att_optimize_c2.setter
    def att_optimize_c2(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttOptimizeC2 = value

    @property
    def att_report(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttReport() As short
                | 
                |     Returns or sets the AttReport parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttReport

    @att_report.setter
    def att_report(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttReport = value

    @property
    def att_show(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttShow() As short
                | 
                |     Returns or sets the AttShow parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttShow

    @att_show.setter
    def att_show(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttShow = value

    @property
    def att_tess_preferred(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttTessPrefered() As short
                | 
                |     Returns or sets the AttTessPrefered parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttTessPrefered

    @att_tess_preferred.setter
    def att_tess_preferred(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttTessPrefered = value

    @property
    def att_tol_def_opt_fit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttTolDefOptFit() As float
                | 
                |     Returns or sets the AttTolDefOptFit parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.step_setting_att.AttTolDefOptFit

    @att_tol_def_opt_fit.setter
    def att_tol_def_opt_fit(self, value: float):
        """
        :param float value:
        """

        self.step_setting_att.AttTolDefOptFit = value

    @property
    def att_uda(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttUDA() As short
                | 
                |     Returns or sets the AttUDA parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttUDA

    @att_uda.setter
    def att_uda(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttUDA = value

    @property
    def att_units(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttUnits() As short
                | 
                |     Returns or sets the AttUnits parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.AttUnits

    @att_units.setter
    def att_units(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.AttUnits = value

    @property
    def edge_in_tess_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EdgeInTessMode() As short
                | 
                |     Returns or sets the EdgeTessMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.step_setting_att.EdgeInTessMode

    @edge_in_tess_mode.setter
    def edge_in_tess_mode(self, value: int):
        """
        :param int value:
        """

        self.step_setting_att.EdgeInTessMode = value

    def get_att_ap_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttAPInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttAP
                |     parameter.
                |     Role:Retrieves the state of the AttAP parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttAPInfo(io_admin_level, io_locked)

    def get_att_asmgvp_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttASMGVPInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttASMGVP
                |     parameter.
                |     Role:Retrieves the state of the AttASMGVP parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttASMGVPInfo(io_admin_level, io_locked)

    def get_att_asm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttASMInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttASM
                |     parameter.
                |     Role:Retrieves the state of the AttASM parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttASMInfo(io_admin_level, io_locked)

    def get_att_angle_def_fiting_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttAngleDefFitingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttAngleDefFiting
                |     parameter.
                |     Role:Retrieves the state of the AttAngleDefFiting parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttAngleDefFitingInfo(io_admin_level, io_locked)

    def get_att_annotation_export_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::

        Introduced in V5-6R2020.

            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetAttAnnotationExportInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves environment informations for the AttAnnotationExport
                |     parameter.
                |     Role:Retrieves the state of the AttAnnotationExport parameter in the
                |     current environment.
                |
                |     Parameters:
                |
                |         ioAdminLevel
                |
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |
                |         ioLocked
                |             Indicates if the parameter has been locked.
                |
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.step_setting_att.GetAttAnnotationExportInfo(io_admin_level, io_locked)

    def get_att_annotation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttAnnotationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttAnnotation
                |     parameter.
                |     Role:Retrieves the state of the AttAnnotation parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttAnnotationInfo(io_admin_level, io_locked)

    def get_att_composites_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttCompositesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttComposites
                |     parameter.
                |     Role:Retrieves the state of the AttComposites parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttCompositesInfo(io_admin_level, io_locked)

    def get_att_export_rep_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttExportRepModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttExportRepMode
                |     parameter.
                |     Role:Retrieves the state of the AttExportRepMode parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttExportRepModeInfo(io_admin_level, io_locked)

    def get_att_fitting_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttFittingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttFitting
                |     parameter.
                |     Role:Retrieves the state of the AttFitting parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttFittingInfo(io_admin_level, io_locked)

    def get_att_gvpcops_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGVPCOPSInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGVP
                |     parameter.
                |     Role:Retrieves the state of the AttGVP parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGVPCOPSInfo(io_admin_level, io_locked)

    def get_att_gvpcopssag_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGVPCOPSSAGInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGVPVA
                |     parameter.
                |     Role:Retrieves the state of the AttGVPVA parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGVPCOPSSAGInfo(io_admin_level, io_locked)

    def get_att_gvpcops_tol_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGVPCOPSTolInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGVPVA
                |     parameter.
                |     Role:Retrieves the state of the AttGVPVA parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGVPCOPSTolInfo(io_admin_level, io_locked)

    def get_att_gvpcdg_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGVPCdGInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGVPCdG
                |     parameter.
                |     Role:Retrieves the state of the AttGVPCdG parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGVPCdGInfo(io_admin_level, io_locked)

    def get_att_gvp_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGVPInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGVP
                |     parameter.
                |     Role:Retrieves the state of the AttGVP parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGVPInfo(io_admin_level, io_locked)

    def get_att_gvpva_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGVPVAInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGVPVA
                |     parameter.
                |     Role:Retrieves the state of the AttGVPVA parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGVPVAInfo(io_admin_level, io_locked)

    def get_att_group_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttGroupModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttGroupMode
                |     parameter.
                |     Role:Retrieves the state of the AttGroupMode parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttGroupModeInfo(io_admin_level, io_locked)

    def get_att_header_author_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttHeaderAuthorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttHeaderAuthor
                |     parameter.
                |     Role:Retrieves the state of the AttHeaderAuthor parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttHeaderAuthorInfo(io_admin_level, io_locked)

    def get_att_header_authorisation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttHeaderAuthorisationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttHeaderAuthorisation
                |     parameter.
                |     Role:Retrieves the state of the AttHeaderAuthorisation parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttHeaderAuthorisationInfo(io_admin_level, io_locked)

    def get_att_header_description_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttHeaderDescriptionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttHeaderDescription
                |     parameter.
                |     Role:Retrieves the state of the AttHeaderDescription parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttHeaderDescriptionInfo(io_admin_level, io_locked)

    def get_att_header_organisation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttHeaderOrganisationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttHeaderOrganisation
                |     parameter.
                |     Role:Retrieves the state of the AttHeaderOrganisation parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttHeaderOrganisationInfo(io_admin_level, io_locked)

    def get_att_iasm_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttIASMInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttIASM
                |     parameter.
                |     Role:Retrieves the state of the AttIASM parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttIASMInfo(io_admin_level, io_locked)

    def get_att_layers_filters_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttLayersFiltersInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttLayersFilters
                |     parameter.
                |     Role:Retrieves the state of the AttLayersFilters parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttLayersFiltersInfo(io_admin_level, io_locked)

    def get_att_multi_cad_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttMultiCADInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttMultiCAD
                |     parameter.
                |     Role:Retrieves the state of the AttMultiCAD parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttMultiCADInfo(io_admin_level, io_locked)

    def get_att_optimize_c2_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttOptimizeC2Info(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttOptimizeC2
                |     parameter.
                |     Role:Retrieves the state of the AttOptimizeC2 parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttOptimizeC2Info(io_admin_level, io_locked)

    def get_att_report_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttReportInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttReport
                |     parameter.
                |     Role:Retrieves the state of the AttReport parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttReportInfo(io_admin_level, io_locked)

    def get_att_show_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttShowInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttShow
                |     parameter.
                |     Role:Retrieves the state of the AttShow parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttShowInfo(io_admin_level, io_locked)

    def get_att_tess_preferred_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttTessPreferedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttTessPrefered
                |     parameter.
                |     Role:Retrieves the state of the AttTessPrefered parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttTessPreferedInfo(io_admin_level, io_locked)

    def get_att_tol_def_opt_fit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttTolDefOptFitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttTolDefOptFit
                |     parameter.
                |     Role:Retrieves the state of the AttTolDefOptFit parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttTolDefOptFitInfo(io_admin_level, io_locked)

    def get_att_uda_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttUDAInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttUDA
                |     parameter.
                |     Role:Retrieves the state of the AttUDA parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttUDAInfo(io_admin_level, io_locked)

    def get_att_units_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttUnitsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AttUnits
                |     parameter.
                |     Role:Retrieves the state of the AttUnits parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetAttUnitsInfo(io_admin_level, io_locked)

    def get_edge_in_tess_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetEdgeInTessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the EdgeTessMode
                |     parameter.
                |     Role:Retrieves the state of the EdgeTessMode parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.step_setting_att.GetEdgeInTessInfo(io_admin_level, io_locked)

    def set_att_ap_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttAPLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttAP parameter.
                |     Role:Locks or unlocks the AttAP parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttAPLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_ap_lock'
        # # vba_code = """
        # # Public Function set_att_ap_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttAPLock iLocked
        # #     set_att_ap_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_asmgvp_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttASMGVPLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttASMGVP parameter.
                |     Role:Locks or unlocks the AttASMGVP parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttASMGVPLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_asmgvp_lock'
        # # vba_code = """
        # # Public Function set_att_asmgvp_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttASMGVPLock iLocked
        # #     set_att_asmgvp_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_asm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttASMLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttASM parameter.
                |     Role:Locks or unlocks the AttASM parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttASMLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_asm_lock'
        # # vba_code = """
        # # Public Function set_att_asm_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttASMLock iLocked
        # #     set_att_asm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_angle_def_fiting_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttAngleDefFitingLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttAngleDefFiting parameter.
                |     Role:Locks or unlocks the AttAngleDefFiting parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttAngleDefFitingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_angle_def_fiting_lock'
        # # vba_code = """
        # # Public Function set_att_angle_def_fiting_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttAngleDefFitingLock iLocked
        # #     set_att_angle_def_fiting_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_annotation_export_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetAttAnnotationExportLock(boolean iLocked)
                |     Locks or unlocks the AttAnnotationExport parameter.
                |     Role:Locks or unlocks the AttAnnotationExport parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                |
                |     Parameters:
                |
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.step_setting_att.SetAttAnnotationExportLock(i_locked)

    def set_att_annotation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttAnnotationLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttAnnotation parameter.
                |     Role:Locks or unlocks the AttAnnotation parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttAnnotationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_annotation_lock'
        # # vba_code = """
        # # Public Function set_att_annotation_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttAnnotationLock iLocked
        # #     set_att_annotation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_composites_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttCompositesLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttComposites parameter.
                |     Role:Locks or unlocks the AttComposites parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttCompositesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_composites_lock'
        # # vba_code = """
        # # Public Function set_att_composites_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttCompositesLock iLocked
        # #     set_att_composites_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_export_rep_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttExportRepModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttExportRepMode parameter.
                |     Role:Locks or unlocks the AttExportRepMode parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttExportRepModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_export_rep_mode_lock'
        # # vba_code = """
        # # Public Function set_att_export_rep_mode_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttExportRepModeLock iLocked
        # #     set_att_export_rep_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_fitting_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttFittingLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttFitting parameter.
                |     Role:Locks or unlocks the AttFitting parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttFittingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_fitting_lock'
        # # vba_code = """
        # # Public Function set_att_fitting_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttFittingLock iLocked
        # #     set_att_fitting_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_gvpcops_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGVPCOPSLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGVP parameter.
                |     Role:Locks or unlocks the AttGVP parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGVPCOPSLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_gvpcops_lock'
        # # vba_code = """
        # # Public Function set_att_gvpcops_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGVPCOPSLock iLocked
        # #     set_att_gvpcops_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_gvpcopssag_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGVPCOPSSAGLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGVPVA parameter.
                |     Role:Locks or unlocks the AttGVPVA parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGVPCOPSSAGLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_gvpcopssag_lock'
        # # vba_code = """
        # # Public Function set_att_gvpcopssag_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGVPCOPSSAGLock iLocked
        # #     set_att_gvpcopssag_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_gvpcops_tol_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGVPCOPSTolLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGVPVA parameter.
                |     Role:Locks or unlocks the AttGVPVA parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGVPCOPSTolLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_gvpcops_tol_lock'
        # # vba_code = """
        # # Public Function set_att_gvpcops_tol_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGVPCOPSTolLock iLocked
        # #     set_att_gvpcops_tol_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_gvpcdg_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGVPCdGLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGVPCdG parameter.
                |     Role:Locks or unlocks the AttGVPCdG parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGVPCdGLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_gvp_cd_g_lock'
        # # vba_code = """
        # # Public Function set_att_gvp_cd_g_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGVPCdGLock iLocked
        # #     set_att_gvp_cd_g_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_gvp_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGVPLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGVP parameter.
                |     Role:Locks or unlocks the AttGVP parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGVPLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_gvp_lock'
        # # vba_code = """
        # # Public Function set_att_gvp_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGVPLock iLocked
        # #     set_att_gvp_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_gvpva_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGVPVALock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGVPVA parameter.
                |     Role:Locks or unlocks the AttGVPVA parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGVPVALock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_gvpva_lock'
        # # vba_code = """
        # # Public Function set_att_gvpva_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGVPVALock iLocked
        # #     set_att_gvpva_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_group_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttGroupModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttGroupMode parameter.
                |     Role:Locks or unlocks the AttGroupMode parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttGroupModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_group_mode_lock'
        # # vba_code = """
        # # Public Function set_att_group_mode_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttGroupModeLock iLocked
        # #     set_att_group_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_header_author_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttHeaderAuthorLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttHeaderAuthor parameter.
                |     Role:Locks or unlocks the AttHeaderAuthor parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttHeaderAuthorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_header_author_lock'
        # # vba_code = """
        # # Public Function set_att_header_author_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttHeaderAuthorLock iLocked
        # #     set_att_header_author_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_header_authorisation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttHeaderAuthorisationLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttHeaderAuthorisation parameter.
                |     Role:Locks or unlocks the AttHeaderAuthorisation parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttHeaderAuthorisationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_header_authorisation_lock'
        # # vba_code = """
        # # Public Function set_att_header_authorisation_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttHeaderAuthorisationLock iLocked
        # #     set_att_header_authorisation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_header_description_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttHeaderDescriptionLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttHeaderDescription parameter.
                |     Role:Locks or unlocks the AttHeaderDescription parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttHeaderDescriptionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_header_description_lock'
        # # vba_code = """
        # # Public Function set_att_header_description_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttHeaderDescriptionLock iLocked
        # #     set_att_header_description_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_header_organisation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttHeaderOrganisationLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttHeaderOrganisation parameter.
                |     Role:Locks or unlocks the AttHeaderOrganisation parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttHeaderOrganisationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_header_organisation_lock'
        # # vba_code = """
        # # Public Function set_att_header_organisation_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttHeaderOrganisationLock iLocked
        # #     set_att_header_organisation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_iasm_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttIASMLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttIASM parameter.
                |     Role:Locks or unlocks the AttIASM parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttIASMLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_iasm_lock'
        # # vba_code = """
        # # Public Function set_att_iasm_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttIASMLock iLocked
        # #     set_att_iasm_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_layers_filters_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttLayersFiltersLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttLayersFilters parameter.
                |     Role:Locks or unlocks the AttLayersFilters parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttLayersFiltersLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_layers_filters_lock'
        # # vba_code = """
        # # Public Function set_att_layers_filters_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttLayersFiltersLock iLocked
        # #     set_att_layers_filters_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_multi_cad_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttMultiCADLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttMultiCAD parameter.
                |     Role:Locks or unlocks the AttMultiCAD parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttMultiCADLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_multi_cad_lock'
        # # vba_code = """
        # # Public Function set_att_multi_cad_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttMultiCADLock iLocked
        # #     set_att_multi_cad_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_optimize_c2_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttOptimizeC2Lock(boolean iLocked)
                | 
                |     Locks or unlocks the AttOptimizeC2 parameter.
                |     Role:Locks or unlocks the AttOptimizeC2 parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttOptimizeC2Lock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_optimize_c2_lock'
        # # vba_code = """
        # # Public Function set_att_optimize_c2_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttOptimizeC2Lock iLocked
        # #     set_att_optimize_c2_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_report_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttReportLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttReport parameter.
                |     Role:Locks or unlocks the AttReport parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttReportLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_report_lock'
        # # vba_code = """
        # # Public Function set_att_report_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttReportLock iLocked
        # #     set_att_report_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_show_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttShowLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttShow parameter.
                |     Role:Locks or unlocks the AttShow parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttShowLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_show_lock'
        # # vba_code = """
        # # Public Function set_att_show_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttShowLock iLocked
        # #     set_att_show_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_tess_preferred_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttTessPreferedLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttTessPrefered parameter.
                |     Role:Locks or unlocks the AttTessPrefered parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttTessPreferedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_tess_prefered_lock'
        # # vba_code = """
        # # Public Function set_att_tess_prefered_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttTessPreferedLock iLocked
        # #     set_att_tess_prefered_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_tol_def_opt_fit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttTolDefOptFitLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttTolDefOptFit parameter.
                |     Role:Locks or unlocks the AttTolDefOptFit parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttTolDefOptFitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_tol_def_opt_fit_lock'
        # # vba_code = """
        # # Public Function set_att_tol_def_opt_fit_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttTolDefOptFitLock iLocked
        # #     set_att_tol_def_opt_fit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_uda_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttUDALock(boolean iLocked)
                | 
                |     Locks or unlocks the AttUDA parameter.
                |     Role:Locks or unlocks the AttUDA parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttUDALock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_uda_lock'
        # # vba_code = """
        # # Public Function set_att_uda_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttUDALock iLocked
        # #     set_att_uda_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_att_units_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttUnitsLock(boolean iLocked)
                | 
                |     Locks or unlocks the AttUnits parameter.
                |     Role:Locks or unlocks the AttUnits parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetAttUnitsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_att_units_lock'
        # # vba_code = """
        # # Public Function set_att_units_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetAttUnitsLock iLocked
        # #     set_att_units_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_edge_in_tess_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetEdgeInTessLock(boolean iLocked)
                | 
                |     Locks or unlocks the EdgeTessMode parameter.
                |     Role:Locks or unlocks the AttGroupMode parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.step_setting_att.SetEdgeInTessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_edge_in_tess_lock'
        # # vba_code = """
        # # Public Function set_edge_in_tess_lock(step_setting_att)
        # #     Dim iLocked (2)
        # #     step_setting_att.SetEdgeInTessLock iLocked
        # #     set_edge_in_tess_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'StepSettingAtt(name="{self.name}")'
