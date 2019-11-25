import tkinter as tk

rootWin = tk.Tk()

greetLabel = tk.Label(rootWin, text="안녕")

def langKoHandler():
    greetLabel['text'] = "안녕"

def langEnHandler():
    greetLabel['text'] = "Hello"

def langEsHandler():
    greetLabel['text'] = "Hola"


korBtn = tk.Button(rootWin, text="한구거", highlightbackground="yellow", bg="yellow", command=langKoHandler)
engBtn = tk.Button(rootWin, text="English", highlightbackground="green", bg="green", command=langEnHandler)
spaBtn = tk.Button(rootWin, text="Spanish", highlightbackground="purple", bg="purple", command=langEsHandler)

greetLabel.pack(side=tk.TOP, fill=tk.BOTH)

korBtn.pack(side=tk.TOP, fill=tk.BOTH)
engBtn.pack(side=tk.TOP, fill=tk.BOTH)
spaBtn.pack(side=tk.TOP, fill=tk.BOTH)

rootWin.mainloop()
