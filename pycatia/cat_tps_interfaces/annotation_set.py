#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect
from typing import TYPE_CHECKING

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.annotation_factory import AnnotationFactory
from pycatia.cat_tps_interfaces.annotation_factory_2 import AnnotationFactory2
from pycatia.cat_tps_interfaces.capture_factory import CaptureFactory
from pycatia.cat_tps_interfaces.captures import Captures
from pycatia.cat_tps_interfaces.tps_view import TPSView
from pycatia.cat_tps_interfaces.tps_view_factory import TPSViewFactory
from pycatia.cat_tps_interfaces.annotations import Annotations
from pycatia.cat_tps_interfaces.tps_views import TPSViews

if TYPE_CHECKING:
    from pycatia.mec_mod_interfaces.part import Part


class AnnotationSet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnnotationSet
                | 
                | Interface for the TPS Set of objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_set = com_object

    @property
    def active_view(self) -> TPSView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveView() As TPSView
                | 
                |     Gets or Sets Annotation Set ActiveView.
                | 
                |     Parameters:
                | 
                |         oView
                |             Value of CATIATPSView.

        :rtype: TPSView
        """

        return TPSView(self.annotation_set.ActiveView)

    @active_view.setter
    def active_view(self, value: TPSView):
        """
        :param TPSView value:
        """

        self.annotation_set.ActiveView = value

    @property
    def an_empty_annotations_list(self) -> Annotations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnEmptyAnnotationsList() As Annotations (Read
                | Only)
                | 
                |     Retrieves an empty Annotations'Collection.
                | 
                |     Parameters:
                | 
                |         oAnnots
                |             Empty Annotations' Collection.

        :rtype: Annotations
        """

        return Annotations(self.annotation_set.AnEmptyAnnotationsList)

    @property
    def annotation_factory(self) -> AnnotationFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotationFactory() As AnnotationFactory (Read
                | Only)
                | 
                |     Obtain the factory to create annotations.
                | 
                |     Parameters:
                | 
                |         oAFact
                |             Annotations' factory.

        :rtype: AnnotationFactory
        """
        import pycatia.cat_tps_interfaces.annotation_factory
        return pycatia.cat_tps_interfaces.annotation_factory.AnnotationFactory(self.annotation_set.AnnotationFactory)

    @property
    def annotation_factory_2(self) -> AnnotationFactory2:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotationFactory2() As AnnotationFactory2 (Read
                | Only)
                | 
                |     Obtain the factory to create annotations.
                | 
                |     Parameters:
                | 
                |         oAFact
                |             Annotations' factory.

        :rtype: AnnotationFactory2
        """
        return AnnotationFactory2(self.annotation_set.AnnotationFactory2)

    @property
    def annotation_set_purpose(self) -> str:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AnnotationSetPupose() As CATBSTR (Read Only)
                |     Gets the annotation Set specifications purpose.
                |     Any existing set is implicitly an Engineering Annotation
                |     Set.
                |
                |     Parameters:
                |
                |         oAnnotationSetSpecification
                |             Value indicating purpose of the Annotation Set.
                |             List of legal values:
                |             oAnnotationSetSpecification = "FTA_EngineeringSet",
                |             oAnnotationSetSpecification = "FTA_ManufacturingSet".

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.annotation_set.AnnotationSetPupose

    @property
    def annotation_set_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotationSetType() As CatAnnotationSetType (Read
                | Only)
                | 
                |     Get the annotation Set type.
                | 
                |     Parameters:
                | 
                |         oAnnotationSetType
                |             Value of Set Type.

        :return: enum cat_annotation_set_type
        :rtype: int
        """

        return self.annotation_set.AnnotationSetType

    @property
    def annotations(self) -> Annotations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Annotations() As Annotations (Read Only)
                | 
                |     Retrieves the TPS components of the set.
                | 
                |     Parameters:
                | 
                |         oAnnots
                |             Collection of returned component.

        :rtype: Annotations
        """

        return Annotations(self.annotation_set.Annotations)

    @property
    def capture_factory(self) -> CaptureFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CaptureFactory() As CaptureFactory (Read Only)
                | 
                |     Obtain the factory to create Capture.
                | 
                |     Parameters:
                | 
                |         opiCapFact
                |             Capture factory.

        :rtype: CaptureFactory
        """

        return CaptureFactory(self.annotation_set.CaptureFactory)

    @property
    def captures(self) -> Captures:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Captures() As Captures (Read Only)
                | 
                |     Retrieves all the Captures that belong to the set.
                | 
                |     Parameters:
                | 
                |         oCaptures
                |             Collection of returned Captures.

        :rtype: Captures
        """
        return Captures(self.annotation_set.Captures)

    @property
    def kind_of_set(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property KindOfSet() As CATBSTR (Read Only)
                | 
                |     Give the kind of set (Part, Product...).
                | 
                |     Parameters:
                | 
                |         oKindOfSet
                |             It could be : Part Product Product_TP Process_BB Cgr Cgr_TP.

        :rtype: str
        """

        return self.annotation_set.KindOfSet

    @property
    def standard(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Standard() As CATBSTR (Read Only)
                | 
                |     Retrieves the Parent Standard defined at set creation.
                | 
                |     Parameters:
                | 
                |         oStandard
                |             Name of the Parent Standard applied for all TPS in the set. The
                |             Parent Standard is the international standard on which Standard File is based
                |             on. It can only be ISO, ANSI and JIS. (ANSI stands for
                |             ASME).

        :rtype: str
        """

        return self.annotation_set.Standard

    @property
    def switch_on(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SwitchOn() As boolean
                | 
                |     Gets or Sets Annotation Set Visualization.
                | 
                |     Parameters:
                | 
                |         oDisplay
                |             Value of visualisation mode.

        :rtype: bool
        """

        return self.annotation_set.SwitchOn

    @switch_on.setter
    def switch_on(self, value: bool):
        """
        :param bool value:
        """

        self.annotation_set.SwitchOn = value

    @property
    def tps_view_factory(self) -> TPSViewFactory:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TPSViewFactory() As TPSViewFactory (Read Only)
                | 
                |     Obtain the factory to create TPS Views.
                | 
                |     Parameters:
                | 
                |         oTPSViewFact
                |             TPS Views' factory.

        :rtype: TPSViewFactory
        """
        return TPSViewFactory(self.annotation_set.TPSViewFactory)

    @property
    def tps_views(self) -> TPSViews:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TPSViews() As TPSViews (Read Only)
                | 
                |     Retrieves all the TPSViews that belong to the set.
                | 
                |     Parameters:
                | 
                |         oViews
                |             Collection of returned views.

        :rtype: TPSViews
        """

        return TPSViews(self.annotation_set.TPSViews)

    def apply_result_with_link_when_copy_set_to(self) -> None:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub ApplyResultWithLinkWhenCopySetTo()
                |     Register for next call to either GlobalCopySetTo and like
                |     methods.
                |
                |     See also:
                |         CATIAAnnotationSet#GlobalCopySetTo or CATIAAnnotationSet, this option
                |         is reset at the end of import. When activated, the annotations are copied as
                |         result with link annotations.
                |     Example:
                |
                |          This example illustrates activation of the 'as result with link'
                |          option for the next import (GlobalCopySetTo) run.
                |
                |          Dim myPart As Part
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim mySelection As Selection
                |          Set mySelection = CATIA.ActiveEditor.Selection
                |          Dim SelectionFilter(0)
                |          SelectionFilter(0)="AnnotationSet"
                |          Dim Status As String
                |          Status = mySelection.SelectElement2(SelectionFilter, "Select an Annotation Set to copy: ", False)
                |          Dim SelectedEntity As SelectedElement
                |          Set SelectedEntity = mySelection.Item( 1 )
                |          Dim SetToReplicate As AnnotationSet
                |          Set SetToReplicate = SelectedEntity.Value
                |          SetToReplicate.ApplyResultWithLinkWhenCopySetTo
                |          SetToReplicate.GlobalCopySetTo(myPart)

        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.annotation_set.ApplyResultWithLinkWhenCopySetTo()

    def apply_view_re_use_when_copy_set_to(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyViewReUseWhenCopySetTo()
                | 
                |     Register for next call to either GlobalCopySetTo and like
                |     methods.
                | 
                |     See also:
                |         CATIAAnnotationSet#GlobalCopySetTo or CATIAAnnotationSet, they are
                |         placed in existing Views. This call sets an option valid for the next import
                |         run only; in other words, this option is reset at the end of import. When
                |         activated, this option will not break the import processing; if no View in
                |         target set can receive a candidate FTA entity resulting from the import,
                |         regular handling is carried on

        :rtype: None
        """
        return self.annotation_set.ApplyViewReUseWhenCopySetTo()

    def global_copy_set_to(self, i_destination_part: 'Part') -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GlobalCopySetTo(Part iDestinationPart) As CATBSTR
                | 
                |     Copies the entire or a subpart of a part level Annotation Set into a
                |     destination CATPart
                | 
                |     Parameters:
                | 
                |         iDestinationPart
                |             destination CATPart. 
                |         oMessage
                |             result of datums merge.

        :param Part i_destination_part:
        :rtype: str
        """
        from pycatia.mec_mod_interfaces.part import Part
        return self.annotation_set.GlobalCopySetTo(i_destination_part.com_object)

    def global_copy_set_to_with_transformation(self, i_destination_part: 'Part', i_transfo: tuple) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GlobalCopySetToWithTransformation(Part
                | iDestinationPart,
                | CATSafeArrayVariant iTransfo) As CATBSTR
                | 
                |     Copies the entire Annotation Set into a destination
                |     CATPart
                | 
                |     Parameters:
                | 
                |         iDestinationPart
                |             destination CATPart. 
                |         iTransfo
                |             Optional argument. Transformation matrix to apply to FTA features
                |             during copy. The transformation is also used for retrieving in the destination
                |             CATPart the geometrical elements the FTA features are rerouted on.
                |             Transformation matrix is composed by a matrix3x3 and a translation vector:
                |             [[a11 a12 a13 a21 a22 a23 a31 a32 a33] [u1 u2 u3]] a11 is in iTransfo(0) a12 is
                |             in iTransfo(1) a13 is in iTransfo(2) a21 is in iTransfo(3) a22 is in
                |             iTransfo(4) a23 is in iTransfo(5) a31 is in iTransfo(6) a32 is in iTransfo(7)
                |             a33 is in iTransfo(8) u1 is in iTransfo(9) u2 is in iTransfo(10) u3 is in
                |             iTransfo(11) 
                |         oMessage
                |             result of datums merge.

        :param Part i_destination_part:
        :param tuple i_transfo:
        :rtype: str
        """
        return self.annotation_set.GlobalCopySetToWithTransformation(i_destination_part.com_object, i_transfo)

    def read_iso_default_properties(self, o_iso_defaults: tuple) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func ReadISODefaultProperties(CATSafeArrayVariant oISODefaults) As
                | long
                |     Retrieves the ISO 14405 and ISO 1101 default specifications. This method is
                |     not relevant in case of ASME Standard.
                |
                |     Parameters:
                |
                |         oISODefaults
                |             Array of ISO default defined onto the annotation set. Composition
                |             of the array may looks like the following schema
                |             [ Linear size ISO 14405 property
                |             Angular size ISO 14405 property
                |             Default specification elements for form association
                |             property
                |             Default specification elements for toleranced feature filtering
                |             property ]
                |             When oCount is not null, minimal size of oISODefaults "vector" of
                |             string is 3 (the 3 first strings are always existing); depending on GDT
                |             toleranced feature filtering options activated on the annotation set, oCount
                |             may reach the limit of 7 (4 more texts).
                |         oCount
                |             Number of lines in returned array of strings. When this procedure
                |             is not applicable (either due to wrong Standard, old annotation set), oCount
                |             equals 0.

        :param tuple o_iso_defaults:
        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.annotation_set.ReadISODefaultProperties(o_iso_defaults)

    def __repr__(self):
        return f'AnnotationSet(name="{self.name}")'
