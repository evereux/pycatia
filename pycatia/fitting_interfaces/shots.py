#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.fitting_interfaces.shot import Shot
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Shots(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Shots
                | 
                | The collection of all shot objects contained in the current
                | sampled.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Shot)
        self.shots = com_object

    def append(self, i_shot: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Append(CATBaseDispatch iShot)
                | 
                |     Adds a shot to the end of the shots collection.
                | 
                |     Parameters:
                | 
                |         iShot
                |             The shot to be added 
                |         Example:
                |             The following example adds a shot (called myShot to the shots
                |             collection.
                | 
                |              Shots.Append (myShot)

        :param AnyObject i_shot:
        :rtype: None
        """
        return self.shots.Append(i_shot.com_object)

    def create_shot(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateShot() As CATBaseDispatch
                | 
                |     Creates a new shot and adds it to the Shots collection.
                | 
                |     Returns:
                |         The created shot 
                |     Example:
                |         The following example creates a shot newShot in the Shots
                |         collection.
                | 
                |          Dim newShot
                |          Set newShot = Shots.CreateShot

        :rtype: AnyObject
        """
        return self.shots.CreateShot()

    def create_specific_shot(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateSpecificShot(CATBSTR iType) As CATBaseDispatch
                | 
                |     Creates a new shot of a specific type and adds it to the Shots
                |     collection.
                | 
                |     Parameters:
                | 
                |         iType
                |             Specifies the type of the shot to be created. The legal values are
                |             FITShotPoints, FITShotDouble, FITShotSimple and FITShotGeneric. These different
                |             types correspond to the need of creating different shots for different types of
                |             objects. 
                | 
                |     Returns:
                |         The created Shot 
                |     Example:
                |         The following example creates a shot shot in the Shots
                |         collection.
                | 
                |          Set newShots = Shots.CreateShot (FITSHOTDouble)

        :param str i_type:
        :rtype: AnyObject
        """
        return self.shots.CreateSpecificShot(i_type)

    def insert_after(self, i_index: int, i_shot: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub InsertAfter(short iIndex,
                | CATBaseDispatch iShot)
                | 
                |     Adds a shot to a specific location to the shots
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The value of the location of an already existing shot. Then when
                |             inserting a new shot, it will be placed after it. It is a positive integer,
                |             with the range of 1 to the value of the last shot.
                |             
                |         iShot
                |             The shot to be added 
                |         Example:
                |             The following example inserts a shot after the second
                |             shot.
                | 
                |              Shots.InsertAfter (2, myShot)

        :param int i_index:
        :param AnyObject i_shot:
        :rtype: None
        """
        return self.shots.InsertAfter(i_index, i_shot.com_object)

    def item(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As CATBaseDispatch
                | 
                |     Returns a shot using its index from the colection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the item to retrieve from the collection of shots.
                |             Numerically, the index value corresponds to the rank of the shot in the
                |             collection (ie. the first is 1, second is 2, ...).
                |             
                | 
                |     Returns:
                |         The retrieved Shot 
                |     Example:
                |         The following example retrieves the second shot from the Shots
                |         collection.
                | 
                |          Dim myShot
                |          Set myShot = myShots.Item (2)

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return self.shots.Item(i_index)

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a shot from the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the shot to remove from the collection of the shots.
                |             Numerically, the index value corresponds to the rank of the shot in the
                |             collection (ie. the first is 1, second is 2, ...).
                |             
                |         Example:
                |             The following example removes the third shot from the Shots
                |             collection of the active document.
                | 
                |              Shots.Remove (3)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.shots.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(shots)
        # #     Dim iIndex (2)
        # #     shots.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Shots(name="{self.name}")'
