#! /usr/bin/python3.6

import csv
import os
import time

from .hybridshapefactory import HybridShapeFactory


def csv_reader(file_name, delimiter=','):
    """
    | Reads contents of csv file and returns a generator object containing tuples in the format:
    | [
    |     (
    |         str(<point_name>),
    |         int(X coordinate),
    |         int(Y coordinate),
    |         int(Z coordinate)
    |     ),
    | ]

    :param file_name: full path to csv file.
    :param delimiter:
    :return: generator()
    """

    if not os.path.isfile(file_name):
        raise FileNotFoundError('Check file exists.')

    with open(file_name) as file:
        csv_file = csv.reader(file, delimiter=delimiter)
        for line in csv_file:
            point_name = line[0]
            x_coordinate = line[1]
            y_coordinate = line[2]
            z_coordinate = line[3]
            yield point_name, x_coordinate, y_coordinate, z_coordinate


def create_points(catia, part, file_name, geometry_set_name='New_Points'):
    """
    Parses a csv file in the format defined in :func:`~csv_reader` and populates the geometry_set_name with new
    points. Once complete the part is updated.

    :param catia: CATIAApplication()
    :param part: active CATPart to add the points to
    :param file_name: full path to csv file.
    :param geometry_set_name: name of new geometrical set in which to add points.
    :return:
    """

    points = csv_reader(file_name)

    geometrical_set = part.part.HybridBodies.Add()
    geometrical_set.Name = geometry_set_name

    hsf = HybridShapeFactory(part)

    for num, point in enumerate(points):
        start = time.time()
        hsf.add_new_point_coord(catia, geometrical_set, (point[1], point[2], point[3]), point[0])
        end = time.time()
        time_taken = end - start
        print(f"Added point: {point[0]}. Time taken = {round(time_taken, 3)} seconds", end="\r")

    part.update()
