#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.assembly_interfaces.assembly_feature import AssemblyFeature
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.body import Body
from pycatia.product_structure_interfaces.product import Product
from pycatia.sketcher_interfaces.sketch import Sketch
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AssemblyFeatures(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AssemblyFeatures
                | 
                | A collection of all the AssemblyFeature objects of a product.
                | 
                | See also:
                |     AssemblyFeature
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AssemblyFeature)
        self.assembly_features = com_object

    def add_assembly_add(self, i_body: Body, i_body_comp: Product, i_component: Product) -> AssemblyFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAssemblyAdd(Body iBody,
                | Product iBodyComp,
                | Product iComponent) As AssemblyFeature
                | 
                |     Creates a new AssemblyBoolean object by adding a body to the
                |     assembly.
                | 
                |     Parameters:
                | 
                |         iBody
                |             The body to add 
                |         iBodyComp
                |             The component that contains the body to add 
                |         iComponent
                |             The component with respect to which the AssemblyBoolean object to
                |             create will be positioned 
                | 
                |     Returns:
                |         The created AssemblyBoolean object 
                |     Example:
                |         This example creates the addBody AssemblyBoolean object in the
                |         assemblyFeats collection using a body referenced as bodyToAdd contained in the
                |         bodyToAddComp component, and positioned with respect to the positioningComp
                |         component.
                | 
                |          Dim addBody As AssemblyBoolean
                |          Set addBody = assemblyFeats.AddAssemblyAdd(bodyToAdd,     _
                |                                                     bodyToAddComp, _
                |                                                     itioningComp)

        :param Body i_body:
        :param Product i_body_comp:
        :param Product i_component:
        :rtype: AssemblyFeature
        """
        return AssemblyFeature(
            self.assembly_features.AddAssemblyAdd(
                i_body.com_object,
                i_body_comp.com_object,
                i_component.com_object
            )
        )

    def add_assembly_hole(
            self,
            i_sketch: Sketch,
            i_sketch_comp:
            Product,
            i_depth: float,
            i_component: Product) -> AssemblyFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAssemblyHole(Sketch iSketch,
                | Product iSketchComp,
                | double iDepth,
                | Product iComponent) As AssemblyFeature
                | 
                |     Creates a new AssemblyHole object.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the hole reference plane and anchor
                |             point.
                |             This sketch must contain a single point that defines the hole axis:
                |             the hole axis in 3D passes through that point and is normal to the sketch
                |             plane. 
                |         iSketchComp
                |             The component that contains the sketch 
                |         iDepth
                |             The hole depth 
                |         iComponent
                |             The component with respect to which the AssemblyHole object to
                |             create will be positioned 
                | 
                |     Returns:
                |         The created AssemblyHole object 
                |     Example:
                |         This example creates the hole AssemblyHole object in the assemblyFeats
                |         collection using a sketch referenced as holeSketch contained in the
                |         holeSketchComp component, with a depth of 60mm, and positioned with respect to
                |         the positioningComp component.
                | 
                |          Dim hole As AssemblyHole
                |          Set hole = assemblyFeats.AddAssemblyHole(holeSketch,     _
                |                                                   holeSketchComp,
                |                                                   _
                |                                                   60,            
                |                                                   _
                |                                                   positioningComp)

        :param Sketch i_sketch:
        :param Product i_sketch_comp:
        :param float i_depth:
        :param Product i_component:
        :rtype: AssemblyFeature
        """
        return AssemblyFeature(
            self.assembly_features.AddAssemblyHole(
                i_sketch.com_object,
                i_sketch_comp.com_object,
                i_depth,
                i_component.com_object
            )
        )

    def add_assembly_pocket(
            self,
            i_sketch: Sketch,
            i_sketch_comp: Product,
            i_depth: float,
            i_component: Product) -> AssemblyFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAssemblyPocket(Sketch iSketch,
                | Product iSketchComp,
                | double iDepth,
                | Product iComponent) As AssemblyFeature
                | 
                |     Creates a new AssemblyPocket object.
                | 
                |     Parameters:
                | 
                |         iSketch
                |             The sketch defining the pocket base 
                |         iSketchComp
                |             The component that contains the sketch 
                |         iDepth
                |             The pocket depth 
                |         iComponent
                |             The component with respect to which the AssemblyPocket object to
                |             create will be positioned 
                | 
                |     Returns:
                |         The created AssemblyPocket object 
                |     Example:
                |         This example creates the pocket AssemblyPocket object in the
                |         assemblyFeats collection using a sketch referenced as pocketSketch contained in
                |         the pocketSketchComp component, with a depth of 20mm, and positioned with
                |         respect to the positioningComp component.
                | 
                |          Dim pocket As AssemblyPocket
                |          Set pocket = assemblyFeats.AddAssemblyPocket(pocketSketch,     _
                |                                                       pocketSketchComp,
                |                                                       _
                |                                                       20,              
                |                                                       _
                |                                                       positioningComp)

        :param Sketch i_sketch:
        :param Product i_sketch_comp:
        :param float i_depth:
        :param Product i_component:
        :rtype: AssemblyFeature
        """
        return AssemblyFeature(
            self.assembly_features.AddAssemblyPocket(
                i_sketch.com_object,
                i_sketch_comp.com_object,
                i_depth,
                i_component.com_object
            )
        )

    def add_assembly_remove(self, i_body: Body, i_body_comp: Product, i_component: Product) -> AssemblyFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAssemblyRemove(Body iBody,
                | Product iBodyComp,
                | Product iComponent) As AssemblyFeature
                | 
                |     Creates a new AssemblyBoolean object by removing a body from the
                |     assembly.
                | 
                |     Parameters:
                | 
                |         iBody
                |             The body to remove 
                |         iBodyComp
                |             The component that contains the body to remove 
                |         iComponent
                |             The component with respect to which the AssemblyBoolean object to
                |             create will be positioned 
                | 
                |     Returns:
                |         The created AssemblyBoolean object 
                |     Example:
                |         This example creates the removeBody AssemblyBoolean object in the
                |         assemblyFeats collection using a body referenced as bodyToRemove contained in
                |         the bodyToRemoveComp component, and positioned with respect to the
                |         positioningComp component.
                | 
                |          Dim removeBody As AssemblyBoolean
                |          Set removeBody = assemblyFeats.AddAssemblyRemove(bodyToRemove,
                |                                                           _
                |                                                           bodyToRemoveComp,
                |                                                           _
                |                                                           positioningComp)

        :param Body i_body:
        :param Product i_body_comp:
        :param Product i_component:
        :rtype: AssemblyFeature
        """
        return AssemblyFeature(
            self.assembly_features.AddAssemblyRemove(
                i_body.com_object,
                i_body_comp.com_object,
                i_component.com_object
            )
        )

    def add_assembly_split(
            self,
            i_splitting_element: Reference,
            i_splitting_elem_comp: Product,
            i_split_side: int,
            i_component: Product) -> AssemblyFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddAssemblySplit(Reference iSplittingElement,
                | Product iSplittingElemComp,
                | CatSplitSide iSplitSide,
                | Product iComponent) As AssemblyFeature
                | 
                |     Creates a new AssemblySplit object.
                | 
                |     Parameters:
                | 
                |         iSplittingElement
                |             The face or plane that will split the current body
                |             
                |         iSplittingElemComp
                |             The component that contains the splitting element 
                |         iSplitSide
                |             The specification for which side of the current body should be kept
                |             at the end of the split operation 
                |         iComponent
                |             The component with respect to which the AssemblySplit object to
                |             create will be positioned 
                | 
                |     Returns:
                |         The created AssemblySplit object 
                |     Example:
                |         This example creates the splitByPlane AssemblySplit object in the
                |         assemblyFeats collection using a plane referenced as splittingPlane contained
                |         in the splittingComp component, in such a way that the material to remove be
                |         the one located in the direction of the splittingPlane normal vector, and
                |         positioned with respect to the positioningComp
                |         component.
                | 
                |          Dim splitByPlane As AssemblySplit
                |          Set splitByPlane = assemblyFeats.AddAssemblySplit(splittingPlane,  _
                |                                                            splittingComp,  
                |                                                            _
                |                                                            catPositiveSide,
                |                                                            _
                |                                                           positioningComp)

        :param Reference i_splitting_element:
        :param Product i_splitting_elem_comp:
        :param int i_split_side: enum cat_split_side
        :param Product i_component:
        :rtype: AssemblyFeature
        """
        return AssemblyFeature(
            self.assembly_features.AddAssemblySplit(
                i_splitting_element.com_object,
                i_splitting_elem_comp.com_object,
                i_split_side,
                i_component.com_object
            )
        )

    def item(self, i_index: cat_variant) -> AssemblyFeature:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AssemblyFeature
                | 
                |     Returns an AssemblyFeature object using its index or its name from the
                |     AssemblyFeatures collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the AssemblyFeature object to retrieve
                |             from the AssemblyFeatures collection. As a numerics, this index is the rank of
                |             the AssemblyFeature object in the collection. The index of the first
                |             AssemblyFeature object in the collection is 1, and the index of the last
                |             AssemblyFeature object is Count. As a string, it is the name you assigned to
                |             the AssemblyFeature object using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved AssemblyFeature object 
                |     Example:
                |         This example retrieves the last item in the assemblyFeats
                |         collection.
                | 
                |          Dim lastAssemblyFeat As AssemblyFeature
                |          Set lastAssemblyFeat = assemblyFeats.Item(assemblyFeats.Count)

        :param cat_variant i_index:
        :rtype: AssemblyFeature
        """
        return AssemblyFeature(self.assembly_features.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an AssemblyFeature object from the AssemblyFeatures
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the AssemblyFeature object to remove from
                |             the AssemblyFeatures collection. As a numerics, this index is the rank of the
                |             AssemblyFeature object in the collection. The index of the first
                |             AssemblyFeature object in the collection is 1, and the index of the last
                |             AssemblyFeature object is Count. As a string, it is the name you assigned to
                |             the AssemblyFeature object using the 
                | 
                |         AnyObject.Name property. 
                |     Example:
                |         This example removes the last AssemblyFeature object in the
                |         assemblyFeats collection.
                | 
                |          assemblyFeats.Remove(assemblyFeats.Count)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.assembly_features.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(assembly_features)
        # #     Dim iIndex (2)
        # #     assembly_features.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AssemblyFeatures(name="{self.name}")'
