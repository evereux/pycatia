import hashlib
import os
from pathlib import Path
import shutil

cwd = Path(os.getcwd())
project_root = cwd.parent
module_root = Path(project_root, 'pycatia')
api_doc_tmp_root = Path(project_root, '__junk__', 'api_temp')
api_doc_root = Path(project_root, 'docs', 'api')

files = module_root.rglob('*.py')

api_text = 'API\n' \
           '===\n\n'
last_parent = None
body = ''

files = [file for file in files]
files.sort()

api_dict = {}

for file in files:
    parent_directory = file.parents[0].stem

    if parent_directory not in api_dict:
        api_dict[parent_directory] = []

    file_name = file.stem

    if "__init__" not in file_name:
        api_dict[parent_directory].append(file_name)

# write api_index
with open('api_index.rst', 'w') as file:
    header = "API\n" \
             "=========\n\n\n" \
             "This part of the documentation covers all the interfaces of pycatia.\n\n" \
             "The entry point for most pycatia use cases is to do the following.\n\n" \
             ">>> from pycatia import catia\n\n" \
             "This creates an instance of the :ref:`Application<Application>` object.\n\n" \
             ".. toctree::\n" \
             "   :maxdepth: 1\n" \
             "   :caption: Contents:\n\n"

    lines = ""
    for api in api_dict:
        lines = lines + f"   api/index_{api}\n"

    file.write(header + lines)

# delete all existing files in api folder
api_files = api_doc_tmp_root.rglob('*.rst')
for api_file in api_files:
    os.remove(api_file)

for file in files:

    # ignore __init__ files
    if '__init__' in str(file):
        continue

    parent = file.parent
    parent_index = Path(api_doc_tmp_root, f'index_{str(parent.stem)}.rst')
    print(parent_index)
    if not parent_index.exists():
        index_stem = parent.stem
        if index_stem != 'pycatia':
            index_stem = 'pycatia.' + index_stem
        parent_index.touch()
        # this is a new file so we write the header to it.
        with open(parent_index, 'w') as f:
            header = index_stem + f"\n{'=' * len(index_stem)}\n\n" \
                                  f".. toctree::\n" \
                                  f"   :maxdepth: 1\n" \
                                  f"   :caption: Contents:\n\n\n"
            f.write(header)

    # append each module to index file.
    with open(parent_index, 'a') as f:
        if parent.stem == 'pycatia':
            stem = 'pycatia'
        else:
            stem = 'pycatia' + '/' + parent.stem
        lines = f"   {stem}/{str(file.stem)}\n"
        f.write(lines)

    if parent.stem == 'pycatia':
        class_file = Path(api_doc_tmp_root, parent.stem, str(file.stem) + '.rst')
        with open(class_file, 'w') as f:
            tag = f'.. _{file.stem.capitalize()}:\n\n'
            title = file.stem
            lines = tag + title + f"\n{'=' * len(title)}\n\n" \
                                  f".. automodule:: pycatia.{title}\n" \
                                  f"    :members:"
            f.write(lines)
    else:
        class_file = Path(api_doc_tmp_root, 'pycatia', str(parent.stem), str(file.stem) + '.rst')
        if not class_file.parent.exists():
            os.mkdir(class_file.parent)
        with open(class_file, 'w') as f:
            tag = f'.. _{file.stem.capitalize()}:\n\n'
            title = f"pycatia.{parent.stem}.{file.stem}"
            lines = tag + title + f"\n{'=' * len(title)}\n\n" \
                                  f".. automodule:: pycatia.{parent.stem}.{file.stem}\n" \
                                  f"    :members:"
            f.write(lines)

files = api_doc_tmp_root.rglob('*.rst')
for source_file in files:
    with open(source_file, 'rb') as rst_file:
        # print(f'getting hash for file {source_file}')
        contents = rst_file.read()
        md5_sum_source = hashlib.md5(contents).hexdigest()

        # get hash of target file
        target_file = Path(str(source_file).replace
            (
            str(api_doc_tmp_root),
            str(api_doc_root)
        )
        )
        # print(source_file, api_doc_root, api_doc_tmp_root, target_file)

    md5_sum_target = None
    if target_file.exists():
        with open(target_file, 'rb') as rst_file_target:
            # print(f'getting hash for file {target_file}')
            contents = rst_file_target.read()
            md5_sum_target = hashlib.md5(contents).hexdigest()

    if md5_sum_source != md5_sum_target:
        print('Do not match!')
        print(source_file, api_doc_root, api_doc_tmp_root, target_file)

        # copy file to target
        shutil.copy(source_file, target_file)
