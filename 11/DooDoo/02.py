import tkinter

window = tkinter.Tk()

def buttonClickHandler():
    print("ANG?")

btn = tkinter.Button(window, text="Click this for best experience ever",  font=('Halvetica', 16), command=buttonClickHandler)

btn.pack()

window.mainloop()
