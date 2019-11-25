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

