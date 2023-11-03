#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.navigator_interfaces.annotated_views import AnnotatedViews
from pycatia.navigator_interfaces.group import Group
from pycatia.navigator_interfaces.marker_3Ds import Marker3Ds
from pycatia.space_analyses_interfaces.conflicts import Conflicts
from pycatia.system_interfaces.any_object import AnyObject


class Clash(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Clash
                | 
                | Represents the Clash object.
                | The Clash object is a specification of a collision detection of
                | products.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.clash = com_object

    @property
    def annotated_views(self) -> AnnotatedViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnnotatedViews() As AnnotatedViews (Read Only)
                | 
                |     Returns the AnnotatedViews collection of the clash.
                | 
                |     Example:
                | 
                |              This example retrieves the AnnotatedViews collection of NewClash
                |              Clash.
                |
                |             Dim TheAnnotatedViewsList As AnnotatedViews
                |             Set TheAnnotatedViewsList = NewClash.AnnotatedViews

        :rtype: AnnotatedViews
        """

        return AnnotatedViews(self.clash.AnnotatedViews)

    @property
    def clearance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Clearance() As double
                | 
                |     Returns or sets the clearance value for the computation.
                | 
                |     The clearance value must be greater than 0. Units are
                |     Millimeter.
                | 
                |     Example:
                | 
                |              The first example retrieves the clearance value of NewClash
                |              Clash.
                |
                |             Dim Value As double
                |             Value = NewClash.Clearance
                |
                |                 The second example sets the clearance value of NewClash
                |                 Clash.
                |
                |                 NewClash.Clearance = 10.

        :rtype: float
        """

        return self.clash.Clearance

    @clearance.setter
    def clearance(self, value: float):
        """
        :param float value:
        """

        self.clash.Clearance = value

    @property
    def computation_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ComputationType() As CatClashComputationType
                | 
                |     Returns or sets the computation type.
                | 
                |     Example:
                | 
                |             The first example retrieves the computation type of NewClash
                |             Clash.
                |             
                |             Dim ComputationType As CatClashComputationType
                |             ComputationType = NewClash.ComputationType
                |
                |            The second example sets the computation type of NewClash
                |            Clash.
                |
                |            NewClash.ComputationType = catClashComputationTypeBetweenAll

        :return: enum cat_clash_computation_type
        :rtype: int
        """

        return self.clash.ComputationType

    @computation_type.setter
    def computation_type(self, value: int):
        """
        :param int value: enum cat_clash_computation_type
        """

        self.clash.ComputationType = value

    @property
    def conflicts(self) -> Conflicts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Conflicts() As Conflicts (Read Only)
                | 
                |     Returns the collection of computed Conflicts.
                | 
                |     Example:
                | 
                |              This example retrieves the conflicts of NewClash
                |              Clash.
                |
                |             Dim NewConflicts As Conflicts
                |             Set NewConflicts = NewClash.Conflicts

        :rtype: Conflicts
        """

        return Conflicts(self.clash.Conflicts)

    @property
    def first_group(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstGroup() As Group
                | 
                |     Returns or sets the first group used by the computation.
                | 
                |     Example:
                | 
                |              The first example retrieves the first group of NewClash
                |              Clash.
                |             
                |             Dim FirstGroup As Group
                |             Set FirstGroup = NewClash.FirstGroup
                |
                |                 The second example sets the first  group of NewClash
                |                 Clash.
                |
                |                 Dim FirstGroup As Group
                |                 NewClash.FirstGroup = FirstGroup

        :rtype: Group
        """

        return Group(self.clash.FirstGroup)

    @first_group.setter
    def first_group(self, group: Group):
        """
        :param Group group:
        """

        self.clash.FirstGroup = group.com_object

    @property
    def interference_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InterferenceType() As CatClashInterferenceType
                | 
                |     Returns or sets the interference type for the computation.
                | 
                |     Example:
                | 
                |              The first example retrieves the interference type of NewClash
                |              Clash.
                |             
                | 
                |             Dim InterferenceType As CatClashInterferenceType
                |             InterferenceType = NewClash.InterferenceType
                |
                |                 The second example sets the interference Type of NewClash
                |                 Clash.
                |
                |                 NewClash.InterferenceType = CatClashInterferenceTypeContact

        :return: enum cat_clash_interference_type
        :rtype: int
        """

        return self.clash.InterferenceType

    @interference_type.setter
    def interference_type(self, value: int):
        """
        :param int value:
        """

        self.clash.InterferenceType = value

    @property
    def marker_3ds(self) -> Marker3Ds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker3Ds() As Marker3Ds (Read Only)
                | 
                |     Returns the Marker3Ds collection of the clash.
                | 
                |     Example:
                | 
                |              This example retrieves the Marker3Ds collection of NewClash
                |              Clash.
                |
                |             Dim TheMarker3DsList As Marker3Ds
                |             Set TheMarker3DsList = NewClash.Marker3Ds

        :rtype: Marker3Ds
        """

        return Marker3Ds(self.clash.Marker3Ds)

    @property
    def second_group(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondGroup() As Group
                | 
                |     Returns or sets the second group used by the computation.
                | 
                |     Example:
                | 
                |              The first example retrieves the second group of NewClash
                |              Clash.
                |
                |             Dim SecondGroup As Group
                |             Set SecondGroup = NewClash.SecondGroup
                |
                |                 The second example sets the second group of NewClash
                |                 Clash.
                |
                |                 Dim SecondGroup As Group
                |                 NewClash.SecondGroup = SecondGroup

        :rtype: Group
        """

        return Group(self.clash.SecondGroup)

    @second_group.setter
    def second_group(self, group: Group):
        """
        :param Group group:
        """

        self.clash.SecondGroup = group.com_object

    def compute(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Compute()
                | 
                |     Computes the conflicts.
                | 
                |     Example:
                | 
                |              This example computes the conflicts of NewClash
                |              Clash.
                |
                |             NewClash.Compute

        :rtype: None
        """
        return self.clash.Compute()

    def export(self, i_type: int, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Export(CatClashExportType iType,
                | CATBSTR iPath)
                | 
                |     Exports the results in a XML file.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of export. 
                |         iPath
                |             The path of the file. 
                | 
                |     Example:
                | 
                |              This example exports the results of NewClash
                |              Clash.
                |
                |             Dim ThePath As String
                |             NewClash.Export CatClashExportTypeXMLResultOnly,
                |             "c:\\tmp\\sample.xml"

        :param int i_type: enum cat_clash_export_type
        :param str i_path:
        :rtype: None
        """
        return self.clash.Export(i_type, i_path)

    def __repr__(self):
        return f'Clash(name="{self.name}")'
