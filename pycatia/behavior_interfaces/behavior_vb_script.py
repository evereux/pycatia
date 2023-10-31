#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.behavior_interfaces.behavior import Behavior
from pycatia.system_interfaces.any_object import AnyObject


class BehaviorVBScript(Behavior):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATBehaviorInterfaces.Behavior
                |                         BehaviorVBScript
                | 
                | Represents the VBScript behavior.
                | Role: The VB script behavior is designed to run a VBScript (or catvbs files) or
                | to reference a VBA project. This interface derives from Behavior and enables
                | the manipulation of the internal variables of the VBScript
                | behavior.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.behavior_vb_script = com_object

    def cancel(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Cancel()
                | 
                |     Inform Client VB has Failed & Has Not operated.
                | 
                |     Example:
                | 
                |     Deprecated:
                |         V5R15 (Not needed)

        :rtype: None
        """
        return self.behavior_vb_script.Cancel()

    def done(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Done()
                | 
                |     Inform Client VB has Successfully Finished.
                | 
                |     Example:
                | 
                |     Deprecated:
                |         V5R15 (Not needed)

        :rtype: None
        """
        return self.behavior_vb_script.Done()

    def get_internal(self, p_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInternal(CATBSTR pName) As AnyObject
                | 
                |     Returns one available io of the behavior. The behavior has to be in
                |     executing mode, otherwise it fails
                | 
                |     Example:
                |         This example retrieves in BehParameter the internal parameter
                |         CATIAReference XXX currently managed by a Behavior
                |         Beh.
                | 
                |          Dim BehParameter as Parameter
                |          Set BehParameter = Beh.GetInternal("XXX")

        :param str p_name:
        :rtype: AnyObject
        """
        return AnyObject(self.behavior_vb_script.GetInternal(p_name))

    def put_internal(self, p_name: str, o_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutInternal(CATBSTR pName,
                | AnyObject oValue)
                | 
                |     provide output of one available io of the behavior. The behavior has to be
                |     in executing mode, otherwise it fails
                | 
                |     Example:
                |         This example assign the BehParameter containing a CATIAReference to the
                |         internal parameter XXX currently managed by a Behavior
                |         Beh.
                | 
                |          Dim BehPower as Parameter
                |          Beh.PutInternal "XXX", BehParameter

        :param str p_name:
        :param AnyObject o_value:
        :rtype: None
        """
        return self.behavior_vb_script.PutInternal(p_name, o_value.com_object)

    def start(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Start()
                | 
                |     Inform Client VB has Started.
                | 
                |     Example:
                | 
                |     Deprecated:
                |         V5R15 (Not needed)

        :rtype: None
        """
        return self.behavior_vb_script.Start()

    def suspend(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Suspend()
                | 
                |     Inform Client VB has not completly finished the task and has to be called
                |     later on
                | 
                |     Example:
                | 
                |     Deprecated:
                |         V5R15 (Not needed)

        :rtype: None
        """
        return self.behavior_vb_script.Suspend()

    def test_internal(self, p_name: str) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TestInternal(CATBSTR pName) As long
                | 
                |     Test for one available output of the behavior. The behavior has to be in
                |     executing mode, otherwise it fails
                | 
                |     Example:
                |         This example test for the value existance of an internal parameter XXX
                |         that may contain or not a CATIAReference currently managed by a Behavior
                |         Beh.
                | 
                |          if (Beh.TestInternal("XXX"))

        :param str p_name:
        :rtype: int
        """
        return self.behavior_vb_script.TestInternal(p_name)

    def __repr__(self):
        return f'BehaviorVBScript(name="{self.name}")'
