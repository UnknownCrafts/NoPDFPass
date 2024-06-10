from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import pathlib
import pikepdf

'''
Initiate filepath and savepath variables, filepath is for the pdf file/folder that needs decoding,
meanwhile savepath is for the path where the decoded files are saved.
'''
filepath = ""
savepath = str(pathlib.Path.home()) + "/Desktop/"

# Helper Functions
def getfile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[('Allowed Types', '*.pdf')])
    filepath_label.set(filepath)

def getdir():
    global savepath
    savepath = filedialog.askdirectory()
    savepath += "/"
    save_path_label.set(savepath)
    
def retrieve_input():
    global passd
    passd = textbox.get("1.0","end-1c").strip().split(",")
    root.destroy()

# --GUI Code Starts Here--
root = Tk()
root.geometry('500x300')
root.eval('tk::PlaceWindow . center')

save_path_label = StringVar()
save_path_label.set(savepath)

filepath_label = StringVar()
filepath_label.set(filepath)

btn = Button(root, text = 'Done', 
                command = lambda: retrieve_input())

btn.pack(side = 'bottom')     

label = Label(root,text="Enter Password/s below: (Separate passwords by ',' if multiple)")
label.pack()

textbox = Text(root, height=2, width=30)
textbox.pack()

open_file_button = Button(root, text="Open File/Folder to decrypt", command=getfile)
open_file_button.pack()

current_chosen_file_or_folder_label = Label(root, textvariable= filepath_label)
current_chosen_file_or_folder_label.pack()

choose_button = Button(root, text="Choose the location to save the file", command=getdir)
choose_button.pack()

current_save_location_label = Label(root, textvariable= save_path_label)
current_save_location_label.pack()

root.mainloop()
# --GUI Code Ends Here--


# Background functionality after the root window has been destroyed
number_of_passwords = len(passd)

if passd[0] != '':

    for x in filepath:
        for i in range(number_of_passwords):
            try:
                file_name = x.split("/")
                file_name = file_name[-1]
                with pikepdf.open(x,password=passd[i].strip()) as pdf:
                    pdf.save(savepath + file_name)
                break
            except:
                pass
