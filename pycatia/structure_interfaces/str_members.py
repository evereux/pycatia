#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.structure_interfaces.str_member import StrMember
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class StrMembers(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrMembers
                | 
                | A collection of the Member objects contained in a given Product object of a
                | ProductDocument object.
                | A Product object aggregates zero or one Members collection. This collection is
                | retrieved using the Product.GetTechnologicalObject method of the
                | product.
                | 
                | Example:
                |     The following example retrieves the member collection from the oProduct
                |     Product.
                | 
                |      Dim oMembers as AnyObject
                |      Set oMembers = oProduct.GetTechnologicalObject("StructureMembers")
                |      
                | 
                |     Method Index
                |     Item
                |         Returns a member from its index in the Members collection.
                |         
                |     Remove
                |         Removes a member from the Members collection. 
                | 
                |     Methods
                | 
                | o Func Item(	CATVariant 	iIndex) As StrMember
                | 
                |     Returns a member from its index in the Members collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the member to retrieve in the collection of members.
                |             This index can either be the rank of the member in the collection or the name
                |             you assign to the member. As a numerics, this index is the rank of the member
                |             in the collection. The index of the first member in the collection is 1, and
                |             the index of the last member is Count. As a string, it is the name you assigned
                |             to the member using the 
                | 
                |         AnyObject.Name property 
                |     Returns:
                |         The retrieved member 
                |     Example:
                | 
                |           The following example returns in ThisMember the third
                |           member,
                |          and in ThatMember the member named
                |          Column_1 in the Assembly_1 member collection.
                |          
                | 
                |          Dim ThisMember As Member
                |          Set ThisMember = Assembly_1.Item(3)
                |          Dim ThatMember As Member
                |          Set ThatMember = Assembly.Item("Column_1")
                |          
                | 
                | o Sub Remove(	CATVariant 	iIndex)
                | 
                |     Removes a member from the Members collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the member to remove. This index can either be the
                |             rank of the member in the collection or the name you assigned to the member. As
                |             a numerics, this index is the rank of the member in the collection. The index
                |             of the first member in the collection is 1, and the index of the last member is
                |             Count. As a string, it is the name you assigned to the member using the
                |             
                | 
                |         AnyObject.Name property 
                |     Example:
                | 
                |           The following example removes the sixth member and the member
                |           named
                |          Column_1 from the Assembly_1 member collection.
                |          
                | 
                |          Assembly_1.Remove(6)
                |          Assembly_1.Remove("Column_1")
                |          
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrMember)
        self.str_members = com_object

    def item(self, i_index: cat_variant) -> StrMember:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As StrMember
                | 
                |     Returns a member from its index in the Members collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the member to retrieve in the collection of members.
                |             This index can either be the rank of the member in the collection or the name
                |             you assign to the member. As a numerics, this index is the rank of the member
                |             in the collection. The index of the first member in the collection is 1, and
                |             the index of the last member is Count. As a string, it is the name you assigned
                |             to the member using the 
                | 
                |         AnyObject.Name property 
                |     Returns:
                |         The retrieved member 
                |     Example:
                | 
                |           The following example returns in ThisMember the third
                |           member,
                |          and in ThatMember the member named
                |          Column_1 in the Assembly_1 member collection.
                |          
                | 
                |          Dim ThisMember As Member
                |          Set ThisMember = Assembly_1.Item(3)
                |          Dim ThatMember As Member
                |          Set ThatMember = Assembly.Item("Column_1")

        :param cat_variant i_index:
        :rtype: StrMember
        """
        return StrMember(self.str_members.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a member from the Members collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the member to remove. This index can either be the
                |             rank of the member in the collection or the name you assigned to the member. As
                |             a numerics, this index is the rank of the member in the collection. The index
                |             of the first member in the collection is 1, and the index of the last member is
                |             Count. As a string, it is the name you assigned to the member using the
                |             
                | 
                |         AnyObject.Name property 
                |     Example:
                | 
                |           The following example removes the sixth member and the member
                |           named
                |          Column_1 from the Assembly_1 member collection.
                |          
                | 
                |          Assembly_1.Remove(6)
                |          Assembly_1.Remove("Column_1")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.str_members.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(str_members)
        # #     Dim iIndex (2)
        # #     str_members.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'StrMembers(name="{self.name}")'
