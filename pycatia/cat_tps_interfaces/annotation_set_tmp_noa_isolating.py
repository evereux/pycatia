#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2026-02-21 14:49:57.443389

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject


class AnnotationSetTmpNoaIsolating(AnyObject):
    """

        Introduced in V5-6R2022.


        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnnotationSetTmpNOAIsolating
                | 
                | Interface for the Technological Product Specification (TPS)
                | objects.
                | Leaf entity in the Design Pattern Composite. TPS modeler enables definition of
                | specification related to surfaces. Temporary interface retrieved using
                | "GetItem" call onto AnnotationSet object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        self.com_object = com_object

    def isolate_links_of_noa(self) -> None:
        """

        Introduced in V5-6R2022.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2026-02-21 14:49:57.443389))
                | Sub IsolateLinksOfNOA()
                |     Method responsible to remove all the links in between ditto NOA and the 2D
                |     instantiated Detail. This call focuses the remaining link in between the ditto
                |     NOA and the 2D Drafting component used for its representation. The handling is
                |     global to the authored content and results in isolating all the existing ditto
                |     NOAs.

        :rtype: None
        """
        self.release_check(
            self.application.system_configuration.release,
            32,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        return self.com_object.IsolateLinksOfNOA()

    def __repr__(self):
        return f'AnnotationSetTmpNoaIsolating(name="{self.name}")'
