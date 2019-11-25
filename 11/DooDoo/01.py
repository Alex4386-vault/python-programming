import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, bg="green", fg="white")
label1['text'] = "UNDERTALE ASHINEUNGOONA"
label1.pack()

label2 = tkinter.Label(window, text="I HATE PYTHON SYNTAX", bg="red", fg="black", font="Halvetica, 50")
label2.pack()

label3 = tkinter.Label(window, text="C++ Forever :heart:")
label3.pack()

window.mainloop()
