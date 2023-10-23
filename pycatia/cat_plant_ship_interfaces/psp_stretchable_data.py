#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_plant_ship_interfaces.psp_list_of_doubles import PSPListOfDoubles
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class PSPStretchableData(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PspStretchableData
                | 
                | Represents the PspStretchableData object.
                | Role: To access the technological data on stretchable objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.psp_stretchable_data = com_object

    def list_bend_data(self) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListBendData() As PspListOfDoubles
                | 
                |     Returns the bend radii.
                | 
                |     Returns:
                |         List of bend radius.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspStretchableData  
                |          Dim objArg1 As PspListOfDoubles
                |           ...
                |          Set objArg1 = objThisIntf.ListBendData

        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_stretchable_data.ListBendData())

    def list_definition_points(self, i_rel_axis: Product) -> PSPListOfDoubles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListDefinitionPoints(Product iRelAxis) As
                | PspListOfDoubles
                | 
                |     Returns the points defining the object.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             The relative axis object (Nothing means relative to parent).
                |             
                | 
                |     Returns:
                |         List of points defining object. A list of X-Y-Z coordinates of the
                |         points. 3 doubles per point.
                |
                |     Example:
                |
                |          Dim objThisIntf As PspStretchableData
                |          Dim objArg1 As Product
                |          Dim objArg2 As PspListOfDoubles
                |           ...
                |          Set objArg2 = objThisIntf.ListDefinitionPoints (objArg1)

        :param Product i_rel_axis:
        :rtype: PSPListOfDoubles
        """
        return PSPListOfDoubles(self.psp_stretchable_data.ListDefinitionPoints(i_rel_axis.com_object))

    def __repr__(self):
        return f'PSPStretchableData(name="{self.name}")'
