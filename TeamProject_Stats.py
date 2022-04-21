#Names: Benjamin Liu & Abraham Medina
#Team Project: Statsitical Anaylsis with CSV files
from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
import pandas

def fileSelect(): #Let's user to browse for the csv file, path to file will be placed in entry box
    filename = filedialog.askopenfilename()
    entryFile.insert(0, filename)

def loadFileInput():
    clear()
    root.geometry('402x300') #Size of window
    
    #Placing entry box for user to type in the file if they choose to
    #Note: File must be placed in the same folder as program in order for it to open the file if typed in
    #      Alternatively the user could type the file path, but in that case they should just use the browse button   
    global entryFile
    entryFile = Entry(root)
    entryFile.place(relx = 0.45, rely = 0.5, anchor = CENTER, height = 20, relwidth = 0.5)

    #Placing button to browse files 
    fileButton = Button(root, text = "Browse", font = ("Roboto", 12), command = fileSelect) 
    fileButton.place(relx = 0.8, rely = 0.5, anchor = CENTER)

    #Placing button to process data from file in entry box
    processButton = Button(root, text = "Process", font = ("Roboto", 12), command = process) 
    processButton.place(relx = 0.45, rely = 0.63, anchor = CENTER) 

    #Label
    inputLabel = Label(root, text = "Input CSV file", font = ("Roboto", 12))
    inputLabel.place(relx = 0.45, rely = 0.4, anchor = CENTER)

def clear():
    for i in root.winfo_children():
        i.destroy()

def createTreeView(data):
    dataTree = ttk.Treeview(root, show = "headings", selectmode = 'browse', height = 5)
    dataTree.place(relx = 0.02, rely = 0.4, height = 290, width = 752)

    #Defining scroll bars for the tree view
    vScroll = ttk.Scrollbar(root, orient = VERTICAL, command = dataTree.yview)
    dataTree.configure(yscrollcommand = vScroll)
    vScroll.place(relx= 0.96, rely = 0.4, height = 290, width = 16)

    hScroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = dataTree.xview)
    dataTree.configure(xscrollcommand = hScroll)
    hScroll.place(y = 2, relx = 0.02, rely = 0.88, width = 752)
    
    colList = list(data.columns) #data.columns has other values associated with it. So create a new list with only the columns
    dataTree['columns'] = colList #Defining the columns of the tree view

    for d in colList:
        dataTree.column(d, width = 30, minwidth = 10, anchor = CENTER) #Setting column size
        dataTree.heading(d, text=d) #Setting the column names in the GUI

    for d in data.values:
        dataTree.insert('', 'end', values = tuple(d))

def process():
    try:
        data = pandas.read_csv(entryFile.get(), skipinitialspace=TRUE)

        clear()
        root.geometry('800x600')
        createTreeView(data)

        resetButton = Button(root, text = "Reset", font = ("Roboto", 12), command = loadFileInput) 
        resetButton.place(relx = 0.45, rely = 0.2, anchor = CENTER)
    except IOError:
        print('Can not open file')
    
#GUI setup
root = Tk()
root.resizable(False, False) #Disable window resizing so the GUI does not get messed up

entryFile = Entry(root) 
loadFileInput()

#Display the GUI
root.mainloop()