#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.i_dispatch import IDispatch


class CATBaseUnknown(IDispatch):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         CATBaseUnknown
                | 
                | Base class for creating interfaces and for implementing
                | interfaces.
                | Role: CATBaseUnknown supplies the infrastructure and the basic mechanisms to
                | create interface abstract classes and to manage interface pointers. It is also
                | the base class for classes which implements interfaces and for their extension
                | classes because it supplies the code for the interface methods QueryInterface,
                | AddRef and Release.
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'CatBaseUnknown()'
