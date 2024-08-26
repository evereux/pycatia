#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.drafting_interfaces.drawing_coord_dim import DrawingCoordDim
from pycatia.system_interfaces.any_object import AnyObject


class CoordDim(AnyObject):
    """

    Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CoordDim


    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.coord_dim = com_object

    def get_2d_annot(self) -> DrawingCoordDim:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func Get2dAnnot() As DrawingCoordDim
                |     Retrieves Drafting Coordinate dimension.

        :rtype: DrawingCoordDim
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return DrawingCoordDim(self.coord_dim.Get2dAnnot())

    def __repr__(self):
        return f'CoordDim(name="{self.name}")'
