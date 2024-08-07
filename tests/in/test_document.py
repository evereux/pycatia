#! /usr/bin/python3.9

import os
from datetime import datetime
from pathlib import Path

import pytest

from pycatia.base_interfaces.context import CATIADocHandler
from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.types.document import document_types
from tests.common_vars import caa
from tests.source_files import cat_part_measurable
from tests.source_files import cat_product
from tests.source_files import stp_file
from tests.source_files import igs_file

junk_folder = os.path.join(os.getcwd(), "__junk__/")
now_string = datetime.now().strftime("%Y%m%d-%H%M%S")
os.makedirs(junk_folder, exist_ok=True)


def test_activate_document():
    documents = caa.documents
    documents.open(cat_part_measurable)
    document_part = caa.active_document
    documents.open(cat_product)
    document_product = caa.active_document

    assert document_part.name == os.path.basename(cat_part_measurable)
    assert document_product.name == os.path.basename(cat_product)

    document_part.activate()
    document = caa.active_document

    assert document.name == os.path.basename(cat_part_measurable)

    document_part.close()
    document_product.close()


def test_add_document():
    with CATIADocHandler(new_document='Analysis') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['Analysis']['extension'] in document.name

    with CATIADocHandler(new_document='CatalogDocument') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['CatalogDocument']['extension'] in document.name

    with CATIADocHandler(new_document='Drawing') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['Drawing']['extension'] in document.name

    with CATIADocHandler(new_document='CATProcess') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['CATProcess']['extension'] in document.name

    with CATIADocHandler(new_document='FeatureDictionary') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['FeatureDictionary']['extension'] in document.name

    with CATIADocHandler(new_document='Part') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['Part']['extension'] in document.name

    with CATIADocHandler(new_document='Product') as caa_:
        document = caa_.document
        assert document is not None
        assert document_types['Product']['extension'] in document.name


def test_count_types():
    with CATIADocHandler(cat_product) as caa_:
        documents = caa_.documents

        num = documents.count_types(".catpart")

        assert num == 1


def test_export_document():
    with CATIADocHandler(cat_part_measurable) as caa_:
        document = caa_.document
        assert document is not None

        export_type = "igs"
        export_name = "export_file"

        path = os.path.dirname(os.path.abspath(cat_part_measurable))
        export_name = os.path.join(path, export_name)

        document.export_data(Path(f"{export_name}.{export_type}"), export_type)

        assert os.path.isfile(f"{export_name}.igs")

        os.remove(f"{export_name}.igs")


def test_full_name():
    """
    :return:
    """
    with CATIADocHandler(cat_part_measurable) as caa_:
        document = caa_.document
        assert document is not None
        assert str(cat_part_measurable) == document.full_name


def test_get_documents_names():
    pass
    # todo: update this test so that's more reliable. currently get_item_names()
    # can return additional documents held open by CATIA.
    #
    # with CATIADocHandler(cat_product) as caa_:
    #     documents = caa_.documents
    #
    #     expected_names = [
    #         "product_top.CATProduct",
    #         "product_sub_2.CATProduct",
    #         "part_measurable.CATPart",
    #         "product_sub_1.CATProduct",
    #     ]
    #
    #     assert expected_names in documents.get_item_names()


def test_is_saved():
    with CATIADocHandler(cat_part_measurable) as caa_:
        document = caa_.document
        assert document is not None
        assert document.is_saved

        part = PartDocument(document.com_object).part

        # create a new geometrical set to add point.
        geometrical_set = part.hybrid_bodies.add()
        geometrical_set.name = "lalalalalala"

        # just adding geometrical set isn't enough to trigger is_saved to be False
        # catia r21 bug?
        # so a new point is also added.
        factory = part.hybrid_shape_factory
        point = factory.add_new_point_coord(0, 1, 2)
        geometrical_set.append_hybrid_shape(point)
        part.update()

        assert not document.is_saved


def test_item():
    with CATIADocHandler(cat_product) as caa_:
        documents = caa_.documents
        doc_com1 = documents.item(cat_product.name)

        assert doc_com1.name == cat_product.name


def test_new_from():
    documents = caa.documents
    document = documents.new_from(cat_part_measurable)

    assert document.name is not os.path.basename(cat_part_measurable)

    document.close()


def test_new_from_str():
    documents = caa.documents
    document = documents.new_from(str(cat_part_measurable))

    assert document.name is not os.path.basename(cat_part_measurable)

    document.close()


def test_open_document():
    documents = caa.documents
    document = documents.open(cat_part_measurable)
    assert type(document) is PartDocument
    document.close()
    document = documents.open(cat_product)
    assert type(document) is ProductDocument
    document.close()


def test_open_document_str():
    documents = caa.documents
    document = documents.open(str(cat_part_measurable))
    assert type(document) is PartDocument
    document.close()


def test_open_document_igs():
    # igs file will need to be created manually.
    if not igs_file.is_file():
        assert False
    documents = caa.documents
    document = documents.open(igs_file)

    assert type(document) is Document

    document.close()


def test_open_document_stp():
    # stp file will need to be created manually.
    if not stp_file.is_file():
        assert False
    documents = caa.documents
    document = documents.open(stp_file)

    assert type(document) is Document

    document.close()


def test_read_document():
    documents = caa.documents
    document = documents.read(cat_part_measurable)
    assert type(document) is PartDocument
    document.close()
    document = documents.read(cat_product)
    assert type(document) is ProductDocument
    document.close()


def test_read_document_str():
    documents = caa.documents
    document = documents.read(str(cat_part_measurable))

    assert type(document) is PartDocument

    document.close()


def test_read_document_igs():
    # igs file will need to be created manually.
    if not igs_file.is_file():
        assert False
    documents = caa.documents
    document = documents.read(igs_file)

    assert type(document) is Document

    document.close()


def test_read_document_stp():
    # stp file will need to be created manually.
    if not stp_file.is_file():
        assert False
    documents = caa.documents
    document = documents.read(stp_file)

    assert type(document) is Document

    document.close()


def test_part():
    with CATIADocHandler(cat_part_measurable) as caa_:
        document = caa_.document
        assert document is not None

        part = PartDocument(document.com_object).part
        assert part.name == "cat_part_measurable"
        assert document.is_part
        assert not document.is_product


def test_product():
    with CATIADocHandler(cat_product) as caa_:
        document = caa_.document
        assert document is not None

        product = ProductDocument(document.com_object).product
        assert "cat_product_1" in product.name
        assert document.is_product


def test_saving():
    new_filename = Path(junk_folder, f"{now_string}.CATPart")

    with CATIADocHandler(cat_part_measurable) as caa_:
        document = caa_.document
        assert document is not None

        document.save_as(new_filename)
        document.save()

        assert os.path.isfile(new_filename)

        with pytest.raises(FileExistsError):
            document.save_as(new_filename)

    os.remove(new_filename)
