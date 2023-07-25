import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue()->tuple:
    """Get uset input value

    Returns:
        tuple: return tuple offcet value
        (Xmax,Xmin,Ymax,Ymin,Zmax,Zmin)
    """
    result=(Xmax.get(),
            Xmin.get(),
            Ymax.get(),
            Ymin.get(),
            Zmax.get(),
            Zmin.get())
    return result


# this is the function called when the button is clicked
def btnClickFunction():
      print(getInputBoxValue())
      exit()
 

root = Tk()

# This is the section of code which creates the main window
root.geometry('555x180')
root.configure(background='#FFEFDB')
root.title('Input offset')


# This is the section of code which creates a text input box
Xmax=Entry(root)
Xmax.place(x=15, y=40)

Xmin=Entry(root)
Xmin.place(x=15, y=90)

Ymax=Entry(root)
Ymax.place(x=195, y=40)

Ymin=Entry(root)
Ymin.place(x=195, y=90)

Zmax=Entry(root)
Zmax.place(x=375, y=40)

Zmin=Entry(root)
Zmin.place(x=375, y=90)


# This is the section of code which creates a button
Button(root, text='Set offset', bg='#FFEFDB', font=('arial', 12, 'normal'), 
       command=btnClickFunction).place(x=200, y=120)


# This is the section of code which creates the a label
Label(root, text='Xmax', bg='#FFEFDB', 
      font=('arial', 12, 'normal')).place(x=25, y=10)
Label(root, text='Xmin', bg='#FFEFDB', 
      font=('arial', 12, 'normal')).place(x=25, y=60)

Label(root, text='Ymax', bg='#FFEFDB', 
      font=('arial', 12, 'normal')).place(x=195, y=10)
Label(root, text='Ymin', bg='#FFEFDB', 
      font=('arial', 12, 'normal')).place(x=195, y=60)

Label(root, text='Zmax', bg='#FFEFDB', 
      font=('arial', 12, 'normal')).place(x=375, y=10)
Label(root, text='Zmin', bg='#FFEFDB', 
      font=('arial', 12, 'normal')).place(x=375, y=60)


root.mainloop()

