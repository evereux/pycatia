#! /usr/bin/python3.6

import csv
import os

from .hybridshapefactory import HybridShapeFactory


def csv_reader(file_name, delimiter=','):
    """
    Reads contents of csv file and returns an iterable of tuples in the format:
    [
        (
            str(<point_name>),
            int(X coordinate),
            int(Y coordinate),
            int(Z cooridnate)
        ),
    ]

    :param file_name: full path to csv file.
    :type file_name: str()
    :param delimiter:
    :type delimiter: str()
    :return: iterable()
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


def create_points(part, file_name, geometry_set_name='New_Points'):
    """
    :param part:
    :type part:
    :param file_name: full path to csv file.
    :type file_name: str()
    :param geometry_set_name:
    :type geometry_set_name: str()
    :return:
    """

    points = csv_reader(file_name)

    geometrical_set = part.part.HybridBodies.Add()
    geometrical_set.Name = geometry_set_name

    hsf = HybridShapeFactory(part)

    for point in points:
        print(f"Adding point: {point[0]}", end="\r")
        hsf.add_new_point_coord(geometrical_set, (point[1],point[2],point[3]), point[0])

    part.update()
