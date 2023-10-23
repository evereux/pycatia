#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_component import SchComponent
from pycatia.cat_sch_platform_interfaces.sch_grr import SchGRR
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_route import SchRoute
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class SchAppComponent(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppComponent
                | 
                | Represents an application component object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_component = com_object

    def app_create_component_inst(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppCreateComponentInst() As AnyObject
                | 
                |     Create a component instance.
                | 
                |     Parameters:
                | 
                |         oNewAppCompInst
                |             Interface pointer (CATISchAppComponent) to the new application
                |             component instance placed. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim objArg1 As AnyObject
                |           ...
                |          Set objArg1 = objThisIntf.AppCreateComponentInst

        :rtype: AnyObject
        """
        return AnyObject(self.sch_app_component.AppCreateComponentInst())

    def app_create_local_reference(self, i_doc_to_copy_to: Document) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppCreateLocalReference(Document iDocToCopyTo) As
                | AnyObject
                | 
                |     Create Local Reference object. Given a reference object (the "this"), This
                |     method make a copy of the reference into another document.
                | 
                |     Parameters:
                | 
                |         iDocToCopyTo
                |             Pointer to a document to copy the reference to, 
                |         oNewAppCompRef
                |             Interface pointer (CATISchAppComponent) to the new application
                |             component Reference copied. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim objArg1 As Document
                |          Dim objArg2 As AnyObject
                |           ...
                |          Set objArg2 = objThisIntf.AppCreateLocalReference(objArg1)

        :param Document i_doc_to_copy_to:
        :rtype: AnyObject
        """
        return AnyObject(self.sch_app_component.AppCreateLocalReference(i_doc_to_copy_to.com_object))

    def app_get_default_grr_name(self, o_grr_default_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppGetDefaultGRRName(CATBSTR oGRRDefaultName)
                | 
                |     Get the default graphical representation names of an application
                |     component.
                | 
                |     Parameters:
                | 
                |         oGRRDefaultName
                |             The default name to be used for the graphical representation of a
                |             component 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.AppGetDefaultGRRNamestrVar1

        :param str o_grr_default_name:
        :rtype: None
        """
        return self.sch_app_component.AppGetDefaultGRRName(o_grr_default_name)

    def app_list_grr_names(self) -> SchListOfBSTRs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListGRRNames() As SchListOfBSTRs
                | 
                |     Find all the valid graphical representation names of an application
                |     component.
                | 
                |     Parameters:
                | 
                |         oLGRRNames
                |             A list of all the valid graphical representation names with this
                |             connector for connections. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim objArg1 As SchListOfBSTRs
                |           ...
                |          Set objArg1 = objThisIntf.AppListGRRNames

        :rtype: SchListOfBSTRs
        """
        return SchListOfBSTRs(self.sch_app_component.AppListGRRNames())

    def app_ok_to_flip_connected(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToFlipConnected(boolean oBYes)
                | 
                |     Query whether it is OK to reconnect a component to a different compatible
                |     configuration.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to flip the component. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToFlipConnectedbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToFlipConnected(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_flip_connected'
        # # vba_code = """
        # # Public Function app_ok_to_flip_connected(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToFlipConnected oBYes
        # #     app_ok_to_flip_connected = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_flip_horizontal(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToFlipHorizontal(boolean oBYes)
                | 
                |     Query whether it is OK to flip the application component about
                |     Y.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to flip the component. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToFlipHorizontalbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToFlipHorizontal(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_flip_horizontal'
        # # vba_code = """
        # # Public Function app_ok_to_flip_horizontal(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToFlipHorizontal oBYes
        # #     app_ok_to_flip_horizontal = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_flip_on_line(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToFlipOnLine(boolean oBYes)
                | 
                |     Query whether it is OK to flip a component about its inserted
                |     line.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to flip the component. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToFlipOnLinebVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToFlipOnLine(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_flip_on_line'
        # # vba_code = """
        # # Public Function app_ok_to_flip_on_line(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToFlipOnLine oBYes
        # #     app_ok_to_flip_on_line = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_flip_vertical(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToFlipVertical(boolean oBYes)
                | 
                |     Query whether it is OK to flip the application component about
                |     X.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to flip the component. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToFlipVerticalbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToFlipVertical(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_flip_vertical'
        # # vba_code = """
        # # Public Function app_ok_to_flip_vertical(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToFlipVertical oBYes
        # #     app_ok_to_flip_vertical = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_place_in_space(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToPlaceInSpace(boolean oBYes)
                | 
                |     Query whether the application component can be placed in free
                |     space.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, the component can be slided. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToPlaceInSpacebVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToPlaceInSpace(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_place_in_space'
        # # vba_code = """
        # # Public Function app_ok_to_place_in_space(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToPlaceInSpace oBYes
        # #     app_ok_to_place_in_space = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_scale(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToScale(boolean oBYes)
                | 
                |     Query whether it is OK to scale the application component.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to scale the component. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToScalebVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToScale(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_scale'
        # # vba_code = """
        # # Public Function app_ok_to_scale(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToScale oBYes
        # #     app_ok_to_scale = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_slide(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToSlide(boolean oBYes)
                | 
                |     Query whether the application component can be slided.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, the component can be slided. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToSlidebVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToSlide(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_slide'
        # # vba_code = """
        # # Public Function app_ok_to_slide(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToSlide oBYes
        # #     app_ok_to_slide = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_ok_to_uninsert(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToUninsert(boolean oBYes)
                | 
                |     Query whether it is OK to uninsert the application
                |     component.
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then it is OK to uninsert the component. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.AppOKToUninsertbVar1

        :param bool o_b_yes:
        :rtype: None
        """
        return self.sch_app_component.AppOKToUninsert(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_uninsert'
        # # vba_code = """
        # # Public Function app_ok_to_uninsert(sch_app_component)
        # #     Dim oBYes (2)
        # #     sch_app_component.AppOKToUninsert oBYes
        # #     app_ok_to_uninsert = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_post_flip_connected_process(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostFlipConnectedProcess()
                | 
                |     Post process after reconnecting a component to a different compatible
                |     configuration.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |           ...
                |          objThisIntf.AppPostFlipConnectedProcess

        :rtype: None
        """
        return self.sch_app_component.AppPostFlipConnectedProcess()

    def app_post_flip_horizontal_process(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostFlipHorizontalProcess()
                | 
                |     Post process after flipping a component in "x".
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |           ...
                |          objThisIntf.AppPostFlipHorizontalProcess

        :rtype: None
        """
        return self.sch_app_component.AppPostFlipHorizontalProcess()

    def app_post_flip_on_line_process(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostFlipOnLineProcess()
                | 
                |     Post process after flipping an inserted component about the inserted line
                |     segment of the route.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |           ...
                |          objThisIntf.AppPostFlipOnLineProcess

        :rtype: None
        """
        return self.sch_app_component.AppPostFlipOnLineProcess()

    def app_post_flip_vertical_process(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostFlipVerticalProcess()
                | 
                |     Post process after flipping a component in "y".
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |           ...
                |          objThisIntf.AppPostFlipVerticalProcess

        :rtype: None
        """
        return self.sch_app_component.AppPostFlipVerticalProcess()

    def app_post_place_process(
            self,
            i_new_comp_inst: SchComponent,
            i_cntbl_connected_to: SchAppConnectable
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostPlaceProcess(SchComponent iNewCompInst,
                | SchAppConnectable iCntblConnectedTo)
                | 
                |     Post process after placing an application component
                |     instance.
                | 
                |     Parameters:
                | 
                |         iNewCompInst
                |             The newly placed component instance (CATISchComponent interface
                |             pointer). 
                |         iCntbleConnectedTo
                |             The connectable that the placed component is connected to or placed
                |             onto 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim objArg1 As SchComponent
                |          Dim objArg2 As SchAppConnectable
                |           ...
                |          objThisIntf.AppPostPlaceProcessobjArg1,objArg2

        :param SchComponent i_new_comp_inst:
        :param SchAppConnectable i_cntbl_connected_to:
        :rtype: None
        """
        return self.sch_app_component.AppPostPlaceProcess(i_new_comp_inst.com_object, i_cntbl_connected_to.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_post_place_process'
        # # vba_code = """
        # # Public Function app_post_place_process(sch_app_component)
        # #     Dim iNewCompInst (2)
        # #     sch_app_component.AppPostPlaceProcess iNewCompInst
        # #     app_post_place_process = iNewCompInst
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_post_slide_process(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostSlideProcess()
                | 
                |     Post process after sliding a component.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |           ...
                |          objThisIntf.AppPostSlideProcess

        :rtype: None
        """
        return self.sch_app_component.AppPostSlideProcess()

    def app_post_switch_graphic_process(self, i_grr: SchGRR) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostSwitchGraphicProcess(SchGRR iGRR)
                | 
                |     Post process after switching a component's graphic
                |     representation.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim objArg1 As SchGRR
                |           ...
                |          objThisIntf.AppPostSwitchGraphicProcessobjArg1

        :param SchGRR i_grr:
        :rtype: None
        """
        return self.sch_app_component.AppPostSwitchGraphicProcess(i_grr.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_post_switch_graphic_process'
        # # vba_code = """
        # # Public Function app_post_switch_graphic_process(sch_app_component)
        # #     Dim iGRR (2)
        # #     sch_app_component.AppPostSwitchGraphicProcess iGRR
        # #     app_post_switch_graphic_process = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_post_uninsert_process(
            self,
            i_old_app_route1: SchRoute,
            i_old_app_route2: SchRoute,
            i_new_app_route: SchRoute
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostUninsertProcess(SchRoute iOldAppRoute1,
                | SchRoute iOldAppRoute2,
                | SchRoute iNewAppRoute)
                | 
                |     Post process after uninserting a component, disconnecting it from a
                |     route.
                | 
                |     Parameters:
                | 
                |         iOldAppRoute1
                |             One of the route that was connected to one connector of the
                |             inserted component before the operation. 
                |         iOldAppRoute2
                |             The other route that was connected to the other connector of the
                |             inserted component before the operation. This would be NULL if the component
                |             was connected at extremity. 
                |         iNewAppRoute
                |             The new route created after the operation. This would be NULL if
                |             the component was connected at extremity. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppComponent
                |          Dim objArg1 As SchRoute
                |          Dim objArg2 As SchRoute
                |          Dim objArg3 As SchRoute
                |           ...
                |          objThisIntf.AppPostUninsertProcessobjArg1,objArg2,objArg3

        :param SchRoute i_old_app_route1:
        :param SchRoute i_old_app_route2:
        :param SchRoute i_new_app_route:
        :rtype: None
        """
        return self.sch_app_component.AppPostUninsertProcess(
            i_old_app_route1.com_object,
            i_old_app_route2.com_object,
            i_new_app_route.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_post_uninsert_process'
        # # vba_code = """
        # # Public Function app_post_uninsert_process(sch_app_component)
        # #     Dim iOldAppRoute1 (2)
        # #     sch_app_component.AppPostUninsertProcess iOldAppRoute1
        # #     app_post_uninsert_process = iOldAppRoute1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppComponent(name="{self.name}")'
