#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.drafting_2dL_interfaces.layout_2d_root import Layout2DRoot
from pycatia.system_interfaces.any_object import AnyObject


class Layout2DFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.layout_2d_factory = com_object

    def create_2d_layout(self, i_standard_name: str) -> Layout2DRoot:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Create2DLayout(CATBSTR iStandardName) As Layout2DRoot
                | 
                |     Create the 2DLayout associated to the 3D mechanical feature tha implement
                |     this interface. E.g. a Mechanical Part.
                | 
                |     Parameters:
                | 
                |         CATBSTR
                |             iStandardName The standard name to apply to the new layout.
                |             
                |         oLayout
                |             The created 2DLayout. This feature is unique for a given 3D context
                |             feature. Consequently requesting this interface on a 3D feature that is already
                |             associated to a 2DLayout feature will fail. You must first request for any
                |             existing 2DLayout via 
                | 
                |         AnyObject.GetItem method using CATLayoutRoot key parameter to check for
                |         2DLayout pre-existing feature as follow :
                | 
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = CATIA.ActiveDocument.Part.GetItem("CATLayoutRoot")
                |          if MyRoot Is Nothing then
                |            Dim MyRootFact As Layout2DFactory
                |            Set MyRootFact = CATIA.ActiveDocument.Part.GetItem("CATLayoutRootFactory")
                |            Set MyRoot = MyRootFact.Create2DLayout("ISO_3D")
                |          end if

        :param str i_standard_name:
        :rtype: Layout2DRoot
        """
        return Layout2DRoot(self.layout_2d_factory.Create2DLayout(i_standard_name))

    def __repr__(self):
        return f'Layout2DFactory(name="{self.name}")'
