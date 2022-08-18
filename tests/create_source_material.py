from pathlib import Path

from pycatia import catia


def get_cat_material():
    caa = catia()
    cat_startup_path = caa.application.system_service.environ('CATStartupPath')
    cat_material_filename = 'Catalog.CATMaterial'
    catpart_materials = Path(cat_startup_path, 'materials', cat_material_filename)

    if not catpart_materials.is_file():
        raise FileNotFoundError(f'Could not find {catpart_materials}.')

    return catpart_materials
