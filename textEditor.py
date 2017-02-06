##########################################################################################
#   textEditor.py                                                                        #
#                                                                                        #
#   Author:          Conor Tracey                                                        #
#   Project Started: 1/31/2017                                                           #
#   Latest Update:   1/06/2017                                                           #
#                                                                                        #
#   Credits:         Original foundation of code taken from youtube tutorial             #
#                       by Zach King                                                     #
#                      (https://www.youtube.com/watch?v=xqDonHEYPgA)                     #                      #
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


def cut():
    global root, text
    
    selected_text = text.selection_get()
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)
    

def copy():
    global root, text

    selected_text = text.selection_get()
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def paste():
    global root, text

    clipboard_text = root.clipboard_get()
    text.insert(tk.INSERT, clipboard_text)
    

root = tk.Tk()
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = tk.Text(root, width=400, height=400)
text.pack()

# CONFIGURE MENUBAR
menubar = tk.Menu(root)

## CONFIGURE FILE MENU
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

##  CONFIGURE EDIT MENU
editmenu = tk.Menu(menubar)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)

newFile()
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python"\
          to true' ''')
root.mainloop()

