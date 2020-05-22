#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePolyline(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape polyline curve object.Role: To access or
                | set the data of the hybrid shape polyline object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_polyline = com_object     

    @property
    def closure(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Closure
                | o Property Closure(    ) As
                | 
                | Returns or sets the flag to decide closure of the polyline.
                | Examples:
                | This example retrieves the closure property of the polyline
                | of the HybShpPolyline hybrid shape polyline. Dim
                | HybShpPolClosure As boolean HybShpPolClosure =
                | HybShpPolyline.Closure

        :return:
        """
        return self.hybrid_shape_polyline.Closure

    @closure.setter
    def closure(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_polyline.Closure = value 

    @property
    def number_of_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NumberOfElements
                | o Property NumberOfElements(    ) As   (Read Only)
                | 
                | Returns the number of elements of the polyline.
                | Examples:
                | This example retrieves the number of elements in the
                | polyline of the HybShpPolyline hybrid shape polyline. Dim
                | HybShpPolNoOfEle As long HybShpPolNoOfEle =
                | HybShpPolyline.NumberOfElements

        :return:
        """
        return self.hybrid_shape_polyline.NumberOfElements

    def get_element(self, i_position, o_element, o_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetElement
                | o Sub GetElement(        iPosition,
                |                          oElement,
                |                          oRadius)
                | 
                | Returns the element of the polyline.
                |
                | Parameters:
                | iPosition
                |      Position at which the element is to be retrieved.
                |    
                |  oElement
                |      Reference to the element.
                |    
                |  ioRadius
                |      Length to the radius.

                | Examples:
                | This example retrieves the element and radius of the
                | polyline at specified position of the HybShpPolyline hybrid
                | shape polyline. Dim HybShpPolylineElement As Reference Dim
                | HybShpPolylineRadius As Reference HybShpPolyline.GetElement
                | 1, HybShpPolylineElement,HybShpPolylineRadius

        :param i_position:
        :param o_element:
        :param o_radius:
        :return:
        """
        return self.hybrid_shape_polyline.GetElement(i_position, o_element, o_radius)

    def insert_element(self, i_point, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertElement
                | o Sub InsertElement(        iPoint,
                |                             iPosition)
                | 
                | Inserts the element at a specified position in the polyline.
                |
                | Parameters:
                | iPoint
                |       Reference of the point object to be inserted.
                |    
                |  iPosition
                |      Position at which the element should be inserted.

                | Examples:
                | This example inserts the element in the polyline of the
                | HybShpPolyline hybrid shape polyline.
                | HybShpPolyline.InsertElement PointReference,1

        :param i_point:
        :param i_position:
        :return:
        """
        return self.hybrid_shape_polyline.InsertElement(i_point, i_position)

    def remove_element(self, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveElement
                | o Sub RemoveElement(        iPosition)
                | 
                | Removes the element at a specified position in the polyline.
                |
                | Parameters:
                | iPosition
                |       Position from which the element should be should be removed.

                | Examples:
                | This example removes the element in the polyline of the
                | HybShpPolyline hybrid shape polyline.
                | HybShpPolyline.RemoveElement 1

        :param i_position:
        :return:
        """
        return self.hybrid_shape_polyline.RemoveElement(i_position)

    def replace_element(self, i_point, i_position):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceElement
                | o Sub ReplaceElement(        iPoint,
                |                              iPosition)
                | 
                | Replaces the element at a specified position in the
                | polyline.
                |
                | Parameters:
                | iPoint
                |       Reference of the point object that will replace the old element.
                |    
                |  iPosition
                |      Position at which the element should be inserted.

                | Examples:
                | This example replaces the element in the polyline of the
                | HybShpPolyline hybrid shape polyline.
                | HybShpPolyline.ReplaceElement PointReference, 1

        :param i_point:
        :param i_position:
        :return:
        """
        return self.hybrid_shape_polyline.ReplaceElement(i_point, i_position)

    def set_radius(self, i_position, i_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRadius
                | o Sub SetRadius(        iPosition,
                |                         iRadius)
                | 
                | Sets the radius at specified position of the polyline.
                |
                | Parameters:
                | iPosition
                |      Position at which radius should be set 
                |    
                |  iRadius
                |       Value of the radius to be set.

                | Examples:
                | This example sets the radius at the specific position of the
                | polyline of the HybShpPolyline hybrid shape polyline.
                | HybShpPolyline.SetRadius 1, 10

        :param i_position:
        :param i_radius:
        :return:
        """
        return self.hybrid_shape_polyline.SetRadius(i_position, i_radius)

    def __repr__(self):
        return f'HybridShapePolyline()'
