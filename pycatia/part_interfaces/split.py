#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.part_interfaces.surface_based_shape import SurfaceBasedShape


class Split(SurfaceBasedShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.SurfaceBasedShape
                |                             Split
                | 
                | Represents the split operation.
                | It splits a shape using a splitting element, such as a surface, a face or a
                | plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.split = com_object

    @property
    def splitting_side(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SplittingSide() As CatSplitSide
                | 
                |     Returns or sets the splitting side . The splitting side is the side of the
                |     splitting element kept after the split. A positive side refers to the same
                |     orientation than the splitting element normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the splitting side of the
                |         split shape mySplit, and then sets it to
                |         catPositiveSide:
                | 
                |          Set sptSide = mySplit.SplittingSide
                |          mySplit.SplittingSide = catPositiveSide

        :return: enum cat_split_side
        :rtype: int
        """

        return self.split.SplittingSide

    @splitting_side.setter
    def splitting_side(self, value: int):
        """
        :param int value: enum cat_split_side
        """

        self.split.SplittingSide = value

    def __repr__(self):
        return f'Split(name="{self.name}")'
