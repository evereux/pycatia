#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.kinematics_interfaces.joint import Joint
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Joints(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Joints
                | 
                | A collection of all Joint entities currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Joint)
        self.joints = com_object

    def add(self) -> Joint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As Joint
                | 
                |     Create a new Joint and adds it to the Joints collection.
                | 
                |     Returns:
                |         The created Joint 
                |     Example:
                |         This example creates a new Joint in the TheJoints
                |         collection.
                | 
                |             Dim NewJoint As Joint
                |             Set NewJoint = TheJoints.Add()

        :rtype: Joint
        """
        return Joint(self.joints.Add())

    def item(self, i_index: cat_variant) -> Joint:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Joint
                | 
                |     Returns a Joint using its index or its name from the Joints
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Joint to retrieve from the collection
                |             of Joints. As a numerics, this index is the rank of the Joint in the
                |             collection. The index of the first Joint in the collection is 1, and the index
                |             of the last Joint is Count. As a string, it is the name you assigned to the
                |             Joint using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Joint 
                |     Example:
                |         This example returns in ThisJoint the third Joint in the collection,
                |         and in ThatJoint the Joint named MyJoint.
                | 
                |          Dim ThisJoint As Joint
                |          Set ThisJoint = TheJoints.Item(3)
                |          Dim ThatJoint As Joint
                |          Set ThatJoint = CATIA.Joints.Item("MyJoint")

        :param cat_variant i_index:
        :rtype: Joint
        """
        return Joint(self.joints.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Remove a Joint from the Joints collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Joint to retrieve from the collection
                |             of Joints. As a numerics, this index is the rank of the Joint in the
                |             collection. The index of the first Joint in the collection is 1, and the index
                |             of the last Joint is Count. As a string, it is the name you assigned to the
                |             Joint. 
                | 
                |     Returns:
                |         Nothing 
                |     Example:
                |         The following example removes the tenth Joint and the Joint named
                |         JointTwo from the TheJoints collection.
                | 
                |             TheJoints.Remove(10)
                |             TheJoints.Remove("JointTwo")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.joints.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(joints)
        # #     Dim iIndex (2)
        # #     joints.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Joints(name="{self.name}")'
