.. _MacroButton_in_Catia:

Installation
============

.. note::

    Catia is installed and registrated as a com server.
    Python installed.
    Created python enviroment *VENV_PyCatia*
    pycatia installed in *VENV_PyCatia*.

Write starting script
-----------------

.. note::

    Script placed in root in *VENV_PyCatia*
    Script name is My_test_script.py

Press Alt+F8 and add macros (VBScript or VBA).

.. code::

    Private Sub Sub CATMain()
        ' Insert the code of your main procedure here
        Set objShell = CreateObject("Wscript.Shell")
        strPath = "*VENV_PyCatia*\Scripts\python.exe *VENV_PyCatia*\My_test_script.py"
        objShell.Run strPath
    End Sub

.. note::

    replace *VENV_PyCatia* to your PATH and My_test_script.py to your script name


Add your own button to Catia Toolbar
-----------------

Pls see in standart Catia Documentation

 *Install_Doc_Path*/English/online/CAAScdInfUseCases/CAAInfAddingMacroInToolbar.htm
 * where *Install_Doc_Path* installation PATH Catia Documentation

