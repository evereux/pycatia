#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.arrangement_interfaces.arrangement_areas import ArrangementAreas
from pycatia.arrangement_interfaces.arrangement_boundaries import ArrangementBoundaries
from pycatia.arrangement_interfaces.arrangement_item_reservations import ArrangementItemReservations
from pycatia.arrangement_interfaces.arrangement_pathways import ArrangementPathways
from pycatia.arrangement_interfaces.arrangement_rectangles import ArrangementRectangles
from pycatia.arrangement_interfaces.arrangement_runs import ArrangementRuns
from pycatia.system_interfaces.any_object import AnyObject


class ArrangementProduct(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementProduct
                | 
                | Use this object as a factory for Arrangement collection
                | objects.
                | Role: Use this interface to get access to the Arrangement collections (Areas,
                | Rectangles, ItemReservations, Runs, Pathways, Boundaries) aggregated a given
                | Product.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_product = com_object

    @property
    def arrangement_areas(self) -> ArrangementAreas:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementAreas() As ArrangementAreas (Read Only)
                | 
                |     Returns the collection of ArrangementAreas under the current
                |     ArrangementProduct.
                | 
                |     Example:
                |         This example retrieves the ArrangementAreas collection, oArrAreas , for
                |         the objArrProd1 ArrangementProduct object.
                | 
                |          Dim oArrAreas As ArrangementAreas
                |          Set oArrAreas = objArrProd1.Areas

        :rtype: ArrangementAreas
        """

        return ArrangementAreas(self.arrangement_product.ArrangementAreas)

    @property
    def arrangement_boundaries(self) -> ArrangementBoundaries:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementBoundaries() As ArrangementBoundaries (Read
                | Only)
                | 
                |     Returns the collection of ArrangementBoundaries under the current
                |     ArrangementProduct.
                | 
                |     Example:
                |         This example retrieves the ArrangementBoundaries collection,
                |         oArrBoundaries , for the objArrProd1 ArrangementProduct
                |         object.
                | 
                |          Dim oArrBoundaries As ArrangementBoundaries
                |          Set oArrBoundaries = objArrProd1.oArrObjType

        :rtype: ArrangementBoundaries
        """

        return ArrangementBoundaries(self.arrangement_product.ArrangementBoundaries)

    @property
    def arrangement_item_reservations(self) -> ArrangementItemReservations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementItemReservations() As ArrangementItemReservations (Read
                | Only)
                | 
                |     Returns the collection of ArrangementItemReservations under the current
                |     ArrangementProduct.
                | 
                |     Example:
                |         This example retrieves the ArrangementItemReservations collection,
                |         oArrItemReservations , for the objArrProd1 ArrangementProduct
                |         object.
                | 
                |          Dim oArrItemReservations As
                |          ArrangementItemReservations
                |          Set oArrItemReservations = objArrProd1.ItemReservations

        :rtype: ArrangementItemReservations
        """

        return ArrangementItemReservations(self.arrangement_product.ArrangementItemReservations)

    @property
    def arrangement_pathways(self) -> ArrangementPathways:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementPathways() As ArrangementPathways (Read
                | Only)
                | 
                |     Returns the collection of ArrangementPathways under the current
                |     ArrangementProduct.
                | 
                |     Example:
                |         This example retrieves the ArrangementPathways collection, oArrPathways
                |         , for the objArrProd1 ArrangementProduct object.
                | 
                |          Dim oArrPathways As ArrangementPathways
                |          Set oArrPathways = objArrProd1.Pathways

        :rtype: ArrangementPathways
        """

        return ArrangementPathways(self.arrangement_product.ArrangementPathways)

    @property
    def arrangement_rectangles(self) -> ArrangementRectangles:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementRectangles() As ArrangementRectangles (Read
                | Only)
                | 
                |     Returns the collection of ArrangementRectangles under the current
                |     ArrangementProduct.
                | 
                |     Example:
                |         This example retrieves the ArrangementRectangles collection,
                |         oArrRectangles , for the objArrProd1 ArrangementProduct
                |         object.
                | 
                |          Dim oArrRectangles As ArrangementRectangles
                |          Set oArrRectangles = objArrProd1.Rectangles

        :rtype: ArrangementRectangles
        """

        return ArrangementRectangles(self.arrangement_product.ArrangementRectangles)

    @property
    def arrangement_runs(self) -> ArrangementRuns:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ArrangementRuns() As ArrangementRuns (Read Only)
                | 
                |     Returns the collection of ArrangementRuns under the current
                |     ArrangementProduct.
                | 
                |     Example:
                |         This example retrieves the ArrangementRuns collection, oArrRuns , for
                |         the objArrProd1 ArrangementProduct object.
                | 
                |          Dim oArrRuns As ArrangementRuns
                |          Set oArrRuns = objArrProd1.Runs

        :rtype: ArrangementRuns
        """

        return ArrangementRuns(self.arrangement_product.ArrangementRuns)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the Type of the ArrangementProduct in the form of a
                |     String.
                | 
                |     Example:
                |         This example retrieves the type information as a string for the
                |         objArrProd1 ArrangementProduct object.
                | 
                |          Dim oArrObjType  As String
                |          oArrObjType  = objArrProd1.Type

        :rtype: str
        """

        return self.arrangement_product.Type

    def get_technological_object(self, i_application_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTechnologicalObject(CATBSTR iApplicationType) As
                | CATBaseDispatch
                | 
                |     Returns the product's applicative data which type is the given
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iApplicationType
                |             The type of applicative data searched. 
                |         oApplicativeObj
                |             The matched applicative object.
                | 
                |             Example:
                |                 This example retrieves the desired applicative object from the
                |                 objArrProd1 object.
                | 
                |                  Dim objProd   As Product
                |                  objProd  = objArrProd1.GetTechnologicalObject("Product")

        :param str i_application_type:
        :rtype: AnyObject
        """
        return self.arrangement_product.GetTechnologicalObject(i_application_type)

    def set_arrangement_nomenclature(self, i_nomenclature: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetArrangementNomenclature(CATBSTR iNomenclature)
                | 
                |     Sets the nomenclature of the ArrangementProduct.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             operation is successful
                |         E_FAIL
                |             operation failed
                | 
                |         Example:
                |             This example sets the ArrangementNomenclature for objArrProd1
                |             ArrangementProduct object.
                | 
                |              objArrProd1.SetArrangementNomenclature = "Building"

        :param str i_nomenclature:
        :rtype: None
        """
        return self.arrangement_product.SetArrangementNomenclature(i_nomenclature)

    def set_auto_name(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoName()
                | 
                |     Causes the name of the ArrangementProduct automatically.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             operation is successful
                |         E_FAIL
                |             operation failed
                | 
                |         Example:
                |             This example shows how the automatic naming of the objArrProd1
                |             ArrangementProduct object can be done.
                | 
                |              objArrProd1.SetAutoName

        :rtype: None
        """
        return self.arrangement_product.SetAutoName()

    def __repr__(self):
        return f'ArrangementProduct(name="{self.name}")'
