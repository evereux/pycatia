#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.navigator_interfaces.group import Group
from pycatia.system_interfaces.collection import Collection


class Merges(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Merges
                | 
                | Interface to compute CATIAMerges
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.merges = com_object

    def clean_up(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CleanUp()
                | 
                |     Performs some clean-up.

        :rtype: None
        """
        return self.merges.CleanUp()

    def compute_merge(
            self,
            group_of_selected_products: Group,
            i_accuracy_for_simplification: float,
            i_keep_edges: int,
            i_decoration: int
    ) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ComputeMerge(Group GroupOfSelectedProducts,
                | double iAccuracyForSimplification,
                | long iKeepEdges,
                | long iDecoration) As Document
                | 
                |     Computes the merge on the selected products.
                | 
                |     Parameters:
                | 
                |         GroupOfSelectedProducts
                |             The selected products on which you want to perform the 3D cut.
                |             
                |         iAccuracyForSimplification
                |             Set this to a non null value to have the simplification activated.
                |             
                |         iKeepEdges
                |             Do you want edges in the result? 
                |         iDecoration
                |             Do you want decorations in the result? 
                | 
                |     Returns:
                |         MergeDocument: Document containing the result.

        :param Group group_of_selected_products:
        :param float i_accuracy_for_simplification:
        :param int i_keep_edges:
        :param int i_decoration:
        :rtype: Document
        """
        return Document(
            self.merges.ComputeMerge(
                group_of_selected_products.com_object,
                i_accuracy_for_simplification,
                i_keep_edges,
                i_decoration
            )
        )

    def merge_shape_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func MergeShapeName() As CATBSTR
                | 
                |     Returns the name of the associated shape.

        :rtype: str
        """
        return self.merges.MergeShapeName()

    def __repr__(self):
        return f'Merges(name="{self.name}")'
