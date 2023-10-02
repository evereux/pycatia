#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_fastener_interfaces.fastener import Fastener


class CurveFastener(Fastener):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBFastenerInterfaces.Fastener
                |                         CurveFastener
                | 
                | Interface DELMIACurveFastener DELMIACurveFastener represent body in white
                | fasteners of type curve.
                | Following kind of curve fasteners are by default available with DPM - Fastening
                | Process Planner Adhesive Curve, Arc Weld, Sealant Curve, Glue
                | Bead.
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.curve_fastener = com_object

    def __repr__(self):
        return f'CurveFastener(name="{self.name}")'
