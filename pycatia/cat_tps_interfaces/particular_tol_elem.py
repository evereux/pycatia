#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ParticularTolElem(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ParticularTolElem
                | 
                | Interface for accessing particular geometry of the toleranced
                | element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.particular_tol_elem = com_object

    @property
    def particular_geometry(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ParticularGeometry() As CATBSTR (Read Only)
                | 
                |     Retrieves particular geometry of the toleranced element.
                | 
                |     Parameters:
                | 
                |         oPartGeom
                |             : Not Defined CenterElement Surface Unsupported

        :rtype: str
        """

        return self.particular_tol_elem.ParticularGeometry

    def __repr__(self):
        return f'ParticularTolElem(name="{ self.name }")'
