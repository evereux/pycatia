#! /usr/bin/python3.6

from .general_functions import run_system_service


class HybridShapeFactory:

    def __init__(self, part):
        """

        :param part: CATIA Part COM object.
        """

        self.hsf = part.part.HybridShapeFactory

    def add_new_point_coord(self, geometrical_set, new_point, point_name):
        """
        .. note::
            CAA V5 Visual Basic help

            | Func AddNewPointCoord(double  iX,
            |                       double  iY,
            |                       double  iZ) As HybridShapePointCoord

            | Creates a new point defined by its cartesian coordinates within the current body.
            | Parameters:
            | iX
            |     X coordinate for the point
            | iY
            |     Y coordinate for the point
            | iZ
            |     Z coordinate for the point
            | oPoint
            |     Created point

        """

        point = self.hsf.AddNewPointCoord(new_point[0], new_point[1], new_point[2])

        vba_function_name = 'add_point'
        vba_function = 'AppendHybridShape'
        vba_code = (f'Public Function {vba_function_name}(geometrical_set, point, point_name)\n'
                    f'    geometrical_set.{vba_function} point\n'
                    f'    point.Name = point_name\n'
                    f'End Function')
        run_system_service(vba_code, vba_function_name, [geometrical_set, point, point_name])
