.. _create_and_run_a_script:

Create And Run A Script
=======================

The process of creating and running python scripts can be executed a number of
different ways. The following will just explain the basics.

* In your pycatia-scripts folder `c:\Users\<username>\python\pycatia-scripts` create
  a new file called `catia_details.py`.


* Open and edit this file in your favourite file text editor (not MS Word etc!) / IDE
  (eg VS Code / pycharm) and write the following:


.. code-block:: python

    from pycatia import catia

    application = catia()

    full_name = application.full_name
    sys_config = application.system_configuration
    release = sys_config.release
    version = sys_config.version
    service_pack = sys_config.service_pack

    print(f'''
    You are currently running CATIA V{version} release {release} SP {service_pack}.
    ''')


* Save the file in your editor.

* You'll need to open a CMD terminal and navigate to your pycatia-scripts folder.

.. code-block::

   cd c:\Users\<username>\python\pycatia-scripts

* Activate the virtual environment.

.. code-block::

    env\Scripts\activate

* You should see the command prompt change to something similar to this.

    (env) c:\Users\<username>\python\pycatia-scripts>

* To run the script you need to type `python` followed by your `script_name.py`:

.. code-block::

    (env) c:\Users\<username>\python\pycatia-scripts>python catia_details.py

The script should then display the following:

.. code-block::

    (env) c:\Users\<username>\python\pycatia-scripts>python catia_details.py

    You are currently running CATIA V5 release XX SP XXX

    (env) c:\Users\<username>\python\pycatia-scripts>

For more detailed examples on how to interact with pycatia see the
:ref:`examples` page. There contain several scripts that can be run in the
terminal.