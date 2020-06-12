#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class AutoFillet(DressUpShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             AutoFillet
                | 
                | Represents the AutoFillet shape.
                | A AutoFillet fillets all the edges of Solid
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.auto_fillet = com_object

    @property
    def curvature_radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CurvatureRadius() As Length (Read Only)
                | 
                |     Returns the Curvature radius.
                | 
                |     Example:
                |         The following example returns in Curvature radius the Curvature radius
                |         of the AutoFillet Autofillet:
                | 
                |          Set Curvatureradius = Autofillet.Radius

        :return: Length
        """

        return Length(self.auto_fillet.CurvatureRadius)

    @property
    def faces_to_fillet(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FacesToFillet() As References (Read Only)
                | 
                |     Returns or sets the faces to fillet.
                | 
                |     Example:
                |         The following example returns in facestofillet the faces required for
                |         autofillet autoFillet, and then sets it to
                |         NewFacestofillet:
                | 
                |          Set Facestofillet = autoFillet.Facestofillet
                |          autofillet.Facestofillet = NewFacestofillet

        :return: References
        """

        return References(self.auto_fillet.FacesToFillet)

    @property
    def faces_to_fillets(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FacesToFillets(Reference iFace) (Write Only)

        :return: False
        """

        return None

    @faces_to_fillets.setter
    def faces_to_fillets(self, value):
        """
        :param False value:
        """

        self.auto_fillet.FacesToFillets = value

    @property
    def fillet_radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FilletRadius() As Length (Read Only)
                | 
                |     Returns the Fillet radius.
                | 
                |     Example:
                |         The following example returns in fillet radius the fillet radius of the
                |         AutoFillet Autofillet:
                | 
                |          Set Filletradius = Autofillet.Radius

        :return: Length
        """

        return Length(self.auto_fillet.FilletRadius)

    @property
    def functional_face(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FunctionalFace(Reference iFace) (Write Only)

        :return: False
        """

        return None

    @functional_face.setter
    def functional_face(self, value):
        """
        :param False value:
        """

        self.auto_fillet.FunctionalFace = value

    @property
    def functional_faces(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FunctionalFaces() As References (Read Only)
                | 
                |     Returns or sets the functional face.
                | 
                |     Example:
                |         The following example returns in functionalface the functional face of
                |         the autofillet autoFillet, and then sets it to
                |         NewfunctionalFace:
                | 
                |          Set functionalFace = autoFillet.FunctionalFace
                |          autofillet.FunctionalFace = NewfunctionalFace

        :return: References
        """

        return References(self.auto_fillet.FunctionalFaces)

    @property
    def parting_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PartingElement() As Reference
                | 
                |     Returns or sets the parting element.
                | 
                |     Example:
                |         The following example returns in partingelement the parting element of
                |         the autofillet autoFillet, and then sets it to Newparting
                |         element:
                | 
                |          Set Parting element = autoFillet.PartingElement
                |          autofillet.PartingElement = NewPartingElement

        :return: Reference
        """

        return Reference(self.auto_fillet.PartingElement)

    @parting_element.setter
    def parting_element(self, value):
        """
        :param Reference value:
        """

        self.auto_fillet.PartingElement = value

    @property
    def round_radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RoundRadius() As Length (Read Only)
                | 
                |     Returns the Round radius.
                | 
                |     Example:
                |         The following example returns in round radius the round radius of the
                |         AutoFillet Autofillet:
                | 
                |          Set roundradius = Autofillet.Radius

        :return: Length
        """

        return Length(self.auto_fillet.RoundRadius)

    @property
    def round_radius_activation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RoundRadiusActivation() As boolean
                | 
                |     Returns the AutoFillet RoundRadiusActivation flag (for AutoFillet
                |     only).
                |     It returns 1 if RoundRadius is activated, 0 if not.
                | 
                |     Returns:
                |         oRoundRadActivation The RoundRadActivation flag as an
                |         int
                | 
                |         Example:

        :return: bool
        """

        return self.auto_fillet.RoundRadiusActivation

    @round_radius_activation.setter
    def round_radius_activation(self, value):
        """
        :param bool value:
        """

        self.auto_fillet.RoundRadiusActivation = value

    @property
    def slivers_and_crack(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SliversAndCrack(Reference iSlivers) (Write Only)

        :return: False
        """

        return None

    @slivers_and_crack.setter
    def slivers_and_crack(self, value):
        """
        :param False value:
        """

        self.auto_fillet.SliversAndCrack = value

    @property
    def slivers_and_cracks(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SliversAndCracks() As References (Read Only)
                | 
                |     Returns or sets the slivers face.
                | 
                |     Example:
                |         The following example returns in slivers the sliver face of the
                |         autofillet autoFillet, and then sets it to Newsliver:
                | 
                |          Set sliversFace = autoFillet.SliversFace
                |          autofillet.SliversFace = NewsliversFace

        :return: References
        """

        return References(self.auto_fillet.SliversAndCracks)

    @property
    def support_surface(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SupportSurface() As Reference
                | 
                |     Returns or sets the support surface.
                | 
                |     Example:
                |         The following example returns in SupportSurface the support surface
                |         required for autofillet autoFillet, and then sets it to
                |         NewSupportSurface:
                | 
                |          Set SupportSurface = autoFillet.SupportSurface
                |          autofillet.SupportSurface = NewSupportSurface

        :return: Reference
        """

        return Reference(self.auto_fillet.SupportSurface)

    @support_surface.setter
    def support_surface(self, value):
        """
        :param Reference value:
        """

        self.auto_fillet.SupportSurface = value

    def __repr__(self):
        return f'AutoFillet(name="{ self.name }")'
