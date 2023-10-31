#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relation import Relation


class Check(Relation):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             KnowledgeInterfaces.Relation
                |                                 Check
                | 
                | Represents the check relation.
                | The following example shows how to create a check which checks if a given mass
                | is less than 10kg. The mass should be defined previously:
                | 
                | 	Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim mass As RealParam
                |  Set mass         = part1.Part.Parameters.CreateReal("mass", 5.)
                |  Dim maximummass As Check
                |  Set maximummass = part1.Relations.CreateCheck
                |                     ("maximummass",
                |                      "Ensures that mass is less than 10 kg",
                |                      "mass<10kg")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.check = com_object

    @property
    def diagnosis(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Diagnosis() As boolean (Read Only)
                | 
                |     Returns the check diagnosis. True if the condition of the check is
                |     verified. False otherwise.

        :rtype: bool
        """

        return self.check.Diagnosis

    @property
    def severity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Severity() As long
                | 
                |     Returns or sets the check severity. The severity is the way the check will
                |     manifest itself:
                |     Silent (1)
                |     Information (2)
                |     Warning (3)

        :rtype: int
        """

        return self.check.Severity

    @severity.setter
    def severity(self, value: int):
        """
        :param int value:
        """

        self.check.Severity = value

    def __repr__(self):
        return f'Check(name="{ self.name }")'
