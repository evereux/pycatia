#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class AnnotationSetTransformIntoAssemblySet(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnnotationSetTransformIntoAssemblySet
                | 
                | Interface designed to transform an annotation set into an assembly annotation
                | set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_set_transform_into_assembly_set = com_object

    def transform(self, i_assemblyannotation_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Transform(CATBSTR iAssemblyannotationSetName)
                | 
                |     Transforms annotation set into an assembly annotation set.
                | 
                |     Parameters:
                | 
                |         iAssemblyannotationSetName
                |             [in] The name of the assembly annotation transformed If the
                |             iAssemblyannotationSetName is an empty string, the assembly annotation set
                |             keeps the name of the annotation set from which it comes. returns S_OK when
                |             transformation succeeded. returns S_OK when the annotation set is already an
                |             assembly annotation set. otherwise returns E_FAIL.

        :param str i_assemblyannotation_set_name:
        :rtype: None
        """
        return self.annotation_set_transform_into_assembly_set.Transform(i_assemblyannotation_set_name)

    def __repr__(self):
        return f'AnnotationSetTransformIntoAssemblySet(name="{ self.name }")'
