#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.move import Move
from pycatia.in_interfaces.position import Position
from pycatia.system_interfaces.any_object import AnyObject


class SceneProductData(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SceneProductData
                | 
                | The interface to access a CATIASceneProduct
                | 
                | Using this prefered syntax will enable mkdoc to document your
                | class.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.scene_product_data = com_object

    @property
    def activation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Activation() As boolean
                | 
                |     Returns / Set the scene product's activation state.
                | 
                |     Example:
                | 
                |              This example retrieves the activation state of the scenePrd
                |              SceneProductData.
                |
                |             IsActivated = scenePrd.Hidden

        :rtype: bool
        """

        return self.scene_product_data.Activation

    @activation.setter
    def activation(self, value: bool):
        """
        :param bool value:
        """

        self.scene_product_data.Activation = value

    @property
    def hidden(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Hidden() As boolean
                | 
                |     Returns / Set the scene product's hide/show mode.
                | 
                |     Example:
                | 
                |              This example retrieves the hide/show mode of the scenePrd
                |              SceneProductData.
                |
                |             IsHidden = scenePrd.Hidden

        :rtype: bool
        """

        return self.scene_product_data.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        """
        :param bool value:
        """

        self.scene_product_data.Hidden = value

    @property
    def move(self) -> Move:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Move() As Move (Read Only)
                | 
                |     Returns the scene product's move object. It aggregates a movable object to
                |     which you can apply a move transformation by means of an isometry matrix. It
                |     moves your product shape representation according to this
                |     isometry.
                | 
                |     Example:
                | 
                |              This example retrieves the EngineMove move
                |             in the scenePrd SceneProductData.
                |
                |             Dim EngineMove As Move
                |             Set EngineMove = scenePrd.GetMove

        :rtype: Move
        """

        return Move(self.scene_product_data.Move)

    @property
    def position(self) -> Position:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Position() As Position (Read Only)
                | 
                |     Returns the scene product's position object. The position object is the
                |     object aggregated by the SceneProductData object that holds the position of the
                |     master shape representation in the space in scene.
                | 
                |     Example:
                | 
                |              This example retrieves the EnginePosition
                |              position
                |             in the scenePrd SceneProductData.
                |
                |             Dim EnginePosition As Position
                |             Set EnginePosition = scenePrd.GetPosition

        :rtype: Position
        """

        return Position(self.scene_product_data.Position)

    def get_real_colour(self, o_red: int, o_green: int, o_blue: int, o_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetRealColor(long oRed,
                | long oGreen,
                | long oBlue,
                | long oInheritance)
                | 
                |     Returns / Set the scene product's color and inheritance.
                | 
                |     Parameters:
                | 
                |         iRed
                |             A value between 0 and 255 
                |         iGreen
                |             A value between 0 and 255 
                |         iBlue
                |             A value between 0 and 255 
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |              This example retrieves the activation state of the scenePrd
                |              SceneProductData.
                |
                |         Dim r, g, b, inh
                |             scenePrd.GetRealColor r, g, b, inh

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :param int o_inheritance:
        :rtype: None
        """
        return self.scene_product_data.GetRealColor(o_red, o_green, o_blue, o_inheritance)

    def get_real_transparency(self, o_transparency: int, o_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetRealTransparency(long oTransparency,
                | long oInheritance)
                | 
                |     Returns the scene product's Transparency and inheritance.
                | 
                |     Parameters:
                | 
                |         oTransparency
                |             A value between 0 and 255 
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |              This example retrieves the transparency of the scenePrd
                |              SceneProductData.
                |
                |         Dim  trans, inh
                |             scenePrd.GetRealTransparency trans, inh

        :param int o_transparency:
        :param int o_inheritance:
        :rtype: None
        """
        return self.scene_product_data.GetRealTransparency(o_transparency, o_inheritance)

    def set_real_colour(self, i_red: int, i_green: int, i_blue: int, i_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRealColor(long iRed,
                | long iGreen,
                | long iBlue,
                | long iInheritance)
                | 
                |     Returns / Set the scene product's color and inheritance.
                | 
                |     Parameters:
                | 
                |         iRed
                |             A value between 0 and 255 
                |         iGreen
                |             A value between 0 and 255 
                |         iBlue
                |             A value between 0 and 255 
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |              This example retrieves the activation state of the scenePrd
                |              SceneProductData.
                |
                |             scenePrd.SetRealColor 255,0,0,1

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :param int i_inheritance:
        :rtype: None
        """
        return self.scene_product_data.SetRealColor(i_red, i_green, i_blue, i_inheritance)

    def set_real_transparency(self, i_transparency: int, i_inheritance: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRealTransparency(long iTransparency,
                | long iInheritance)
                | 
                |     Set the scene product's Transparency and inheritance.
                | 
                |     Parameters:
                | 
                |         iTransparency
                |             A value between 0 and 255 
                |         iInheritance
                |             Legal value:
                | 
                |             0
                |                 No heritance 
                |             1
                |                 Heritance 
                | 
                |     Example:
                | 
                |              This example applies the transparency of the scenePrd
                |              SceneProductData.
                |
                |             scenePrd.SetRealTransparency 10, 1

        :param int i_transparency:
        :param int i_inheritance:
        :rtype: None
        """
        return self.scene_product_data.SetRealTransparency(i_transparency, i_inheritance)

    def __repr__(self):
        return f'SceneProductData(name="{self.name}")'
