#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect
from typing import TYPE_CHECKING

from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.edge_fillet import EdgeFillet

if TYPE_CHECKING:
    from pycatia.part_interfaces.const_rad_edge_fillet import ConstRadEdgeFillet


class VarRadEdgeFillet(EdgeFillet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 PartInterfaces.EdgeFillet
                |                                     VarRadEdgeFillet
                | 
                | Represents the edge fillet shape with a variable radius.
                | The resulting shape is made up of edges fillets controlled by couples of
                | radius/vertex.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.var_rad_edge_fillet = com_object

    @property
    def bitangency_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BitangencyType() As CatFilletBitangencyType
                | 
                |     Returns or set the fillet bitangency type.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type used to perform the fillet : catSphereBitangencyType or catCircleBitangencyType

        :return: enum cat_fillet_bitangency_type
        :rtype: int
        """

        return self.var_rad_edge_fillet.BitangencyType

    @bitangency_type.setter
    def bitangency_type(self, value: int):
        """
        :param int value: enum cat_fillet_bitangency_type
        """

        self.var_rad_edge_fillet.BitangencyType = value

    @property
    def edges_to_fillet(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EdgesToFillet() As References (Read Only)
                | 
                |     Returns the collection of edges to be filleted.
                | 
                |     Example:
                |         The following example returns in edges the edges to fillet of variable
                |         radius edge filletfirstVarEdgeFillet:
                | 
                |          Set edges = firstVarEdgeFillet.EdgesToFillet

        :rtype: References
        """

        return References(self.var_rad_edge_fillet.EdgesToFillet)

    @property
    def fillet_spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FilletSpine() As Reference
                | 
                |     Returns or set the spine for circle bitangency fillet.
                | 
                |     Parameters:
                | 
                |         iSpin
                |             The spine to be used for a circle bitangency
                |             fillet

        :rtype: Reference
        """

        return Reference(self.var_rad_edge_fillet.FilletSpine)

    @fillet_spine.setter
    def fillet_spine(self, value: Reference):
        """
        :param Reference value:
        """

        self.var_rad_edge_fillet.FilletSpine = value.com_object

    @property
    def fillet_variation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FilletVariation() As CatFilletVariation
                | 
                |     Returns or sets the edge fillet radius variation mode.
                | 
                |     Example:
                |         The following example returns in mode the radius variation mode of the
                |         variable radius edge filletfirstVarEdgeFillet, and then sets it to
                |         CATLinearFilletVariation so that the radius variation is linear between two
                |         control vertices:
                | 
                |          mode = firstVarEdgeFillet.FilletVariation
                |          firstVarEdgeFillet.FilletVariation = CATLinearFilletVariation

        :return: enum cat_fillet_variation
        :rtype: int
        """

        return self.var_rad_edge_fillet.FilletVariation

    @fillet_variation.setter
    def fillet_variation(self, value: int):
        """
        :param int value: enum cat_fillet_variation
        """

        self.var_rad_edge_fillet.FilletVariation = value

    @property
    def imposed_vertices(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ImposedVertices() As References (Read Only)
                | 
                |     Returns the collection of vertices where a radius has been
                |     imposed.
                | 
                |     Example:
                |         The following example returns in vertices the collection of imposed
                |         vertices of the variable radius edge
                |         filletfirstVarEdgeFillet:
                | 
                |          Set vertices = firstVarEdgeFillet.ImposedVertices

        :rtype: References
        """

        return References(self.var_rad_edge_fillet.ImposedVertices)

    @property
    def sharp_edge_removal_mode(self) -> int:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property SharpEdgeRemovalMode() As short
                |     Returns or set the sharp edge removal mode for variable edge
                |     fillet.
                |
                |     Parameters:
                |
                |         iMode
                |             The mode to be used for variable edge fillet

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.var_rad_edge_fillet.SharpEdgeRemovalMode

    @sharp_edge_removal_mode.setter
    def sharp_edge_removal_mode(self, value: int):
        """
        :param int value:
        """

        self.var_rad_edge_fillet.SharpEdgeRemovalMode = value

    def add_edge_to_fillet(self, i_edge: Reference, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddEdgeToFillet(Reference iEdge,
                | double iRadius)
                | 
                |     Adds a new edge to the variable radius edge fillet.
                | 
                |     Parameters:
                | 
                |         iEdge
                |             The edge to be filleted
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                |     iRadius
                |         The radius to impose along the edge. This radius is imposed at both end
                |         points of the edge. 
                | 
                | Example:
                |     The following example adds the new edge edge to be filleted to the variable
                |     radius edge fillet firstVarEdgeFillet:
                | 
                |      call firstVarEdgeFillet.AddEdgeToFillet(edge, 5.)

        :param Reference i_edge:
        :param float i_radius:
        :rtype: None
        """
        return self.var_rad_edge_fillet.AddEdgeToFillet(i_edge.com_object, i_radius)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_edge_to_fillet'
        # # vba_code = """
        # # Public Function add_edge_to_fillet(var_rad_edge_fillet)
        # #     Dim iEdge (2)
        # #     var_rad_edge_fillet.AddEdgeToFillet iEdge
        # #     add_edge_to_fillet = iEdge
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_imposed_vertex(self, i_vertex: Reference, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddImposedVertex(Reference iVertex,
                | double iRadius)
                | 
                |     Adds a new control couple. A control couple is made up of a vertex and a
                |     radius.
                | 
                |     Parameters:
                | 
                |         iVertex
                |             The vertex where to impose the radius 
                |         iRadius
                |             The radius to impose at the given vertex 
                | 
                |     Example:
                |         The following example adds a new control couple (vertex, radius) to the
                |         variable radius edge fillet firstVarEdgeFillet set with the vertex vertex and a
                |         radius of 50.
                | 
                |          call firstVarEdgeFillet.AddImposedVertex(vertex, 50.)

        :param Reference i_vertex:
        :param float i_radius:
        :rtype: None
        """
        return self.var_rad_edge_fillet.AddImposedVertex(i_vertex.com_object, i_radius)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_imposed_vertex'
        # # vba_code = """
        # # Public Function add_imposed_vertex(var_rad_edge_fillet)
        # #     Dim iVertex (2)
        # #     var_rad_edge_fillet.AddImposedVertex iVertex
        # #     add_imposed_vertex = iVertex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def imposed_vertex_radius(self, i_imposed_vertex: Reference) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func ImposedVertexRadius(Reference iImposedVertex) As
                | Length
                | 
                |     Returns the fillet radius on an imposed vertex.
                | 
                |     Parameters:
                | 
                |         iImposedVertex
                |             The vertex where to retrieve the fillet radius 
                | 
                |     Returns:
                |         The fillet radius 
                |     Example:
                |         The following example returns in radius the fillet radius of the
                |         variable radius edge fillet firstVarEdgeFillet at the vertex
                |         vertex:
                | 
                |          Set radius = firstVarEdgeFillet.ImposedVertexRadius(vertex)

        :param Reference i_imposed_vertex:
        :rtype: Length
        """
        return Length(self.var_rad_edge_fillet.ImposedVertexRadius(i_imposed_vertex.com_object))

    def switch_to_const_fillet_type(self) -> 'ConstRadEdgeFillet':
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func SwitchToConstFilletType() As ConstRadEdgeFillet
                |     Changes the type of EdgeFillet to constant EdgeFillet and return
                |     it.
                |
                |     Parameters:
                |
                |         opConstFillet
                |             The opConstFillet is the variable edge fillet

        :rtype: ConstRadEdgeFillet
        """
        from pycatia.part_interfaces.const_rad_edge_fillet import ConstRadEdgeFillet

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return ConstRadEdgeFillet(self.var_rad_edge_fillet.SwitchToConstFilletType())

    def withdraw_edge_to_fillet(self, i_edge: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawEdgeToFillet(Reference iEdge)
                | 
                |     Withdraws an edge from the variable radius edge fillet.
                | 
                |     Parameters:
                | 
                |         iEdge
                |             The edge to be withdrawn
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example withdraws the edge edge from those to be filleted of
                |     the variable radius edge fillet firstVarEdgeFillet:
                | 
                |      call firstVarEdgeFillet.WithdrawEdgeToFillet(edge)

        :param Reference i_edge:
        :rtype: None
        """
        return self.var_rad_edge_fillet.WithdrawEdgeToFillet(i_edge.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_edge_to_fillet'
        # # vba_code = """
        # # Public Function withdraw_edge_to_fillet(var_rad_edge_fillet)
        # #     Dim iEdge (2)
        # #     var_rad_edge_fillet.WithdrawEdgeToFillet iEdge
        # #     withdraw_edge_to_fillet = iEdge
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_imposed_vertex(self, i_vertex: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawImposedVertex(Reference iVertex)
                | 
                |     Withdraws a control couple.
                | 
                |     Parameters:
                | 
                |         iVertex
                |             The vertex where the radius is imposed 
                | 
                |     Example:
                |         The following example withdraws the imposed radius on the vertex vertex
                |         for the variable radius edge fillet
                |         firstVarEdgeFillet:
                | 
                |          call firstVarEdgeFillet.WithdrawImposedVertex(vertex)

        :param Reference i_vertex:
        :rtype: None
        """
        return self.var_rad_edge_fillet.WithdrawImposedVertex(i_vertex.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_imposed_vertex'
        # # vba_code = """
        # # Public Function withdraw_imposed_vertex(var_rad_edge_fillet)
        # #     Dim iVertex (2)
        # #     var_rad_edge_fillet.WithdrawImposedVertex iVertex
        # #     withdraw_imposed_vertex = iVertex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'VarRadEdgeFillet(name="{self.name}")'
