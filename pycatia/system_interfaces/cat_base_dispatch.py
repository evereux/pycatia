#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.cat_base_unknown import CATBaseUnknown


class CATBaseDispatch(CATBaseUnknown):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             CATBaseDispatch
                | 
                | Base class for Automation interfaces.
                | Role: All Automation interfaces must inherit from the CATBaseDispatch
                | interface. They usually do not inherit directly from CATBaseDispatch, but
                | rather from one of its subclasses: AnyObject for individual objects or
                | Collection for collection objects. Some methods may however have arguments of
                | type CATBaseDispatch when they accept both individual objects or collection
                | objects. The interface provides no functionalities per se.
                | 
                | Copyright © 1999-2011, Dassault Systèmes. All rights reserved.
    
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'CatBaseDispatch()'
