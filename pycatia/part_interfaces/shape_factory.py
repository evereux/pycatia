#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.hybrid_shape_interfaces.hybrid_shape_symmetry import HybridShapeSymmetry
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.factory import Factory
from pycatia.part_interfaces.add import Add
from pycatia.part_interfaces.assemble import Assemble
from pycatia.part_interfaces.auto_draft import AutoDraft
from pycatia.part_interfaces.auto_fillet import AutoFillet
from pycatia.part_interfaces.chamfer import Chamfer
from pycatia.part_interfaces.circ_pattern import CircPattern
from pycatia.part_interfaces.close_surface import CloseSurface
from pycatia.part_interfaces.const_rad_edge_fillet import ConstRadEdgeFillet
from pycatia.part_interfaces.defeaturing import Defeaturing
from pycatia.part_interfaces.draft import Draft
from pycatia.part_interfaces.face_fillet import FaceFillet
from pycatia.part_interfaces.groove import Groove
from pycatia.part_interfaces.hole import Hole
from pycatia.part_interfaces.intersect import Intersect
from pycatia.part_interfaces.mirror import Mirror
from pycatia.part_interfaces.pad import Pad
from pycatia.part_interfaces.pocket import Pocket
from pycatia.part_interfaces.rect_pattern import RectPattern
from pycatia.part_interfaces.remove import Remove
from pycatia.part_interfaces.remove_face import RemoveFace
from pycatia.part_interfaces.replace_face import ReplaceFace
from pycatia.part_interfaces.rib import Rib
from pycatia.part_interfaces.scaling import Scaling
from pycatia.part_interfaces.sew_surface import SewSurface
from pycatia.part_interfaces.shaft import Shaft
from pycatia.part_interfaces.shell import Shell
from pycatia.part_interfaces.slot import Slot
from pycatia.part_interfaces.solid_combine import SolidCombine
from pycatia.part_interfaces.split import Split
from pycatia.part_interfaces.stiffener import Stiffener
from pycatia.part_interfaces.thick_surface import ThickSurface
from pycatia.part_interfaces.thickness import Thickness
from pycatia.part_interfaces.thread import Thread
from pycatia.part_interfaces.translate import Translate
from pycatia.part_interfaces.trim import Trim
from pycatia.part_interfaces.tritangent_fillet import TritangentFillet
from pycatia.part_interfaces.user_pattern import UserPattern
from pycatia.part_interfaces.var_rad_edge_fillet import VarRadEdgeFillet
from pycatia.sketcher_interfaces.sketch import Sketch
from pycatia.system_interfaces.any_object import AnyObject


class ShapeFactory(Factory):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Factory
                |                         ShapeFactory
                | 
                | Represents the factory for shapes to create all kinds of shapes that may be
                | needed for part design.
                | 
                | The ShapeFactory mission is to build from scratch shapes that will be used
                | within the design process of parts. Those shapes have a strong mechanical
                | built-in knowledge, such as chamfer or hole, and in most cases apply
                | contextually to the part being designed. When created, they become part of the
                | definition of whichever body or shape that is current at that time. After they
                | are created, they become in turn the current body or shape. In most cases,
                | shapes are created from a factory with a minimum number of parameters. Other
                | shapes parameters may be set further on by using methods offered by the shape
                | itself.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape_factory = com_object

    def add_new_add(self, i_body_to_add: Body) -> Add:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAdd(Body iBodyToAdd) As Add
                | 
                |     Creates and returns a new add operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iBodyToAdd
                |             The body to add to the current body 
                | 
                |     Returns:
                |         The created add operation

        :param Body i_body_to_add:
        :rtype: Add
        """
        return Add(self.shape_factory.AddNewAdd(i_body_to_add.com_object))

    def add_new_affinity2(self, x_ratio: float, y_ratio: float, z_ratio: float) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAffinity2(double XRatio,
                | double YRatio,
                | double ZRatio) As AnyObject
                | 
                |     Creates and returns a Affinity feature.
                | 
                |     Parameters:
                | 
                |         XRatio
                |             Value for the XRatio. 
                |         YRatio
                |             Value for the YRatio. 
                |         ZRatio
                |             Value for the ZRatio. 
                | 
                |     Returns:
                |         the created Affinity feature.

        :param float x_ratio:
        :param float y_ratio:
        :param float z_ratio:
        :rtype: AnyObject
        """
        return AnyObject(self.shape_factory.AddNewAffinity2(x_ratio, y_ratio, z_ratio))

    def add_new_assemble(self, i_body_to_assemble: Body) -> Assemble:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAssemble(Body iBodyToAssemble) As Assemble
                | 
                |     Creates and returns a new assembly operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iBodyToAssemble
                |             The body to assemble with the current body 
                | 
                |     Returns:
                |         The created assembly operation

        :param Body i_body_to_assemble:
        :rtype: Assemble
        """
        return Assemble(self.shape_factory.AddNewAssemble(i_body_to_assemble.com_object))

    def add_new_auto_draft(self, i_draft_angle: float) -> AutoDraft:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAutoDraft(double iDraftAngle) As AutoDraft
                | 
                |     Creates and returns a new solid autodraft.
                |     Use this method to create autodraft by providing draft
                |     angle.
                | 
                |     Parameters:
                | 
                |         iDraftAngle
                |             The draft angle. 
                | 
                |     Returns:
                |         The created autodraft.

        :param float i_draft_angle:
        :rtype: AutoDraft
        """
        return AutoDraft(self.shape_factory.AddNewAutoDraft(i_draft_angle))

    def add_new_auto_fillet(self, i_fillet_radius: float, i_round_radius: float) -> AutoFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAutoFillet(double iFilletRadius,
                | double iRoundRadius) As AutoFillet
                | 
                |     Creates and returns a new solid autofillet.
                |     Use this method to create autofillet by providing fillet and round radius
                |     values.
                | 
                |     Parameters:
                | 
                |         iFilletRadius
                |             The fillet radius 
                |         iRoundRadius
                |             The round radius 
                | 
                |     Returns:
                |         The created autofillet

        :param float i_fillet_radius:
        :param float i_round_radius:
        :rtype: AutoFillet
        """
        return AutoFillet(self.shape_factory.AddNewAutoFillet(i_fillet_radius, i_round_radius))

    def add_new_axis_to_axis2(self, i_reference: Reference, i_target: Reference) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewAxisToAxis2(Reference iReference,
                | Reference iTarget) As AnyObject
                | 
                |     Creates and returns an AxisToAxis transformation feature.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference axis. 
                |         iTarget
                |             The target axis. 
                | 
                |     Returns:
                |         The created AxisToAxis transformation feature.

        :param Reference i_reference:
        :param Reference i_target:
        :rtype: AnyObject
        """
        return AnyObject(self.shape_factory.AddNewAxisToAxis2(i_reference.com_object, i_target.com_object))

    def add_new_blend(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewBlend() As AnyObject
                | 
                |     Creates and returns a new Blend feature.
                | 
                |     Returns:
                |         The created Blend feature

        :rtype: AnyObject
        """
        return AnyObject(self.shape_factory.AddNewBlend())

    def add_new_chamfer(
            self,
            i_object_to_chamfer: Reference,
            i_propagation: int,
            i_mode: int,
            i_orientation: int,
            i_length1: float,
            i_length2_or_angle: float
    ) -> Chamfer:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewChamfer(Reference iObjectToChamfer,
                | CatChamferPropagation iPropagation,
                | CatChamferMode iMode,
                | CatChamferOrientation iOrientation,
                | double iLength1,
                | double iLength2OrAngle) As Chamfer
                | 
                |     Creates and returns a new chamfer within the current body.
                | 
                |     Parameters:
                | 
                |         iObjectToChamfer
                |             The first edge or face to chamfer
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iPropagation
                |         Controls if and how the chamfering operation should propagate beyond
                |         the first chamfer element iObjectToChamfer, when it is an edge
                |         
                |     iMode
                |         Controls if the chamfer is defined by two lengthes, or by an angle and
                |         a length
                |         The value of this argument changes the way the arguments iLength1 and
                |         iLength2OrAngle should be interpreted. 
                |     iOrientation
                |         Defines the relative meaning of arguments iLength1 and iLength2OrAngle
                |         when defining a chamfer by two lengthes 
                |     iLength1
                |         The first value for chamfer dimensioning. It represents the chamfer
                |         first length if the chamfer is defined by two lengthes, or the chamfer length
                |         if the chamfer is defined by a length and an angle. 
                |     iLength2OrAngle
                |         The second value for chamfer dimensioning. It represents the chamfer
                |         second length if the chamfer is defined by two lengthes, or the chamfer angle
                |         if the chamfer is defined by a length and an angle. 
                |     Returns:
                |         The created chamfer

        :param Reference i_object_to_chamfer:
        :param int i_propagation: enum cat_chamfer_propagation
        :param int i_mode:
        :param int i_orientation:
        :param float i_length1:
        :param float i_length2_or_angle:
        :rtype: Chamfer
        """
        return Chamfer(
            self.shape_factory.AddNewChamfer(
                i_object_to_chamfer.com_object,
                i_propagation,
                i_mode,
                i_orientation,
                i_length1,
                i_length2_or_angle
            )
        )

    def add_new_circ_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                             i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                             i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                             i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                             i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool, i_rotation_angle: float,
                             i_is_radius_aligned: bool) -> CircPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircPattern(AnyObject iShapeToCopy,
                | long iNbOfCopiesInRadialDir,
                | long iNbOfCopiesInAngularDir,
                | double iStepInRadialDir,
                | double iStepInAngularDir,
                | long iShapeToCopyPositionAlongRadialDir,
                | long iShapeToCopyPositionAlongAngularDir,
                | Reference iRotationCenter,
                | Reference iRotationAxis,
                | boolean iIsReversedRotationAxis,
                | double iRotationAngle,
                | boolean iIsRadiusAligned) As CircPattern
                | 
                |     Creates and returns a new circular pattern within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the circular pattern 
                |         iNbOfInstancesInRadialDir
                |             The number of times iShapeToCopy will be copied along pattern
                |             radial direction 
                |         iNbOfInstancesInAngularDir
                |             The number of times iShapeToCopy will be copied along pattern
                |             angular direction 
                |         iStepInRadialDir
                |             The distance that will separate two consecutive copies in the
                |             pattern along its radial direction 
                |         iStepInAngularDir
                |             The angle that will separate two consecutive copies in the pattern
                |             along its angular direction 
                |         iShapeToCopyPositionAlongRadialDir
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along the radial direction 
                |         iShapeToCopyPositionAlongAngularDir
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along the angular direction 
                |         iRotationCenter
                |             The point or vertex that specifies the pattern center of rotation
                |             
                |         iRotationAxis
                |             The line or linear edge that specifies the axis around which
                |             instances will be rotated relative to each other
                |             The following 
                | 
                |         Boundary objects are supported: PlanarFace , CylindricalFace ,
                |         RectilinearTriDimFeatEdge and RectilinearBiDimFeatEdge.
                |         
                |     iIsReversedRotationAxis
                |         The boolean flag indicating wether the natural orientation of
                |         iRotationAxis should be used to orient the pattern operation. A value of true
                |         indicates that iItemToDuplicate are copied in the direction of the natural
                |         orientation of iRotationAxis. 
                |     iRotationAngle
                |         The angle applied to the direction iRotationAxis prior to applying the
                |         pattern. The original shape iShapeToCopy is used as the rotation center.
                |         Nevertheless, the copied shapes themselves are not rotated. This allows the
                |         definition of a circular pattern relatively to existing geometry, but not
                |         necessarily parallel to it. 
                |     iIsRadiusAligned
                |         The boolean flag that specifies whether the instances of
                |         iItemToDuplicate copied by the pattern should be kept parallel to each other
                |         (True) or if they should be aligned with the radial direction they lie upon
                |         (False). 
                |     Returns:
                |         The created circular pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_radial_dir:
        :param int i_nb_of_copies_in_angular_dir:
        :param float i_step_in_radial_dir:
        :param float i_step_in_angular_dir:
        :param int i_shape_to_copy_position_along_radial_dir:
        :param int i_shape_to_copy_position_along_angular_dir:
        :param Reference i_rotation_center:
        :param Reference i_rotation_axis:
        :param bool i_is_reversed_rotation_axis:
        :param float i_rotation_angle:
        :param bool i_is_radius_aligned:
        :rtype: CircPattern
        """
        return CircPattern(
            self.shape_factory.AddNewCircPattern(i_shape_to_copy.com_object, i_nb_of_copies_in_radial_dir,
                                                 i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                 i_step_in_angular_dir, i_shape_to_copy_position_along_radial_dir,
                                                 i_shape_to_copy_position_along_angular_dir,
                                                 i_rotation_center.com_object, i_rotation_axis.com_object,
                                                 i_is_reversed_rotation_axis, i_rotation_angle, i_is_radius_aligned))

    def add_new_circ_patternof_list(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                                    i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                                    i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                                    i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                                    i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool,
                                    i_rotation_angle: float, i_is_radius_aligned: bool) -> CircPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCircPatternofList(AnyObject iShapeToCopy,
                | long iNbOfCopiesInRadialDir,
                | long iNbOfCopiesInAngularDir,
                | double iStepInRadialDir,
                | double iStepInAngularDir,
                | long iShapeToCopyPositionAlongRadialDir,
                | long iShapeToCopyPositionAlongAngularDir,
                | Reference iRotationCenter,
                | Reference iRotationAxis,
                | boolean iIsReversedRotationAxis,
                | double iRotationAngle,
                | boolean iIsRadiusAligned) As CircPattern
                | 
                |     V5R8 Only: Creates and returns a new circular pattern within the current
                |     body using a list of shapes.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the circular pattern. Others shapes will
                |             be add by put_ItemToCopy with CATIAPattern interface
                |             
                |         iNbOfInstancesInRadialDir
                |             The number of times iShapeToCopy will be copied along pattern
                |             radial direction 
                |         iNbOfInstancesInAngularDir
                |             The number of times iShapeToCopy will be copied along pattern
                |             angular direction 
                |         iStepInRadialDir
                |             The distance that will separate two consecutive copies in the
                |             pattern along its radial direction 
                |         iStepInAngularDir
                |             The angle that will separate two consecutive copies in the pattern
                |             along its angular direction 
                |         iShapeToCopyPositionAlongRadialDir
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along the radial direction 
                |         iShapeToCopyPositionAlongAngularDir
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along the angular direction 
                |         iRotationCenter
                |             The point or vertex that specifies the pattern center of rotation
                |             
                |         iRotationAxis
                |             The line or linear edge that specifies the axis around which
                |             instances will be rotated relative to each other 
                |         iIsReversedRotationAxis
                |             The boolean flag indicating wether the natural orientation of
                |             iRotationAxis should be used to orient the pattern operation. A value of true
                |             indicates that iItemToDuplicate are copied in the direction of the natural
                |             orientation of iRotationAxis. 
                |         iRotationAngle
                |             The angle applied to the direction iRotationAxis prior to applying
                |             the pattern. The original shape iShapeToCopy is used as the rotation center.
                |             Nevertheless, the copied shapes themselves are not rotated. This allows the
                |             definition of a circular pattern relatively to existing geometry, but not
                |             necessarily parallel to it. 
                |         iIsRadiusAligned
                |             The boolean flag that specifies whether the instances of
                |             iItemToDuplicate copied by the pattern should be kept parallel to each other
                |             (True) or if they should be aligned with the radial direction they lie upon
                |             (False). 
                | 
                |     Returns:
                |         The created circular pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_radial_dir:
        :param int i_nb_of_copies_in_angular_dir:
        :param float i_step_in_radial_dir:
        :param float i_step_in_angular_dir:
        :param int i_shape_to_copy_position_along_radial_dir:
        :param int i_shape_to_copy_position_along_angular_dir:
        :param Reference i_rotation_center:
        :param Reference i_rotation_axis:
        :param bool i_is_reversed_rotation_axis:
        :param float i_rotation_angle:
        :param bool i_is_radius_aligned:
        :rtype: CircPattern
        """
        return CircPattern(
            self.shape_factory.AddNewCircPatternofList(i_shape_to_copy.com_object, i_nb_of_copies_in_radial_dir,
                                                       i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                       i_step_in_angular_dir, i_shape_to_copy_position_along_radial_dir,
                                                       i_shape_to_copy_position_along_angular_dir,
                                                       i_rotation_center.com_object, i_rotation_axis.com_object,
                                                       i_is_reversed_rotation_axis, i_rotation_angle,
                                                       i_is_radius_aligned))

    def add_new_close_surface(self, i_close_element: Reference) -> CloseSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewCloseSurface(Reference iCloseElement) As
                | CloseSurface
                | 
                |     Creates and returns a new CloseSurface feature.
                | 
                |     Parameters:
                | 
                |         iCloseElement
                |             The skin that will be closed and add with the current body
                |             
                | 
                |     Returns:
                |         The created CloseSurface feature

        :param Reference i_close_element:
        :rtype: CloseSurface
        """
        return CloseSurface(self.shape_factory.AddNewCloseSurface(i_close_element.com_object))

    def add_new_defeaturing(self) -> Defeaturing:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewDefeaturing() As Defeaturing
                | 
                |     Creates and returns a new defeaturing operation within the current
                |     container.
                | 
                |     Returns:
                |         The created defeaturing operation

        :rtype: Defeaturing
        """
        return Defeaturing(self.shape_factory.AddNewDefeaturing())

    def add_new_draft(
            self,
            i_face_to_draft: Reference,
            i_neutral: Reference,
            i_neutral_mode: int,
            i_parting: Reference,
            i_dir_x: float,
            i_dir_y: float,
            i_dir_z: float,
            i_mode: int,
            i_angle: float,
            i_multiselection_mode: int
    ) -> Draft:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewDraft(Reference iFaceToDraft,
                | Reference iNeutral,
                | CatDraftNeutralPropagationMode iNeutralMode,
                | Reference iParting,
                | double iDirX,
                | double iDirY,
                | double iDirZ,
                | CatDraftMode iMode,
                | double iAngle,
                | CatDraftMultiselectionMode iMultiselectionMode) As Draft
                | 
                |     Creates and returns a new draft within the current body.
                |     The draft needs a reference face on the body. This face will remain
                |     unchanged in the draft operation, while faces adjacent to it and specified for
                |     drafting will be rotated by the draft angle.
                | 
                |     Parameters:
                | 
                |         iFaceToDraft
                |             The first face to draft in the body. This face should be adjacent
                |             to the iFaceToDraft face. If several faces are to be drafted, only the first
                |             one is specified here, the others being inferred by propagating the draft
                |             operation onto faces adjacent to this first face. This is controlled by the
                |             iNeutralMode argument.
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iNeutral
                |         The reference face for the draft. The draft needs a reference face on
                |         the body, that will remain unchanged in the draft operation, while faces
                |         adjacent to it and specified for drafting will be rotated according to the
                |         draft angle iAngle.
                |         The following Boundary object is supported:
                |         PlanarFace.
                |     iNeutralMode
                |         Controls if and how the drafting operation should be propagated beyond
                |         the first face to draft iFaceToDraft to other adjacent faces.
                |         
                |     iParting
                |         The draft parting plane, face or surface. It specifies the element
                |         within the body to draft that represents the bottom of the mold. This element
                |         can be located either somewhere in the middle of the body or be one of its
                |         boundary faces. When located in the middle of the body, it crosses the faces to
                |         draft, and as a result, those faces are drafted with a positive angle on one
                |         side of the parting surface, and with a negative angle on the other
                |         side.
                |         The following Boundary object is supported:
                |         PlanarFace.
                |     iDirX,iDirY,iDirZ
                |         The X, Y, and Z components of the absolute vector representing the
                |         drafting direction (i.e. the mold extraction direction).
                |         
                |     iMode
                |         The draft connecting mode to its reference face iFaceToDraft
                |         
                |     iAngle
                |         The draft angle 
                |     iMultiselectionMode.
                |         The elements to be drafted can be selected explicitly or can implicitly
                |         selected as neighbors of the neutral face 
                |     Returns:
                |         The created draft

        :param Reference i_face_to_draft:
        :param Reference i_neutral:
        :param int i_neutral_mode: enum cat_draft_neutral_propagation_mode
        :param Reference i_parting:
        :param float i_dir_x:
        :param float i_dir_y:
        :param float i_dir_z:
        :param int i_mode: enum cat_draft_mode
        :param float i_angle:
        :param int i_multiselection_mode: enum cat_draft_multiselection_mode
        :rtype: Draft
        """
        return Draft(
            self.shape_factory.AddNewDraft(
                i_face_to_draft.com_object,
                i_neutral.com_object,
                i_neutral_mode,
                i_parting.com_object,
                i_dir_x,
                i_dir_y,
                i_dir_z,
                i_mode,
                i_angle,
                i_multiselection_mode
            )
        )

    def add_new_edge_fillet_with_constant_radius(self, i_edge_to_fillet: Reference, i_propag_mode: int,
                                                 i_radius: float) -> ConstRadEdgeFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewEdgeFilletWithConstantRadius(Reference
                | iEdgeToFillet,
                | CatFilletEdgePropagation iPropagMode,
                | double iRadius) As ConstRadEdgeFillet
                | 
                |     Deprecated:
                |         V5R14 #AddNewEdgeFilletWithConstantRadius use
                |         AddNewSolidEdgeFilletWithConstantRadius or
                |         AddNewSurfaceEdgeFilletWithConstantRadius depending on the type of fillet you
                |         want to create

        :param Reference i_edge_to_fillet:
        :param int i_propag_mode: enum cat_fillet_edge_propagation
        :param float i_radius:
        :rtype: ConstRadEdgeFillet
        """
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewEdgeFilletWithConstantRadius(i_edge_to_fillet.com_object, i_propag_mode, i_radius))

    def add_new_edge_fillet_with_varying_radius(self, i_edge_to_fillet: Reference, i_propag_mode: int,
                                                i_variation_mode: int, i_default_radius: float) -> VarRadEdgeFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewEdgeFilletWithVaryingRadius(Reference
                | iEdgeToFillet,
                | CatFilletEdgePropagation iPropagMode,
                | CatFilletVariation iVariationMode,
                | double iDefaultRadius) As VarRadEdgeFillet
                | 
                |     Deprecated:
                |         V5R14 #AddNewEdgeFilletWithVaryingRadius use
                |         AddNewSolidEdgeFilletWithVaryingRadius or
                |         AddNewSurfaceEdgeFilletWithVaryingRadius depending on the type of fillet you
                |         want to create

        :param Reference i_edge_to_fillet:
        :param int i_propag_mode: enum cat_fillet_edge_propagation
        :param int i_variation_mode: enum cat_fillet_variation
        :param float i_default_radius:
        :rtype: VarRadEdgeFillet
        """
        return VarRadEdgeFillet(
            self.shape_factory.AddNewEdgeFilletWithVaryingRadius(i_edge_to_fillet.com_object, i_propag_mode,
                                                                 i_variation_mode, i_default_radius))

    def add_new_face_fillet(self, i_f1: Reference, i_f2: Reference, i_radius: float) -> FaceFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewFaceFillet(Reference iF1,
                | Reference iF2,
                | double iRadius) As FaceFillet
                | 
                |     Deprecated:
                |         V5R14 #AddNewFaceFillet use AddNewSolidFaceFillet or
                |         AddNewSurfaceFaceFillet depending on the type of fillet you want to create

        :param Reference i_f1:
        :param Reference i_f2:
        :param float i_radius:
        :rtype: FaceFillet
        """
        return FaceFillet(self.shape_factory.AddNewFaceFillet(i_f1.com_object, i_f2.com_object, i_radius))

    def add_new_gsd_circ_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                                 i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                                 i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                                 i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                                 i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool, i_rotation_angle: float,
                                 i_is_radius_aligned: bool, i_complete_crown: bool, i_type: float) -> CircPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewGSDCircPattern(AnyObject iShapeToCopy,
                | long iNbOfCopiesInRadialDir,
                | long iNbOfCopiesInAngularDir,
                | double iStepInRadialDir,
                | double iStepInAngularDir,
                | long iShapeToCopyPositionAlongRadialDir,
                | long iShapeToCopyPositionAlongAngularDir,
                | Reference iRotationCenter,
                | Reference iRotationAxis,
                | boolean iIsReversedRotationAxis,
                | double iRotationAngle,
                | boolean iIsRadiusAligned,
                | boolean iCompleteCrown,
                | double iType) As CircPattern
                | 
                |     Deprecated:
                |         V5R15 #AddNewSurfacicCircPattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_radial_dir:
        :param int i_nb_of_copies_in_angular_dir:
        :param float i_step_in_radial_dir:
        :param float i_step_in_angular_dir:
        :param int i_shape_to_copy_position_along_radial_dir:
        :param int i_shape_to_copy_position_along_angular_dir:
        :param Reference i_rotation_center:
        :param Reference i_rotation_axis:
        :param bool i_is_reversed_rotation_axis:
        :param float i_rotation_angle:
        :param bool i_is_radius_aligned:
        :param bool i_complete_crown:
        :param float i_type:
        :rtype: CircPattern
        """
        return CircPattern(
            self.shape_factory.AddNewGSDCircPattern(i_shape_to_copy.com_object, i_nb_of_copies_in_radial_dir,
                                                    i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                    i_step_in_angular_dir, i_shape_to_copy_position_along_radial_dir,
                                                    i_shape_to_copy_position_along_angular_dir,
                                                    i_rotation_center.com_object, i_rotation_axis.com_object,
                                                    i_is_reversed_rotation_axis, i_rotation_angle, i_is_radius_aligned,
                                                    i_complete_crown, i_type))

    def add_new_gsd_rect_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int,
                                 i_nb_of_copies_in_dir2: int, i_step_in_dir1: float, i_step_in_dir2: float,
                                 i_shape_to_copy_position_along_dir1: int, i_shape_to_copy_position_along_dir2: int,
                                 i_dir1: Reference, i_dir2: Reference, i_is_reversed_dir1: bool,
                                 i_is_reversed_dir2: bool, i_rotation_angle: float, i_type: float) -> RectPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewGSDRectPattern(AnyObject iShapeToCopy,
                | long iNbOfCopiesInDir1,
                | long iNbOfCopiesInDir2,
                | double iStepInDir1,
                | double iStepInDir2,
                | long iShapeToCopyPositionAlongDir1,
                | long iShapeToCopyPositionAlongDir2,
                | Reference iDir1,
                | Reference iDir2,
                | boolean iIsReversedDir1,
                | boolean iIsReversedDir2,
                | double iRotationAngle,
                | double iType) As RectPattern
                | 
                |     Deprecated:
                |         V5R15 #AddNewSurfacicRectPattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_dir1:
        :param int i_nb_of_copies_in_dir2:
        :param float i_step_in_dir1:
        :param float i_step_in_dir2:
        :param int i_shape_to_copy_position_along_dir1:
        :param int i_shape_to_copy_position_along_dir2:
        :param Reference i_dir1:
        :param Reference i_dir2:
        :param bool i_is_reversed_dir1:
        :param bool i_is_reversed_dir2:
        :param float i_rotation_angle:
        :param float i_type:
        :rtype: RectPattern
        """
        return RectPattern(self.shape_factory.AddNewGSDRectPattern(i_shape_to_copy.com_object, i_nb_of_copies_in_dir1,
                                                                   i_nb_of_copies_in_dir2, i_step_in_dir1,
                                                                   i_step_in_dir2, i_shape_to_copy_position_along_dir1,
                                                                   i_shape_to_copy_position_along_dir2,
                                                                   i_dir1.com_object, i_dir2.com_object,
                                                                   i_is_reversed_dir1, i_is_reversed_dir2,
                                                                   i_rotation_angle, i_type))

    def add_new_groove(self, i_sketch: Sketch) -> Groove:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewGroove(Sketch iSketch) As Groove
                | 
                |     Creates and returns a new groove within the current body.
                |     The Revolution, as a supertype for grooves, provides starting and ending
                |     angles for the groove definition.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the groove section. The sketch must contain a
                |             contour and an axis that will be used to rotate the contour in the space, thus
                |             defining the groove. The contour has to penetrate in 3D space the current
                |             shape. 
                | 
                |     Returns:
                |         The created groove

        :param Sketch i_sketch:
        :rtype: Groove
        """
        return Groove(self.shape_factory.AddNewGroove(i_sketch.com_object))

    def add_new_groove_from_ref(self, i_profile_elt: Reference) -> Groove:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewGrooveFromRef(Reference iProfileElt) As Groove
                | 
                |     Creates and returns a new groove within the current body.
                | 
                |     Parameters:
                | 
                |         iProfileElt
                |             The reference on the element defining the groove base
                |             
                | 
                |     Returns:
                |         The created groove

        :param Reference i_profile_elt:
        :rtype: Groove
        """
        return Groove(self.shape_factory.AddNewGrooveFromRef(i_profile_elt.com_object))

    def add_new_hole(self, i_support: Reference, i_depth: float) -> Hole:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHole(Reference iSupport,
                | double iDepth) As Hole
                | 
                |     Creates and returns a new hole within the current shape.
                |     Actual hole shape is defined by editing hole properties after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The support defining the hole reference plane.
                |             Anchor point is located at the barycenter of the support. The hole
                |             axis in 3D passes through that point and is normal to the
                |             plane.
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iDepth
                |         The hole depth. 
                |     Returns:
                |         The created hole

        :param Reference i_support:
        :param float i_depth:
        :rtype: Hole
        """
        return Hole(self.shape_factory.AddNewHole(i_support.com_object, i_depth))

    def add_new_hole_from_point(self, i_x: float, i_y: float, i_z: float, i_support: Reference, i_depth: float) -> Hole:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHoleFromPoint(double iX,
                | double iY,
                | double iZ,
                | Reference iSupport,
                | double iDepth) As Hole
                | 
                |     Creates and returns a new hole within the current shape.
                |     Actual hole shape is defined by editing hole properties after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iX
                |             Origin point x absolute coordinate 
                |         iY
                |             Origin point y absolute coordinate 
                |         iZ
                |             Origin point z absolute coordinate
                |             Sets the origin point which the hole is anchored
                |             to.
                |             If mandatory, the entry point will be projected onto a tangent
                |             plane. 
                |         iSupport
                |             The support defining the hole reference plane.
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iDepth
                |         The hole depth. 
                |     Returns:
                |         The created hole

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param Reference i_support:
        :param float i_depth:
        :rtype: Hole
        """
        return Hole(self.shape_factory.AddNewHoleFromPoint(i_x, i_y, i_z, i_support.com_object, i_depth))

    def add_new_hole_from_ref_point(self, i_origin: Reference, i_support: Reference, i_depth: float) -> Hole:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHoleFromRefPoint(Reference iOrigin,
                | Reference iSupport,
                | double iDepth) As Hole
                | 
                |     Creates and returns a new hole within the current shape.
                |     Actual hole shape is defined by editing hole properties after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The origin point which the hole is anchored to. 
                |         iSupport
                |             The support defining the hole reference plane.
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iDepth
                |         The hole depth. 
                |     Returns:
                |         The created hole

        :param Reference i_origin:
        :param Reference i_support:
        :param float i_depth:
        :rtype: Hole
        """
        return Hole(self.shape_factory.AddNewHoleFromRefPoint(i_origin.com_object, i_support.com_object, i_depth))

    def add_new_hole_from_sketch(self, i_sketch: Sketch, i_depth: float) -> Hole:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHoleFromSketch(Sketch iSketch,
                | double iDepth) As Hole
                | 
                |     Creates and returns a new hole within the current shape.
                |     Actual hole shape is defined by editing hole properties after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the hole reference plane and anchor
                |             point.
                |             This sketch must contain a single point that defines the hole axis:
                |             the hole axis in 3D passes through that point and is normal to the sketch
                |             plane. 
                |         iDepth
                |             The hole depth. 
                | 
                |     Returns:
                |         The created hole

        :param Sketch i_sketch:
        :param float i_depth:
        :rtype: Hole
        """
        return Hole(self.shape_factory.AddNewHoleFromSketch(i_sketch.com_object, i_depth))

    def add_new_hole_with2_constraints(self, i_x: float, i_y: float, i_z: float, i_edge1: Reference, i_edge2: Reference,
                                       i_support: Reference, i_depth: float) -> Hole:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHoleWith2Constraints(double iX,
                | double iY,
                | double iZ,
                | Reference iEdge1,
                | Reference iEdge2,
                | Reference iSupport,
                | double iDepth) As Hole
                | 
                |     Creates and returns a new hole within the current shape.
                |     Actual hole shape is defined by editing hole properties after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iX
                |             Origin point x absolute coordinate 
                |         iY
                |             Origin point y absolute coordinate 
                |         iZ
                |             Origin point z absolute coordinate
                |             Sets the origin point which the hole is anchored
                |             to.
                |             If mandatory, the entry point will be projected onto a tangent
                |             plane. 
                |         iEdge
                |             The edge which the hole is constrained to.
                |             The origin of the hole will have a length constraint with each
                |             edge.
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iSupport
                |         The support defining the hole reference plane.
                |         The following Boundary object is supported: Face.
                |     iDepth
                |         The hole depth. 
                |     Returns:
                |         The created hole

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param Reference i_edge1:
        :param Reference i_edge2:
        :param Reference i_support:
        :param float i_depth:
        :rtype: Hole
        """
        return Hole(self.shape_factory.AddNewHoleWith2Constraints(i_x, i_y, i_z, i_edge1.com_object, i_edge2.com_object,
                                                                  i_support.com_object, i_depth))

    def add_new_hole_with_constraint(self, i_x: float, i_y: float, i_z: float, i_edge: Reference, i_support: Reference,
                                     i_depth: float) -> Hole:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewHoleWithConstraint(double iX,
                | double iY,
                | double iZ,
                | Reference iEdge,
                | Reference iSupport,
                | double iDepth) As Hole
                | 
                |     Creates and returns a new hole within the current shape.
                |     Actual hole shape is defined by editing hole properties after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iX
                |             Origin point x absolute coordinate 
                |         iY
                |             Origin point y absolute coordinate 
                |         iZ
                |             Origin point z absolute coordinate
                |             Sets the origin point which the hole is anchored
                |             to.
                |             If mandatory, the entry point will be projected onto a tangent
                |             plane. 
                |         iEdge
                |             The edge which the hole is constrained to.
                |             If edge is circular, the origin of the hole will be concentric to
                |             the edge (iX, iY, iZ will be overridden). if not, the origin of the hole will
                |             have a length constraint with the edge.
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iSupport
                |         The support defining the hole reference plane.
                |         The following Boundary object is supported: Face.
                |     iDepth
                |         The hole depth. 
                |     Returns:
                |         The created hole

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param Reference i_edge:
        :param Reference i_support:
        :param float i_depth:
        :rtype: Hole
        """
        return Hole(self.shape_factory.AddNewHoleWithConstraint(i_x, i_y, i_z, i_edge.com_object, i_support.com_object,
                                                                i_depth))

    def add_new_intersect(self, i_body_to_intersect: Body) -> Intersect:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewIntersect(Body iBodyToIntersect) As Intersect
                | 
                |     Creates and returns a new intersect operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iBodyToIntersect
                |             The body to intersect with the current body 
                | 
                |     Returns:
                |         The created intersect operation

        :param Body i_body_to_intersect:
        :rtype: Intersect
        """
        return Intersect(self.shape_factory.AddNewIntersect(i_body_to_intersect.com_object))

    def add_new_loft(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewLoft() As AnyObject
                | 
                |     Creates and returns a new Loft feature.
                | 
                |     Returns:
                |         The created Loft feature

        :rtype: AnyObject
        """
        return AnyObject(self.shape_factory.AddNewLoft())

    def add_new_mirror(self, i_mirroring_element: Reference) -> Mirror:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewMirror(Reference iMirroringElement) As Mirror
                | 
                |     Creates and returns a new mirror within the current body.
                |     A mirror allows for transforming existing shapes by a symmetry with respect
                |     to an existing plane.
                | 
                |     Parameters:
                | 
                |         iMirroringElement
                |             The plane used by the mirror as the symmetry
                |             plane.
                |             The following 
                | 
                |         Boundary object is supported: PlanarFace. 
                |     Returns:
                |         The created mirror

        :param Reference i_mirroring_element:
        :rtype: Mirror
        """
        return Mirror(self.shape_factory.AddNewMirror(i_mirroring_element.com_object))

    def add_new_pad(self, i_sketch: Sketch, i_height: float) -> Pad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPad(Sketch iSketch,
                | double iHeight) As Pad
                | 
                |     Creates and returns a new pad within the current body.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the pad base 
                |         iHeight
                |             The pad height 
                | 
                |     Returns:
                |         The created pad

        :param Sketch i_sketch:
        :param float i_height:
        :rtype: Pad
        """
        return Pad(self.shape_factory.AddNewPad(i_sketch.com_object, i_height))

    def add_new_pad_from_ref(self, i_profile_elt: Reference, i_height: float) -> Pad:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPadFromRef(Reference iProfileElt,
                | double iHeight) As Pad
                | 
                |     Creates and returns a new pad within the current body.
                | 
                |     Parameters:
                | 
                |         iProfileElt
                |             The reference on the element defining the pad base
                |             
                |         iHeight
                |             The pad height 
                | 
                |     Returns:
                |         The created pad

        :param Reference i_profile_elt:
        :param float i_height:
        :rtype: Pad
        """
        return Pad(self.shape_factory.AddNewPadFromRef(i_profile_elt.com_object, i_height))

    def add_new_pocket(self, i_sketch: Sketch, i_height: float) -> Pocket:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPocket(Sketch iSketch,
                | double iHeight) As Pocket
                | 
                |     Creates and returns a new pocket within the current shape.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the pocket base 
                |         iDepth
                |             The pocket depth 
                | 
                |     Returns:
                |         The created pocket

        :param Sketch i_sketch:
        :param float i_height:
        :rtype: Pocket
        """
        return Pocket(self.shape_factory.AddNewPocket(i_sketch.com_object, i_height))

    def add_new_pocket_from_ref(self, i_profile_elt: Reference, i_height: float) -> Pocket:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewPocketFromRef(Reference iProfileElt,
                | double iHeight) As Pocket
                | 
                |     Creates and returns a new pocket within the current shape.
                | 
                |     Parameters:
                | 
                |         iProfileElt
                |             The reference on the element defining the pocket base
                |             
                |         iDepth
                |             The pocket depth 
                | 
                |     Returns:
                |         The created pocket

        :param Reference i_profile_elt:
        :param float i_height:
        :rtype: Pocket
        """
        return Pocket(self.shape_factory.AddNewPocketFromRef(i_profile_elt.com_object, i_height))

    def add_new_rect_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int, i_nb_of_copies_in_dir2: int,
                             i_step_in_dir1: float, i_step_in_dir2: float, i_shape_to_copy_position_along_dir1: int,
                             i_shape_to_copy_position_along_dir2: int, i_dir1: Reference, i_dir2: Reference,
                             i_is_reversed_dir1: bool, i_is_reversed_dir2: bool,
                             i_rotation_angle: float) -> RectPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRectPattern(AnyObject iShapeToCopy,
                | long iNbOfCopiesInDir1,
                | long iNbOfCopiesInDir2,
                | double iStepInDir1,
                | double iStepInDir2,
                | long iShapeToCopyPositionAlongDir1,
                | long iShapeToCopyPositionAlongDir2,
                | Reference iDir1,
                | Reference iDir2,
                | boolean iIsReversedDir1,
                | boolean iIsReversedDir2,
                | double iRotationAngle) As RectPattern
                | 
                |     Creates and returns a new rectangular pattern within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the rectangular pattern 
                |         iNbOfCopiesInDir1
                |             The number of times iShapeToCopy will be copied along the pattern
                |             first direction 
                |         iNbOfCopiesInDir2
                |             The number of times iShapeToCopy will be copied along the pattern
                |             second direction 
                |         iStepInDir1
                |             The distance that will separate two consecutive copies in the
                |             pattern along its first direction 
                |         iStepInDir2
                |             The distance that will separate two consecutive copies in the
                |             pattern along its second direction 
                |         iShapeToCopyPositionAlongDir1
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along iDir1 
                |         iShapeToCopyPositionAlongDir2
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along iDir2 
                |         iDir1
                |             The line or linear edge that specifies the pattern first
                |             repartition direction
                |             The following 
                | 
                |         Boundary objects are supported: PlanarFace, RectilinearTriDimFeatEdge,
                |         RectilinearBiDimFeatEdge. 
                |     iDir2
                |         The line or linear edge that specifies the pattern second repartition
                |         direction
                |         The following Boundary objects are supported: PlanarFace,
                |         RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge.
                |     iIsReversedDir1
                |         The boolean flag indicating whether the natural orientation of iDir1
                |         should be used to orient the pattern operation. True indicates that
                |         iShapeToCopy is copied in the direction of the natural orientation of iDir1.
                |         
                |     iIsReversedDir2
                |         The boolean flag indicating whether the natural orientation of iDir2
                |         should be used to orient the pattern operation. True indicates that
                |         iShapeToCopy is copied in the direction of the natural orientation of iDir2.
                |         
                |     iRotationAngle
                |         The angle applied to both directions iDir1 and iDir2 prior to applying
                |         the pattern. The original shape iShapeToCopy is used as the rotation center.
                |         Nevertheless, the copied shapes themselves are not rotated. This allows the
                |         definition of a rectangular pattern relatively to existing geometry, but not
                |         necessarily parallel to it. 
                |     Returns:
                |         The created rectangular pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_dir1:
        :param int i_nb_of_copies_in_dir2:
        :param float i_step_in_dir1:
        :param float i_step_in_dir2:
        :param int i_shape_to_copy_position_along_dir1:
        :param int i_shape_to_copy_position_along_dir2:
        :param Reference i_dir1:
        :param Reference i_dir2:
        :param bool i_is_reversed_dir1:
        :param bool i_is_reversed_dir2:
        :param float i_rotation_angle:
        :rtype: RectPattern
        """
        return RectPattern(self.shape_factory.AddNewRectPattern(i_shape_to_copy.com_object, i_nb_of_copies_in_dir1,
                                                                i_nb_of_copies_in_dir2, i_step_in_dir1, i_step_in_dir2,
                                                                i_shape_to_copy_position_along_dir1,
                                                                i_shape_to_copy_position_along_dir2, i_dir1.com_object,
                                                                i_dir2.com_object, i_is_reversed_dir1,
                                                                i_is_reversed_dir2, i_rotation_angle))

    def add_new_rect_patternof_list(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int,
                                    i_nb_of_copies_in_dir2: int, i_step_in_dir1: float, i_step_in_dir2: float,
                                    i_shape_to_copy_position_along_dir1: int, i_shape_to_copy_position_along_dir2: int,
                                    i_dir1: Reference, i_dir2: Reference, i_is_reversed_dir1: bool,
                                    i_is_reversed_dir2: bool, i_rotation_angle: float) -> RectPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRectPatternofList(AnyObject iShapeToCopy,
                | long iNbOfCopiesInDir1,
                | long iNbOfCopiesInDir2,
                | double iStepInDir1,
                | double iStepInDir2,
                | long iShapeToCopyPositionAlongDir1,
                | long iShapeToCopyPositionAlongDir2,
                | Reference iDir1,
                | Reference iDir2,
                | boolean iIsReversedDir1,
                | boolean iIsReversedDir2,
                | double iRotationAngle) As RectPattern
                | 
                |     V5R8 Only: Creates and returns a new rectangular pattern within the current
                |     body using a list of shapes.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the rectangular pattern Others shapes
                |             will be add by put_ItemToCopy with CATIAPattern interface
                |             
                |         iNbOfCopiesInDir1
                |             The number of times iShapeToCopy will be copied along the pattern
                |             first direction 
                |         iNbOfCopiesInDir2
                |             The number of times iShapeToCopy will be copied along the pattern
                |             second direction 
                |         iStepInDir1
                |             The distance that will separate two consecutive copies in the
                |             pattern along its first direction 
                |         iStepInDir2
                |             The distance that will separate two consecutive copies in the
                |             pattern along its second direction 
                |         iShapeToCopyPositionAlongDir1
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along iDir1 
                |         iShapeToCopyPositionAlongDir2
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along iDir2 
                |         iDir1
                |             The line or linear edge that specifies the pattern first
                |             repartition direction 
                |         iDir2
                |             The line or linear edge that specifies the pattern second
                |             repartition direction 
                |         iIsReversedDir1
                |             The boolean flag indicating whether the natural orientation of
                |             iDir1 should be used to orient the pattern operation. True indicates that
                |             iShapeToCopy is copied in the direction of the natural orientation of iDir1.
                |             
                |         iIsReversedDir2
                |             The boolean flag indicating whether the natural orientation of
                |             iDir2 should be used to orient the pattern operation. True indicates that
                |             iShapeToCopy is copied in the direction of the natural orientation of iDir2.
                |             
                |         iRotationAngle
                |             The angle applied to both directions iDir1 and iDir2 prior to
                |             applying the pattern. The original shape iShapeToCopy is used as the rotation
                |             center. Nevertheless, the copied shapes themselves are not rotated. This allows
                |             the definition of a rectangular pattern relatively to existing geometry, but
                |             not necessarily parallel to it. 
                | 
                |     Returns:
                |         The created rectangular pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_dir1:
        :param int i_nb_of_copies_in_dir2:
        :param float i_step_in_dir1:
        :param float i_step_in_dir2:
        :param int i_shape_to_copy_position_along_dir1:
        :param int i_shape_to_copy_position_along_dir2:
        :param Reference i_dir1:
        :param Reference i_dir2:
        :param bool i_is_reversed_dir1:
        :param bool i_is_reversed_dir2:
        :param float i_rotation_angle:
        :rtype: RectPattern
        """
        return RectPattern(
            self.shape_factory.AddNewRectPatternofList(i_shape_to_copy.com_object, i_nb_of_copies_in_dir1,
                                                       i_nb_of_copies_in_dir2, i_step_in_dir1, i_step_in_dir2,
                                                       i_shape_to_copy_position_along_dir1,
                                                       i_shape_to_copy_position_along_dir2, i_dir1.com_object,
                                                       i_dir2.com_object, i_is_reversed_dir1, i_is_reversed_dir2,
                                                       i_rotation_angle))

    def add_new_remove(self, i_body_to_remove: Body) -> Remove:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRemove(Body iBodyToRemove) As Remove
                | 
                |     Creates and returns a new remove operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iBodyToRemove
                |             The body to remove from the current body 
                | 
                |     Returns:
                |         The created remove operation

        :param Body i_body_to_remove:
        :rtype: Remove
        """
        return Remove(self.shape_factory.AddNewRemove(i_body_to_remove.com_object))

    def add_new_remove_face(self, i_keep_faces: Reference, i_remove_faces: Reference) -> RemoveFace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRemoveFace(Reference iKeepFaces,
                | Reference iRemoveFaces) As RemoveFace
                | 
                |     Creates and returns a new RemoveFace feature.
                | 
                |     Parameters:
                | 
                |         iKeepFaces
                |             The reference of the face to Keep. 
                |         iRemoveFaces
                |             The reference of the face to Remove. 
                | 
                |     Returns:
                |         The created RemoveFace feature.

        :param Reference i_keep_faces:
        :param Reference i_remove_faces:
        :rtype: RemoveFace
        """
        return RemoveFace(self.shape_factory.AddNewRemoveFace(i_keep_faces.com_object, i_remove_faces.com_object))

    def add_new_removed_blend(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRemovedBlend() As AnyObject
                | 
                |     Creates and returns a new Removed Blend feature.
                | 
                |     Returns:
                |         The created Removed Blend feature

        :rtype: AnyObject
        """
        return AnyObject(self.shape_factory.AddNewRemovedBlend())

    def add_new_removed_loft(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRemovedLoft() As AnyObject
                | 
                |     Creates and returns a new Removed Loft feature.
                | 
                |     Returns:
                |         The created Removed Loft feature

        :rtype: AnyObject
        """
        return AnyObject(self.shape_factory.AddNewRemovedLoft())

    def add_new_replace_face(self, i_split_plane: Reference, i_remove_face: Reference,
                             i_splitting_side: int) -> ReplaceFace:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewReplaceFace(Reference iSplitPlane,
                | Reference iRemoveFace,
                | CatSplitSide iSplittingSide) As ReplaceFace
                | 
                |     Creates and returns a new Align/ ReplaceFace feature.
                | 
                |     Parameters:
                | 
                |         iSplitPlane
                |             The reference of the element defining the Splitting Plane.
                |             
                |         iRemoveFace
                |             The reference of the Face to Remove. 
                |         iSplittingSide
                |             The specification for which side of the current body should be
                |             Align 
                | 
                |     Returns:
                |         The created Align/ ReplaceFace feature.

        :param Reference i_split_plane:
        :param Reference i_remove_face:
        :param int i_splitting_side: enum cat_split_side
        :rtype: ReplaceFace
        """
        return ReplaceFace(
            self.shape_factory.AddNewReplaceFace(i_split_plane.com_object, i_remove_face.com_object, i_splitting_side))

    def add_new_rib(self, i_sketch: Sketch, i_center_curve: Sketch) -> Rib:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRib(Sketch iSketch,
                | Sketch iCenterCurve) As Rib
                | 
                |     Creates and returns a new rib within the current body.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the rib section 
                |         iCenterCurve
                |             The sketched curve that defines the rib center curve. It must cross
                |             the section definition sketch iSketch within the inner part of its contour.
                |             
                | 
                |     Returns:
                |         The created rib

        :param Sketch i_sketch:
        :param Sketch i_center_curve:
        :rtype: Rib
        """
        return Rib(self.shape_factory.AddNewRib(i_sketch.com_object, i_center_curve.com_object))

    def add_new_rib_from_ref(self, i_profile: Reference, i_center_curve: Reference) -> Rib:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewRibFromRef(Reference iProfile,
                | Reference iCenterCurve) As Rib
                | 
                |     Creates and returns a new rib within the current body.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The Profile defining the rib section 
                |         iCenterCurve
                |             The curve that defines the rib center curve.
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     Returns:
                |         The created rib

        :param Reference i_profile:
        :param Reference i_center_curve:
        :rtype: Rib
        """
        return Rib(self.shape_factory.AddNewRibFromRef(i_profile.com_object, i_center_curve.com_object))

    def add_new_scaling(self, i_scaling_reference: Reference, i_factor: float) -> Scaling:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewScaling(Reference iScalingReference,
                | double iFactor) As Scaling
                | 
                |     Creates and returns a new scaling within the current body.
                | 
                |     Parameters:
                | 
                |         iScalingReference
                |             The point, plane or face of the current body that will remain fixed
                |             during the scaling process: even if the face itself shrinks or expands during
                |             the scaling, its supporting plane will remain unchanged after the
                |             scaling.
                |             The following 
                | 
                |         Boundary objects are supported: PlanarFace and Vertex.
                |         
                |     iFactor
                |         The scaling factor 
                |     Returns:
                |         The created scaling

        :param Reference i_scaling_reference:
        :param float i_factor:
        :rtype: Scaling
        """
        return Scaling(self.shape_factory.AddNewScaling(i_scaling_reference.com_object, i_factor))

    def add_new_rotate2(self, i_axis: Reference, i_angle: float) -> AnyObject:
        """
            .. note::
                :class: toggle

                Microsoft Visual Basic Object Browser
                    | Function AddNewRotate2(iAxis As Reference, iAngle As Double) As AnyObject
                    |   Member of PARTITF.ShapeFactory

        :param Reference i_axis:
        :param float i_angle:
        :rtype: AnyObject
        """

        return AnyObject(self.shape_factory.AddNewRotate2(i_axis.com_object, i_angle))

    def add_new_sew_surface(self, i_sewing_element: Reference, i_sewing_side: int) -> SewSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSewSurface(Reference iSewingElement,
                | CatSplitSide iSewingSide) As SewSurface
                | 
                |     Creates and returns a new sewing operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iSewingElement
                |             The face or skin or surface that will be sewn on the current body
                |             
                |         iSewingSide
                |             The specification for which side of the current body should be kept
                |             at the end of the sewing operation 
                | 
                |     Returns:
                |         The created sewing operation

        :param Reference i_sewing_element:
        :param int i_sewing_side: enum cat_split_side
        :rtype: SewSurface
        """
        return SewSurface(self.shape_factory.AddNewSewSurface(i_sewing_element.com_object, i_sewing_side))

    def add_new_shaft(self, i_sketch: Sketch) -> Shaft:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewShaft(Sketch iSketch) As Shaft
                | 
                |     Creates and returns a new shaft within the current body.
                |     The Revolution, as a supertype for shafts, provides starting and ending
                |     angles for the shaft definition.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the shaft section.
                | 
                |                 If the shaft applies to the current body, then the sketch must
                |                 contain a contour and an axis that will be used to rotate the contour in the
                |                 space, thus defining the shaft.
                |                 If the shaft is the first shape defined, there is not current
                |                 body to apply to. In such a case, the sketch must contain a curve whose end
                |                 points are linked by an axis. By rotating the curve in the space around the
                |                 axis, the shaft operation will define a revolution shape. This also works if
                |                 the sketch contains a closed contour and an axis outside of this contour: in
                |                 that case a revolution shape will be created, for example a torus.
                |                 
                | 
                |     Returns:
                |         The created shaft

        :param Sketch i_sketch:
        :rtype: Shaft
        """
        return Shaft(self.shape_factory.AddNewShaft(i_sketch.com_object))

    def add_new_shaft_from_ref(self, i_profile_elt: Reference) -> Shaft:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewShaftFromRef(Reference iProfileElt) As Shaft
                | 
                |     Creates and returns a new shaft within the current body.
                | 
                |     Parameters:
                | 
                |         iProfileElt
                |             The reference on the element defining the shaft base
                |             
                | 
                |     Returns:
                |         The created shaft

        :param Reference i_profile_elt:
        :rtype: Shaft
        """
        return Shaft(self.shape_factory.AddNewShaftFromRef(i_profile_elt.com_object))

    def add_new_shell(self, i_face_to_remove: Reference, i_internal_thickness: float,
                      i_external_thickness: float) -> Shell:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewShell(Reference iFaceToRemove,
                | double iInternalThickness,
                | double iExternalThickness) As Shell
                | 
                |     Creates and returns a new shell within the current body.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The first face to be removed in the shell process.
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iInternalThickness
                |         The thickness of material to be added on the internal side of all the
                |         faces during the shell process, except for those to be removed
                |         
                |     iExternaThickness
                |         The thickness of material to be added on the external side of all the
                |         faces during the shell process, except for those to be removed
                |         
                |     Returns:
                |         The created shell

        :param Reference i_face_to_remove:
        :param float i_internal_thickness:
        :param float i_external_thickness:
        :rtype: Shell
        """
        return Shell(
            self.shape_factory.AddNewShell(i_face_to_remove.com_object, i_internal_thickness, i_external_thickness))

    def add_new_slot(self, i_sketch: Sketch, i_center_curve: Sketch) -> Slot:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSlot(Sketch iSketch,
                | Sketch iCenterCurve) As Slot
                | 
                |     Creates and returns a new slot within the current shape.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the slot section 
                |         iCenterCurve
                |             The sketched curve that defines the slot center curve. It must
                |             cross the section definition sketch iSketch within the inner part of its
                |             contour. 
                | 
                |     Returns:
                |         The created slot

        :param Sketch i_sketch:
        :param Sketch i_center_curve:
        :rtype: Slot
        """
        return Slot(self.shape_factory.AddNewSlot(i_sketch.com_object, i_center_curve.com_object))

    def add_new_slot_from_ref(self, i_profile: Reference, i_center_curve: Reference) -> Slot:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSlotFromRef(Reference iProfile,
                | Reference iCenterCurve) As Slot
                | 
                |     Creates and returns a new slot within the current shape.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The sketch defining the slot section 
                |         iCenterCurve
                |             The curve that defines the slot center curve.
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     Returns:
                |         The created slot

        :param Reference i_profile:
        :param Reference i_center_curve:
        :rtype: Slot
        """
        return Slot(self.shape_factory.AddNewSlotFromRef(i_profile.com_object, i_center_curve.com_object))

    def add_new_solid_combine(self, i_profile_elt_first: Reference, i_profile_elt_second: Reference) -> SolidCombine:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSolidCombine(Reference iProfileEltFirst,
                | Reference iProfileEltSecond) As SolidCombine
                | 
                |     Creates and returns a new SolidCombine feature.
                | 
                |     Parameters:
                | 
                |         iProfileEltFirst
                |             The reference of the element defining the profile for first
                |             component. 
                |         iProfileEltSecond
                |             The reference of the element defining the profile for second
                |             component. 
                | 
                |     Returns:
                |         The created SolidCombine feature.

        :param Reference i_profile_elt_first:
        :param Reference i_profile_elt_second:
        :rtype: SolidCombine
        """
        return SolidCombine(
            self.shape_factory.AddNewSolidCombine(i_profile_elt_first.com_object, i_profile_elt_second.com_object))

    def add_new_solid_edge_fillet_with_constant_radius(self, i_edge_to_fillet: Reference, i_propag_mode: int,
                                                       i_radius: float) -> ConstRadEdgeFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSolidEdgeFilletWithConstantRadius(Reference
                | iEdgeToFillet,
                | CatFilletEdgePropagation iPropagMode,
                | double iRadius) As ConstRadEdgeFillet
                | 
                |     Creates and returns a new solid edge fillet with a constant radius. within
                |     the current body.
                | 
                |     Parameters:
                | 
                |         iEdgeToFillet
                |             The edge that will be filleted first
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iPropagMode
                |         Controls whether other edges found adjacent to the first one should
                |         also be filleted in the same operation 
                |     iRadius
                |         The fillet radius 
                |     Returns:
                |         The created edge fillet

        :param Reference i_edge_to_fillet:
        :param int i_propag_mode: enum cat_fillet_edge_propagation
        :param float i_radius:
        :rtype: ConstRadEdgeFillet
        """
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewSolidEdgeFilletWithConstantRadius(i_edge_to_fillet.com_object, i_propag_mode,
                                                                       i_radius))

    def add_new_solid_edge_fillet_with_varying_radius(self, i_edge_to_fillet: Reference, i_propag_mode: int,
                                                      i_variation_mode: int,
                                                      i_default_radius: float) -> VarRadEdgeFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSolidEdgeFilletWithVaryingRadius(Reference
                | iEdgeToFillet,
                | CatFilletEdgePropagation iPropagMode,
                | CatFilletVariation iVariationMode,
                | double iDefaultRadius) As VarRadEdgeFillet
                | 
                |     Creates and returns a new solid edge fillet with a varying radius. within
                |     the current body.
                | 
                |     Parameters:
                | 
                |         iEdgeToFillet
                |             The edge that will be filleted first
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iPropagMode
                |         Controls whether other edges found adjacent to the first one should
                |         also be filleted in the same operation 
                |     iVariationMode
                |         Controls the law of evolution for the fillet radius between specified
                |         control points, such as edges extremities 
                |     iDefaultRadius
                |         The fillet default radius, that will apply when no other radius can be
                |         inferred from the iVariationMode parameter 
                |     Returns:
                |         The created edge fillet

        :param Reference i_edge_to_fillet:
        :param int i_propag_mode: enum cat_fillet_edge_propagation
        :param int i_variation_mode: enum cat_fillet_variation
        :param float i_default_radius:
        :rtype: VarRadEdgeFillet
        """
        return VarRadEdgeFillet(
            self.shape_factory.AddNewSolidEdgeFilletWithVaryingRadius(i_edge_to_fillet.com_object, i_propag_mode,
                                                                      i_variation_mode, i_default_radius))

    def add_new_solid_face_fillet(self, i_f1: Reference, i_f2: Reference, i_radius: float) -> FaceFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSolidFaceFillet(Reference iF1,
                | Reference iF2,
                | double iRadius) As FaceFillet
                | 
                |     Creates and returns a new solid face-to-face fillet.
                |     Use this method to created face-to-face fillets with varying fillet radii,
                |     by editing fillet attributes driving its radius after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iF1
                |             The first face that will support the fillet
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iF2
                |         The second face that will support the fillet
                |         The following Boundary object is supported: Face.
                |     iRadius
                |         The fillet radius 
                |     Returns:
                |         The created face-to-face fillet

        :param Reference i_f1:
        :param Reference i_f2:
        :param float i_radius:
        :rtype: FaceFillet
        """
        return FaceFillet(self.shape_factory.AddNewSolidFaceFillet(i_f1.com_object, i_f2.com_object, i_radius))

    def add_new_solid_tritangent_fillet(self, i_f1: Reference, i_f2: Reference,
                                        i_removed_face: Reference) -> TritangentFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSolidTritangentFillet(Reference iF1,
                | Reference iF2,
                | Reference iRemovedFace) As TritangentFillet
                | 
                |     Creates and returns a new solid tritangent fillet within the current
                |     body.
                |     This kind of fillet begins with tangency on a first face iF1, gets tangent
                |     to a second one iRemovedFace and ends with tangency to a third one iF2. During
                |     the process the second face iRemovedFace is removed.
                | 
                |     Parameters:
                | 
                |         iF1
                |             The starting face for the fillet
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iF2
                |         The ending face for the fillet
                |         The following Boundary object is supported: Face.
                |     iRemovedFace
                |         The face used as an intermediate tangent support for the fillet during
                |         its course from iF1 to iF2. This face will be removed at the end of the
                |         filleting operation.
                |         The following Boundary object is supported: Face
                |     Returns:
                |         The created tritangent fillet

        :param Reference i_f1:
        :param Reference i_f2:
        :param Reference i_removed_face:
        :rtype: TritangentFillet
        """
        return TritangentFillet(
            self.shape_factory.AddNewSolidTritangentFillet(i_f1.com_object, i_f2.com_object, i_removed_face.com_object))

    def add_new_split(self, i_splitting_element: Reference, i_split_side: int) -> Split:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSplit(Reference iSplittingElement,
                | CatSplitSide iSplitSide) As Split
                | 
                |     Creates and returns a new split operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iSplittingElement
                |             The face or plane that will split the current body
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iSplitSide
                |         The specification for which side of the current body should be kept at
                |         the end of the split operation 
                |     Returns:
                |         The created split operation

        :param Reference i_splitting_element:
        :param int i_split_side: enum cat_split_side
        :rtype: Split
        """
        return Split(self.shape_factory.AddNewSplit(i_splitting_element.com_object, i_split_side))

    def add_new_stiffener(self, i_sketch: Sketch) -> Stiffener:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewStiffener(Sketch iSketch) As Stiffener
                | 
                |     Creates and returns a new stiffener within the current
                |     body.
                |     A stiffener is made up of a sketch used as the stiffener profile, that is
                |     extruded (offset) and that fills the nearest shape.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the stiffener border. It must contain a line or
                |             a curve that does not cross in 3D space the face(s) to stiffen.
                |             
                | 
                |     Returns:
                |         The created stiffener

        :param Sketch i_sketch:
        :rtype: Stiffener
        """
        return Stiffener(self.shape_factory.AddNewStiffener(i_sketch.com_object))

    def add_new_stiffener_from_ref(self, i_profile_elt: Reference) -> Stiffener:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewStiffenerFromRef(Reference iProfileElt) As
                | Stiffener
                | 
                |     Creates and returns a new stiffener within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iProfileElt
                |             The reference on the element defining the stiffener profile
                |             
                | 
                |     Returns:
                |         The created stiffener

        :param Reference i_profile_elt:
        :rtype: Stiffener
        """
        return Stiffener(self.shape_factory.AddNewStiffenerFromRef(i_profile_elt.com_object))

    def add_new_surface_edge_fillet_with_constant_radius(self, i_edge_to_fillet: Reference, i_propag_mode: int,
                                                         i_radius: float) -> ConstRadEdgeFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfaceEdgeFilletWithConstantRadius(Reference
                | iEdgeToFillet,
                | CatFilletEdgePropagation iPropagMode,
                | double iRadius) As ConstRadEdgeFillet
                | 
                |     Creates and returns a new surface edge fillet with a constant radius.
                |     within the current body.
                | 
                |     Parameters:
                | 
                |         iEdgeToFillet
                |             The edge that will be filleted first
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iPropagMode
                |         Controls whether other edges found adjacent to the first one should
                |         also be filleted in the same operation 
                |     iRadius
                |         The fillet radius 
                |     Returns:
                |         The created edge fillet

        :param Reference i_edge_to_fillet:
        :param int i_propag_mode: enum cat_fillet_edge_propagation
        :param float i_radius:
        :rtype: ConstRadEdgeFillet
        """
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewSurfaceEdgeFilletWithConstantRadius(i_edge_to_fillet.com_object, i_propag_mode,
                                                                         i_radius))

    def add_new_surface_edge_fillet_with_varying_radius(self, i_edge_to_fillet: Reference, i_propag_mode: int,
                                                        i_variation_mode: int,
                                                        i_default_radius: float) -> VarRadEdgeFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfaceEdgeFilletWithVaryingRadius(Reference
                | iEdgeToFillet,
                | CatFilletEdgePropagation iPropagMode,
                | CatFilletVariation iVariationMode,
                | double iDefaultRadius) As VarRadEdgeFillet
                | 
                |     Creates and returns a new surface edge fillet with a varying radius. within
                |     the current body.
                | 
                |     Parameters:
                | 
                |         iEdgeToFillet
                |             The edge that will be filleted first
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iPropagMode
                |         Controls whether other edges found adjacent to the first one should
                |         also be filleted in the same operation 
                |     iVariationMode
                |         Controls the law of evolution for the fillet radius between specified
                |         control points, such as edges extremities 
                |     iDefaultRadius
                |         The fillet default radius, that will apply when no other radius can be
                |         inferred from the iVariationMode parameter 
                |     Returns:
                |         The created edge fillet

        :param Reference i_edge_to_fillet:
        :param int i_propag_mode: enum cat_fillet_edge_propagation
        :param int i_variation_mode: enum cat_fillet_variation
        :param float i_default_radius:
        :rtype: VarRadEdgeFillet
        """
        return VarRadEdgeFillet(
            self.shape_factory.AddNewSurfaceEdgeFilletWithVaryingRadius(i_edge_to_fillet.com_object, i_propag_mode,
                                                                        i_variation_mode, i_default_radius))

    def add_new_surface_face_fillet(self, i_f1: Reference, i_f2: Reference, i_radius: float) -> FaceFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfaceFaceFillet(Reference iF1,
                | Reference iF2,
                | double iRadius) As FaceFillet
                | 
                |     Creates and returns a new surface face-to-face fillet.
                |     Use this method to created face-to-face fillets with varying fillet radii,
                |     by editing fillet attributes driving its radius after its
                |     creation.
                | 
                |     Parameters:
                | 
                |         iF1
                |             The first face that will support the fillet
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iF2
                |         The second face that will support the fillet
                |         The following Boundary object is supported: Face.
                |     iRadius
                |         The fillet radius 
                |     Returns:
                |         The created face-to-face fillet

        :param Reference i_f1:
        :param Reference i_f2:
        :param float i_radius:
        :rtype: FaceFillet
        """
        return FaceFillet(self.shape_factory.AddNewSurfaceFaceFillet(i_f1.com_object, i_f2.com_object, i_radius))

    def add_new_surface_tritangent_fillet(self, i_f1: Reference, i_f2: Reference,
                                          i_removed_face: Reference) -> TritangentFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfaceTritangentFillet(Reference iF1,
                | Reference iF2,
                | Reference iRemovedFace) As TritangentFillet
                | 
                |     Creates and returns a new surface tritangent fillet within the current
                |     body.
                |     This kind of fillet begins with tangency on a first face iF1, gets tangent
                |     to a second one iRemovedFace and ends with tangency to a third one iF2. During
                |     the process the second face iRemovedFace is removed.
                | 
                |     Parameters:
                | 
                |         iF1
                |             The starting face for the fillet
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iF2
                |         The ending face for the fillet
                |         The following Boundary object is supported: Face.
                |     iRemovedFace
                |         The face used as an intermediate tangent support for the fillet during
                |         its course from iF1 to iF2. This face will be removed at the end of the
                |         filleting operation.
                |         The following Boundary object is supported: Face
                |     Returns:
                |         The created tritangent fillet

        :param Reference i_f1:
        :param Reference i_f2:
        :param Reference i_removed_face:
        :rtype: TritangentFillet
        """
        return TritangentFillet(self.shape_factory.AddNewSurfaceTritangentFillet(i_f1.com_object, i_f2.com_object,
                                                                                 i_removed_face.com_object))

    def add_new_surfacic_auto_fillet(self, i_fillet_radius: float) -> AutoFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfacicAutoFillet(double iFilletRadius) As
                | AutoFillet
                | 
                |     Creates and returns a new Surfacic autofillet.
                |     Use this method to create autofillet by providing fillet radius
                |     value.
                | 
                |     Parameters:
                | 
                |         iFilletRadius
                |             The fillet radius 
                | 
                |     Returns:
                |         The created autofillet

        :param float i_fillet_radius:
        :rtype: AutoFillet
        """
        return AutoFillet(self.shape_factory.AddNewSurfacicAutoFillet(i_fillet_radius))

    def add_new_surfacic_circ_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_radial_dir: int,
                                      i_nb_of_copies_in_angular_dir: int, i_step_in_radial_dir: float,
                                      i_step_in_angular_dir: float, i_shape_to_copy_position_along_radial_dir: int,
                                      i_shape_to_copy_position_along_angular_dir: int, i_rotation_center: Reference,
                                      i_rotation_axis: Reference, i_is_reversed_rotation_axis: bool,
                                      i_rotation_angle: float, i_is_radius_aligned: bool,
                                      i_complete_crown: bool) -> CircPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfacicCircPattern(AnyObject iShapeToCopy,
                | long iNbOfCopiesInRadialDir,
                | long iNbOfCopiesInAngularDir,
                | double iStepInRadialDir,
                | double iStepInAngularDir,
                | long iShapeToCopyPositionAlongRadialDir,
                | long iShapeToCopyPositionAlongAngularDir,
                | Reference iRotationCenter,
                | Reference iRotationAxis,
                | boolean iIsReversedRotationAxis,
                | double iRotationAngle,
                | boolean iIsRadiusAligned,
                | boolean iCompleteCrown) As CircPattern
                | 
                |     Creates and returns a new gsd circular pattern within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the circular pattern 
                |         iNbOfInstancesInRadialDir
                |             The number of times iShapeToCopy will be copied along pattern
                |             radial direction 
                |         iNbOfInstancesInAngularDir
                |             The number of times iShapeToCopy will be copied along pattern
                |             angular direction 
                |         iStepInRadialDir
                |             The distance that will separate two consecutive copies in the
                |             pattern along its radial direction 
                |         iStepInAngularDir
                |             The angle that will separate two consecutive copies in the pattern
                |             along its angular direction 
                |         iShapeToCopyPositionAlongRadialDir
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along the radial direction 
                |         iShapeToCopyPositionAlongAngularDir
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along the angular direction 
                |         iRotationCenter
                |             The point or vertex that specifies the pattern center of rotation
                |             
                |         iRotationAxis
                |             The line or linear edge that specifies the axis around which
                |             instances will be rotated relative to each other
                |             The following 
                | 
                |         Boundary objects are supported: PlanarFace , CylindricalFace ,
                |         RectilinearTriDimFeatEdge and RectilinearBiDimFeatEdge.
                |         
                |     iIsReversedRotationAxis
                |         The boolean flag indicating wether the natural orientation of
                |         iRotationAxis should be used to orient the pattern operation. A value of true
                |         indicates that iItemToDuplicate are copied in the direction of the natural
                |         orientation of iRotationAxis. 
                |     iRotationAngle
                |         The angle applied to the direction iRotationAxis prior to applying the
                |         pattern. The original shape iShapeToCopy is used as the rotation center.
                |         Nevertheless, the copied shapes themselves are not rotated. This allows the
                |         definition of a circular pattern relatively to existing geometry, but not
                |         necessarily parallel to it. 
                |     iIsRadiusAligned
                |         The boolean flag that specifies whether the instances of
                |         iItemToDuplicate copied by the pattern should be kept parallel to each other
                |         (True) or if they should be aligned with the radial direction they lie upon
                |         (False). 
                |     iCompleteCrown
                |         The boolean flag specifies the mode of angular distribution. True
                |         indicates that the angular step will be equal to 360 degrees iNba.
                |         
                |     Returns:
                |         The created circular pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_radial_dir:
        :param int i_nb_of_copies_in_angular_dir:
        :param float i_step_in_radial_dir:
        :param float i_step_in_angular_dir:
        :param int i_shape_to_copy_position_along_radial_dir:
        :param int i_shape_to_copy_position_along_angular_dir:
        :param Reference i_rotation_center:
        :param Reference i_rotation_axis:
        :param bool i_is_reversed_rotation_axis:
        :param float i_rotation_angle:
        :param bool i_is_radius_aligned:
        :param bool i_complete_crown:
        :rtype: CircPattern
        """
        return CircPattern(
            self.shape_factory.AddNewSurfacicCircPattern(i_shape_to_copy.com_object, i_nb_of_copies_in_radial_dir,
                                                         i_nb_of_copies_in_angular_dir, i_step_in_radial_dir,
                                                         i_step_in_angular_dir,
                                                         i_shape_to_copy_position_along_radial_dir,
                                                         i_shape_to_copy_position_along_angular_dir,
                                                         i_rotation_center.com_object, i_rotation_axis.com_object,
                                                         i_is_reversed_rotation_axis, i_rotation_angle,
                                                         i_is_radius_aligned, i_complete_crown))

    def add_new_surfacic_rect_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies_in_dir1: int,
                                      i_nb_of_copies_in_dir2: int, i_step_in_dir1: float, i_step_in_dir2: float,
                                      i_shape_to_copy_position_along_dir1: int,
                                      i_shape_to_copy_position_along_dir2: int, i_dir1: Reference, i_dir2: Reference,
                                      i_is_reversed_dir1: bool, i_is_reversed_dir2: bool,
                                      i_rotation_angle: float) -> RectPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfacicRectPattern(AnyObject iShapeToCopy,
                | long iNbOfCopiesInDir1,
                | long iNbOfCopiesInDir2,
                | double iStepInDir1,
                | double iStepInDir2,
                | long iShapeToCopyPositionAlongDir1,
                | long iShapeToCopyPositionAlongDir2,
                | Reference iDir1,
                | Reference iDir2,
                | boolean iIsReversedDir1,
                | boolean iIsReversedDir2,
                | double iRotationAngle) As RectPattern
                | 
                |     Creates and returns a new GSD rectangular pattern within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the rectangular pattern 
                |         iNbOfCopiesInDir1
                |             The number of times iShapeToCopy will be copied along the pattern
                |             first direction 
                |         iNbOfCopiesInDir2
                |             The number of times iShapeToCopy will be copied along the pattern
                |             second direction 
                |         iStepInDir1
                |             The distance that will separate two consecutive copies in the
                |             pattern along its first direction 
                |         iStepInDir2
                |             The distance that will separate two consecutive copies in the
                |             pattern along its second direction 
                |         iShapeToCopyPositionAlongDir1
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along iDir1 
                |         iShapeToCopyPositionAlongDir2
                |             Specifies the position of the original shape iShapeToCopy among its
                |             copies along iDir2 
                |         iDir1
                |             The line or linear edge that specifies the pattern first
                |             repartition direction
                |             The following 
                | 
                |         Boundary objects are supported: PlanarFace, RectilinearTriDimFeatEdge,
                |         RectilinearBiDimFeatEdge. 
                |     iDir2
                |         The line or linear edge that specifies the pattern second repartition
                |         direction
                |         The following Boundary objects are supported: PlanarFace,
                |         RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge.
                |     iIsReversedDir1
                |         The boolean flag indicating whether the natural orientation of iDir1
                |         should be used to orient the pattern operation. True indicates that
                |         iShapeToCopy is copied in the direction of the natural orientation of iDir1.
                |         
                |     iIsReversedDir2
                |         The boolean flag indicating whether the natural orientation of iDir2
                |         should be used to orient the pattern operation. True indicates that
                |         iShapeToCopy is copied in the direction of the natural orientation of iDir2.
                |         
                |     iRotationAngle
                |         The angle applied to both directions iDir1 and iDir2 prior to applying
                |         the pattern. The original shape iShapeToCopy is used as the rotation center.
                |         Nevertheless, the copied shapes themselves are not rotated. This allows the
                |         definition of a rectangular pattern relatively to existing geometry, but not
                |         necessarily parallel to it. 
                |     Returns:
                |         The created rectangular pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies_in_dir1:
        :param int i_nb_of_copies_in_dir2:
        :param float i_step_in_dir1:
        :param float i_step_in_dir2:
        :param int i_shape_to_copy_position_along_dir1:
        :param int i_shape_to_copy_position_along_dir2:
        :param Reference i_dir1:
        :param Reference i_dir2:
        :param bool i_is_reversed_dir1:
        :param bool i_is_reversed_dir2:
        :param float i_rotation_angle:
        :rtype: RectPattern
        """
        return RectPattern(
            self.shape_factory.AddNewSurfacicRectPattern(i_shape_to_copy.com_object, i_nb_of_copies_in_dir1,
                                                         i_nb_of_copies_in_dir2, i_step_in_dir1, i_step_in_dir2,
                                                         i_shape_to_copy_position_along_dir1,
                                                         i_shape_to_copy_position_along_dir2, i_dir1.com_object,
                                                         i_dir2.com_object, i_is_reversed_dir1, i_is_reversed_dir2,
                                                         i_rotation_angle))

    def add_new_surfacic_sew_surface(self, i_type: int, i_support_surface: Reference, i_sewing_element: Reference,
                                     i_sewing_side: int) -> SewSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfacicSewSurface(long iType,
                | Reference iSupportSurface,
                | Reference iSewingElement,
                | CatSplitSide iSewingSide) As SewSurface
                | 
                |     Creates and returns a new volume sewing operation within the current
                |     OGS/GS.
                | 
                |     Parameters:
                | 
                |         iType
                |             Parameter to determine the sewing type. For Volume sewing Type = 4 
                |         iSupportSurface
                |             The surfacic support on which sew operation will be performed
                |             
                |         iSewingElement
                |             The face or skin or surface that will be sewn on the current volume
                |             support 
                |         iSewingSide
                |             The specification for which side of the current volume should be
                |             kept at the end of the sewing operation 
                | 
                |     Returns:
                |         The created sewing operation

        :param int i_type:
        :param Reference i_support_surface:
        :param Reference i_sewing_element:
        :param int i_sewing_side: enum cat_split_side
        :rtype: SewSurface
        """
        return SewSurface(self.shape_factory.AddNewSurfacicSewSurface(i_type, i_support_surface.com_object,
                                                                      i_sewing_element.com_object, i_sewing_side))

    def add_new_surfacic_user_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies: int) -> UserPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewSurfacicUserPattern(AnyObject iShapeToCopy,
                | long iNbOfCopies) As UserPattern
                | 
                |     Creates and returns a new GSD user pattern within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the user pattern 
                |         iNbOfCopies
                |             The number of times iShapeToCopy will be copied 
                | 
                |     Returns:
                |         The created user pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies:
        :rtype: UserPattern
        """
        return UserPattern(self.shape_factory.AddNewSurfacicUserPattern(i_shape_to_copy.com_object, i_nb_of_copies))

    def add_new_symmetry_2(self, i_reference: Reference) -> HybridShapeSymmetry:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help - Manually created. (2022-10-10)
                | o Func AddNewSymmetry2(Reference iReference) As HybridShapeSymmetry
                | 
                |     Creates a new Symmetry within the current body.
                | 
                |     Parameters:
                |         
                |     iReference
                |         Point, line or reference plane.
                |         Sub-element(s) supported (see Boundary object): see PlanarFace, Edge
                |         and Vertex.
                |     oSymmetry
                |         Created symmetry.

        :param Reference i_reference:
        :rtype: HybridShapeSymmetry
        """
        return HybridShapeSymmetry(
            self.shape_factory.AddNewSymmetry2(i_reference.com_object)
        )

    def add_new_thick_surface(self, i_offset_element: Reference, i_isens_offset: int, i_top_offset: float,
                              i_bot_offset: float) -> ThickSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewThickSurface(Reference iOffsetElement,
                | long iIsensOffset,
                | double iTopOffset,
                | double iBotOffset) As ThickSurface
                | 
                |     Creates and returns a new ThickSurface feature.
                | 
                |     Parameters:
                | 
                |         iOffsetElement
                |             The skin that will be thicken and added with the current body
                |             
                |         iIsensOffset
                |             The direction of the offset in regard to the direction of the
                |             normal 
                |         iTopOffset
                |             The Offset between the iOffsetElement and the upper skin of the
                |             resulting feature 
                |         iBotOffset
                |             The Offset between the iOffsetElement and the lower skin of the
                |             resulting feature 
                | 
                |     Returns:
                |         The created ThickSurface feature

        :param Reference i_offset_element:
        :param int i_isens_offset:
        :param float i_top_offset:
        :param float i_bot_offset:
        :rtype: ThickSurface
        """
        return ThickSurface(
            self.shape_factory.AddNewThickSurface(i_offset_element.com_object, i_isens_offset, i_top_offset,
                                                  i_bot_offset))

    def add_new_thickness(self, i_face_to_thicken: Reference, i_offset: float) -> Thickness:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewThickness(Reference iFaceToThicken,
                | double iOffset) As Thickness
                | 
                |     Creates and returns a new thickness within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The first face to thicken in the thickening
                |             process.
                |             New faces to thicken can be added to the thickness afterwards by
                |             using methods offered by the created thickness
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iOffset
                |         The thickness of material to be added on the external side of the face
                |         iFaceToThicken during the thickening process 
                |     Returns:
                |         The created thickness

        :param Reference i_face_to_thicken:
        :param float i_offset:
        :rtype: Thickness
        """
        return Thickness(self.shape_factory.AddNewThickness(i_face_to_thicken.com_object, i_offset))

    def add_new_thread_with_out_ref(self) -> Thread:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewThreadWithOutRef() As Thread
                | 
                |     Creates and returns a new thread\tap within the current
                |     body.
                | 
                |     Returns:
                |         The created Thread

        :rtype: Thread
        """
        return Thread(self.shape_factory.AddNewThreadWithOutRef())

    def add_new_thread_with_ref(self, i_lateral_face: Reference, i_limit_face: Reference) -> Thread:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewThreadWithRef(Reference iLateralFace,
                | Reference iLimitFace) As Thread
                | 
                |     Creates and returns a new thread\tap within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iLateralFace
                |             The Face defining the support of thread\tap
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iLimitFacee
                |         The Face defining the origin of the thread.
                |         The following Boundary object is supported:
                |         PlanarFace.
                |     Returns:
                |         The created Thread

        :param Reference i_lateral_face:
        :param Reference i_limit_face:
        :rtype: Thread
        """
        return Thread(self.shape_factory.AddNewThreadWithRef(i_lateral_face.com_object, i_limit_face.com_object))

    def add_new_translate2(self, i_distance: float) -> Translate:

        """
            .. note::
                :class: toggle

                Microsoft Visual Basic Object Browser
                    | Function AddNewTranslate2(iDistance As Double) As AnyObject
                    | Member of PARTITF.ShapeFactory


        :param float i_distance:
        :rtype: AnyObject
        """

        return Translate(self.shape_factory.AddNewTranslate2(i_distance))

    def add_new_trim(self, i_body_to_trim: Body) -> Trim:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewTrim(Body iBodyToTrim) As Trim
                | 
                |     Creates and returns a new Trim operation within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iBodyToTrim
                |             The body to Trim with current body. 
                | 
                |     Returns:
                |         The created Trim operation

        :param Body i_body_to_trim:
        :rtype: Trim
        """
        return Trim(self.shape_factory.AddNewTrim(i_body_to_trim.com_object))

    def add_new_tritangent_fillet(self, i_f1: Reference, i_f2: Reference,
                                  i_removed_face: Reference) -> TritangentFillet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewTritangentFillet(Reference iF1,
                | Reference iF2,
                | Reference iRemovedFace) As TritangentFillet
                | 
                |     Deprecated:
                |         V5R14 #AddNewTritangentFillet use AddNewSolidTritangentFillet or
                |         AddNewSurfaceTritangentFillet depending on the type of fillet you want to
                |         create

        :param Reference i_f1:
        :param Reference i_f2:
        :param Reference i_removed_face:
        :rtype: TritangentFillet
        """
        return TritangentFillet(
            self.shape_factory.AddNewTritangentFillet(i_f1.com_object, i_f2.com_object, i_removed_face.com_object))

    def add_new_user_pattern(self, i_shape_to_copy: AnyObject, i_nb_of_copies: int) -> UserPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewUserPattern(AnyObject iShapeToCopy,
                | long iNbOfCopies) As UserPattern
                | 
                |     Creates and returns a new user pattern within the current
                |     body.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the user pattern 
                |         iNbOfCopies
                |             The number of times iShapeToCopy will be copied 
                | 
                |     Returns:
                |         The created user pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies:
        :rtype: UserPattern
        """
        return UserPattern(self.shape_factory.AddNewUserPattern(i_shape_to_copy.com_object, i_nb_of_copies))

    def add_new_user_patternof_list(self, i_shape_to_copy: AnyObject, i_nb_of_copies: int) -> UserPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewUserPatternofList(AnyObject iShapeToCopy,
                | long iNbOfCopies) As UserPattern
                | 
                |     V5R8 Only: Creates and returns a new user pattern within the current body
                |     using a list of shapes.
                | 
                |     Parameters:
                | 
                |         iShapeToCopy
                |             The shape to be copied by the user pattern Others shapes will be
                |             add by put_ItemToCopy with CATIAPattern interface 
                |         iNbOfCopies
                |             The number of times iShapeToCopy will be copied 
                | 
                |     Returns:
                |         The created user pattern

        :param AnyObject i_shape_to_copy:
        :param int i_nb_of_copies:
        :rtype: UserPattern
        """
        return UserPattern(self.shape_factory.AddNewUserPatternofList(i_shape_to_copy.com_object, i_nb_of_copies))

    def add_new_volume_add(self, i_body1: Reference, i_body2: Reference, i_type: float) -> Add:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeAdd(Reference iBody1,
                | Reference iBody2,
                | double iType) As Add
                | 
                |     Creates and returns a Volumic Add feature.
                | 
                |     Parameters:
                | 
                |         iBody1
                |             The volume or body to be modified. 
                |         iBody2
                |             The volume or body to be operated. 
                |         iType
                |             iType = 0 if Part Design, = 4 if GSD. 
                | 
                |     Returns:
                |         The created Volumic Add feature.

        :param Reference i_body1:
        :param Reference i_body2:
        :param float i_type:
        :rtype: Add
        """
        return Add(self.shape_factory.AddNewVolumeAdd(i_body1.com_object, i_body2.com_object, i_type))

    def add_new_volume_close_surface(self, i_close_element: Reference) -> CloseSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeCloseSurface(Reference iCloseElement) As
                | CloseSurface
                | 
                |     Creates and returns a new VolumeCloseSurface feature.
                | 
                |     Parameters:
                | 
                |         iCloseElement
                |             The skin that will be closed and add with the current body
                |             
                | 
                |     Returns:
                |         The created CloseSurface feature

        :param Reference i_close_element:
        :rtype: CloseSurface
        """
        return CloseSurface(self.shape_factory.AddNewVolumeCloseSurface(i_close_element.com_object))

    def add_new_volume_intersect(self, i_body1: Reference, i_body2: Reference, i_type: float) -> Intersect:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeIntersect(Reference iBody1,
                | Reference iBody2,
                | double iType) As Intersect
                | 
                |     Creates and returns a Volumic Intersect feature.
                | 
                |     Parameters:
                | 
                |         iBody1
                |             The volume or body to be modified. 
                |         iBody2
                |             The volume or body to be operated. 
                |         iType
                |             iType = 0 if Part Design, = 4 if GSD. 
                | 
                |     Returns:
                |         The created Volumic Intersect feature.

        :param Reference i_body1:
        :param Reference i_body2:
        :param float i_type:
        :rtype: Intersect
        """
        return Intersect(self.shape_factory.AddNewVolumeIntersect(i_body1.com_object, i_body2.com_object, i_type))

    def add_new_volume_remove(self, i_body1: Reference, i_body2: Reference, i_type: float) -> Remove:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeRemove(Reference iBody1,
                | Reference iBody2,
                | double iType) As Remove
                | 
                |     Creates and returns a Volumic Remove feature.
                | 
                |     Parameters:
                | 
                |         iBody1
                |             The volume or body to be modified. 
                |         iBody2
                |             The volume or body to be operated. 
                |         iType
                |             iType = 0 if Part Design, = 4 if GSD. 
                | 
                |     Returns:
                |         The created Volumic Remove feature.

        :param Reference i_body1:
        :param Reference i_body2:
        :param float i_type:
        :rtype: Remove
        """
        return Remove(self.shape_factory.AddNewVolumeRemove(i_body1.com_object, i_body2.com_object, i_type))

    def add_new_volume_sew_surface(self, i_type: int, i_support_volume: Reference, i_sewing_element: Reference,
                                   i_sewing_side: int) -> SewSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeSewSurface(long iType,
                | Reference iSupportVolume,
                | Reference iSewingElement,
                | CatSplitSide iSewingSide) As SewSurface
                | 
                |     Creates and returns a new volume sewing operation within the current
                |     OGS/GS.
                | 
                |     Parameters:
                | 
                |         iType
                |             Parameter to determine the sewing type. For Volume sewing Type = 4 
                |         iSupportVolume
                |             The volume support on which sew operation will be performed
                |             
                |         iSewingElement
                |             The face or skin or surface that will be sewn on the current volume
                |             support 
                |         iSewingSide
                |             The specification for which side of the current volume should be
                |             kept at the end of the sewing operation 
                | 
                |     Returns:
                |         The created sewing operation

        :param int i_type:
        :param Reference i_support_volume:
        :param Reference i_sewing_element:
        :param int i_sewing_side: enum cat_split_side
        :rtype: SewSurface
        """
        return SewSurface(
            self.shape_factory.AddNewVolumeSewSurface(i_type, i_support_volume.com_object, i_sewing_element.com_object,
                                                      i_sewing_side))

    def add_new_volume_shell(self, i_face_to_remove: Reference, i_internal_thickness: float,
                             i_external_thickness: float, i_volume_support: Reference) -> Shell:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeShell(Reference iFaceToRemove,
                | double iInternalThickness,
                | double iExternalThickness,
                | Reference iVolumeSupport) As Shell
                | 
                |     Creates and returns a Volumic Shell feature.
                | 
                |     Parameters:
                | 
                |         iFacesToRemove
                |             The Faces of the Volume 
                |         iFacesToThicken
                |             The Faces of the Volume 
                |         iInternalThickness
                |             The thickness of material to be added on the internal side of all
                |             the faces during the shell process, except for those to be removed
                |             
                |         iExternaThickness
                |             The thickness of material to be added on the external side of all
                |             the faces during the shell process, except for those to be removed
                |             
                |         iVolumeSupport
                |             The Volume related the faces to remove and faces to thicken
                |             
                | 
                |     Returns:
                |         The created Volumic Shell.

        :param Reference i_face_to_remove:
        :param float i_internal_thickness:
        :param float i_external_thickness:
        :param Reference i_volume_support:
        :rtype: Shell
        """
        return Shell(self.shape_factory.AddNewVolumeShell(i_face_to_remove.com_object, i_internal_thickness,
                                                          i_external_thickness, i_volume_support.com_object))

    def add_new_volume_thick_surface(self, i_offset_element: Reference, i_isens_offset: int, i_top_offset: float,
                                     i_bot_offset: float) -> ThickSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeThickSurface(Reference iOffsetElement,
                | long iIsensOffset,
                | double iTopOffset,
                | double iBotOffset) As ThickSurface
                | 
                |     Creates and returns a new VolumeThickSurface feature.
                | 
                |     Parameters:
                | 
                |         iOffsetElement
                |             The skin that will be thicken and added with the current OGS/GS
                |             
                |         iIsensOffset
                |             The direction of the offset in regard to the direction of the
                |             normal 
                |         iTopOffset
                |             The Offset between the iOffsetElement and the upper skin of the
                |             resulting feature 
                |         iBotOffset
                |             The Offset between the iOffsetElement and the lower skin of the
                |             resulting feature 
                | 
                |     Returns:
                |         The created ThickSurface feature

        :param Reference i_offset_element:
        :param int i_isens_offset:
        :param float i_top_offset:
        :param float i_bot_offset:
        :rtype: ThickSurface
        """
        return ThickSurface(
            self.shape_factory.AddNewVolumeThickSurface(i_offset_element.com_object, i_isens_offset, i_top_offset,
                                                        i_bot_offset))

    def add_new_volume_thickness(self, i_face_to_thicken: Reference, i_offset: float, i_type: int,
                                 i_volume_support: Reference) -> Thickness:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeThickness(Reference iFaceToThicken,
                | double iOffset,
                | long iType,
                | Reference iVolumeSupport) As Thickness
                | 
                |     Creates and returns a volume new thickness within the current GS or
                |     OGS.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The first face to thicken in the thickening
                |             process.
                |             New faces to thicken can be added to the thickness afterwards by
                |             using methods offered by the created thickness
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iOffset
                |         The thickness of material to be added on the external side of the face
                |         iFaceToThicken during the thickening process 
                |     iType
                |         The mode of thickness creation (4=Volume) 
                |     iVolumeSupport
                |         The support volume for volumic draft 
                |     Returns:
                |         The created thickness

        :param Reference i_face_to_thicken:
        :param float i_offset:
        :param int i_type:
        :param Reference i_volume_support:
        :rtype: Thickness
        """
        return Thickness(self.shape_factory.AddNewVolumeThickness(i_face_to_thicken.com_object, i_offset, i_type,
                                                                  i_volume_support.com_object))

    def add_new_volume_trim(self, i_support_volume: Reference, i_cutting_volume: Reference) -> Trim:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumeTrim(Reference iSupportVolume,
                | Reference iCuttingVolume) As Trim
                | 
                |     Creates and returns a new Volume Trim operation within the
                |     GS/OGS.
                | 
                |     Parameters:
                | 
                |         iSupportVolume
                |             The Support Volume 
                |         iCutttingVolume
                |             The trimming Volume 
                | 
                |     Returns:
                |         The created Trim operation

        :param Reference i_support_volume:
        :param Reference i_cutting_volume:
        :rtype: Trim
        """
        return Trim(self.shape_factory.AddNewVolumeTrim(i_support_volume.com_object, i_cutting_volume.com_object))

    def add_new_volumic_draft(self, i_face_to_draft: Reference, i_neutral: Reference, i_neutral_mode: int,
                              i_parting: Reference, i_dir_x: float, i_dir_y: float, i_dir_z: float, i_mode: int,
                              i_angle: float, i_multiselection_mode: int, i_type: int,
                              i_volume_support: Reference) -> Draft:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddNewVolumicDraft(Reference iFaceToDraft,
                | Reference iNeutral,
                | CatDraftNeutralPropagationMode iNeutralMode,
                | Reference iParting,
                | double iDirX,
                | double iDirY,
                | double iDirZ,
                | CatDraftMode iMode,
                | double iAngle,
                | CatDraftMultiselectionMode iMultiselectionMode,
                | long iType,
                | Reference iVolumeSupport) As Draft
                | 
                |     Creates and returns a new volume draft within the current
                |     body.
                |     The draft needs a reference face on the body. This face will remain
                |     unchanged in the draft operation, while faces adjacent to it and specified for
                |     drafting will be rotated by the draft angle.
                | 
                |     Parameters:
                | 
                |         iFaceToDraft
                |             The first face to draft in the body. This face should be adjacent
                |             to the iFaceToDraft face. If several faces are to be drafted, only the first
                |             one is specified here, the others being inferred by propagating the draft
                |             operation onto faces adjacent to this first face. This is controlled by the
                |             iNeutralMode argument.
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iNeutral
                |         The reference face for the draft. The draft needs a reference face on
                |         the body, that will remain unchanged in the draft operation, while faces
                |         adjacent to it and specified for drafting will be rotated according to the
                |         draft angle iAngle.
                |         The following Boundary object is supported:
                |         PlanarFace.
                |     iNeutralMode
                |         Controls if and how the drafting operation should be propagated beyond
                |         the first face to draft iFaceToDraft to other adjacent faces.
                |         
                |     iParting
                |         The draft parting plane, face or surface. It specifies the element
                |         within the body to draft that represents the bottom of the mold. This element
                |         can be located either somewhere in the middle of the body or be one of its
                |         boundary faces. When located in the middle of the body, it crosses the faces to
                |         draft, and as a result, those faces are drafted with a positive angle on one
                |         side of the parting surface, and with a negative angle on the other
                |         side.
                |         The following Boundary object is supported:
                |         PlanarFace.
                |     iDirX,iDirY,iDirZ
                |         The X, Y, and Z components of the absolute vector representing the
                |         drafting direction (i.e. the mold extraction direction).
                |         
                |     iMode
                |         The draft connecting mode to its reference face iFaceToDraft
                |         
                |     iAngle
                |         The draft angle 
                |     iMultiselectionMode.
                |         The elements to be drafted can be selected explicitly or can implicitly
                |         selected as neighbors of the neutral face 
                |     iType
                |         The mode of draft creation (4=Volume) 
                |     iVolumeSupport
                |         The support volume for volumic draft 
                |     Returns:
                |         The created draft

        :param Reference i_face_to_draft:
        :param Reference i_neutral:
        :param int i_neutral_mode: enum cat_draft_neutral_propagation_mode
        :param Reference i_parting:
        :param float i_dir_x:
        :param float i_dir_y:
        :param float i_dir_z:
        :param int i_mode: enum cat_draft_mode
        :param float i_angle:
        :param int i_multiselection_mode: enum cat_draft_multiselection_mode
        :param int i_type:
        :param Reference i_volume_support:
        :rtype: Draft
        """
        return Draft(
            self.shape_factory.AddNewVolumicDraft(i_face_to_draft.com_object, i_neutral.com_object, i_neutral_mode,
                                                  i_parting.com_object, i_dir_x, i_dir_y, i_dir_z, i_mode, i_angle,
                                                  i_multiselection_mode, i_type, i_volume_support.com_object))

    def __repr__(self):
        return f'ShapeFactory(name="{self.name}")'
