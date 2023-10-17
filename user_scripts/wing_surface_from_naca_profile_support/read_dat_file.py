from pathlib import Path


def append_point(point_list: list, coordinate: tuple[float, float]) -> None:
    """

    :param list point_list:
    :param tuple[float, float] coordinate:
    :return: None
    """
    point_list.append(coordinate)


def read_dat_file(naca_dat_file: Path, chord_length: float) -> tuple[list, list]:
    """
    :param Path naca_dat_file:
    :param float chord_length: chord length in mm
    :return: tuple[list, list]
    """

    if not naca_dat_file.is_file():
        raise FileNotFoundError(f'Could find load {naca_dat_file}.')

    upper_coordinates: list = []
    lower_coordinates: list = []

    with open(naca_dat_file, 'r') as file:
        lines = file.readlines()[3:]
        upper = True
        for line in lines:
            line = line.strip()
            s = line.split()
            if len(s) == 2:
                x = float(s[0]) * chord_length
                y = float(s[1]) * chord_length
                # ignore the root point, we'll add that manually.
                if x == 0 and y == 0:
                    continue
                if upper is True:
                    point_list = upper_coordinates
                else:
                    point_list = lower_coordinates
                append_point(point_list, (x, y))
            else:
                upper = False

    return upper_coordinates, lower_coordinates
