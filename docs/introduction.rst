Getting Started
===============

Before proceeding with this introduction to pycatia you should have already have
pycatia installed. Visit the :ref:`installation` page.

.. _install:

Before going through the introductory examples on this page you need to have
CATIA V5 running and a CMD terminal open with the environment that has pycatia
installed activated prior to starting the python interpreter.

Opening A New CATPart
---------------------

You will almost always want to import the `catia`
:ref:`Application<Application>` object or the CATIADocHandler [1]_.

.. code-block:: python

    from pycatia import catia
    # initialise the catia automation appliction. CATIA V5 should already be running.
    caa = catia()
    documents = caa.documents

documents is an instance of the :ref:`Documents<Documents>`
class.

.. code-block:: python

    documents.add('Part')

the add method of the documents class expects the string 'Part', 'Product' or
'Drawing'. ``documents.add('Part')`` adds a new CATPart to the documents
collection.

We want to work on this new document. Since this has just been added it's the
active document.

.. code-block:: python

    document = caa.active_document

The document object :ref:`Document<Document>` has a
number of properties that can be accessed.

.. code-block:: python

    document.name
    # returns the name of the new document.
    document.path
    # returns the pathlib.Path object of the document.


Creating A Geometrical Set
--------------------------

A geometrical set created using the :ref:`HybridBodies<Hybrid_bodies>` collection. Your CATIA
configuration may by default create a geometrical set in a new CATPart but we'll
create one here anyway.

.. code-block:: python

    part = document.part()
    hybrid_bodies = part.hybrid_bodies
    new_set = hybrid_bodies.add()
    new_set.name
    # returns the name of your new set.
    # to rename the set.
    new_set.name = 'Construction Geometry'




For more detailed examples on how to interact with pycatia see the
:ref:`examples` page. There contain several scripts that can be run in the
terminal.

Footnotes
---------

.. [1]
    The CATIADocHandler is for those cases where you are opening and closing
    several documents consecutively. This will be covered at a later date in the
    meantime check out the :ref:`examples` for examples of usage.
