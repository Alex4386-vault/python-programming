## Homework 1

import tkinter as tk

# macOS Catalina Image Rendering issue resolve
whatIsAComputer = False

import sys

if sys.platform == "darwin":
    whatIsAComputer = True
    import PIL.Image
    import PIL.ImageTk
    
# macOS Catalina Image Rendering issue resolve section end

rootWindow = tk.Tk()
rootWindow.title("Map")

topbar = tk.Frame(rootWindow)
title = tk.Label(topbar, text="MAP", font=("Halvetica", 16))

title.pack(side=tk.TOP)

selectionSection = tk.Frame(topbar)
selectionData = {}
selectVar = tk.StringVar(value="africa")

worldMapList = {
    "africa": {
        "labelName": "Africa",
        "fileName": "africa.png"
    },
    "america": {
        "labelName": "America",
        "fileName": "america.png"
    },
    "asia": {
        "labelName": "Asia",
        "fileName": "asia.png"
    },
    "europe": {
        "labelName": "Europe",
        "fileName": "europe.png"
    }
}

def updateImg():
    imgLabel['image'] = worldMapList[selectVar.get()]['image']

# the counter measure for old versions of python where
# dictionaries are not sorted by the keys
for i in sorted(list(worldMapList.keys())):
    labelName = worldMapList.get(i).get("labelName")
    fileName = worldMapList.get(i).get("fileName")
    print(i, labelName, fileName)
    
    # A Workaround.... for macOS catalina 10.15.1
    if whatIsAComputer:
        tempImage = PIL.Image.open(fileName)
        worldMapList[i]["image"] = PIL.ImageTk.PhotoImage(tempImage)
    else:
        tempImage = tk.PhotoImage(file=fileName)
        worldMapList[i]["image"] = tempImage

    selectionData[i] = tk.Radiobutton(selectionSection, text=labelName, fg="black", variable=selectVar, value=i, command=updateImg)
    selectionData[i].pack(side=tk.LEFT)

selectionSection.pack(side=tk.TOP)

topbar.pack()

imgLabel = tk.Label(rootWindow, image=worldMapList['africa']['image'], bg="blue")
imgLabel.pack(fill=tk.BOTH, expand=tk.YES)
rootWindow.mainloop()


## Homework 2

import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Contact")

tk.Label(mainWindow, text="name : ").grid(row=0, column=0)
nameEntry = tk.Entry(mainWindow)
nameEntry.grid(row=0,column=1,columnspan=2)

tk.Label(mainWindow, text="contact : ").grid(row=1, column=0)
contactEntry = tk.Entry(mainWindow)
contactEntry.grid(row=1,column=1,columnspan=2)

totalCount = 0

def addThing():
    global totalCount

    name = nameEntry.get()
    contact = contactEntry.get()

    if name == "" or contact == "":
        return

    formatStr = "{:10s} {:20s}".format(name, contact)
    nameEntry.delete(0, tk.END)
    contactEntry.delete(0, tk.END)
    theListbox.insert(tk.END, formatStr)
    
    totalCount += 1
    totalCountLabel['text'] = "total : "+str(totalCount)


tk.Button(mainWindow, text="Insert", command=addThing).grid(row=2, column=0, columnspan=3, sticky="ew")

totalCountLabel = tk.Label(mainWindow, text="total : "+str(totalCount), anchor=tk.W)
totalCountLabel.grid(row=3, column=0, columnspan=3, sticky="ew")

theListbox = tk.Listbox(mainWindow, height=7, selectmode=tk.SINGLE)
theListbox.grid(row=4, column=0, rowspan=6, columnspan=3, sticky="ew")
theListbox.insert(tk.END, "{:10s} {:20s}".format("name", "contact"))

mainWindow.mainloop()
