#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relation import Relation


class Rule(Relation):

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
                |                                 Rule
                | 
                | Represents the program relation.
                | The following example shows how to create a program that selects a depth with
                | respect to a mass value. The depth and mass parameters should exist before the
                | creation of the program (also called Rule) object.
                | 
                | 	Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim mass As RealParam
                |  Set mass         = part1.Part.Parameters.CreateReal("mass", 5.)
                |  Dim depth As RealParam
                |  Set depth        = part1.Part.Parameters.CreateReal("depth", 0.)
                |  Dim selectdepth As Relation
                |  Set selectdepth = part1.Part.Relations.CreateProgram
                |                     ("select_depth",
                |                      "Select depth with respect to mass", 
                |                      "if (mass>2kg) { depth=2mm } else { depth=1mm
                |                      }")
                |  
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rule = com_object

    def __repr__(self):
        return f'Rule(name="{ self.name }")'
