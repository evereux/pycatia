#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.workbench import Workbench
from pycatia.navigator_interfaces.annotated_view import AnnotatedView
from pycatia.navigator_interfaces.annotated_views import AnnotatedViews
from pycatia.navigator_interfaces.dmu_data_flow import DMUDataFlow
from pycatia.navigator_interfaces.groups import Groups
from pycatia.navigator_interfaces.hyperlinks import Hyperlinks
from pycatia.navigator_interfaces.marker_3Ds import Marker3Ds
from pycatia.system_interfaces.any_object import AnyObject


class NavigatorWorkbench(Workbench):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Workbench
                |                         NavigatorWorkbench
                | 
                | The object to manage all DMU Navigator entities.
                | 
                | This version allows to manage groups and annotated views.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.navigator_workbench = com_object

    @property
    def annotated_views(self) -> AnnotatedViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AnnotatedViews() As AnnotatedViews (Read Only)
                | 
                |     Returns the AnnotatedViews collection.
                | 
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("AnnotatedViews") on the
                |     root product, to retrieve the AnnotatedViews collection.
                | 
                |     Example:
                | 
                |              This example retrieves the AnnotatedViews collection of the active
                |              document.
                |             
                | 
                |             Dim TheNavigatorWorkbench As Workbench
                |             Set TheNavigatorWorkbench = CATIA.ActiveDocument.GetWorkbench ( "NavigatorWorkbench" )
                |             Dim TheAnnotatedViewsList As AnnotatedViews
                |             Set TheAnnotatedViewsList = TheNavigatorWorkbench.AnnotatedViews

        :rtype: AnnotatedViews
        """

        return AnnotatedViews(self.navigator_workbench.AnnotatedViews)

    @property
    def dmu_data_flow(self) -> DMUDataFlow:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUDataFlow() As DMUDataFlow (Read Only)
                | 
                |     Returns the DMU DataFlow object.

        :rtype: DMUDataFlow
        """

        return DMUDataFlow(self.navigator_workbench.DMUDataFlow)

    @property
    def groups(self) -> Groups:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Groups() As Groups (Read Only)
                | 
                |     Returns the Groups collection.
                | 
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Groups") on the root
                |     product, to retrieve the Groups collection.
                | 
                |     Example:
                | 
                |              This example retrieves the Groups collection of the active
                |              document.
                |             
                | 
                |             Dim TheNavigatorWorkbench As Workbench
                |             Set TheNavigatorWorkbench = CATIA.ActiveDocument.GetWorkbench ( "NavigatorWorkbench" )
                |             Dim TheGroupsList As Groups
                |             Set TheGroupsList = TheNavigatorWorkbench.Groups

        :rtype: Groups
        """

        return Groups(self.navigator_workbench.Groups)

    @property
    def hyperlinks(self) -> Hyperlinks:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Hyperlinks() As Hyperlinks (Read Only)
                | 
                |     Returns the Hyperlinks collection.
                | 
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Hyperlinks") on the root
                |     product, to retrieve the Hyperlinks collection.
                | 
                |     Example:
                | 
                |              This example retrieves the Hyperlinks collection of the active
                |              document.
                |             
                | 
                |             Dim TheNavigatorWorkbench As Workbench
                |             Set TheNavigatorWorkbench = CATIA.ActiveDocument.GetWorkbench ( "NavigatorWorkbench" )
                |             Dim HyperlinksList As Hyperlinks
                |             Set HyperlinksList = TheNavigatorWorkbench.Hyperlinks

        :rtype: Hyperlinks
        """

        return Hyperlinks(self.navigator_workbench.Hyperlinks)

    @property
    def marker3_ds(self) -> Marker3Ds:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker3Ds() As Marker3Ds (Read Only)
                | 
                |     Returns the Marker3Ds collection.
                | 
                |     WARNING: this method will be DEPRECATED in the next release. It is
                |     recommended to use the method GetTechnologicalObject("Marker3Ds") on the root
                |     product, to retrieve the Marker3Ds collection.
                | 
                |     Example:
                | 
                |              This example retrieves the Marker3Ds collection of the active
                |              document.
                |             
                | 
                |             Dim TheNavigatorWorkbench As Workbench
                |             Set TheNavigatorWorkbench = CATIA.ActiveDocument.GetWorkbench ( "NavigatorWorkbench" )
                |             Dim TheMarker3DsList As AnnotatedViews
                |             Set TheMarker3DsList = TheNavigatorWorkbench.Marker3Ds

        :rtype: Marker3Ds
        """

        return Marker3Ds(self.navigator_workbench.Marker3Ds)

    def advanced_view(self, i_annotated_view: AnnotatedView, i_view_option: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AdvancedView(AnnotatedView iAnnotatedView,
                | short iViewOption)
                | 
                |     Applies the annotated view to the current viewer.
                | 
                |     Parameters:
                | 
                |         iAnnotatedView
                |             The annotated view to apply. 
                |         iViewOptions
                |             The option to launch the annotated view command, possible values
                |             are
                | 
                |                 CatAnnotatedViewCmdOption_NoToolbar : No Toolbar for annotation creation
                |                 CatAnnotatedViewCmdOption_NoAnimation : No Animation when applying the view 
                | 
                |     Example:
                | 
                |              This example applies the view of the NewAnnotatedView
                |              AnnotatedView.
                |             
                |              TheNavigatorWorkbench.View,
                |              CatAnnotatedViewCmdOption_NoAnimation+CatAnnotatedViewCmdOption_NoToolbar(
                |              NewAnnotatedView)


        :param AnnotatedView i_annotated_view:
        :param int i_view_option:
        :rtype: None
        """
        return self.navigator_workbench.AdvancedView(i_annotated_view.com_object, i_view_option)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'advanced_view'
        # # vba_code = """
        # # Public Function advanced_view(navigator_workbench)
        # #     Dim iAnnotatedView (2)
        # #     navigator_workbench.AdvancedView iAnnotatedView
        # #     advanced_view = iAnnotatedView
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_order(self, i_object: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOrder(CATBaseDispatch iObject) As long
                | 
                |     Returns the order of an object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object whose rank has to be returned. 
                |         oCurrentRank
                |             The current rank of the object (from 1 to n the number of objects
                |             in the collection). 
                | 
                |     Example:
                | 
                |              This example creates an annotated view NewAnnotatedView and
                |              returns its position.
                |             
                | 
                |             Dim TheNavigatorWorkbench As Workbench
                |             Set TheNavigatorWorkbench = CATIA.ActiveDocument.GetWorkbench ( "NavigatorWorkbench" )
                |             
                |             Dim NewAnnotatedView As AnnotatedView
                |             Set NewAnnotatedView = TheAnnotatedViews.Add
                |             
                |             Dim iOrder As Integer
                |             iOrder = TheNavigatorWorkbench.GetOrder(NewAnnotatedView)

        :param AnyObject i_object:
        :rtype: int
        """
        return self.navigator_workbench.GetOrder(i_object.com_object)

    def set_order(self, i_object: AnyObject, i_new_rank: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOrder(CATBaseDispatch iObject,
                | long iNewRank)
                | 
                |     Sets the order of an object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object whose rank has to be modified. 
                |         iNewRank
                |             The new rank of the object (from 1 to n the number of objects in
                |             the collection). 
                | 
                |     Example:
                | 
                |              This example creates an annotated view NewAnnotatedView and move
                |              it to the first position.
                |             
                | 
                |             Dim TheNavigatorWorkbench As Workbench
                |             Set TheNavigatorWorkbench = CATIA.ActiveDocument.GetWorkbench ( "NavigatorWorkbench" )
                |             
                |             Dim NewAnnotatedView As AnnotatedView
                |             Set NewAnnotatedView = TheAnnotatedViews.Add
                |             TheNavigatorWorkbench.SetOrder NewAnnotatedView, 1

        :param AnyObject i_object:
        :param int i_new_rank:
        :rtype: None
        """
        return self.navigator_workbench.SetOrder(i_object.com_object, i_new_rank)

    def view(self, i_annotated_view: AnnotatedView) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub View(AnnotatedView iAnnotatedView)
                | 
                |     Applies the annotated view to the current viewer.
                | 
                |     Parameters:
                | 
                |         iAnnotatedView
                |             The annotated view to apply. 
                | 
                |     Example:
                | 
                |              This example applies the view of the NewAnnotatedView
                |              AnnotatedView.
                |             
                | 
                |             TheNavigatorWorkbench.View(NewAnnotatedView)

        :param AnnotatedView i_annotated_view:
        :rtype: None
        """
        return self.navigator_workbench.View(i_annotated_view.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'view'
        # # vba_code = """
        # # Public Function view(navigator_workbench)
        # #     Dim iAnnotatedView (2)
        # #     navigator_workbench.View iAnnotatedView
        # #     view = iAnnotatedView
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'NavigatorWorkbench(name="{self.name}")'
