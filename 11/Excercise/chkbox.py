import tkinter as tk

mainWin = tk.Tk()
agreeVar = tk.IntVar()

agree = tk.Checkbutton(mainWin, variable=agreeVar)
agree.pack()

mainWin.mainloop()
