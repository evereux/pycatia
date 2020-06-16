#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Chamfer(DressUpShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Chamfer
                | 
                | Represents the chamfer shape.
                | A chamfer is made up of a list of geometrical elements to process, such as
                | faces, and is defined using a couple of parameters, such as two lengths, or a
                | length and an angle.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.chamfer = com_object

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Angle() As Angle (Read Only)
                | 
                |     Returns the chamfer angle. This is valid only if the chamfer is defined
                |     using a length and an angle, that is if the chamfer definition mode
                |     CatChamferMode is set to catLengthAngleChamfer.
                | 
                |     Example:
                |         The following example returns in angle the angle of the firstChamfer
                |         chamfer:
                | 
                |          Set angle = firstChamfer.Angle

        :return: Angle
        """

        return Angle(self.chamfer.Angle)

    @property
    def elements_to_chamfer(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ElementsToChamfer() As References (Read Only)
                | 
                |     Returns the collection of geometrical elements to be
                |     chamfered.
                | 
                |     Example:
                |         The following example returns in list the list of elements of the
                |         firstChamfer chamfer:
                | 
                |          Set list = firstChamfer.ElementsToChamfer

        :return: References
        """

        return References(self.chamfer.ElementsToChamfer)

    @property
    def length1(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Length1() As Length (Read Only)
                | 
                |     Returns the chamfer first length. This is the first length if the chamfer
                |     is defined by two lengths, or the chamfer if the chamfer is defined by a
                |     length and an angle.
                | 
                |     Example:
                |         The following example returns in length1 the first length of the
                |         firstChamfer chamfer:
                | 
                |          Set length1 = firstChamfer.Length1

        :return: Length
        """

        return Length(self.chamfer.Length1)

    @property
    def length2(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Length2() As Length (Read Only)
                | 
                |     Returns the chamfer second length. This is valid only if the chamfer is
                |     defined using two lengths, that is if the chamfer definition mode
                |     CatChamferMode is set to catTwoLengthChamfer.
                | 
                |     Example:
                |         The following example returns in length2 the second length of the
                |         firstChamfer chamfer:
                | 
                |          Set length2 = firstChamfer.Length2

        :return: Length
        """

        return Length(self.chamfer.Length2)

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Mode() As CatChamferMode
                | 
                |     Returns or sets the chamfer definition mode. The chamfer definition mode
                |     enables the chamfer to be defined using either two lengths or a length and an
                |     angle.
                | 
                |     Example:
                |         The following example returns in mode how the parameters of the
                |         firstChamfer chamfer are defined, and then sets it to
                |         catTwoLengthChamfer:
                | 
                |          Set mode = firstChamfer.Mode
                |          firstChamfer.Mode = catTwoLengthChamfer

        :return: enum cat_chamfer_mode
        """

        return self.chamfer.Mode

    @mode.setter
    def mode(self, value):
        """
        :param enum cat_chamfer_mode value:
        """

        self.chamfer.Mode = value

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Orientation() As CatChamferOrientation
                | 
                |     Returns or sets the chamfer orientation.
                | 
                |     Example:
                |         The following example returns in orient the orientation mode of the
                |         firstChamfer chamfer, and then sets it to
                |         catReverseChamfer:
                | 
                |          Set orient = firstChamfer.Orientation
                |          firstChamfer.Orientation = catReverseChamfer

        :return: enum cat_chamfer_orientation
        """

        return self.chamfer.Orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param enum cat_chamfer_orientation value:
        """

        self.chamfer.Orientation = value

    @property
    def propagation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Propagation() As CatChamferPropagation
                | 
                |     Returns or sets the propagation mode of the geometrical elements to be
                |     chamfered.
                | 
                |     Example:
                |         The following example returns in prop the propagation mode of the
                |         firstChamfer chamfer, and then sets it to
                |         catMinimalChamfer:
                | 
                |          Set prop = firstChamfer.Propagation
                |          firstChamfer.Propagation = catMinimalChamfer

        :return: enum cat_chamfer_propagation
        """

        return self.chamfer.Propagation

    @propagation.setter
    def propagation(self, value):
        """
        :param enum cat_chamfer_propagation value:
        """

        self.chamfer.Propagation = value

    def add_element_to_chamfer(self, i_element_to_chamfer):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddElementToChamfer(Reference iElementToChamfer)
                | 
                |     Adds a new geometrical element to be chamfered.
                | 
                |     Parameters:
                | 
                |         iElementToChamfer
                |             The new element to be chamfered
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example adds the new element element to be chamfered for the
                |     firstChamfer chamfer:
                | 
                |      firstChamfer.AddElementToChamfer(element)

        :param Reference i_element_to_chamfer:
        :return: None
        """
        return self.chamfer.AddElementToChamfer(i_element_to_chamfer.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element_to_chamfer'
        # # vba_code = """
        # # Public Function add_element_to_chamfer(chamfer)
        # #     Dim iElementToChamfer (2)
        # #     chamfer.AddElementToChamfer iElementToChamfer
        # #     add_element_to_chamfer = iElementToChamfer
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_element_to_chamfer(self, i_element_to_withdraw):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub WithdrawElementToChamfer(Reference iElementToWithdraw)
                | 
                |     Withdraws a geometrical element from those to be
                |     chamfered.
                | 
                |     Parameters:
                | 
                |         iElementToWithdraw
                |             The existing element to withdraw
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example withdraws an existing element element to be chamfered
                |     from the firstChamfer chamfer:
                | 
                |      firstChamfer.WithdrawElementToChamfer(element)

        :param Reference i_element_to_withdraw:
        :return: None
        """
        return self.chamfer.WithdrawElementToChamfer(i_element_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_element_to_chamfer'
        # # vba_code = """
        # # Public Function withdraw_element_to_chamfer(chamfer)
        # #     Dim iElementToWithdraw (2)
        # #     chamfer.WithdrawElementToChamfer iElementToWithdraw
        # #     withdraw_element_to_chamfer = iElementToWithdraw
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Chamfer(name="{ self.name }")'
