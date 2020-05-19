#! /usr/bin/python3.6

"""

    Example 6:

    Open a catia file.

    Export catia file to igs.

    Close a catia file.

"""

from pathlib import Path
import os

from pycatia.in_interfaces.application import catia_application as catia

# path to file to open.
file_name = r'tests\CF_Part_1.CATPart'

# open document
documents = catia.documents
documents.open(file_name)

document = catia.active_document

# Full path of new file. This uses current working directory.
new_file_name = Path(os.getcwd(), 'new_part.CATPart')
# save document as new name.
document.save_as(new_file_name, overwrite=True)

# to export to another support fileformat (license permitting).
new_export_file_name = r"c:\temp\new_export_part"
document.export_data(new_export_file_name, "stp")

# close document
document.close()
