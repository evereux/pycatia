#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_machinable_area import ManufacturingMachinableArea
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingPrismaticMachiningArea(ManufacturingMachinableArea):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingFeature
                |                        ManufacturingInterfaces.ManufacturingMachinableFeature
                |                            ManufacturingInterfaces.ManufacturingMachinableArea
                |                                ManufacturingPrismaticMachiningArea
                | 
                | ManufacturingPrismaticMachiningArea defines a set of properties and
                | methods.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_prismatic_machining_area = com_object

    @property
    def bottom_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BottomType() As CATBSTR
                | 
                |     Returns or sets the Hardness Mode on Bottom of a Manufacturing Prismatic
                |     Machining Area.
                | 
                |     Examples:
                |         The following example returns the hardness mode on bottom
                |         ThisBottomType of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim ThisBottomType As CATBSTR
                |          ThisBottomType = CurrentPMA.BottomType
                |
                |         The next example sets the hardness mode on bottom of the manufacturing
                |         prismatic machining area CurrentPMA
                | 
                |          CurrentPMA.BottomType = "MfgHard"
                |          
                |         To be allowed to change BottomType into MfgSoft, Islands geometries
                |         must be removed first.
                |          
                | 
                |     Legal values: BottomType can be
                | 
                |     MfgHard
                |     MfgSoft

        :rtype: str
        """

        return self.manufacturing_prismatic_machining_area.BottomType

    @bottom_type.setter
    def bottom_type(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_prismatic_machining_area.BottomType = value

    @property
    def contours_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ContoursCount() As long (Read Only)
                | 
                |     Retreives the number of Contour of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Example:
                |         The following example returns the number of Contour NumberOfContour of
                |         the manufacturing prismatic machining area CurrentPMA
                | 
                |          Dim NumberOfContour As Long
                |          NumberOfContour = CurrentPMA.ContoursCount

        :rtype: int
        """

        return self.manufacturing_prismatic_machining_area.ContoursCount

    @property
    def islands_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IslandsCount() As long (Read Only)
                | 
                |     Retreives the number of Island of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Example:
                |         The following example returns the number of Island NumberOfIsland of
                |         the manufacturing prismatic machining area CurrentPMA
                | 
                |          Dim NumberOfIsland As Long
                |          NumberOfIsland = CurrentPMA.IslandsCount

        :rtype: int
        """

        return self.manufacturing_prismatic_machining_area.IslandsCount

    @property
    def top_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TopType() As CATBSTR
                | 
                |     Returns or sets the Hardness Mode on top of a Manufacturing Prismatic
                |     Machining Area.
                | 
                |     Examples:
                |         The following example returns the hardness mode on top ThisTopType of
                |         the manufacturing prismatic machining area CurrentPMA
                | 
                |          Dim ThisTopType As CATBSTR
                |          ThisTopType = CurrentPMA.TopType
                |
                |         The next example sets the hardness mode on top of the manufacturing
                |         prismatic machining area CurrentPMA
                | 
                |          CurrentPMA.TopType = "MfgHard"
                |
                |     Legal values: TopType can be
                | 
                |     MfgHard
                |     MfgSoft

        :rtype: str
        """

        return self.manufacturing_prismatic_machining_area.TopType

    @top_type.setter
    def top_type(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_prismatic_machining_area.TopType = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR
                | 
                |     Returns or sets the Type of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Examples:
                |         The following example returns the feature type ThisType of the
                |         manufacturing prismatic machining area CurrentPMA
                | 
                |          Dim ThisType As CATBSTR
                |          ThisType = CurrentPMA.Type
                |          
                |         The next example sets the feature type of the manufacturing prismatic
                |         machining area CurrentPMA
                | 
                |          CurrentPMA.Type = "MfgPocketType"
                |          
                |         To be allowed to change Type into MfgPocketType or into
                |         MfgContouringType, Contours and Islands geometries must be removed
                |         first.
                |
                |     Legal values: Type can be
                | 
                |     MfgPocketType
                |     MfgContouringType

        :rtype: str
        """

        return self.manufacturing_prismatic_machining_area.Type

    @type.setter
    def type(self, value: str):
        """
        :param str value:
        """

        self.manufacturing_prismatic_machining_area.Type = value

    def get_contour_side(self, i_contour_number: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetContourSide(long iContourNumber) As short
                | 
                |     Gets the side of one contour of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Parameters:
                | 
                |         iContourNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be between 1 and ContoursCount (see Properties).
                |
                |         Example: The following example gets the side of the contour number
                |         iContourNumber of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iContourNumber As Long
                |          iContourNumber = 3
                | 
                |          Dim oContourSide As short
                |          oContourSide = CurrentPMA.GetContourSide(iContourNumber)

        :param int i_contour_number:
        :rtype: int
        """
        return self.manufacturing_prismatic_machining_area.GetContourSide(i_contour_number)

    def get_geometries_aquisition_mode(self, i_geometry_type: str, i_geometry_number: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGeometriesAquisitionMode(CATBSTR iGeometryType,
                | long iGeometryNumber) As short
                | 
                |     Gets the aquisition mode of one geometry of a Manufacturing Prismatic
                |     Machining Area.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be
                | 
                |             Contours
                |                 to get the aquisition mode of a guiding element
                |                 
                |             Islands
                |                 to get the aquisition mode of an island
                |                 (not allowed if Type == "MfgContouringType" or
                |                 if BottomType == "MfgSoft") (see Properties). 
                | 
                |         iGeometryNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be 1 if Type == "MfgPocketType" (see Properties) and
                |                 iGeometryType == "Contours". 
                |                 Must be between 1 and IslandsCount + 1 (or ContoursCount + 1)
                |                 (see Properties). 
                |
                |         Example: The following example gets the aquisition mode of the contour
                |         number iGeometryNumber of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iGeometryNumber As Long
                |          iGeometryNumber = 3
                | 
                |          Dim oMode As Short
                |          oMode = CurrentPMA.GetGeometriesAquisitionMode("Contours",iGeometryNumber)
                |
                |         Legal values: GetGeometriesAquisitionMode value can be
                | 
                |         0
                |             by Edges 
                |         1
                |             by Belt of Faces 
                |         2
                |             by Boundary of Faces (Islands only) 
                |         5
                |             by Boundary of Faces (Contours only)

        :param str i_geometry_type:
        :param int i_geometry_number:
        :rtype: int
        """
        return self.manufacturing_prismatic_machining_area.GetGeometriesAquisitionMode(
            i_geometry_type,
            i_geometry_number
        )

    def is_contour_closed(self, i_contour_number: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsContourClosed(long iContourNumber) As short
                | 
                |     Return the status of one contour of a Manufacturing Prismatic Machining Area : closed or open.
                | 
                |     Parameters:
                | 
                |         iContourNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be between 1 and ContoursCount (see Properties).
                |
                |         Example: The following example returns the status of the contour number
                |         iContourNumber of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iContourNumber As Long
                |          iContourNumber = 3
                | 
                |          Dim oIsClosed As short
                |          oIsClosed = CurrentPMA.IsContourClosed(iContourNumber)
                |
                |         Legal values: IsContourClosed value can be
                | 
                |         0 (means open contour)
                |         1 (means closed contour)

        :param int i_contour_number:
        :rtype: int
        """
        return self.manufacturing_prismatic_machining_area.IsContourClosed(i_contour_number)

    def remove_all_geometry(self, i_geometry_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAllGeometry(CATBSTR iGeometryType)
                | 
                |     Removes all the geometry of a specified type linked to a Manufacturing
                |     Prismatic Machining Area.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be
                | 
                |             RelimitingPlane
                |                 to remove the top plane 
                |             Parts
                |                 to remove the bottom 
                |             Checks
                |                 to remove the check elements 
                |             Contours
                |                 to remove the guiding elements 
                |             Islands
                |                 to remove the islands 
                |
                |         Example: The following example removes the bottom of the manufacturing
                |         prismatic machining area CurrentPMA
                | 
                |          Call CurrentPMA.RemoveAllGeometry("Parts")

        :param str i_geometry_type:
        :rtype: None
        """
        return self.manufacturing_prismatic_machining_area.RemoveAllGeometry(i_geometry_type)

    def set_closed_contour_side(self, i_contour_number: int, i_side: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClosedContourSide(long iContourNumber,
                | CATBSTR iSide)
                | 
                |     Sets the side of one closed contour of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Parameters:
                | 
                |         iContourNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be between 1 and ContoursCount (see Properties).
                |
                |         iSide
                |             Legal values: iSide can be
                | 
                |             Inside
                |             Outside
                |
                |         Example: The following example sets the side of the closed contour
                |         number iContourNumber of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iContourNumber As Long
                |          iContourNumber = 3
                | 
                |          Dim iContourSide As CATBSTR
                |          iContourSide = "Inside"
                |          Call CurrentPMA.SetClosedContourSide(iContourNumber,iContourSide)

        :param int i_contour_number:
        :param str i_side:
        :rtype: None
        """
        return self.manufacturing_prismatic_machining_area.SetClosedContourSide(i_contour_number, i_side)

    def set_contour_side(self, i_contour_number: int, i_side: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetContourSide(long iContourNumber,
                | short iSide)
                | 
                |     Sets the side of one contour of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Parameters:
                | 
                |         iContourNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be between 1 and ContoursCount (see Properties).
                |
                |         iSide
                |             Legal values: iSide can be
                | 
                |             1
                |             2
                |
                |         Example: The following example sets the side of the contour number
                |         iContourNumber of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iContourNumber As Long
                |          iContourNumber = 3
                | 
                |          Dim iContourSide As Short
                |          iContourSide = 2
                |          Call CurrentPMA.SetContourSide(iContourNumber,iContourSide)

        :param int i_contour_number:
        :param int i_side:
        :rtype: None
        """
        return self.manufacturing_prismatic_machining_area.SetContourSide(i_contour_number, i_side)

    def set_geometries(
            self,
            i_geometry_type: str,
            i_mode: int,
            i_geometry_number: int,
            i_reference: AnyObject,
            i_product: AnyObject,
            i_position: int
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGeometries(CATBSTR iGeometryType,
                | short iMode,
                | long iGeometryNumber,
                | AnyObject iReference,
                | AnyObject iProduct,
                | short iPosition)
                | 
                |     Sets or adds geometry in a collection of a specified type to a
                |     Manufacturing Prismatic Machining Area.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be
                | 
                |             Contours
                |                 to set or to add a guiding element 
                |             Islands
                |                 to set or to add an island
                |                 (not allowed if Type == "MfgContouringType" or
                |                 if BottomType == "MfgSoft") (see Properties). 
                | 
                |         iMode
                |             Legal values: iMode can be
                | 
                |             0
                |                 by Edges 
                | 
                |         iGeometryNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be 1 if Type == "MfgPocketType" (see Properties) and
                |                 iGeometryType == "Contours". 
                |                 Must be between 1 and IslandsCount + 1 (or ContoursCount + 1)
                |                 (see Properties). 
                | 
                |         iReference
                |             The geometry to be set. 
                |         iProduct
                |             The product containing the geometry to be set. 
                |         iPosition
                |             0 
                |
                |         Example: The following example sets 3 Islands, linked to 2 circles and
                |         3 lines, to the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iGeometryNumber As Long
                |          iGeometryNumber = 0
                |          ...
                |          'Get number of Island of CurrentPMA and add 1 to create a new island
                |          (Island number 1)
                |          iGeometryNumber = CurrentPMA.IslandsCount + 1
                |          Call CurrentPMA.SetGeometries("Islands",0,iGeometryNumber,Circle1,PartMachined,0)
                |
                |          'Get number of Island of CurrentPMA and add 1 to create a new island 
                |          (Island number 2)
                |          iGeometryNumber = CurrentPMA.IslandsCount + 1
                |          Call CurrentPMA.SetGeometries("Islands",0,iGeometryNumber,Circle2,PartMachined,0)
                |
                |          'Get number of Island of CurrentPMA and add 1 to create a new island 
                |          (Island number 3)
                |          iGeometryNumber = CurrentPMA.IslandsCount + 1
                |          Call CurrentPMA.SetGeometries("Islands",0,iGeometryNumber,Line5,PartMachined,0)
                |
                |          'Adding Line6 to Island number 3
                |          Call CurrentPMA.SetGeometries("Islands",0,iGeometryNumber,Line6,PartMachined,0)
                |
                |          'Adding Line7 to Island number 3
                |          Call CurrentPMA.SetGeometries("Islands",0,iGeometryNumber,Line7,PartMachined,0)

        :param str i_geometry_type:
        :param int i_mode:
        :param int i_geometry_number:
        :param AnyObject i_reference:
        :param AnyObject i_product:
        :param int i_position:
        :rtype: None
        """
        return self.manufacturing_prismatic_machining_area.SetGeometries(
            i_geometry_type,
            i_mode,
            i_geometry_number,
            i_reference.com_object,
            i_product.com_object,
            i_position
        )

    def set_geometry(self, i_geometry_type: str, i_reference: AnyObject, i_product: AnyObject, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGeometry(CATBSTR iGeometryType,
                | AnyObject iReference,
                | AnyObject iProduct,
                | short iPosition)
                | 
                |     Sets a geometry of a specified type to a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Parameters:
                | 
                |         iGeometryType
                |             Legal values: iGeometryType can be
                | 
                |             RelimitingPlane
                |                 to set the top plane 
                |             Parts
                |                 to set the bottom 
                |             Checks
                |                 to set a check element 
                | 
                |         iReference
                |             The geometry to be set. 
                |         iProduct
                |             The product containing the geometry to be set. 
                |         iPosition
                |             0 
                | 
                | 
                |         Example: The following example sets the top plane Plane2 to the
                |         manufacturing prismatic machining area CurrentPMA
                | 
                |          Call CurrentPMA.SetGeometry("RelimitingPlane",Plane2,PartMachined,0)

        :param str i_geometry_type:
        :param AnyObject i_reference:
        :param AnyObject i_product:
        :param int i_position:
        :rtype: None
        """
        return self.manufacturing_prismatic_machining_area.SetGeometry(
            i_geometry_type,
            i_reference.com_object,
            i_product.com_object,
            i_position
        )

    def set_open_contour_side(self, i_contour_number: int, i_point: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOpenContourSide(long iContourNumber,
                | AnyObject iPoint)
                | 
                |     Sets the side of one open contour of a Manufacturing Prismatic Machining
                |     Area.
                | 
                |     Parameters:
                | 
                |         iContourNumber
                |             The geometry index inside the collection.
                | 
                |                 Must be between 1 and ContoursCount (see Properties).
                |                 
                | 
                |         iPoint
                |             A point near one of both limits of the contour.
                | 
                |                 From this limit to the other one, the side of the contour is on
                |                 the left. 
                |
                |         Example: The following example sets the side of the open contour number
                |         iContourNumber of the manufacturing prismatic machining area
                |         CurrentPMA
                | 
                |          Dim iContourNumber As Long
                |          iContourNumber = 3
                | 
                |          Dim Point1 As CATIABase
                |          ...
                |          Set Point1 = hybridShapes1.Item("Point.1")
                |          ...
                | 
                |          Call
                |          CurrentPMA.SetOpenContourSide(iContourNumber,Point1)

        :param int i_contour_number:
        :param AnyObject i_point:
        :rtype: None
        """
        return self.manufacturing_prismatic_machining_area.SetOpenContourSide(i_contour_number, i_point.com_object)

    def __repr__(self):
        return f'ManufacturingPrismaticMachiningArea(name="{self.name}")'
