#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class FastenerGroup(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FastenerGroup

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fastener_group = com_object

    @property
    def colour(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Color(long iColor) (Write Only)
                | 
                |     Sets the color of the fasteners.
                | 
                |     Example:
                |         This example sets the Color type of all the fasteners to
                |         red
                | 
                |          redCol  =16711680 'Encoded RGB color within long integer (R=255 G=0
                |          B=0)
                |          MyFastenerGroup.Color = redCol

        :rtype: int
        """

        return self.fastener_group.Color

    @colour.setter
    def colour(self, value: int):
        """
        :param int value:
        """

        self.fastener_group.Color = value

    @property
    def style(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Style(CATBSTR iStyle) (Write Only)
                | 
                |     Sets the CGR Style representation for the Spot Welds in the 3D
                |     Viewer.
                | 
                |     Parameters:
                | 
                |         iStyleType
                |             of the CGR Style to be used for representation.
                |             The valid set of Styles are :-
                | 
                |                 As specified in XML in tools-options page
                | 
                |             Example:
                |                 This example sets the CGR Style type of all the fasteners to
                |                 Sphere provided it is available in XML file
                | 
                |                  MyFastenerGroup.Style = "Sphere"

        :rtype: str
        """

        return self.fastener_group.Style

    @style.setter
    def style(self, value: str):
        """
        :param str value:
        """

        self.fastener_group.Style = value

    @property
    def symbol(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Symbol(CATBSTR iColor) (Write Only)
                | 
                |     Sets the symbol for representation for the Spot Welds in the 3D
                |     Viewer.
                | 
                |     Parameters:
                | 
                |         iSymbolType
                |             of the symbol to be used for representation.
                |             The valid set of symbols are :-
                | 
                |                 CROSS
                |                 PLUS
                |                 CONCENTRIC
                |                 COINCIDENT
                |                 FULLCIRCLE
                |                 FULLSQUARE
                |                 STAR
                |                 DOT
                |                 SMALLDOT
                | 
                |             Example:
                |                 This example sets the Symbol type of all the fasteners to
                |                 FULLSquare
                | 
                |                  MyFastenerGroup.Symbol = "FULLSQUARE"

        :rtype: str
        """

        return self.fastener_group.Symbol

    @symbol.setter
    def symbol(self, value: str):
        """
        :param str value:
        """

        self.fastener_group.Symbol = value

    def get_count(self, id_name: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCount(CATBSTR IDName) As long
                | 
                |     Returns the number of entities in the fastener group of the
                |     Type.
                | 
                |     Parameters:
                | 
                |         oNumOfEntities
                |             The number of Entities 
                | 
                |     Example:
                |         This example gets number of welds in the fastener
                |         Group
                | 
                |          Dim NumberOfWelds
                |          NumberOfWelds = MyFastenerGroup.GetCount("DELMIASpotWeld")
                |          
                | 
                |         This example gets number of FastenerGroups in the fastener
                |         Group
                | 
                |          Dim NumberOfGroups
                |          NumberOfGroups = MyFastenerGroup.GetCount("DELMIAFastenerGroup")

        :param str id_name:
        :rtype: int
        """
        return self.fastener_group.GetCount(id_name)

    def get_items(self, id_name: str, o_list_of_entities: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetItems(CATBSTR IDName,
                | CATSafeArrayVariant oListOfEntities)
                | 
                |     Returns the entities in the fastener group of the type which is input.
                |     which are direct children only 
                | 
                | Example:
                |     This example gets welds in the fastener Group
                | 
                |      Dim NumberOfWelds
                |      NumberOfWelds = MyFastenerGroup.GetItems("DELMIASpotWeld")
                |      
                | 
                |     This example gets the FastenerGroups in the fastener Group
                | 
                |      Dim NumberOfGroups
                |      NumberOfGroups = MyFastenerGroup.GetItems("DELMIAFastenerGroup")

        :param str id_name:
        :param tuple o_list_of_entities:
        :rtype: None
        """
        return self.fastener_group.GetItems(id_name, o_list_of_entities)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_items'
        # # vba_code = """
        # # Public Function get_items(fastener_group)
        # #     Dim IDName (2)
        # #     fastener_group.GetItems IDName
        # #     get_items = IDName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_joined_part_names(self, o_list_of_parts: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetJoinedPartNames(CATSafeArrayVariant oListOfParts)
                | 
                |     Returns the list of part names joined by fastener.
                | 
                |     Parameters:
                | 
                |         oListOfParts
                |             The list of parts 
                | 
                |     Example:
                |         This example gets list of parts joined by fastener
                | 
                |          Dim NumberOfParts
                |          Dim JoiningParts()
                |          NumberOfParts = MyFastenerGroup.NumberOfJoiningParts
                |          ReDim JoiningParts(NumParts-1)
                |          MyFastenerGroup.GetJoinedPartNames(JoiningParts)

        :param tuple o_list_of_parts:
        :rtype: None
        """
        return self.fastener_group.GetJoinedPartNames(o_list_of_parts)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_joined_part_names'
        # # vba_code = """
        # # Public Function get_joined_part_names(fastener_group)
        # #     Dim oListOfParts (2)
        # #     fastener_group.GetJoinedPartNames oListOfParts
        # #     get_joined_part_names = oListOfParts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_part(self, index: int) -> Product:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPart(short index) As Product
                | 
                |     Returns the product at the specified index from the list of parts joined by
                |     fastener group.
                | 
                |     Parameters:
                | 
                |         index
                |             Index should be greater than equal to 1. 
                | 
                |     Example:
                |         This example gets the part at index 1
                | 
                |          Dim MyProduct As Product
                |          Set MyProduct = MyFastenerGroup.GetPart(1)

        :param int index:
        :rtype: Product
        """
        return Product(self.fastener_group.GetPart(index))

    def hide(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Hide()
                | 
                |     Hides all the entities in the fastener group. 
                | 
                | Example:
                |     This example hides all the welds in the fastener Group
                | 
                |      MyFastenerGroup.Hide

        :rtype: None
        """
        return self.fastener_group.Hide()

    def number_of_joining_parts(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NumberOfJoiningParts() As long
                | 
                |     Returns the number of parts joined by the fastener group.
                | 
                |     Parameters:
                | 
                |         oNumOfParts
                |             The number of parts 
                | 
                |     Example:
                |         This example gets number of parts joined by fastener
                | 
                |          Dim NumberOfParts
                |          NumberOfParts = MyFastenerGroup.NumberOfJoiningParts

        :rtype: int
        """
        return self.fastener_group.NumberOfJoiningParts()

    def show(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Show()
                | 
                |     Shows all the entities in the fastener group. 
                | 
                | Example:
                |     This example shows all the welds in the fastener Group
                | 
                |      MyFastenerGroup.Show

        :rtype: None
        """
        return self.fastener_group.Show()

    def __repr__(self):
        return f'FastenerGroup(name="{self.name}")'
