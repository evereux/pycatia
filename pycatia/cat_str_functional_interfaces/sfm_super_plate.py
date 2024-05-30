#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_object import SFMObject
from pycatia.cat_str_functional_interfaces.sfm_slots import SFMSlots
from pycatia.cat_str_functional_interfaces.sfm_split_plates import SFMSplitPlates
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.length import Length
from pycatia.types.general import cat_variant


class SFMSuperPlate(SFMObject):
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
                |                         SfmSuperPlate
                | 
                | Interface to manage the Structure Functional Modeler SuperPlate
                | object.
                | Role: Allows accessing and setting of SuperPlate's data.
                | 
                | See also:
                |     SfmFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_super_plate = com_object

    @property
    def limit_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LimitMode() As long
                | 
                |     Returns or sets the SuperPlate's limit mode.
                | 
                |     Example:
                |         This example retrieves in LimitMode the limit mode of the SuperPlate
                |         feature.
                | 
                |          Dim LimitMode As Integer
                |          Set LimitMode = SuperPlate.LimitMode

        :rtype: int
        """

        return self.sfm_super_plate.LimitMode

    @limit_mode.setter
    def limit_mode(self, value: int):
        """
        :param int value:
        """

        self.sfm_super_plate.LimitMode = value

    @property
    def molded_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MoldedSurface() As Reference (Read Only)
                | 
                |     Returns the molded surface.
                | 
                |     Example:
                |         This example retrieves in MoldedSurface the molded surface for the
                |         SuperPlate feature.
                | 
                |          Dim MoldedSurface As Reference
                |          Set MoldedSurface = SuperPlate.MoldedSurface

        :rtype: Reference
        """

        return Reference(self.sfm_super_plate.MoldedSurface)

    @property
    def split_plates(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplitPlates() As References (Read Only)
                | 
                |     Returns the SplitPlates.
                | 
                |     Example:
                |         This example retrieves in SplitPlates the list of SplitPlates for the
                |         SuperPlate feature.
                | 
                |          Dim SplitPlates As References
                |          Set SplitPlates = SuperPlate.SplitPlates

        :rtype: References
        """

        return References(self.sfm_super_plate.SplitPlates)

    @property
    def split_plates_objects(self) -> SFMSplitPlates:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SplitPlatesObjects() As SfmSplitPlates (Read Only)
                | 
                |     Returns the SplitPlates.
                | 
                |     Example:
                |         This example retrieves in SplitPlates the list of SplitPlates for the
                |         SuperPlate feature.
                | 
                |          Dim SuperPlate2 As SfmSuperPlate
                |          Set SuperPlate2 = SuperPlates.Item(2)
                |          Dim OperatedSuperPlateObject  As SfmSuperPlateObject
                |          Set OperatedSuperPlateObject = SuperPlate2.GetItem("SfmSuperPlateObject")
                |          Dim SplitPlates As SplitPlatesObjects
                |          Set SplitPlates = SuperPlate.SplitPlatesObjects

        :rtype: SFMSplitPlates
        """

        return SFMSplitPlates(self.sfm_super_plate.SplitPlatesObjects)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Support() As Reference
                | 
                |     Returns the SuperPlate's support.
                | 
                |     Example:
                |         This example retrieves in Support the support of the SuperPlate
                |         feature.
                | 
                |          Dim Support As Reference
                |          Set Support = SuperPlate.Support

        :rtype: Reference
        """

        return Reference(self.sfm_super_plate.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.sfm_super_plate.Support = value.com_object

    @property
    def support_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SupportOffset() As double
                | 
                |     Returns or sets the SuperPlate's support offset.
                | 
                |     Example:
                |         This example retrieves in Offset the support offset of the SuperPlate
                |         feature.
                | 
                |          Dim Offset As Double
                |          Set Offset = SuperPlate.SupportOffset

        :rtype: float
        """

        return self.sfm_super_plate.SupportOffset

    @support_offset.setter
    def support_offset(self, value: float):
        """
        :param float value:
        """

        self.sfm_super_plate.SupportOffset = value

    @property
    def support_offset_param(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SupportOffsetParam() As Length (Read Only)

        :rtype: Length
        """

        return Length(self.sfm_super_plate.SupportOffsetParam)

    @property
    def thickness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Thickness() As double
                | 
                |     Returns or sets the SuperPlate's Thickness.
                | 
                |     Example:
                |         This example retrieves the Thickness of existing
                |         SuperPlate.
                | 
                |          Dim ThicknessValue As Double
                |          Set ThicknessValue = SuperPlate.Thickness

        :rtype: float
        """

        return self.sfm_super_plate.Thickness

    @thickness.setter
    def thickness(self, value: float):
        """
        :param float value:
        """

        self.sfm_super_plate.Thickness = value

    def add_limit(self, i_limit: Reference, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddLimit(Reference iLimit,
                | long iOrientation)
                | 
                |     Adds one object to the list of connected object.
                | 
                |     Parameters:
                | 
                |         iLimit
                |             [in] New Limit to add. 
                |         iOrientation
                |             [in] iOrientation value can be selected from
                |                  InvertOrientation = -1,
                |                  UnknownOrientation = 0,
                |                  SameOrientation = 1,
                |                  GlobalOrientation(Xp) = 2,
                |                  GlobalOrientation(Xm) = 3,
                |                  GlobalOrientation(Yp) = 4,
                |                  GlobalOrientation(Ym) = 5,
                |                  GlobalOrientation(Zp) = 6,
                |                  GlobalOrientation(Zm) = 7,
                |                  GlobalOrientation_Inside = 8,
                |                  [SameOrientation ] GlobalOrientation_Outside = 9,
                |                  [InvertOrientation ] GlobalOrientation_LInboard = 10
                |                  [Toward center line] GlobalOrientation_LOutboard = 11
                |                  [Opposite of previous one ] GlobalOrientation_TInboard = 12 [Toward midship ]
                |                  GlobalOrientation_TOutboard = 13 [Opposite of previous one]
                | 
                |             Example:
                |                 This example adds one limit to Deck Plate, and keeps Fore
                |                 Side.
                | 
                |                  Set PlateLimit = ObjPart.FindObjectByName("CROSS.60")
                |                  Dim LimitRef As Reference
                |                  Set LimitRef = ObjPart.CreateReferenceFromObject(PlateLimit)
                |                  Dim Orientation As Long
                |                  Orientation = 2
                |                  SuperPlate.AddLimit LimitRef, Orientation

        :param Reference i_limit:
        :param int i_orientation:
        :rtype: None
        """
        return self.sfm_super_plate.AddLimit(i_limit.com_object, i_orientation)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_limit'
        # # vba_code = """
        # # Public Function add_limit(sfm_super_plate)
        # #     Dim iLimit (2)
        # #     sfm_super_plate.AddLimit iLimit
        # #     add_limit = iLimit
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_free_edges(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFreeEdges() As References
                | 
                |     Returns the Free Edges of Super Plate.
                | 
                |     Example:
                |         This example retrieves in FreeEdges the list of free edges for the
                |         SuperPlate feature.
                | 
                |           
                |         Dim FreeEdges As References
                |         Set FreeEdges = SuperPlate.GetFreeEdges

        :rtype: References
        """
        return References(self.sfm_super_plate.GetFreeEdges())

    def get_slots_on_plate(self) -> SFMSlots:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSlotsOnPlate() As SfmSlots
                | 
                |     Retrieves Slots on Plate.
                | 
                |     Parameters:
                | 
                |         oSfmSlots
                |             [out] Slots. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This example gets the Slots.
                | 
                |              Dim SlotsonPlate As SfmSlots
                |              Set SlotsonPlate = PlateObj.GetSlotsOnPlate

        :rtype: SFMSlots
        """
        return SFMSlots(self.sfm_super_plate.GetSlotsOnPlate())

    def get_split_plate_attributes(
            self,
            i_split_plate_number: int,
            o_thickness: float,
            o_material_name: str,
            o_grade_name: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSplitPlateAttributes(long iSplitPlateNumber,
                | double oThickness,
                | CATBSTR oMaterialName,
                | CATBSTR oGradeName)
                | 
                |     Returns the SplitPlate(ChildPlate)
                |     Attributes(Thickness,Material,Grade).
                | 
                |     Parameters:
                | 
                |         iSplitPlateNumber
                |             [in] This Number is the Split Plate number desired.
                |             
                |         oThickness
                |             [out] Thickness of the child Plate. 
                |         oMaterialName
                |             [out] Material of the child Plate. 
                |         oGradeName
                |             [out] Grade of the child Plate.
                | 
                |             Example:
                |                 This example retrieves the attributes of the
                |                 ChildPlate.
                | 
                |                  'Retrieve the Split Plates under the
                |                  SuperPlate
                |                  Dim SplitPlates as References
                |                  Set SplitPlates = SuperPlateObj.SplitPlates
                |                  Dim SplitPlate1 As Reference
                |                  Set SplitPlate1 = SplitPlates.Item(1)
                |                  'Add the Split Plate to Selection
                |                  Set SelctionObj = CATIA.ActiveDocument.Selection
                |                  SelctionObj.Add SplitPlate1
                |                  'Retrieve the Split Plate From Selection
                |                  Dim SplitPlateObj As SfmSuperPlate
                |                  Set SplitPlateObj = SelctionObj.FindObject("CATIASfmSuperPlate")
                |                  Dim Thickness As Double
                |                  Dim Material As String
                |                  Dim Grade As String    
                |                  SplitPlateObj.GetSplitPlateAttributes 1, Thickness ,Material
                |                  ,Grade

        :param int i_split_plate_number:
        :param float o_thickness:
        :param str o_material_name:
        :param str o_grade_name:
        :rtype: None
        """
        return self.sfm_super_plate.GetSplitPlateAttributes(
            i_split_plate_number,
            o_thickness,
            o_material_name,
            o_grade_name
        )

    def invert_limit(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InvertLimit(CATVariant iIndex)
                | 
                |     Invert a limit orientation by its index or its name.
                | 
                |     Example:
                |         This example removes the first object from the list of connected
                |         objects for the StfConnection feature.
                | 
                |          StfConnection.RemoveObject 1

        :param cat_variant i_index:
        :rtype: None
        """
        return self.sfm_super_plate.InvertLimit(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'invert_limit'
        # # vba_code = """
        # # Public Function invert_limit(sfm_super_plate)
        # #     Dim iIndex (2)
        # #     sfm_super_plate.InvertLimit iIndex
        # #     invert_limit = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def limit_orientations(self, io_orientations: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub LimitOrientations(CATSafeArrayVariant ioOrientations)
                | 
                |     Returns the orientation of the limits.
                | 
                |     Example:
                |         This example retrieves in Orientations the list of orientations limit
                |         for the SuperPlate feature.
                | 
                |          Dim Orientations As References
                |          SuperPlate.LimitOrientations Orientations

        :param tuple io_orientations:
        :rtype: None
        """
        return self.sfm_super_plate.LimitOrientations(io_orientations)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'limit_orientations'
        # # vba_code = """
        # # Public Function limit_orientations(sfm_super_plate)
        # #     Dim ioOrientations (2)
        # #     sfm_super_plate.LimitOrientations ioOrientations
        # #     limit_orientations = ioOrientations
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def limits(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Limits() As References
                | 
                |     Returns the limits.
                | 
                |     Example:
                |         This example retrieves in Limits the list of limits for the SuperPlate
                |         feature.
                | 
                |          Dim Limits As References
                |          SuperPlate.Limits Limits, Orientations

        :rtype: References
        """
        return References(self.sfm_super_plate.Limits())

    def remove_limit(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveLimit(CATVariant iIndex)
                | 
                |     Removes one object from the list of limits by its index or its
                |     name.
                | 
                |     Example:
                |         This example removes the first object from the list of connected
                |         objects for the StfConnection feature.
                | 
                |          StfConnection.RemoveObject 1

        :param cat_variant i_index:
        :rtype: None
        """
        return self.sfm_super_plate.RemoveLimit(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_limit'
        # # vba_code = """
        # # Public Function remove_limit(sfm_super_plate)
        # #     Dim iIndex (2)
        # #     sfm_super_plate.RemoveLimit iIndex
        # #     remove_limit = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def run(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Run()
                | 
                |     Build the SplitPlates.
                | 
                |     Example:
                |         This example build the SplitPlates for the SuperPlate
                |         feature.
                | 
                |          SuperPlate.Run

        :rtype: None
        """
        return self.sfm_super_plate.Run()

    def set_as_last_limit(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAsLastLimit(CATVariant iIndex)
                | 
                |     Adds one limit at the end of the list.
                | 
                |     Example:
                |         This example sets the limit at the end of the list of
                |         limits.
                | 
                |          SuperPlate.SetAsLastLimit Index

        :param cat_variant i_index:
        :rtype: None
        """
        return self.sfm_super_plate.SetAsLastLimit(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_as_last_limit'
        # # vba_code = """
        # # Public Function set_as_last_limit(sfm_super_plate)
        # #     Dim iIndex (2)
        # #     sfm_super_plate.SetAsLastLimit iIndex
        # #     set_as_last_limit = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_split_plate_attributes(
            self,
            i_split_plate_number: int,
            i_thickness: float,
            i_material_name: str,
            i_grade_name: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSplitPlateAttributes(long iSplitPlateNumber,
                | double iThickness,
                | CATBSTR iMaterialName,
                | CATBSTR iGradeName)
                | 
                |     Set the SplitPlate(ChildPlate)
                |     Attributes(Thickness,Material,Grade).
                | 
                |     Parameters:
                | 
                |         iSplitPlateNumber
                |             [in] iSplitPlateNumber will be 1,2,3... 
                |         iThickness
                |             [in] Thickness of the child Plate. 
                |         iMaterialName
                |             [in] Material of the child Plate. 
                |         iGradeName
                |             [in] Grade of the child Plate.
                | 
                |             Example:
                |                 This example sets the attributes of the
                |                 ChildPlate.
                | 
                |                  'Retrieve the Split Plates under the
                |                  SuperPlate
                |                  Dim SplitPlates as References
                |                  Set SplitPlates = SuperPlateObj.SplitPlates
                |                  Dim SplitPlate1 As Reference
                |                  Set SplitPlate1 = SplitPlates.Item(1)
                |                  'Add the Split Plate to Selection
                |                  Set SelctionObj = CATIA.ActiveDocument.Selection
                |                  SelctionObj.Add SplitPlate1
                |                  'Retrieve the Split Plate From Selection
                |                  Dim SplitPlateObj As SfmSuperPlate
                |                  Set SplitPlateObj = SelctionObj.FindObject("CATIASfmSuperPlate")
                |                  SplitPlateObj.SetSplitPlateAttributes 1, 30, "Steel",
                |                  "A45"

        :param int i_split_plate_number:
        :param float i_thickness:
        :param str i_material_name:
        :param str i_grade_name:
        :rtype: None
        """
        return self.sfm_super_plate.SetSplitPlateAttributes(
            i_split_plate_number,
            i_thickness,
            i_material_name,
            i_grade_name
        )

    def __repr__(self):
        return f'SFMSuperPlate(name="{self.name}")'
