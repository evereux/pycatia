from pathlib import Path

from tests.common_vars import caa


def get_cat_material():
    env_startup_path = caa.application.system_service.environ("CATStartupPath")
    cat_material_filename = "Catalog.CATMaterial"

    cat_startup_paths = []
    if ";" in env_startup_path:
        _paths = env_startup_path.split(";")
        cat_startup_paths = [p.strip() for p in _paths]
    else:
        cat_startup_paths.append(env_startup_path.strip())

    catpart_materials = ""

    for cat_startup_path in cat_startup_paths:
        catpart_materials = Path(cat_startup_path, "materials", cat_material_filename)

        if not catpart_materials.is_file():
            continue
        else:
            break

    if not catpart_materials.is_file():
        raise FileNotFoundError(f"Could not find {catpart_materials}.")

    return catpart_materials
