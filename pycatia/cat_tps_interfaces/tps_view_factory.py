#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.tps_view import TPSView
from pycatia.types.general import cat_variant


class TPSViewFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSViewFactory
                | 
                | Represents the TPS view factory object.
                | All the created views are added to the annotation set object from which this
                | interface is retrieved, thanks to the AnnotationSet.TPSFactory
                | property.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_view_factory = com_object

    def create_view(self, i_plane: Reference, i_view_type: cat_variant) -> TPSView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateView(Reference iPlane,
                | CATVariant iViewType) As TPSView
                | 
                |     Creates a view.
                | 
                |     Parameters:
                | 
                |         iPlane
                |             The plane onto which the view will be created 
                |         iViewType
                |             The view type
                |             Legal values:
                | 
                |                 1: Front View
                |                 2: Section View
                |                 3: Cut View

        :param Reference i_plane:
        :param cat_variant i_view_type:
        :rtype: TPSView
        """
        return TPSView(self.tps_view_factory.CreateView(i_plane.com_object, i_view_type))

    def __repr__(self):
        return f'TpsViewFactory(name="{self.name}")'
