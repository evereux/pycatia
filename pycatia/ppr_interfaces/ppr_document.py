#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activities import Activities
from pycatia.in_interfaces.document import Document
from pycatia.ppr_interfaces.ppr_products import PPRProducts


class PPRDocument(Document):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Document
                |                         PPRDocument
                | 
                | This interface is used to access Processes, Products and
                | Resources.
                | Due to the inherent design restrictions, PPRDocument and another interface ProcessDocument need to
                | be used with care, since the ActiveDocument could be either ProcessDocument or PPRDocument. With that
                | in mind, a good practice of writing more robust VB script is to first tell the real type of document
                | (interface).
                | E.g. The following sentence
                | Dim MyDoc As PPRDocument
                | Set MyDoc = DELMIA.ActiveDocument.PPRDocument
                | could be replaced by the following:
                | Dim MyDoc As PPRDocument
                | Set MyProcDoc = DELMIA.ActiveDocument
                | if (TypeName(MyProcDoc)="ProcessDocument")
                | then MyDoc = MyProcDoc.PPRDocument
                | else MyDoc = DELMIA.ActiveDocument
                | end if
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ppr_document = com_object

    @property
    def processes(self) -> Activities:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Processes() As Activities (Read Only)
                | 
                |     Retrieves the list of Processes as Activities contained in the current
                |     document.
                | 
                |     Returns:
                |         The list of Activities contained in the current document.

        :rtype: Activities
        """

        return Activities(self.ppr_document.Processes)

    @property
    def products(self) -> PPRProducts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Products() As PPRProducts (Read Only)
                | 
                |     Retrieves the list of Products contained in the current
                |     document.
                | 
                |     Returns:
                |         The list of Products contained in the current document.

        :rtype: PPRProducts
        """

        return PPRProducts(self.ppr_document.Products)

    @property
    def resources(self) -> PPRProducts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Resources() As PPRProducts (Read Only)
                | 
                |     Retrieves the list of Resources contained in the current
                |     document.
                | 
                |     Returns:
                |         The list of Resources contained in the current document.

        :rtype: PPRProducts
        """

        return PPRProducts(self.ppr_document.Resources)

    def __repr__(self):
        return f'PprDocument(name="{self.name}")'
