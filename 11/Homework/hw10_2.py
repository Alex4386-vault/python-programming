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
