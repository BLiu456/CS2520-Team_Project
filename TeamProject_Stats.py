#Names: Benjamin Liu & Abraham Medina
#Team Project: Statsitical Anaylsis with CSV files
#Sources for CSV files: https://climate.nasa.gov/vital-signs/global-temperature/ ~~~ For global temperatures
#                       https://devstronomy.com/#/ ~~~ For planet data

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox as mb
import matplotlib.pyplot as plt
import pandas

def fileSelect():  #Let's user to browse for the csv file, path to file will be placed in entry box
    filename = filedialog.askopenfilename()
    entryFile.delete(0, END) #Clear entry box before inserting filename
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

def createTreeView(data, stats):
    dataTree = ttk.Treeview(root, show = "headings", selectmode = 'browse', height = 5) #Tree view properties
    dataTree.place(relx = 0.02, rely = 0.4, height = 290, width = 752)

    #Defining scroll bars for the tree view
    vScroll = ttk.Scrollbar(root, orient = VERTICAL, command = dataTree.yview)
    dataTree.configure(yscrollcommand = vScroll)
    vScroll.place(relx= 0.96, rely = 0.4, height = 290, width = 16)

    hScroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = dataTree.xview)
    dataTree.configure(xscrollcommand = hScroll)
    hScroll.place(y = 2, relx = 0.02, rely = 0.88, width = 752)
    
    #colList = list(data.columns) 
    dataTree['columns'] = colList #Defining the columns of the tree view

    for d in colList: #Setting the properties/name of each column
        dataTree.column(d, width = 75, minwidth = 10, anchor = CENTER) #Setting column size
        dataTree.heading(d, text=d) #Setting the column names in the GUI

    for d in data.values: #Insert values row by row
        dataTree.insert('', 'end', values = tuple(d))

    for s in stats: #Insert the stastical 
        dataTree.insert('', 'end', values = tuple(s))

def process():
    try:
        global data, colList #Other functions may need these values
        data = pandas.read_csv(entryFile.get(), skipinitialspace=TRUE) #Where all the data from the file will be stored
        colList = list(data.columns) #Pulling the columns from the data set
        
        #creation of lists to hold names and values
        statCollection = []

        valTotal = ['Total']
        statCollection.append(valTotal + list(round(data.loc[:, data.columns != colList[0]].sum(numeric_only=True), 2))) #Excludes the first column and then performs the statstical calculation

        valMin = ['Min']
        statCollection.append(valMin + list(data.loc[:, data.columns != colList[0]].min(numeric_only=True)))

        valMax = ['Max']
        statCollection.append(valMax + list(data.loc[:, data.columns != colList[0]].max(numeric_only=True)))

        valMean = ['Mean']
        statCollection.append(valMean + list(round(data.loc[:, data.columns != colList[0]].mean(numeric_only=True), 2)))

        valMedian = ['Median']
        statCollection.append(valMedian + list(data.loc[:, data.columns != colList[0]].median(numeric_only=True)))

        valStdDev = ['Standard Deviation']
        statCollection.append(valStdDev + list(round(data.loc[:, data.columns != colList[0]].std(numeric_only=True), 2)))

        clear() #Clearing the current window to make room for the new window
        root.geometry('800x600')
        createTreeView(data, statCollection) #Calls function to display the data in the file in a tree view

        #Placing buttons for the new window
        resetButton = Button(root, text = "Reset", font = ("Roboto", 12), command = loadFileInput) 
        resetButton.place(relx = 0.25, rely = 0.2, anchor = CENTER)

        barButton = Button(root, text = "Bar Graph", font = ("Roboto", 12), command = barHelper) 
        barButton.place(relx = 0.7, rely = 0.13, anchor = CENTER)
        
        pieButton = Button(root, text = "Pie Graph", font = ("Roboto", 12), command = pieHelper) 
        pieButton.place(relx = 0.7, rely = 0.20, anchor = CENTER)
        
        lpButton = Button(root, text = "Lollipop Graph", font = ("Roboto", 12), command = lpHelper) 
        lpButton.place(relx = 0.7, rely = 0.27, anchor = CENTER)
    except IOError:
        mb.showinfo('', 'Could not open file')

def radioHelper(func): #Opens a new window to let the user select which data they would like to display on the graphs
    tempWindow = Tk()
    tempWindow.resizable(False, True)
    tempWindow.geometry('200x200')    

    global radioOp
    radioOp = StringVar(tempWindow) #Remembers which radio button was selected 
    isFirstCol = True #To skip the first column

    for c in data.columns:
        if isFirstCol:
            isFirstCol = False
            continue
        Radiobutton(tempWindow, text = c, variable = radioOp, value = c).pack(anchor = CENTER)
    
    Button(tempWindow, text = "Confirm", font = ("Roboto", 12), command = func).pack(anchor = S) #func calls the respective graph the user wants to view
    Button(tempWindow, text = "Exit Graph", font = ("Roboto", 12), command = tempWindow.destroy).pack(anchor = S) #Exits out the selection window

#Helper functions will pass the function name of their respective graphs to the radioHelper function.
def barHelper(): 
    radioHelper(barGraph)

def barGraph(): 
    #colList = list(data.columns)
    labelList = list(data[colList[0]])
    valList = list(data[radioOp.get()]) #Takes the set of values corresponding to the column the user selected

    try:
        plt.clf()    
        plt.bar(labelList, valList)
        plt.xlabel(colList[0])
        plt.ylabel(colList[colList.index(radioOp.get())])   
        plt.show()
    except:
        mb.showinfo('', 'Could not create bar chart from this data set')

def pieHelper():
    radioHelper(pieGraph)

def pieGraph():   
    #colList = list(data.columns)
    labelList = list(data[colList[0]])
    valList = list(data[radioOp.get()]) #Takes the set of values corresponding to the column the user selected
    try:
        plt.clf()
        plt.pie(valList, labels = labelList, autopct='%1.1f%%')
        plt.show()
    except:
        mb.showinfo('', 'Could not create pie chart from this data set') #Will typically occur if there are negative values

def lpHelper():
    radioHelper(lpGraph)

def lpGraph():
    #colList = list(data.columns)
    labelList = list(data[colList[0]])
    valList = list(data[radioOp.get()]) #Takes the set of values corresponding to the column the user selected
    
    try:    
        plt.clf()
        (markers, stemlines, baseline) = plt.stem(labelList, valList, bottom = 0)
        plt.setp(markers, marker='*', markersize=10, markeredgecolor="red", markeredgewidth=2) #Customizing the graph     
        plt.xlabel(colList[0])
        plt.ylabel(colList[colList.index(radioOp.get())])  
        plt.show()
    except:
        mb.showinfo('', 'Could not create lollipop chart from this data set')

#GUI setup
root = Tk()
root.resizable(False, False) #Disable window resizing so the GUI does not get messed up

entryFile = Entry(root) 
loadFileInput()

#Display the GUI
root.mainloop()