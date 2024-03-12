#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator
from typing import TYPE_CHECKING

from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.in_interfaces.reference import Reference


class Publications(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Publications
                | 
                | The collection of the Product publications.
                | A Product object can aggregate one or zero Publications
                | collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.publications = com_object

    def add(self, i_public_name: str) -> Publication:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CATBSTR iPublicName) As Publication
                | 
                |     Adds a publication object to the product and returns a pointer to the
                |     publication object.
                | 
                |     Parameters:
                | 
                |         iPublicName
                |             The name of the publication 
                |         oPub
                |             The publication object
                | 
                |             Example: The following example adds a new publication object with
                |             the name "PubName" to the product and returns the publication object
                |             Pub1.
                | 
                |              Dim Prod1 As Product
                |              Set Pub1 = Prod1.Add(PubName)

        :param str i_public_name:
        :rtype: Publication
        """
        return Publication(self.publications.Add(i_public_name))

    def item(self, i_identifier: cat_variant) -> Publication:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIdentifier) As Publication
                | 
                |     Returns the publication object corresponding to the given publication
                |     name.
                | 
                |     Parameters:
                | 
                |         iIdentifier
                |             The name of the publication 
                |         oPub
                |             The publication object
                | 
                |             Example: The following example returns Pub1 publication object from
                |             the product referencing the published name PubId.
                | 
                |              Dim Prod1 As Product
                |              Set Pub1 = Prod1.Item(PubId)

        :param cat_variant i_identifier:
        :rtype: Publication
        """
        return Publication(self.publications.Item(i_identifier))

    def remove(self, i_identifier: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATBSTR iIdentifier)
                | 
                |     Removes a publication from the product.
                | 
                |     Parameters:
                | 
                |         iIdentifier
                |             The name of the publication
                | 
                |             Example: The following example removes the publication object
                |             corresponding to the name PubId.
                | 
                |              Dim Prod1 As Product
                |              Prod1.Remove(PubId)

        :param str i_identifier:
        :rtype: None
        """
        return self.publications.Remove(i_identifier)

    def set_direct(self, i_identifier: cat_variant, i_pointed: 'Reference') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDirect(CATVariant iIdentifier,
                | Reference iPointed)
                | 
                |     Valuates a publication object directly with the object it
                |     publishes.
                | 
                |     Parameters:
                | 
                |         iIdentifier
                |             The name of the publication 
                |         iPointed
                |             The published object
                |             The following 
                | 
                |         Boundary objects is supported: Boundary
                | 
                |         Example: The following example valuates the publication object of
                |         product Prod1 having the name PubId with the reference object
                |         RefObject.
                | 
                |          Dim Prod1 As Product
                |          Prod1.SetDirect(PubId,RefObject)

        :param cat_variant i_identifier:
        :param Reference i_pointed:
        :rtype: None
        """
        return self.publications.SetDirect(i_identifier, i_pointed.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_direct'
        # # vba_code = """
        # # Public Function set_direct(publications)
        # #     Dim iIdentifier (2)
        # #     publications.SetDirect iIdentifier
        # #     set_direct = iIdentifier
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_relay(self, i_identifier: cat_variant, i_relayer: 'Publications', i_name_in_relay: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetRelay(CATVariant iIdentifier,
                | Publications iRelayer,
                | CATVariant iNameInRelay)
                | 
                |     Valuates a publication object with another publication
                |     object.
                | 
                |     Parameters:
                | 
                |         iIdentifier
                |             The name of the publication to be valuated 
                |         iRelayer
                |             The product aggregating the valuating intermediate publication
                |             object 
                |         iNameInRelay
                |             The name of the valuating publication object
                | 
                |             Example: The following example valuates the publication object of
                |             product Prod1 having the name PubId1 with the publication object of product
                |             Prod2 having the name PubId2.
                | 
                |              Dim Prod1 As Product
                |              Prod1.SetRelay(PubId1,Prod2,PubId2)

        :param cat_variant i_identifier:
        :param Publications i_relayer:
        :param cat_variant i_name_in_relay:
        :rtype: None
        """
        return self.publications.SetRelay(i_identifier, i_relayer.com_object, i_name_in_relay)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relay'
        # # vba_code = """
        # # Public Function set_relay(publications)
        # #     Dim iIdentifier (2)
        # #     publications.SetRelay iIdentifier
        # #     set_relay = iIdentifier
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __getitem__(self, n: int) -> Publication:
        if (n + 1) > self.count:
            raise StopIteration

        return Publication(self.publications.Item(n + 1))

    def __iter__(self) -> Iterator[Publication]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Publications(name="{self.name}")'
