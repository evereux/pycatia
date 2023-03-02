Private Sub CommandButton1_Click()
' Insert the code of your main procedure here
Set objShell = CreateObject("Wscript.Shell")
strPath = "C:\Users\CAD-002\PyCatia\Scripts\python.exe C:\Users\CAD-002\PyCatia\dpg.py"
objShell.Run strPath
End Sub
