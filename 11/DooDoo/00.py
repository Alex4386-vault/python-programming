import tkinter

window = tkinter.Tk()
window.title("Window Title")

window.geometry("300x300+100+100")

label = tkinter.Label(window, text="wa")
label.pack()

newLabel = tkinter.Label(window, bg="black", fg="white", text="SANS")
newLabel.pack()

window.mainloop()
