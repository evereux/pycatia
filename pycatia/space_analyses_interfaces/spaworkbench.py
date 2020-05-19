#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.base_object import AnyObject
from .measurable import Measurable


class SPAWorkbench(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic help

                | The object to manage all Space Analysis objects.This version allows
                | you to manage inertia data, clashes, distances and sections.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.spa_workbench = com_object.GetWorkbench("SPAWorkbench")

    @property
    def clashes(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Clashes
                | o Property Clashes(    ) As   (Read Only)
                | 
                | Returns the Clashes collection. WARNING: this method will be
                | DEPRECATED in the next release. It is recommended to use the
                | method GetTechnologicalObject("Clashes") on the root
                | product, to retrieve the Clashes collection.
                |
                | Example: This example retrieves the Clashes collection of the active
                | document.
                | Dim TheSPAWorkbench As Workbench
                | Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ("SPAWorkbench")
                | Dim TheClashesList As Clashes
                | Set TheClashesList = TheSPAWorkbench.Clashes

        :return:
        """
        return self.spa_workbench.Clashes

    @property
    def distances(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Distances
                | o Property Distances(    ) As   (Read Only)
                | 
                | Returns the Distances collection. WARNING: this method will
                | be DEPRECATED in the next release. It is recommended to use
                | the method GetTechnologicalObject("Distances") on the root
                | product, to retrieve the Distances collection.
                |
                | Example: This example retrieves the Distances collection of
                | the active document.
                | Dim TheSPAWorkbench As Workbench
                | Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ("SPAWorkbench" )
                | Dim TheDistancesList As Distances
                | Set TheDistancesList = TheSPAWorkbench.Distances

        :return:
        """
        return self.spa_workbench.Distances

    @property
    def inertias(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Inertias
                | o Property Inertias(    ) As   (Read Only)
                | 
                | Returns the Inertias collection. WARNING: this method will
                | be DEPRECATED in the next release. It is recommended to use
                | the method GetTechnologicalObject("Inertia") on the product
                | to analyze, to retrieve an Inertia object.
                |
                | Example: This
                | example retrieves the Inertias collection of the active
                | document.
                | Dim TheSPAWorkbench As Workbench
                | Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                | Dim TheInertiasList As Inertias
                | Set TheInertiasList = TheSPAWorkbench.Inertias
                |

        :return:
        """
        return self.spa_workbench.Inertias

    @property
    def sections(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Sections
                | o Property Sections(    ) As   (Read Only)
                | 
                | Returns the Sections collection. WARNING: this method will
                | be DEPRECATED in the next release. It is recommended to use
                | the method GetTechnologicalObject("Sections") on the root
                | product, to retrieve the Sections collection.
                |
                | Example: This example retrieves the Sections collection of the active
                | document.
                | Dim TheSPAWorkbench As Workbench
                | Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                | Dim TheSectionsList As Sections
                | Set TheSectionsList = TheSPAWorkbench.Sections

        :return:
        """
        return self.spa_workbench.Sections

    def get_measurable(self, i_measured_item):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMeasurable
                | o Func GetMeasurable(        iMeasuredItem) As
                | 
                | Returns the Measurable object.
                |
                | Example: This example get the Measurable from the SPAWorkBench.
                | Dim referenceObject As referenceObject
                | Set referenceObject = "GetReference"
                | Dim TheSPAWorkbench As Workbench
                | Set TheSPAWorkbench = CATIA.ActiveDocument.GetWorkbench ( "SPAWorkbench" )
                | Dim TheMeasurable As Measurable
                | Set TheMeasurable = TheSPAWorkbench.GetMeasurable(referenceObject)

        :param i_measured_item:
        :return: Measurable()
        """
        return Measurable(self.spa_workbench.GetMeasurable(i_measured_item.com_object))

    def __repr__(self):
        return f'SPAWorkbench()'
