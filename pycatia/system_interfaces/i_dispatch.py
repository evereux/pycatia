#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.i_unknown import IUnknown


class IDispatch(IUnknown):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     IDispatch
                | 
                | Base interface for all Automation interfaces.
                | Role: All Automation interfaces derive from IDispatch which replaces for UNIX
                | the native Microsoft(R) IDispatch interface. This interface supplies basic
                | methods to be Microsoft(R) Automation compliant.
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'IDispatch()'
