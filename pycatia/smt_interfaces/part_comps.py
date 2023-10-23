#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.product_structure_interfaces.product import Product
from pycatia.smt_interfaces.part_comp import PartComp
from pycatia.system_interfaces.collection import Collection


class PartComps(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PartComps
                | 
                | Interface to access a CATIAPartComps
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=PartComp)
        self.part_comps = com_object

    @property
    def added_material_percentage(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AddedMaterialPercentage() As double (Read Only)
                | 
                |     Returns the added material percentage.

        :rtype: float
        """

        return self.part_comps.AddedMaterialPercentage

    @property
    def added_material_volume(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AddedMaterialVolume() As double (Read Only)
                | 
                |     Returns the added material volume.

        :rtype: float
        """

        return self.part_comps.AddedMaterialVolume

    @property
    def removed_material_percentage(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RemovedMaterialPercentage() As double (Read Only)
                | 
                |     Returns the removed material percentage.

        :rtype: float
        """

        return self.part_comps.RemovedMaterialPercentage

    @property
    def removed_material_volume(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RemovedMaterialVolume() As double (Read Only)
                | 
                |     Returns the removed material volume.

        :rtype: float
        """

        return self.part_comps.RemovedMaterialVolume

    def add(
            self,
            i_product1: Product,
            i_product2: Product,
            i_comp_accuracy: float,
            i_disp_accuracy: float,
            i_computation_type: int
    ) -> PartComp:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(Product iProduct1,
                | Product iProduct2,
                | double iCompAccuracy,
                | double iDispAccuracy,
                | long iComputationType) As PartComp
                | 
                |     Computes a new comparison between products. Documents created are added to
                |     the documents in the session. Document containing the added material is called
                |     AddedMaterial.3dmap. Document containing the removed material is called
                |     RemovedMaterial.3dmap. Document containing the changed material is called
                |     ChangedMaterial.3dmap. If the document are meant to be kept they must be
                |     renamed, otherwise they should be deleted. Document lifecyle must be managed
                |     either with SaveAs or Close.
                | 
                |     Parameters:
                | 
                |         iCompAccuracy
                |             Accuracy of the 3dmaps for the computation. 
                |         iDispAccuracy
                |             Accuracy of the displayed 3dmaps. 
                |         iComputationType
                |             0 : Added with position taken into account
                |             1 : Removed with position
                |             2 : Added + Removed with positions
                |             3 : Added without position
                |             4 : Removed without position
                |             5 : Added + Removed without positions
                | 
                |     Returns:
                |         Created PartComp 
                |     Example:
                | 
                |           The following example computes a comparison between two
                |           products:
                |          
                | 
                |          Dim newPartComp As PartComp
                |          Set newPartComp = PartComps.Add(product1, product2, 5.0, 5.0, 2)
                |          Dim documents1 As Documents
                |          Set documents1 = CATIA.Documents
                |          Dim document1 As Document
                |          Set document1 = documents1.Item("AddedMaterial.3dmap")

        :param Product i_product1:
        :param Product i_product2:
        :param float i_comp_accuracy:
        :param float i_disp_accuracy:
        :param int i_computation_type:
        :rtype: PartComp
        """
        return PartComp(
            self.part_comps.Add(
                i_product1.com_object,
                i_product2.com_object,
                i_comp_accuracy,
                i_disp_accuracy,
                i_computation_type
            )
        )

    def __repr__(self):
        return f'PartComps(name="{self.name}")'
