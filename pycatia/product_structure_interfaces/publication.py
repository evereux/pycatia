#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Publication(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Publication
                | 
                | The interface to access a CATIAPublication.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.publication = com_object

    @property
    def relay(self) -> 'Publication':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Relay(Publication iPub) (Write Only)
                | 
                |     Valuates a publication object with another publication object. Role: This
                |     method allows to valuate a publication with an intermediate
                |     one.
                | 
                |     Parameters:
                | 
                |         iPub
                |             The intermediate publication object
                | 
                |             Example: The following example valuates the publication object Pub1
                |             with the publication object Pub2
                | 
                |              Pub1.Relay(Pub2)

        :rtype: Publication
        """

        return self.publication.Relay

    @relay.setter
    def relay(self, publication: 'Publication'):
        """
        :param Publication publication:
        """

        self.publication.Relay = publication.com_object

    @property
    def valuation(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Valuation() As CATBaseDispatch
                | 
                |     Returns published object. Role: This method gives access to the finally
                |     published object.
                | 
                |     Parameters:
                | 
                |         oRef
                |             The final reference of the publication object.
                | 
                |             Example: This example returns the final reference Ref of the
                |             publication object Pub1.
                | 
                |              Dim Ref As Reference
                |              Ref = Pub1.Valuation

        :rtype: AnyObject
        """

        return AnyObject(self.publication.Valuation)

    @valuation.setter
    def valuation(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.publication.Valuation = value

    def __repr__(self):
        return f'Publication(name="{ self.name }")'
