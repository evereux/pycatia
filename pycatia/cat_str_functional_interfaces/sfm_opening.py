#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject


class SFMOpening(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmOpening
                | 
                | Defines Edition Techniques for Openings created using sketch and 3D
                | Object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_opening = com_object

    @property
    def creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CreationMode(long iMode)
                | 
                |     Returns or Sets the Opening Creation Mode. 0 for 3D Mode. 1 for Sketch
                |     Mode. 2 for StandardOpening Mode.
                | 
                |     Example:
                |         This example gets the Creation Mode for existing
                |         Opening.
                | 
                |          'Get the Existing Opening
                |          Dim OpeningPlate As SfmOpening
                |          Set OpeningPlate = part1.FindObjectByName("Opening_028")
                |          Dim Sel As Selection
                |          Set Sel = CATIA.ActiveDocument.Selection
                |          Sel.Add OpeningPlate 
                |          Dim OpenFact As SfmOpening
                |          Set OpenFact = Sel.FindObject("CATIASfmOpening")
                |          Dim CreationMode As Long
                |          CreationMode = OpenFact.CreationMode

        :rtype: int
        """

        return self.sfm_opening.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: int):
        """
        :param int value:
        """

        self.sfm_opening.CreationMode = value

    @property
    def direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Direction(Reference iDirection)
                | 
                |     Returns or Sets the Direction for a Wire Element Case.
                | 
                |     Example:
                |         This example modifies the direction of existing
                |         opening.
                | 
                |          'Get the element to be used as direction element.
                |          Set Dir = part1.FindObjectByName("Line.4")
                |          Set DirRef = part1.CreateReferenceFromObject(Dir)
                |          Opening1.Direction = DirRef

        :rtype: Reference
        """

        return self.sfm_opening.Direction

    @direction.setter
    def direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_opening.Direction = value.com_object

    @property
    def intersecting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IntersectingElement(Reference
                | iIntersectingElement)
                | 
                |     Returns or Sets the Intersecting Element to Create a
                |     Opening.
                | 
                |     Example:
                |         This example sets the intersecting element for the existing opening,
                |         after changing it's mode to sketch mode.
                | 
                |          'Get the Creation Mode for Existing Opening. The Existing Opening is
                |          created using 3D Mode.
                |           CreationMode = Opening1.CreationMode
                |          'Set the Creation Mode for Existing Opening to sketch
                |          mode
                |          Opening1.CreationMode = 1
                |          'Assign a new sketch to the existing opening
                |          Set Sketch = part1.FindObjectByName("Sketch.4")
                |          Set sketchref = part1.CreateReferenceFromObject(Sketch)
                |          Opening1.IntersectingElement = sketchref

        :rtype: Reference
        """

        return self.sfm_opening.IntersectingElement

    @intersecting_element.setter
    def intersecting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_opening.IntersectingElement = value.com_object

    @property
    def molded_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MoldedSurface(Reference iMoldedSurface)
                | 
                |     Returns or Sets the Molded Surface for the Opening.
                | 
                |     Example:
                |         This example modifies the molded surface for the existing
                |         opening.
                | 
                |          'Get the Surface to be used as molded surface for the
                |          opening
                |          Dim GSDSurf As Reference
                |          Set GSDSurf = part1.FindObjectByName("Fill.1")
                |          Set GSDSurfref = part1.CreateReferenceFromObject(GSDSurf)
                |          Opening1.MoldedSurface = GSDSurfref

        :rtype: Reference
        """

        return self.sfm_opening.MoldedSurface

    @molded_surface.setter
    def molded_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_opening.MoldedSurface = value.com_object

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDirection() As CATSafeArrayVariant
                | 
                |     Gets the Direction for Opening in the form of Vector.
                | 
                |     Parameters:
                | 
                |         oDirection
                |             [out] Direction vector 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example Gets the Direction for the Opening.
                | 
                |              Dim Dir() As Variant
                |              Dir = OpeningPlate.GetDirection
                |              Dim x, y, z As Double
                |              x = Dir(0)
                |              y = Dir(1)
                |              z = Dir(2)

        :rtype: tuple
        """
        return self.sfm_opening.GetDirection()

    def is_a_plate_opening(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAPlateOpening() As long
                | 
                |     Determines if it is a Plate Opening or a Profile one.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             [out] oStatus=0, if the Opening is on Plate oStatus=1, if the
                |             Opening is Not on Plate 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example Checks weather the opening is a Plate
                |             Opening.
                | 
                |              'Get the Existing Opening in the Part Document
                |              Dim OpeningPlate As SfmOpening
                |              Set OpeningPlate = part1.FindObjectByName("Opening_028")
                |              Dim Sel As Selection
                |              Set Sel = CATIA.ActiveDocument.Selection
                |              Sel.Add OpeningPlate 
                |              Dim OpenFact As SfmOpening
                |              Set OpenFact = Sel.FindObject("CATIASfmOpening")
                |              'Get the Status of Opening
                |              Dim status As Long
                |              status = OpenFact.IsAPlateOpening

        :rtype: int
        """
        return self.sfm_opening.IsAPlateOpening()

    def set_master_mode(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMasterMode()
                | 
                |     Sets Master mode on Copy Pasted Opening. It breaks the dependency by
                |     duplicating the sketch.
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example Sets Master Mdoe on a Copy Pasted
                |             Opening.
                | 
                |              Dim OpeningMaster As SfmOpening
                |              Set OpeningMaster = part1.FindObjectByName("Opening_035")
                |              Dim Sel As Selection
                |              Set Sel = CATIA.ActiveDocument.Selection
                |              Sel.Add OpeningMaster 
                |              Dim OpenFact As SfmOpening
                |              Set OpenFact = Sel.FindObject("CATIASfmOpening")
                |              OpenFact.SetMasterMode

        :rtype: None
        """
        return self.sfm_opening.SetMasterMode()

    def __repr__(self):
        return f'SFMOpening(name="{self.name}")'
