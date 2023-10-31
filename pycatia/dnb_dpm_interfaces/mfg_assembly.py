#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.item import Item
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant


class MfgAssembly(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MfgAssembly
                | 
                | This Interface represents a Manufacturing Assembly.
                | Role: It gives access to the C++ DNBIMfgAssembly interface methods Such
                | as
                | 
                |     set and get the Name and PartNumber
                |     get the type DNBIAMfgAssemblyType
                |     get the assigned parts
                |     add and remove the assigned parts
                | 
                | Example:
                |     This example fetches an instance of a Manufacturing Assembly from a
                |     selected Activity
                | 
                |      Dim myActivity As Activity
                |      myActivity = 
                |      Dim myItem As Item
                |      Set myItem = myActivity.Items.Item(1)
                |      Dim obj As MfgAssembly
                |      Set obj = mySel.FindObject("DNBIAMfgAssembly")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mfg_assembly = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Count() As long (Read Only)
                | 
                |     Returns the number of assigned Parts (can be fetched via Item
                |     ).
                | 
                |     Example:
                |         This example fetches the Number of assigned Parts of a Manufacturing
                |         Assembly
                | 
                |          Dim Number As Long
                |          Number = obj.Count

        :rtype: int
        """

        return self.mfg_assembly.Count

    @property
    def ma_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MAName() As CATBSTR
                | 
                |     Returns or sets the Name of the Manufacturing Assembly. Name of the AST
                |     Manufacturing Assembly cannot be set/changed
                | 
                |     Example:
                |         This example fetches the Name of a Manufacturing
                |         Assembly
                | 
                |          Dim myName As String
                |          myName = obj.MAName
                |          
                | 
                |         This example sets the Name of a Manufacturing Assembly
                | 
                |          Dim newName As String
                |          newName = "NewMAName"
                |          obj.MAName = newName

        :rtype: str
        """

        return self.mfg_assembly.MAName

    @ma_name.setter
    def ma_name(self, value: str):
        """
        :param str value:
        """

        self.mfg_assembly.MAName = value

    @property
    def ma_part_number(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MAPartNumber() As CATBSTR
                | 
                |     Returns or sets the Part Number of the Manufacturing Assembly. Part Number
                |     of the AST MA cannot be set/changed
                | 
                |     Example:
                |         This example fetches the Part Number of a Manufacturing
                |         Assembly
                | 
                |          Dim myPart As String
                |          myPart = obj.MAPartNumber
                |
                |         This example sets the Part Number of a Manufacturing
                |         Assembly
                | 
                |          Dim newPartNbr As String
                |          newPartNbr = "NewMAPartNumber"
                |          obj.MAPartNumber = newPartNbr

        :rtype: str
        """

        return self.mfg_assembly.MAPartNumber

    @ma_part_number.setter
    def ma_part_number(self, value: str):
        """
        :param str value:
        """

        self.mfg_assembly.MAPartNumber = value

    @property
    def ma_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MAType() As DNBIAMfgAssemblyType (Read Only)
                | 
                |     Returns the Type of the Manufacturing Assembly. It will be either a
                |     manufacturingAssembly or a manufacturingKit defined in
                |     DNBIAMfgAssemblyType
                | 
                |     Example:
                |         This example fetches the Type of a Manufacturing
                |         Assembly
                | 
                |          Dim MAtype As String
                |          If obj.MAType = manufacturingAssembly Then
                |            MAtype = "Manufacturing Assembly"
                |          Else
                |            MAtype = "Manufacturing Kit"
                |          End If

        :return: enum dnbia_mfg_assembly_type
        :rtype: int
        """

        return self.mfg_assembly.MAType

    def add_part(self, i_item: Item) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPart(Item iItem)
                | 
                |     Assignes a part (Product, Resource or other MA/MK) to the Manufacturing
                |     Assembly. No part can be assigned to AST MA
                | 
                |     Parameters:
                | 
                |         iItem
                |             The item to be assigned
                | 
                |             Example:
                |                 This example adds a product to the assigned Parts of a
                |                 Manufacturing Assembly
                | 
                |                  Dim myProducts As PPRProducts
                |                  Set myProducts = DELMIA.ActiveDocument.PPRDocument.Products
                |                  Dim Part As Item
                |                  Set Part = myProducts.Item(2)
                |                  obj.AddPart(Part)

        :param Item i_item:
        :rtype: None
        """
        return self.mfg_assembly.AddPart(i_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_part'
        # # vba_code = """
        # # Public Function add_part(mfg_assembly)
        # #     Dim iItem (2)
        # #     mfg_assembly.AddPart iItem
        # #     add_part = iItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def item(self, i_index: cat_variant) -> Item:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Item
                | 
                |     Returns one assigned Part (Product, Resource or other MA/MK) of the
                |     Manufacturing Assembly.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index to the item to be returned 
                | 
                |     Returns:
                |         The assigned item
                | 
                |         Example:
                |             This example cycles through the list of assigned Parts of a
                |             Manufacturing Assembly
                | 
                |              Dim j As Long
                |              For j = 1 To obj.Count
                |                Dim it As Item
                |                Set it = obj.Item(j)
                |                Dim ItemName As String
                |                ItemName = it.Name
                |              Next

        :param cat_variant i_index:
        :rtype: Item
        """
        return Item(self.mfg_assembly.Item(i_index))

    def remove_part(self, i_item: Item) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePart(Item iItem)
                | 
                |     Removes a part (Product, Resource or other MA/MK) from the Manufacturing
                |     Assembly. No part can be removed from AST MA
                | 
                |     Parameters:
                | 
                |         iItem
                |             The item to be removed
                | 
                |             Example:
                |                 This example removes a product from the assigned Parts of a
                |                 Manufacturing Assembly
                | 
                |                  Dim myProducts As PPRProducts
                |                  Set myProducts = DELMIA.ActiveDocument.PPRDocument.Products
                |                  Dim Part As Item
                |                  Set Part = myProducts.Item(2)
                |                  obj.RemovePart(Part)

        :param Item i_item:
        :rtype: None
        """
        return self.mfg_assembly.RemovePart(i_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_part'
        # # vba_code = """
        # # Public Function remove_part(mfg_assembly)
        # #     Dim iItem (2)
        # #     mfg_assembly.RemovePart iItem
        # #     remove_part = iItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MfgAssembly(name="{self.name}")'
