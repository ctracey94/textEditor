##########################################################################################
#   textEditor.py                                                                        #
#                                                                                        #
#   Author:          Conor Tracey                                                        #
#   Project Started: 1/31/2017                                                           #
#   Latest Update:   1/31/2017                                                           #
#                                                                                        #
#   Credits:         Foundation of code taken from youtube tutorial by Zach King         #
#                    (https://www.youtube.com/watch?v=xqDonHEYPgA)                       #
#                                                                                        #
#   A basic text editor written in Python 3.4.3.                                         #
##########################################################################################

import tkinter as tk
from tkinter import filedialog
import os


filename = None


def newFile():
    global filename, text, root
    filename = None
    root.title("Untitled")
    text.delete(0.0, tk.END)
    

def saveFile():
    global filename, text
    t = text.get(0.0, tk.END)

    if filename == None:
        saveAs()
    else:
        file = open(filename, 'w')
        file.write(t)
        file.close()
    

def saveAs():
    global filename, text, root

    if filename == None:
        file = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt')
    else:
        file = filedialog.asksaveasfile(mode = 'w',\
                                    initialfile = filename[filename.rfind('/')+1:])
    filename = file.name
    t = text.get(0.0, tk.END)

    #Change title of window to be the same as the f(ile name (without file path)
    root.title(filename[filename.rfind('/')+1:])

        
    try:
        file.write(t.rstrip())
    except:
        filedialog.showerror(title="Oops!", message="Unable to save file...")
        

def openFile():
    global filename, text, root
    file = filedialog.askopenfile(mode='r')
    filename = file.name
    
    #Change title of window to be the same as the file name (without file path)
    root.title(filename[filename.rfind('/')+1:])
        
    t = file.read()   
    text.delete(0.0, tk.END)
    text.insert(0.0, t)
    

root = tk.Tk()
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = tk.Text(root, width=400, height=400)
text.pack()

#Configure file menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

newFile()
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python"\
          to true' ''')
root.mainloop()

