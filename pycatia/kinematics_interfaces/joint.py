#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class Joint(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Joint
                | 
                | Interface to manage the Joint object.
                | Depending on their type, joints have parameters or not, representing length or
                | angle:
                | Joint type 	Parameter1 	Parameter2
                | Revolute 	Angle 	
                | Prismatic 	Length 	
                | Cylindrical 	Length 	Angle
                | Screw 	Length 	Angle
                | Gear 	Angle 	Angle
                | Rack 	Length 	Angle
                | Cable 	Length 	Length
                | PointOnCurve 	Length 	
                | RollCurve 	Length 	
                | 
                | Each parameter can have a lower and/or an upper limit.
                | 
                | Methods are provided to set, unset and return the limits for each
                | parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.joint = com_object

    def unset_lower_limit1(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnsetLowerLimit1()
                | 
                |     Unsets the lower limit of the joint, for the first
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iLimitValue
                |             The value for the limit When reading, an error is returned if the
                |             joint type has no such parameter, or if the limit is
                |             unset.

        :rtype: None
        """
        return self.joint.UnsetLowerLimit1()

    def unset_lower_limit2(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnsetLowerLimit2()
                | 
                |     Unsets the lower limit of the joint, for the second
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iLimitValue
                |             The value for the limit

        :rtype: None
        """
        return self.joint.UnsetLowerLimit2()

    def unset_upper_limit1(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnsetUpperLimit1()
                | 
                |     Unsets the upper limit of the joint, for the first
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iLimitValue
                |             The value for the limit

        :rtype: None
        """
        return self.joint.UnsetUpperLimit1()

    def unset_upper_limit2(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnsetUpperLimit2()
                | 
                |     Unsets the upper limit of the joint, for the second
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iLimitValue
                |             The value for the limit

        :rtype: None
        """
        return self.joint.UnsetUpperLimit2()

    def __repr__(self):
        return f'Joint(name="{ self.name }")'
