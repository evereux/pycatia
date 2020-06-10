import os
from pathlib import Path

cwd = Path(os.getcwd())
parent = cwd.parent
path_pycatia = Path(parent, 'pycatia')

files = path_pycatia.rglob('*.py')

api_text = 'API\n' \
           '===\n\n'
last_parent = None
body = ''

for file in files:
    name = file.name
    parent_module = file.parent.name
    header = '\n' + str(parent_module)
    header = header + '\n' + '-' * len(header)
    header = header + '\n\n'
    if name != '__init__.py':
        auto_module = 'pycatia' + '.' + str(parent_module) + '.' + name
        auto_module = auto_module[0:-3]
        body = '.. automodule:: ' + auto_module + '\n' \
                                                  '    :members:\n\n'
        if last_parent != parent_module:
            api_text = api_text + header
        api_text = api_text + body

        last_parent = parent_module

with open('api.rst', 'w') as file:
    file.write(api_text)
