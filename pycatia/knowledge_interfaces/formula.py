#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relation import Relation


class Formula(Relation):

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
                |                                 Formula
                | 
                | Represents the formula relation.
                | The following example shows how to create a formula that computes the mass of a
                | cuboid, given its geometric dimensions and the density of the material it is
                | made of:
                | 
                | 	Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim width As RealParam
                |  Set width        = part1.Part.Parameters.CreateReal("width", 1.)  
                |  Dim height As RealParam
                |  Set height       = part1.Part.Parameters.CreateReal("height", 2.)  
                |  Dim depth As RealParam
                |  Set depth        = part1.Part.Parameters.CreateReal("depth", 3.)  
                |  Dim density As RealParam
                |  Set density      = part1.Part.Parameters.CreateReal("density", 1.5)  
                |  Dim mass As RealParam
                |  Set mass         = part1.Part.Parameters.CreateReal("mass", 0.)  
                |  Dim computemass As RealParam
                |  Set computemass = part1.Part.Relations.CreateFormula
                |                     ("computemass",
                |                      "Computes the cuboid mass",  mass,
                |                      "(width*height*depth)*density")
                |   
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.formula = com_object

    def __repr__(self):
        return f'Formula(name="{ self.name }")'
