#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.line import Line


class HybridShapeLineExplicit(Line):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineExplicit
                | 
                | Represents the hybrid shape line explicit feature object.
                | Role: Declare hybrid shape line explicit feature object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewLineDatum 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_explicit = com_object

    def __repr__(self):
        return f'HybridShapeLineExplicit(name="{self.name}")'
