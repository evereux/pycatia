#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from typing import Iterator

from pycatia.in_interfaces.reference import Reference
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.collection import Collection
from pycatia.cat_tps_interfaces.user_surface import UserSurface
from pycatia.types.general import cat_variant


class UserSurfaces(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     UserSurfaces

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_surfaces = com_object

    def generate(self, i_support: Reference) -> UserSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Generate(Reference iSupport) As UserSurface
                | 
                |     Use this method in a Part. Creates a new user surface and adds it to the
                |     Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The first reference that will support the user surface
                |             
                | 
                |     Returns:
                |         The created user surface 
                |     Example:
                |         The following example creates a user surface names NewUserSurf from the
                |         reference Ref in the Surfaces collection of the rootPart part in the partDoc
                |         part document.
                | 
                |          Set rootPart = partDoc.Part
                |          Set NewUserSurf = rootPart.UserSurfaces.Add(Ref)

        :param Reference i_support:
        :rtype: UserSurface
        """
        return UserSurface(self.user_surfaces.Generate(i_support.com_object))

    def generate_in_a_product_ctx(self, i_product: Product, i_prod_inst: Product, i_support: Reference) -> UserSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GenerateInAProductCtx(Product iProduct,
                | Product iProdInst,
                | Reference iSupport) As UserSurface
                | 
                |     Use this method in a Product. Creates a new user surface and adds it to the
                |     Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The level on which you want to create annotation (part or product).
                |             
                |         iProdInst
                |             The product instance where there is the geometry. 
                |         iSupport
                |             The first reference that will support the user surface
                |             
                | 
                |     Returns:
                |         The created user surface

        :param Product i_product:
        :param Product i_prod_inst:
        :param Reference i_support:
        :rtype: UserSurface
        """
        return UserSurface(self.user_surfaces.GenerateInAProductCtx(i_product.com_object, i_prod_inst.com_object,
                                                                    i_support.com_object))

    def item(self, i_index: cat_variant) -> UserSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As UserSurface
                | 
                |     Find a user surface inside the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the users surface in the collection
                |             
                | 
                |     Returns:
                |         The user surface that is in the iIndex position in the collection

        :param cat_variant i_index:
        :rtype: UserSurface
        """
        return UserSurface(self.user_surfaces.Item(i_index))

    def make_user_surface_node(self, i_first_user_surf: UserSurface, i_second_user_surf: UserSurface) -> UserSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func MakeUserSurfaceNode(UserSurface iFirstUserSurf,
                | UserSurface iSecondUserSurf) As UserSurface
                | 
                |     Usefull to create a User Surface Node from two others User Surface. Creates
                |     a new user surface and adds it to the Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iFirstUserSurf
                |             The first User Surface to use. 
                |         iSecondUserSurf
                |             The second User Surface to use. 
                | 
                |     Returns:
                |         The created user surface

        :param UserSurface i_first_user_surf:
        :param UserSurface i_second_user_surf:
        :rtype: UserSurface
        """
        return UserSurface(
            self.user_surfaces.MakeUserSurfaceNode(i_first_user_surf.com_object, i_second_user_surf.com_object))

    def make_user_surface_node_2(self, i_list_of_user_surfaces: tuple) -> UserSurface:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func MakeUserSurfaceNode2(CATSafeArrayVariant iListOfUserSurfaces) As
                | UserSurface
                | 
                |     Usefull to create a User Surface Node from a list of User Surfaces. Creates
                |     a new user surface and adds it to the Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iListOfUserSurfaces
                |             The list User Surfaces to use. 
                | 
                |     Returns:
                |         The created user surface

        :param tuple i_list_of_user_surfaces:
        :rtype: UserSurface
        """
        return UserSurface(self.user_surfaces.MakeUserSurfaceNode2(i_list_of_user_surfaces))

    def __getitem__(self, n: int) -> UserSurface:
        if (n + 1) > self.count:
            raise StopIteration

        return UserSurface(self.user_surfaces.Item(n + 1))

    def __iter__(self) -> Iterator[UserSurface]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'UserSurfaces(name="{self.name}")'
