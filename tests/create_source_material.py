import os
from pathlib import Path

from tests.common_vars import caa

def get_path_from_cat_startup(filename):
    def dfs(dir):
        if not os.path.exists(dir):
            return None
        for name in os.listdir(dir):
            path = os.path.join(dir,name)
            if os.path.isfile(path) and name == filename:
                return path
            if os.path.isdir(path):
                res = dfs(path)
                if res:
                    return res
        return None

    for dir in caa.application.system_service.environ('CATStartupPath').split(os.pathsep):
        path = dfs(dir)
        if path:
            return path
    return None


def get_cat_material():
    cat_material_filename = "Catalog.CATMaterial"
    catpart_materials = get_path_from_cat_startup(cat_material_filename)

    if catpart_materials is None:
        cat_startup_path = caa.application.system_service.environ('CATStartupPath')
        raise FileNotFoundError(f'Could not find {cat_material_filename} in {cat_startup_path}.')

    return catpart_materials
