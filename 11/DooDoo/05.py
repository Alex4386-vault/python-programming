import tkinter as tk

window = tk.Tk()

pic1 = tk.PhotoImage(file="balloon1.png")

label1 = tk.Label(window, image=pic1)
label1.pack(fill=tk.BOTH)

window.mainloop()
