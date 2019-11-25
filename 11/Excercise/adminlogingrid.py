import tkinter as tk
import tkinter.messagebox

mainWindow = tk.Tk()
mainWindow.title("Login")

tk.Label(mainWindow, text="ID").grid(row=0, column=0)
idEntry = tk.Entry(mainWindow).grid(row=0, column=1, columnspan=3)

tk.Label(mainWindow, text="PWD").grid(row=1, column=0)
pwdEntry = tk.Entry(mainWindow, show="*").grid(row=1, column=1, columnspan=3)

def loginHandler():
    theId = idEntry.get()
    thePwd = pwdEntry.get()

    if theId == "python":
        if thePwd == "tkinter":
            if adminVar.get() == 1:
                tk.messagebox.showinfo("Login Success!", "Login Success! Welcome admin "+theId+"!")
            else:
                tk.messagebox.showinfo("Login Success!", "Login Success! Welcome user "+theId+"!")
        else:
            tk.messagebox.showerror("Login Failed!", "Check your password!")
    else:
        tk.messagebox.showerror("Login Failed!", "Check your username!")

def cancel():
    tk.messagebox.showwarning("CANCELLED!", "Bird up! Bwah Bwah Bwah!")
    mainWindow.quit()

adminVar = tk.IntVar(mainWindow)
tk.Checkbutton(mainWindow, text="admin", variable=adminVar).grid(row=2, column=0, columnspan=2)
tk.Button(mainWindow, text="Login", bg="black", fg="white", command=loginHandler, highlightbackground="black").grid(row=2, column=2)
tk.Button(mainWindow, text="Cancel", bg="black", fg="white", command=cancel, highlightbackground="black").grid(row=2, column=3)


mainWindow.mainloop()
