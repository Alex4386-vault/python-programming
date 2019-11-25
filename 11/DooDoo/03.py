import tkinter as tk

window = tk.Tk()
window.geometry("300x300+100+100")

window.title = "ANG?"

btn1 = tk.Button(window, text='1')
btn1.pack(side=tk.LEFT)

btn2 = tk.Button(window, text='2')
btn2.pack(side=tk.LEFT)

window.mainloop()