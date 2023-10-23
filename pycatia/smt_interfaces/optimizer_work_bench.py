#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.workbench import Workbench
from pycatia.smt_interfaces.dmo_offsets import DMOOffsets
from pycatia.smt_interfaces.dmo_thicknesses import DMOThicknesses
from pycatia.smt_interfaces.free_spaces import FreeSpaces
from pycatia.smt_interfaces.part_comps import PartComps
from pycatia.smt_interfaces.silhouettes import Silhouettes
from pycatia.smt_interfaces.swept_volumes import SweptVolumes
from pycatia.smt_interfaces.wrappings import Wrappings


class OptimizerWorkBench(Workbench):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         OptimizerWorkBench
                | 
                | Interface to access a CATIAOptimizerWorkBench
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimizer_work_bench = com_object

    @property
    def free_spaces(self) -> FreeSpaces:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FreeSpaces() As FreeSpaces (Read Only)
                | 
                |     Returns FreeSpaces.

        :rtype: FreeSpaces
        """

        return FreeSpaces(self.optimizer_work_bench.FreeSpaces)

    @property
    def offsets(self) -> DMOOffsets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Offsets() As DMOOffsets (Read Only)
                | 
                |     Returns Offsets.

        :rtype: DMOOffsets
        """

        return DMOOffsets(self.optimizer_work_bench.Offsets)

    @property
    def part_comps(self) -> PartComps:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PartComps() As PartComps (Read Only)
                | 
                |     Returns PartComps.

        :rtype: PartComps
        """

        return PartComps(self.optimizer_work_bench.PartComps)

    @property
    def silhouettes(self) -> Silhouettes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Silhouettes() As Silhouettes (Read Only)
                | 
                |     Returns or sets the constraint driving mode. For constraint types
                |     supporting the concept of value, such as distance constraints, the driving mode
                |     tells whether the constraint value actually drives the geometry position, or,
                |     conversely, is driven by it.
                | 
                |     Example:
                |         The following example retrieves in currentSilhouettes the driving mode
                |         for the distCst distance constraint:
                | 
                |          currentSilhouettes = distCst.Silhouettes

        :rtype: Silhouettes
        """

        return Silhouettes(self.optimizer_work_bench.Silhouettes)

    @property
    def swept_volumes(self) -> SweptVolumes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SweptVolumes() As SweptVolumes (Read Only)
                | 
                |     Returns SweptVolumes.

        :rtype: SweptVolumes
        """

        return SweptVolumes(self.optimizer_work_bench.SweptVolumes)

    @property
    def thicknesses(self) -> DMOThicknesses:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Thicknesses() As DMOThicknesses (Read Only)
                | 
                |     Returns Thicknesses.

        :rtype: DMOThicknesses
        """

        return DMOThicknesses(self.optimizer_work_bench.Thicknesses)

    @property
    def wrappings(self) -> Wrappings:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Wrappings() As Wrappings (Read Only)
                | 
                |     Returns Wrappings.

        :rtype: Wrappings
        """

        return Wrappings(self.optimizer_work_bench.Wrappings)

    def check(self, i_context: str, i_instance_id: str, i_latest_shape: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Check(CATBSTR iContext,
                | CATBSTR iInstanceID,
                | CATBSTR iLatestShape) As long
                | 
                |     Check 1 component

        :param str i_context:
        :param str i_instance_id:
        :param str i_latest_shape:
        :rtype: int
        """
        return self.optimizer_work_bench.Check(i_context, i_instance_id, i_latest_shape)

    def query_neighbours(
            self,
            i_accuracy: float,
            i_clearance: float,
            i_reference_selection: tuple,
            i_type_query: int
    ) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func QueryNeighbours(double iAccuracy,
                | double iClearance,
                | CATSafeArrayVariant iReferenceSelection,
                | long iTypeQuery) As long
                | 
                |     Compute the Neighbours

        :param float i_accuracy:
        :param float i_clearance:
        :param tuple i_reference_selection:
        :param int i_type_query:
        :rtype: int
        """
        return self.optimizer_work_bench.QueryNeighbours(i_accuracy, i_clearance, i_reference_selection, i_type_query)

    def __repr__(self):
        return f'OptimizerWorkBench(name="{self.name}")'
