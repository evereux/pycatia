#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""

from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.workbench import Workbench
from pycatia.space_analyses_interfaces.clashes import Clashes
from pycatia.space_analyses_interfaces.distances import Distances
from pycatia.space_analyses_interfaces.inertias import Inertias
from pycatia.space_analyses_interfaces.measurable import Measurable
from pycatia.space_analyses_interfaces.sections import Sections


class SPAWorkbench(Workbench):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         SPAWorkbench
                |
                | The object to manage all Space Analysis objects.
                |
                | This version allows you to manage inertia data, clashes, distances and
                | sections.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.spa_workbench = com_object.GetWorkbench("SPAWorkbench")

    @property
    def clashes(self) -> Clashes:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Clashes() As Clashes (Read Only)
                | 
                |     Returns the Clashes collection.
                |
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Clashes") on the root
                |     product, to retrieve the Clashes collection.
                |
                |     Example:
                |
                |              This example retrieves the Clashes collection of the active
                |              document.
                |
                |
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheClashesList As Clashes
                |             Set TheClashesList = TheSPAWorkbench.Clashes

        :return: Clashes
        :rtype: Clashes
        """

        return Clashes(self.spa_workbench.Clashes)

    @property
    def distances(self) -> Distances:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Distances() As Distances (Read Only)
                | 
                |     Returns the Distances collection.
                |
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Distances") on the root
                |     product, to retrieve the Distances collection.
                |
                |     Example:
                |
                |              This example retrieves the Distances collection of the active
                |              document.
                |
                |
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheDistancesList As Distances
                |             Set TheDistancesList = TheSPAWorkbench.Distances

        :return: Distances
        :rtype: Distances
        """

        return Distances(self.spa_workbench.Distances)

    @property
    def inertias(self) -> Inertias:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Inertias() As Inertias (Read Only)
                | 
                |     Returns the Inertias collection.
                |
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Inertia") on the product
                |     to analyze, to retrieve an Inertia object.
                |
                |     Example:
                |
                |              This example retrieves the Inertias collection of the active
                |              document.
                |
                |
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheInertiasList As Inertias
                |             Set TheInertiasList = TheSPAWorkbench.Inertias

        :return: Inertias
        :rtype: Inertias
        """

        return Inertias(self.spa_workbench.Inertias)

    @property
    def sections(self) -> Sections:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Sections() As Sections (Read Only)
                | 
                |     Returns the Sections collection.
                |
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Sections") on the root
                |     product, to retrieve the Sections collection.
                |
                |     Example:
                |
                |              This example retrieves the Sections collection of the active
                |              document.
                |
                |
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheSectionsList As Sections
                |             Set TheSectionsList = TheSPAWorkbench.Sections

        :return: Sections
        :rtype: Sections
        """

        return Sections(self.spa_workbench.Sections)

    def get_measurable(self, i_measured_item: Reference) -> Measurable:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetMeasurable(Reference iMeasuredItem) As Measurable
                | 
                |     Returns the Measurable object.
                |
                |     Example:
                |
                |              This example get the Measurable from the
                |              SPAWorkBench.
                |
                |
                |             Dim referenceObject As referenceObject
                |             Set referenceObject = "GetReference"
                |             Dim TheSPAWorkbench As Workbench
                |             Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                |             Dim TheMeasurable As Measurable
                |             Set TheMeasurable = TheSPAWorkbench.GetMeasurable(referenceObject)

        :param Reference i_measured_item:
        :return: Measurable
        :rtype: Measurable
        """
        return Measurable(self.spa_workbench.GetMeasurable(i_measured_item.com_object))

    def __repr__(self):
        return f'SpaWorkbench(name="{self.name}")'
