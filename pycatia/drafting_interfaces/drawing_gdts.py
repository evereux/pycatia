#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.drafting_interfaces.drawing_gdt import DrawingGDT
from pycatia.system_interfaces.collection import Collection


class DrawingGDTs(Collection):
    """

    Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingGDTs
                |
                | A collection of all the drawing GDTs currently managed by a drawing view of
                | drawing sheet in a drawing document.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_gd_ts = com_object

    def add(
            self,
            i_position_leader_x: float,
            i_position_leader_y: float,
            i_position_x: float,
            i_position_y: float,
            i_gdt_symbol: int,
            i_text: str
    ) -> DrawingGDT:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func Add(double iPositionLeaderX,double iPositionLeaderY,double
                | iPositionX,double iPositionY,long iGDTSymbol,CATBSTR iText) As
                | DrawingGDT
                |     Creates a drawing GDT and adds it to the drawing GDTs collection. This
                |     drawing GDT becomes the active one.
                |
                |     Parameters:
                |
                |         iPositionLeaderX,
                |             iPositionLeaderY The drawing leader of the GDT x and y coordinates,
                |             expressed in millimeters, and expressed with respect to the view coordinate
                |             system
                |         iPositionX,
                |             iPositionY The drawing GDT x and y coordinates, expressed in
                |             millimeters, and expressed with respect to the view coordinate system
                |
                |         iGDTSymbol
                |             The symbol to use in the first row.
                |
                |     See also:
                |         CATIADrawingGDT::GetToleranceType
                |     Parameters:
                |
                |         iText
                |             The text of the iGDTSymbol

        :param float i_position_leader_x:
        :param float i_position_leader_y:
        :param float i_position_x:
        :param float i_position_y:
        :param int i_gdt_symbol:
        :param str i_text:
        :rtype: DrawingGDT
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingGDT(
            self.drawing_gd_ts.Add(
                i_position_leader_x,
                i_position_leader_y,
                i_position_x,
                i_position_y,
                i_gdt_symbol,
                i_text
            )
        )

    def item(self, i_index: int) -> DrawingGDT:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func Item(long iIndex) As DrawingGDT
                |     Returns a drawing GDT using its index from the drawing GDTs
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the drawing GDT to retrieve from the collection of
                |             drawing GDTs. As a numerics, this index is the rank of the drawing GDT in the
                |             collection. The index of the first drawing GDT in the collection is 1, and the
                |             index of the last drawing GDT is Count.
                |
                |     Returns:
                |         The retrieved drawing GDT
                |
                | Example:
                |     This example retrieves in ThisDrawingGDT the second drawing GDT, in the
                |     drawing GDT collection of the active view in the active sheet, in the active
                |     document supposed to be a drawing document.
                |
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingGDT As DrawingGDT
                |      Set ThisDrawingGDT = MyView.GDTs.Item(2)

        :param int i_index:
        :rtype: DrawingGDT
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DrawingGDT(self.drawing_gd_ts.Item(i_index))

    def remove(self, i_index: int) -> None:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub Remove(long iIndex)
                |     Removes a drawing GDT from the drawing GDTs collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index of the drawing GDT to remove from the collection of
                |             drawing GDTs. As a numerics, this index is the rank of the drawing text in the
                |             collection. The index of the first drawing GDT in the collection is 1, and the
                |             index of the last drawing GDT is Count.
                |
                |     Example:
                |         The following example removes the third drawing GDT from the drawing
                |         GDT collection of the active view of the active document, supposed to be a
                |         drawing document.
                |
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.GDTs.Remove(3)

        :param int i_index:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.drawing_gd_ts.Remove(i_index)

    def __repr__(self):
        return f'DrawingGDTs(name="{self.name}")'
