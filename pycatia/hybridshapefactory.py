#! /usr/bin/python3.6

import os
import warnings


class HybridShapeFactory:

    def __init__(self, part):
        """

        :param part: CATIA Part COM object.
        """

        self.hsf = part.part.HybridShapeFactory

    def add_new_point_coord(self, catia, geometrical_set, new_point, point_name):
        """

        .. warning::
            Replaced run_system service in attempt to solve this issue:
            http://www-01.ibm.com/support/docview.wss?uid=swg1HD79859
            Issue was not resolved. Adding a large number of points gets slower and slower when adding large numbers of
            points. This is visible when adding over 1500 points on test machine (run example_5.py).
            In these cases it's probably best to split the csv file into several files and run the import in batches.


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

        :param catia: CATIAApplication()
        :param geometrical_set:
        :param new_point:
        :param point_name:
        """

        macro_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r'macros')

        point = self.hsf.AddNewPointCoord(new_point[0], new_point[1], new_point[2])

        vba_function_name = 'add_point'

        message = ('Adding points gets exponentially slower for tested version of CATIA.'
                   'If this slow down becomes an issue please split input files. This is not a limitation of pycatia'
                   'but of the CATIA automation API.')
        warnings.warn(message)

        catia.execute_script(macro_path,
                             1,
                             'pycatia_macros.catvbs',
                             vba_function_name,
                             [geometrical_set, point, point_name])
