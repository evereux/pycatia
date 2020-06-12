#! /usr/bin/python3.6

import csv
import os
import time

unit_conversion = {
    'mm': 1,
    'cm': 10,
    'm': 1000,
    'km': 1000000,
    'in': 25.4,
    'mile': 1.609344e+6,
}


def convert_units(number, unit):
    """

    Convert input 'length' from unit to millimeters.

    :param number:
    :param str unit: A string representing the unit 'mm', 'in', 'cm', 'm', 'mile', 'km'
    :return:
    """

    try:
        number = float(number)
    except ValueError:
        raise FloatingPointError("Input {number} can not be converted to float(). Check csv data.")

    try:
        return number * unit_conversion[unit]
    except KeyError:
        raise KeyError(f'Unit {unit} is not currently supported.')


def csv_reader(file_name, units, delimiter=','):
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
    :param units:
    :param delimiter:
    :return: generator()
    """

    if not os.path.isfile(file_name):
        raise FileNotFoundError('Check file exists.')

    with open(file_name) as file:
        csv_file = csv.reader(file, delimiter=delimiter)
        for line in csv_file:
            point = {}
            point['name'] = line[0]
            point['x'] = convert_units(line[1], units)
            point['y'] = convert_units(line[2], units)
            point['z'] = convert_units(line[3], units)
            yield point


def create_points(part, file_name, units='mm', geometry_set_name='New_Points'):
    """
    Parses a csv file in the format defined in :func:`~csv_reader` and populates the geometry_set_name with new
    points. Once complete the part is updated.

    :param Part part:
    :param str file_name: full path to csv file.
    :param str units: length units of csv_file eg 'in'
    :param str geometry_set_name: name of new geometrical set in which to add points.
    :return:
    """

    points = csv_reader(file_name, units)

    geometrical_set = part.hybrid_bodies.add()
    geometrical_set.Name = geometry_set_name

    hsf = part.hybrid_shape_factory

    for point in points:
        start = time.time()
        hsf.add_new_point_coord(point['x'], point['y'], point['z'])
        end = time.time()
        time_taken = end - start
        print(f"Added point: {point['name']}. Time taken = {round(time_taken, 3)} seconds", end="\r")

    part.update()
