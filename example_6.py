#! /usr/bin/python3.6

"""

    Example 6:

    Open a catia file.

    Close a catia file.

"""

from pycatia import CATIAApplication
from pycatia import Document
from pycatia import Documents

# path to file to open.
file_name = r'tests\CF_Part_1.CATPart'
new_file_name = 'new_part.CATPart'

catia = CATIAApplication()
# open document
documents = catia.documents()
documents.open(file_name)

document = catia.document()
# save document as new name.
document.save_as(new_file_name)
# close document
document.close()
