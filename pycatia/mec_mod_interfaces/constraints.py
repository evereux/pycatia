#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
from typing import Iterator

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.constraint import Constraint
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Constraints(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Constraints
                |
                | A collection of all geometric constraints set on a part, a sketch, or a
                | product.
                | A constraint collection is created with default values for its properties (such
                | as value, orientation, etc.). Use the constraint properties edition services to
                | set them to appropriate values after constraint creation.
                |
                | See also:
                |     Constraint

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Constraint)
        self.constraints = com_object

    @property
    def broken_constraints_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BrokenConstraintsCount() As long (Read Only)
                | 
                |     Returns the number of broken constraints from the Constraints
                |     collection.
                | 
                |     Example:
                |         The following example retrieves in BknCstNum the number of broken
                |         constraints from the myListofConstraints collection of
                |         constraints:
                | 
                |          BknCstNum = myListofConstraints.BrokenConstraintsCount

        :rtype: int
        """

        return self.constraints.BrokenConstraintsCount

    @property
    def un_updated_constraints_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UnUpdatedConstraintsCount() As long (Read Only)
                | 
                |     Returns the number of unupdated constraints from the Constraints
                |     collection.
                | 
                |     Example:
                |         The following example retrieves in UnUpdCstNum the number of unupdated
                |         constraints from the myListofConstraints collection of
                |         constraints:
                | 
                |          UnUpdCstNum = myListofConstraints.UnUpdatedConstraintsCount

        :rtype: int
        """

        return self.constraints.UnUpdatedConstraintsCount

    def add_bi_elt_cst(self, i_cst_type: int, i_first_elem: Reference, i_second_elem: Reference) -> Constraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddBiEltCst(CatConstraintType iCstType,
                | Reference iFirstElem,
                | Reference iSecondElem) As Constraint
                | 
                |     Creates a new constraint applying to two geometric elements and adds it to
                |     the Constraints collection.
                |
                |     Parameters:
                |
                |         iCstType
                |             The constraint type
                |         iFirstElem
                |             The first constrained geometric element
                |             The following
                | 
                |         Boundary object is supported: Boundary.
                |     iSecondElem
                |         The second constrained geometric element
                |         The following Boundary object is supported: Boundary.
                |
                | Example:
                |     This example adds the NewCst tangency constraint in a sketch, between the
                |     two circles c1 and c2 using the value 4 for
                |     catCstTypeTangency.
                |
                |      Set newCst = skCstList.AddBiEltCst(4, c1, c2)

        :param int i_cst_type: enum cat_constraint_type
        :param Reference i_first_elem:
        :param Reference i_second_elem:
        :rtype: Constraint
        """
        return Constraint(self.constraints.AddBiEltCst(i_cst_type, i_first_elem.com_object, i_second_elem.com_object))

    def add_mono_elt_cst(self, i_cst_type: int, i_elem: Reference) -> Constraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddMonoEltCst(CatConstraintType iCstType,
                | Reference iElem) As Constraint
                | 
                |     Creates a new constraint applying to a single geometric element and adds it
                |     to the Constraints collection.
                |
                |     Parameters:
                |
                |         iCstType
                |             The constraint type
                |         iElem
                |             The constrained geometric element
                |             The following
                |
                |         Boundary object is supported: Boundary.
                |
                | Example:
                |     This example creates the reference constraint NewCst to a part, stating
                |     that the P1 point should remain fixed with respect to the part's origin
                |     elements using the value 0 for catCstTypeReference, and adds it to the cstList
                |     collection.
                |
                |      Set NewCst = cstList.AddMonoEltCst(0, P1)

        :param int i_cst_type: enum cat_constraint_type
        :param Reference i_elem:
        :rtype: Constraint
        """
        return Constraint(self.constraints.AddMonoEltCst(i_cst_type, i_elem.com_object))

    def add_tri_elt_cst(self, i_cst_type: int, i_first_elem: Reference, i_second_elem: Reference,
                        i_third_elem: Reference) -> Constraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddTriEltCst(CatConstraintType iCstType,
                | Reference iFirstElem,
                | Reference iSecondElem,
                | Reference iThirdElem) As Constraint
                | 
                |     Creates a new constraint applying to three geometric elements and adds it
                |     to the Constraints collection.
                |
                |     Parameters:
                |
                |         iCstType
                |             The constraint type
                |         iFirstElem
                |             The first constrained geometric element
                |             The following
                | 
                |         Boundary object is supported: Boundary.
                |     iSecondElem
                |         The second constrained geometric element
                |         The following Boundary object is supported: Boundary.
                |     iThirdElem
                |         The third constrained geometric element
                |         The following Boundary object is supported: Boundary.
                | 
                | Example:
                |     This example adds symCst symmetry constraint in a part, stating that the
                |     cylinders cyl1 and cyl2 are symmetric with respect to the plane symPlane using
                |     the value 15 for catCstTypeSymmetry.
                |
                |      Set symCst = prtCstList.AddTriEltCst(15, cyl1, cyl2, symPlane)

        :param int i_cst_type: enum cat_constraint_type
        :param Reference i_first_elem:
        :param Reference i_second_elem:
        :param Reference i_third_elem:
        :rtype: Constraint
        """
        return Constraint(self.constraints.AddTriEltCst(i_cst_type, i_first_elem.com_object, i_second_elem.com_object,
                                                        i_third_elem.com_object))

    def item(self, i_index: cat_variant) -> Constraint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Constraint
                | 
                |     Returns a constraint using its index or its name from the Constraints
                |     collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index or the name of the constraint to retrieve frm the
                |             collection of constraints. As a numerics, this index is the rank of the
                |             constraint in the collection. The index of the first constraint in the
                |             collection is 1, and the index of the last constraint is Count. As a string, it
                |             is the name you assigned to the constraint using the
                |
                | 
                |         AnyObject.Name property.
                |     Returns:
                |         The retrieved constraint
                |     Example:
                |         This example retrieves in cst1 the first constraint in the collection
                |         and in cst2 the constraint Constraint.2.
                |
                |          Set cst1 = cstList.Item(1)
                |          Set cst2 = cstList.Item("Constraint.2")

        :param cat_variant i_index:
        :rtype: Constraint
        """
        return Constraint(self.constraints.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a constraint from the Constraints collection.
                |
                |     Parameters:
                |
                |         iIndex
                |             The index or the name of the constraint to remove from the
                |             Constraints collection. As a numerics, this index is the rank of the constraint
                |             in the collection. The index of the first constraint in the collection is 1,
                |             and the index of the last constraint is Count. As a string, it is the name you
                |             assigned to the constraint using the
                |
                |         AnyObject.Name property.
                |
                | Example:
                |     This example removes the last constraint in the
                |     collection.
                | 
                |      cstList.Remove(cstList.Count)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.constraints.Remove(i_index)

    def __getitem__(self, n: int) -> Constraint:
        if (n + 1) > self.count:
            raise StopIteration

        return Constraint(self.constraints.Item(n + 1))

    def __iter__(self) -> Iterator[Constraint]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Constraints(name="{self.name}")'
