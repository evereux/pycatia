from pathlib import Path

from pycatia.dnb_human_modeling_interfaces.swk_human_catalog import SWKHumanCatalog
from pycatia.dnb_human_modeling_interfaces.swk_manikin import SWKManikin
from pycatia.system_interfaces.any_object import AnyObject


class SWKHmiWorkbench(AnyObject):
    """
    This class is not documented in the CAA V5 Visual Basic Help file.

    This class was created by referring to the Microsoft Visual Basic object explorer.
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_manikin_for_clash(self) -> SWKManikin:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub AddManikinForClash(piManikin As SWKManikin)
                |    Member of SWKHumanModelingItf.SWKHmiWorkbench

        :rtype: SWKManikin
        """

        return self.com_object.AddManikinForClash()

    def clean_clash_results(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub CleanClashResults()
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench
        """

        return self.com_object.CleanClashResults()

    def compute_clash(self) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function ComputeClash(piMakeExplicitCall As Boolean) As Long
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench
        """

        return self.com_object.ComputeClash()

    def create_color_from_rgb(self, pi_red: int, pi_green: int, pi_blue: int) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function CreateColorFromRGB(piRed As Long, piGreen As Long, piBlue As Long) As Long
                |    Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param int pi_red:
        :param int pi_green:
        :param int pi_blue:
        :rtype: int
        """

        return self.com_object.CreateColorFromRGB(pi_red, pi_green, pi_blue)

    def create_left_forearm(
            self,
            pi_manikin_name: str,
            pi_sex: int,
            pi_percentile: float,
            pi_population: int
    ) -> SWKManikin:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function CreateLeftForearm(piManikinName As String,
                |                            piSex As SWKAnthroSex,
                |                            piPercentile As Double,
                |                            piPopulation As Long) As SWKManikin
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param str pi_manikin_name:
        :param int pi_sex: enum swk_anthro_sex
        :param float pi_percentile:
        :param int pi_population:
        :rtype: SWKHumanCatalog
        """

        return SWKManikin(self.com_object.CreateLeftForearm(pi_manikin_name, pi_sex, pi_percentile, pi_population))

    def create_manikin(
            self,
            pi_manikin_name: str,
            pi_sex: int,
            pi_percentile: float,
            pi_population: int
    ) -> SWKManikin:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function CreateManikin(piManikinName As String,
                |                        piSex As SWKAnthroSex,
                |                        piPercentile As Double,
                |                        piPopulation As Long) As SWKManikin
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param str pi_manikin_name:
        :param int pi_sex: enum swk_anthro_sex
        :param float pi_percentile:
        :param int pi_population:
        :rtype: SWKHumanCatalog
        """

        return SWKManikin(self.com_object.CreateManikin(pi_manikin_name, pi_sex, pi_percentile, pi_population))

    def create_right_forearm(
            self,
            pi_manikin_name: str,
            pi_sex: int,
            pi_percentile: float,
            pi_population: int) -> SWKManikin:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function CreateRightForearm(piManikinName As String,
                |                             piSex As SWKAnthroSex,
                |                             piPercentile As Double,
                |                             piPopulation As Long) As SWKManikin
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param str pi_manikin_name:
        :param int pi_sex: enum swk_anthro_sex
        :param float pi_percentile:
        :param int pi_population:
        :rtype: SWKHumanCatalog
        """

        return SWKManikin(self.com_object.CreateRightForearm(pi_manikin_name, pi_sex, pi_percentile, pi_population))

    def new_human_catalog(self) -> SWKHumanCatalog:
        """

        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function NewHumanCatalog(piPathFile As String) As SWKHumanCatalog
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :rtype: SWKHumanCatalog
        """

        return SWKHumanCatalog(self.com_object.NewHumanCatalog())

    def open_human_catalog(self, pi_path_file: Path, pi_doc_env: str) -> SWKHumanCatalog:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function OpenHumanCatalog(piPathFile As String, piDocEnv As String) As SWKHumanCatalog
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param Path pi_path_file:
        :param Path pi_doc_env:
        :rtype: SWKHumanCatalog
        """

        return SWKHumanCatalog(self.com_object.OpenHumanCatalog(pi_path_file, pi_doc_env))

    def open_writable_human_catalog(self, pi_path_file: Path, pi_doc_env: str) -> SWKHumanCatalog:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Function OpenWritableHumanCatalog(piPathFile As String, piDocEnv As String) As SWKHumanCatalog
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param Path pi_path_file:
        :param Path pi_doc_env:
        :rtype: SWKHumanCatalog
        """

        return SWKHumanCatalog(self.com_object.OpenWritableHumanCatalog(pi_path_file, pi_doc_env))

    def reset_clash_list(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub ResetClashList()
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :rtype: None
        """

        return self.com_object.ResetClashList()

    def set_clash_mode(self, pi_clash_mode) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub SetClashMode(piClashMode As String)
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param str pi_clash_mode:
        :rtype: None
        """

        return self.com_object.SetClashMode(pi_clash_mode)

    def start_command(self, pi_command_header_name: str) -> int:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub StartCommand(piCommandHeaderName As String)
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param str pi_command_header_name:
        :rtype: None
        """

        return self.com_object.StartCommand(pi_command_header_name)

    def stop_command(self, pi_command_header_name: str) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub StopCommand(piCommandHeaderName As String)
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :param str pi_command_header_name:
        :rtype: None
        """

        return self.com_object.StopCommand(pi_command_header_name)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub Update()
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :rtype: None
        """

        return self.com_object.Update()

    def update_ppr_tree(self) -> None:
        """
        .. note::
            :class: toggle

            Microsoft Visual Basic Object Browser
                | Sub UpdatePPRTree()
                |     Member of SWKHumanModelingItf.SWKHmiWorkbench

        :rtype: None
        """

        return self.com_object.UpdatePPRTree()
