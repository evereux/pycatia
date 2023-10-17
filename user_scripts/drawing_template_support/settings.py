#! /usr/bin/python3.8

import json
from pathlib import Path
import os


def read_json(f: Path):
    with open(f) as file:
        data = json.load(file)

    return data


# you probably wouldn't have to do this out of a development environment.
path_prefix = Path(os.getcwd(), 'user_scripts', 'drawing_template_support')

json_settings = Path(path_prefix, 'settings.json')
json_data = read_json(json_settings)

border_offset = json_data['border_offset']
company_details = json_data['company_details']
logo = Path(path_prefix, json_data['logo'])
parameters = json_data['parameters']
sheet_names = json_data['sheet_names']
sheet_sizes = json_data['sheet_sizes']
template_name = json_data['template_name']
tolerances = json_data['tolerances']
units = json_data['units']
