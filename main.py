from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os
import pathlib
import pikepdf


filepath = ""
savepath = pathlib.Path.home()
def getfile():
    global filepath
    filepath = filedialog.askopenfilename()

def getdir():
    global savepath
    savepath = filedialog.askdirectory()
    savepath += "/"

root = Tk()
root.geometry('300x300')
root.eval('tk::PlaceWindow . center')

btn = Button(root, text = 'Done', 
                command = root.destroy)

btn.pack(side = 'bottom')     

label = Label(root,text="Enter Password below:")
label.pack()
textbox = Entry(root)
passd = textbox.get().strip().split(",")
textbox.pack()

open_button = Button(root, text="Open File/Folder to decrypt", command=getfile)
open_button.pack()

choose_button = Button(root, text="Choose the location to save the file", command=getdir)
choose_button.pack()

root.mainloop()

number_of_passwords = len(passd)

isDir = os.path.isdir(filepath)

passd = "144011999"
with pikepdf.open('input.pdf',password=passd) as pdf:
    pdf.save(savepath + 'output.pdf')