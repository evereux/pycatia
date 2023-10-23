#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapePolyline(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapePolyline
                | 
                | Represents the hybrid shape polyline curve object.
                | Role: To access or set the data of the hybrid shape polyline object. This data
                | includes:
                | 
                |     Elements
                |     Radius
                |     Closure
                | 
                | Use the HybridShapeFactory object to create a HybridShapePolyline
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_polyline = com_object

    @property
    def closure(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Closure() As boolean
                | 
                |     Returns or sets the flag to decide closure of the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         Closure
                |             (For get_Closure) Returns or sets the closure
                |             property
                | 
                |             Example:
                |                 This example retrieves the closure property of the polyline of
                |                 the HybShpPolyline hybrid shape polyline.
                | 
                |                  Dim HybShpPolClosure As  boolean
                |                  HybShpPolClosure = HybShpPolyline.Closure

        :rtype: bool
        """

        return self.hybrid_shape_polyline.Closure

    @closure.setter
    def closure(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_polyline.Closure = value

    @property
    def number_of_elements(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NumberOfElements() As long (Read Only)
                | 
                |     Returns the number of elements of the polyline.
                | 
                |     Parameters:
                | 
                |         NumberOfElements
                |             Number of elements in the polyline.
                | 
                |             Example:
                |                 This example retrieves the number of elements in the polyline
                |                 of the HybShpPolyline hybrid shape polyline.
                | 
                |                  Dim HybShpPolNoOfEle As  long
                |                  HybShpPolNoOfEle = HybShpPolyline.NumberOfElements

        :rtype: int
        """

        return self.hybrid_shape_polyline.NumberOfElements

    def get_element(self, i_position: int, o_element: Reference, o_radius: Length) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetElement(long iPosition,
                | Reference oElement,
                | Length oRadius)
                | 
                |     Returns the element of the polyline.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which the element is to be retrieved. 
                |         oElement
                |             Reference to the element. 
                |         ioRadius
                |             Length to the radius.
                | 
                |             Example:
                |                 This example retrieves the element and radius of the polyline
                |                 at specified position of the HybShpPolyline hybrid shape
                |                 polyline.
                | 
                |                  Dim HybShpPolylineElement As Reference
                |                  Dim HybShpPolylineRadius As Reference
                |                  HybShpPolyline.GetElement 1,
                |                  HybShpPolylineElement,HybShpPolylineRadius

        :param int i_position:
        :param Reference o_element:
        :param Length o_radius:
        :rtype: None
        """
        return self.hybrid_shape_polyline.GetElement(i_position, o_element.com_object, o_radius.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_element'
        # # vba_code = """
        # # Public Function get_element(hybrid_shape_polyline)
        # #     Dim iPosition (2)
        # #     hybrid_shape_polyline.GetElement iPosition
        # #     get_element = iPosition
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def insert_element(self, i_point: Reference, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertElement(Reference iPoint,
                | long iPosition)
                | 
                |     Inserts the element at a specified position in the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Reference of the point object to be inserted. 
                |         iPosition
                |             Position at which the element should be inserted.
                | 
                |             Example:
                |                 This example inserts the element in the polyline of the
                |                 HybShpPolyline hybrid shape polyline.
                | 
                |                  HybShpPolyline.InsertElement PointReference,1

        :param Reference i_point:
        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_polyline.InsertElement(i_point.com_object, i_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_element'
        # # vba_code = """
        # # Public Function insert_element(hybrid_shape_polyline)
        # #     Dim iPoint (2)
        # #     hybrid_shape_polyline.InsertElement iPoint
        # #     insert_element = iPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_element(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveElement(long iPosition)
                | 
                |     Removes the element at a specified position in the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position from which the element should be should be
                |             removed.
                | 
                |             Example:
                |                 This example removes the element in the polyline of the
                |                 HybShpPolyline hybrid shape polyline.
                | 
                |                  HybShpPolyline.RemoveElement 1

        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_polyline.RemoveElement(i_position)

    def replace_element(self, i_point: Reference, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ReplaceElement(Reference iPoint,
                | long iPosition)
                | 
                |     Replaces the element at a specified position in the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Reference of the point object that will replace the old element.
                |             
                |         iPosition
                |             Position at which the element should be inserted.
                | 
                |             Example:
                |                 This example replaces the element in the polyline of the
                |                 HybShpPolyline hybrid shape polyline.
                | 
                |                  HybShpPolyline.ReplaceElement PointReference, 1

        :param Reference i_point:
        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_polyline.ReplaceElement(i_point.com_object, i_position)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_element'
        # # vba_code = """
        # # Public Function replace_element(hybrid_shape_polyline)
        # #     Dim iPoint (2)
        # #     hybrid_shape_polyline.ReplaceElement iPoint
        # #     replace_element = iPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_radius(self, i_position: int, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRadius(long iPosition,
                | double iRadius)
                | 
                |     Sets the radius at specified position of the polyline.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which radius should be set 
                |         iRadius
                |             Value of the radius to be set.
                | 
                |             Example:
                |                 This example sets the radius at the specific position of the
                |                 polyline of the HybShpPolyline hybrid shape
                |                 polyline.
                | 
                |                  HybShpPolyline.SetRadius 1, 10

        :param int i_position:
        :param float i_radius:
        :rtype: None
        """
        return self.hybrid_shape_polyline.SetRadius(i_position, i_radius)

    def __repr__(self):
        return f'HybridShapePolyline(name="{self.name}")'
