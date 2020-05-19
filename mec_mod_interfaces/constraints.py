#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection
from .constraint import Constraint


class Constraints(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all geometric constraints set on a part, a sketch, or
                | a product.A constraint collection is created with default values for
                | its properties (such as value, orientation, etc.). Use the constraint
                | properties  edition services to set them to appropriate values after
                | constraint creation.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object)
        self.constraints = collection_com_object

    @property
    def broken_constraints_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BrokenConstraintsCount
                | o Property BrokenConstraintsCount(    ) As long
                | 
                | Returns the number of broken constraints from the Constraints
                | collection.
                | Example:
                |   The following example retrieves in BknCstNum the
                |   number of broken constraints from the myListofConstraints collection
                |   of constraints:
                |       BknCstNum = myListofConstraints.BrokenConstraintsCount

        :return: int
        """
        return self.constraints.BrokenConstraintsCount

    @property
    def un_updated_constraints_count(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UnUpdatedConstraintsCount
                | o Property UnUpdatedConstraintsCount(    ) As long
                | 
                | Returns the number of unupdated constraints from the Constraints
                | collection.
                | Example:
                | The following example retrieves in UnUpdCstNum
                | the number of unupdated constraints from the myListofConstraints
                | collection of constraints:
                |   UnUpdCstNum = myListofConstraints.UnUpdatedConstraintsCount

        :return: int
        """
        return self.constraints.UnUpdatedConstraintsCount

    def add_bi_elt_cst(self, i_cst_type, i_first_elem, i_second_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddBiEltCst
                | o Func AddBiEltCst(CatConstraintType iCstType,
                |                    Reference iFirstElem,
                |                    Reference iSecondElem) As Constraint
                | 
                | Creates a new constraint applying to two geometric elements and adds
                | it to the Constraints collection.
                |
                | Parameters:
                | iCstType
                |    The constraint type
                |  
                |  iFirstElem
                |    The first constrained geometric element
                |    The following 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:    
                |  activateLinkAnchor('Boundary','','Boundary') . 
                |      iSecondElem
                |    The second constrained geometric element
                |    The following 
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:    
                |  activateLinkAnchor('Boundary','','Boundary') .
                |
                | Examples:
                | This example adds  the NewCst tangency constraint in a sketch,
                | between the two circles c1 and c2
                | using the value 4 for catCstTypeTangency.
                |   Set newCst = skCstList.AddBiEltCst(4, c1, c2)

        :param int i_cst_type:
        :param Reference() i_first_elem:
        :param Reference() i_second_elem:
        :return: Constraint()
        """
        return Constraint(self.constraints.AddBiEltCst(i_cst_type, i_first_elem.com_object, i_second_elem.com_object))

    def add_mono_elt_cst(self, i_cst_type, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddMonoEltCst
                | o Func AddMonoEltCst(    CatConstraintType    iCstType,
                |                          Reference    iElem) As Constraint
                | 
                | Creates a new constraint applying to a single geometric element and
                | adds it to the Constraints collection.
                |
                | Parameters:
                | iCstType
                |    The constraint type
                |  iElem
                |    The constrained geometric element
                |  The following
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:    
                |  activateLinkAnchor('Boundary','','Boundary') .
                |
                | Examples:
                | This example creates the reference constraint NewCst to a part,
                | stating that
                | the P1 point should remain fixed with respect to the part's
                | origin elements using the value 0 for catCstTypeReference,
                | and adds it to the cstList collection.
                |   Set NewCst = cstList.AddMonoEltCst(0, P1)

        :param int i_cst_type:
        :param Reference() i_elem:
        :return: Constraint()
        """
        return Constraint(self.constraints.AddMonoEltCst(i_cst_type, i_elem.com_object))

    def add_tri_elt_cst(self, i_cst_type, i_first_elem, i_second_elem, i_third_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddTriEltCst
                | o Func AddTriEltCst(    CatConstraintType    iCstType,
                |                         Reference    iFirstElem,
                |                         Reference    iSecondElem,
                |                         Reference    iThirdElem) As Constraint
                | 
                | Creates a new constraint applying to three geometric elements and adds
                | it to the Constraints collection.


                | Parameters:
                | iCstType
                |    The constraint type
                |  
                |  iFirstElem
                |    The first constrained geometric element
                |    The following 
                | 
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:    
                |  activateLinkAnchor('Boundary','','Boundary') . 
                |      iSecondElem
                |    The second constrained geometric element
                |    The following 
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:    
                |  activateLinkAnchor('Boundary','','Boundary') . 
                |      iThirdElem
                |    The third constrained geometric element
                |    The following 
                |  activateLinkAnchor('Boundary','','Boundary')  object is supported:    
                |  activateLinkAnchor('Boundary','','Boundary') .


                | Examples:
                | 
                | 
                | This example adds symCst symmetry constraint in a part,
                | stating that the cylinders cyl1 and cyl2 are
                | symmetric with respect to the plane symPlane using the
                | value 15 for catCstTypeSymmetry.
                |   Set symCst = prtCstList.AddTriEltCst(15, cyl1, cyl2, symPlane)

        :param int i_cst_type:
        :param Reference() i_first_elem:
        :param Reference() i_second_elem:
        :param Reference() i_third_elem:
        :return: Constraint()
        """
        return Constraint(
            self.constraints.AddTriEltCst(i_cst_type,
                                          i_first_elem.com_object,
                                          i_second_elem.com_object,
                                          i_third_elem.com_object)
        )

    def item(self, i_index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As Constraint
                | 
                | Returns a constraint using its index or its name from the Constraints
                | collection.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the constraint to retrieve frm
                |    the collection of constraints.
                |    As a numerics, this index is the rank of the constraint
                |    in the collection.
                |    The index of the first constraint in the collection is 1, and
                |    the index of the last constraint is Count.
                |    As a string, it is the name you assigned to the constraint using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved constraint
                |
                | Examples:
                | This example retrieves in cst1 the first constraint
                | in the collection and in cst2 the constraint Constraint.2.
                |   Set cst1 = cstList.Item(1)
                |   Set cst2 = cstList.Item("Constraint.2")

        :return: Constraint()
        """

        if isinstance(i_index, int):
            i_index += 1

        return Constraint(self.constraints.Item(i_index))

    def remove(self, i_index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(    CATVariant    iIndex)
                | 
                | Removes a constraint from the Constraints collection.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the constraint to remove from the Constraints
                |    collection.
                |    As a numerics, this index is the rank of the constraint
                |    in the collection.
                |    The index of the first constraint in the collection is 1, and
                |    the index of the last constraint is Count.
                |    As a string, it is the name you assigned to the constraint using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property.


                | Examples:
                | This example removes the last constraint in the collection.
                |   cstList.Remove(cstList.Count)

        """

        if isinstance(i_index, int):
            i_index += 1

        return self.constraints.Remove(i_index)

    def __repr__(self):
        return f'Contraints()'
