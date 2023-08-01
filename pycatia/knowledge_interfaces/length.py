#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.dimension import Dimension


class Length(Dimension):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         KnowledgeInterfaces.RealParam
                |                             KnowledgeInterfaces.Dimension
                |                                 Length
                | 
                | Represents the length parameter.
                | The following example shows how to create it:
                | 
                |  Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart") 
                |  Dim Width As Length
                |  Set width   = part1.Part.Parameters.CreateDimension("width", "LENGTH", 20.)
                |  
                | 
                | By default the units are the default units of the IS of units.
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.length = com_object

    def __repr__(self):
        return f'Length(name="{ self.name }")'
