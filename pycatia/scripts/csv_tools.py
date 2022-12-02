#! /usr/bin/python3.9

import csv
import os
import time

from typing import Generator

from pycatia.mec_mod_interfaces.part import Part

unit_conversion = {
    'mm': 1,
    'cm': 10,
    'm': 1000,
    'km': 1000000,
    'in': 25.4,
    'mile': 1.609344e+6,
}


def convert_units(number: str, unit: str) -> float:
    """

    Convert input 'length' from unit to millimeters.

    :param number:
    :param str unit: A string representing the unit 'mm', 'in', 'cm', 'm', 'mile', 'km'
    :return:
    """

    try:
        n = float(number)
    except ValueError:
        raise FloatingPointError("Input {number} can not be converted to float(). Check csv data.")

    try:
        return float(n * unit_conversion[unit])
    except KeyError:
        raise KeyError(f'Unit {unit} is not currently supported.')


def csv_reader(file_name: str, units: str, delimiter: str = ',') -> Generator[dict, None, None]:
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
    :param str units:
    :param delimiter:
    :return: generator()
    """

    if not os.path.isfile(file_name):
        raise FileNotFoundError('Check file exists.')

    with open(file_name) as file:
        csv_file = csv.reader(file, delimiter=delimiter)
        for line in csv_file:
            point = {'name': line[0],
                     'x': convert_units(line[1], units),
                     'y': convert_units(line[2], units),
                     'z': convert_units(line[3], units)}
            yield point


def create_points(part: Part, file_name: str, units: str = 'mm', geometry_set_name: str = 'New_Points') -> None:
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
    geometrical_set.name = geometry_set_name

    hsf = part.hybrid_shape_factory

    for point in points:
        start = time.time()
        new_point = hsf.add_new_point_coord(point['x'], point['y'], point['z'])
        geometrical_set.append_hybrid_shape(new_point)
        end = time.time()
        time_taken = end - start
        print(f"Added point: {point['name']}. Time taken = {round(time_taken, 3)} seconds", end="\r")

    part.update()
