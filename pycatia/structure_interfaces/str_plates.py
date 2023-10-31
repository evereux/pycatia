#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.structure_interfaces.str_plate import StrPlate
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class StrPlates(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrPlates
                | 
                | A collection of the Plate objects contained in a given Product object of a
                | ProductDocument object.
                | A Product object can aggregate one or zero Plates collection. This collection
                | is retrieved using the Product.GetTechnologicalObject method of the
                | product.
                | 
                | Example:
                |     The following example retrieves the plate collection from the oProduct
                |     Product.
                | 
                |      Dim oPlates as AnyObject
                |      Set oPlates = oProduct.GetTechnologicalObject("StructurePlates")
                |      
                | 
                |     Method Index
                |     Item
                |         Returns a plate from its index in the Plates collection.
                |         
                |     Remove
                |         Removes a plate from the Plates collection. 
                | 
                |     Methods
                | 
                | o Func Item(	CATVariant 	iIndex) As StrPlate
                | 
                |     Returns a plate from its index in the Plates collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the plate to retrieve in the collection of plates.
                |             This index can either be the rank of the plate in the collection or the name
                |             you assign to the plate. As a numerics, this index is the rank of the plate in
                |             the collection. The index of the first plate in the collection is 1, and the
                |             index of the last plate is Count. As a string, it is the name you assigned to
                |             the plate using the 
                | 
                |         AnyObject.Name property 
                |     Returns:
                |         The retrieved plate
                | 
                |         Example:
                |             The following example returns in ThisPlate the third plate, and in
                |             ThatPlate the plate named EndPlate_1 in the Assembly_1 plate
                |             collection.
                | 
                |              Dim ThisPlate As Plate
                |              Set ThisPlate = Assembly_1.Item(3)
                |              Dim ThatPlate As Plate
                |              Set ThatPlate = Assembly.Item("EndPlate_1")
                |              
                | 
                | o Sub Remove(	CATVariant 	iIndex)
                | 
                |     Removes a plate from the Plates collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the plate to remove. This index can either be the rank
                |             of the plate in the collection or the name you assigned to the plate. As a
                |             numerics, this index is the rank of the plate in the collection. The index of
                |             the first plate in the collection is 1, and the index of the last plate is
                |             Count. As a string, it is the name you assigned to the plate using the
                |             
                | 
                |         AnyObject.Name property
                | 
                |         Example:
                |             The following example removes the sixth plate and the plate named
                |             EndPlate_1 from the Assembly_1 plate collection.
                | 
                |              Assembly_1.Remove(6)
                |              Assembly_1.Remove("EndPlate_1")
                |              
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrPlate)
        self.str_plates = com_object

    def item(self, i_index: cat_variant) -> StrPlate:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As StrPlate
                | 
                |     Returns a plate from its index in the Plates collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the plate to retrieve in the collection of plates.
                |             This index can either be the rank of the plate in the collection or the name
                |             you assign to the plate. As a numerics, this index is the rank of the plate in
                |             the collection. The index of the first plate in the collection is 1, and the
                |             index of the last plate is Count. As a string, it is the name you assigned to
                |             the plate using the 
                | 
                |         AnyObject.Name property 
                |     Returns:
                |         The retrieved plate
                | 
                |         Example:
                |             The following example returns in ThisPlate the third plate, and in
                |             ThatPlate the plate named EndPlate_1 in the Assembly_1 plate
                |             collection.
                | 
                |              Dim ThisPlate As Plate
                |              Set ThisPlate = Assembly_1.Item(3)
                |              Dim ThatPlate As Plate
                |              Set ThatPlate = Assembly.Item("EndPlate_1")

        :param cat_variant i_index:
        :rtype: StrPlate
        """
        return StrPlate(self.str_plates.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a plate from the Plates collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the plate to remove. This index can either be the rank
                |             of the plate in the collection or the name you assigned to the plate. As a
                |             numerics, this index is the rank of the plate in the collection. The index of
                |             the first plate in the collection is 1, and the index of the last plate is
                |             Count. As a string, it is the name you assigned to the plate using the
                |             
                | 
                |         AnyObject.Name property
                | 
                |         Example:
                |             The following example removes the sixth plate and the plate named
                |             EndPlate_1 from the Assembly_1 plate collection.
                | 
                |              Assembly_1.Remove(6)
                |              Assembly_1.Remove("EndPlate_1")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.str_plates.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(str_plates)
        # #     Dim iIndex (2)
        # #     str_plates.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'StrPlates(name="{self.name}")'
