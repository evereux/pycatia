#! /usr/bin/python3.9

"""

    Example - BOM CUSTOM - 001

    Description:
        Create a custom formatted html of the product tree.

    Requirements:
        - An open product document with parts inside.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from collections import Counter
from datetime import datetime

from pycatia import catia
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
product_document: ProductDocument = caa.active_document
product = product_document.product
products = product.products

part_numbers = []
prd_dict = {}

for product_item in products:
    part_numbers.append(product_item.part_number)
    prd_dict[product_item.part_number] = product_item.nomenclature

part_numbers.sort()
c = Counter(part_numbers)

html = f"""<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

        <title>{product.part_number} - {product.nomenclature}</title>
    </head>
    <body>
        <div class="container">
            <h1>{product.part_number} - {product.nomenclature}</h1>
            <p>
                Product BOM generated on {datetime.now()}.
            </p>
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                        <th>Part Number</th>
                        <th>Title</th>
                        <th>QTY</th>
                    </tr>
                </thead>
            <tbody>
"""

for item in c:
    print(item, prd_dict[item], c[item])
    row = f"""
                    <tr>
                        <td>{item}</td>
                        <td>{prd_dict[item]}</td>
                        <td>{c[item]}</td>
                    </tr>"""
    html += row

html += """  
            <tbody>
        </table>
    </body>
</html>"""

with open((product.part_number + ".html"), "w") as f:
    f.write(html)
