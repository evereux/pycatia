"""
    A simple script to generate API documentation for new modules.
"""

import os
from pathlib import Path

# module folder(s) within pycatia
modules = ['threed_xml_interfaces']

cwd = Path(os.getcwd())

folder_doc_api = Path(cwd, 'docs/api')
folder_pycatia = Path(cwd, 'pycatia')


def get_index_contents(module_name):
    folder = Path(folder_pycatia, module_name)
    dir_contents = os.listdir(folder)

    o = ''

    for file in dir_contents:
        if file == '__init__.py' or file == '__pycache__':
            continue
        f = file[0:-3]
        o = o + f'   pycatia/{module_name}/{f}\n'

    return o, dir_contents


def build_index(module_name):
    index_filename = Path(folder_doc_api, f'index_{module_name}.rst')

    # if file already exists skip.
    if index_filename.exists():
        print(f'"{index_filename}" already exists.')
        os.remove(index_filename)

    header = f'pycatia.{module_name}\n'
    header_underline = '=' * len(header)
    toc_tree = '\n\n' \
               '.. toctree::\n' \
               '   :maxdepth: 1\n' \
               '   :caption: Contents:\n\n\n'
    contents, dir_content = get_index_contents(module_name)

    text = header + header_underline + toc_tree + contents

    print(f'creating file {index_filename}')
    with open(index_filename, 'w') as file:
        file.write(text)

    return dir_content


def build_api(module_name, dir_content):
    module_api_folder = Path(folder_doc_api, 'pycatia', module_name)
    # create the folder 
    if not module_api_folder.exists():
        print(f'Creating folder {module_api_folder}.')
        os.mkdir(module_api_folder)

    for file in dir_content:
        m = file[0:-3]
        if file == '__init__.py' or file == '__pycache__':
            continue
        f_api_name = Path(module_api_folder, f'{m}.rst')

        header_link = f'.. _{module_name.capitalize()}:\n\n'
        header = f'pycatia.{module_name}.{m}\n'
        header_underline = '=' * len(header)
        auto_module = f'\n\n.. automodule:: pycatia.{module_name}.{m}\n' \
                      f'    :members:\n'

        text = header_link + header + header_underline + auto_module

        with open(f_api_name, 'w') as file:
            file.write(text)


for module_name in modules:
    # build index

    dir_content = build_index(module_name)
    build_api(module_name, dir_content)
