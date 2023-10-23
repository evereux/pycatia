#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchPostReplace(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchPostReplace
                | 
                | Manage post component replacement behaviors.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_post_replace = com_object

    def post_replace_text(self, i_new_sch_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PostReplaceText(AnyObject iNewSchObject)
                | 
                |     Handle associated annotations after replace.
                | 
                |     Parameters:
                | 
                |         iNewSchObject
                |             Pointer to the object that is replacing 'this' object.
                |             
                |     Example:
                |
                |          Dim objThisIntf As SchPostReplace
                |          Dim objArg1 As AnyObject
                |           ...
                |          objThisIntf.PostReplaceTextobjArg1

        :param AnyObject i_new_sch_object:
        :rtype: None
        """
        return self.sch_post_replace.PostReplaceText(i_new_sch_object.com_object)

    def __repr__(self):
        return f'SchPostReplace(name="{self.name}")'
