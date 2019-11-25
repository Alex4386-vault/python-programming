import tkinter as tk
import tkinter.messagebox

mainWindow = tk.Tk()
mainWindow.title("Login")

idSection = tk.Frame(mainWindow)
idLabel = tk.Label(idSection, text="ID")
idEntry = tk.Entry(idSection)

idSection.pack(side=tk.TOP)
idLabel.pack(side=tk.TOP)
idEntry.pack(fill=tk.BOTH, side=tk.TOP)

pwdSection = tk.Frame(mainWindow)
pwdLabel = tk.Label(pwdSection, text="PWD")
pwdEntry = tk.Entry(pwdSection, show="*")

pwdSection.pack(side=tk.TOP)
pwdLabel.pack(side=tk.TOP)
pwdEntry.pack(fill=tk.BOTH, side=tk.TOP)

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

controlSection = tk.Frame(mainWindow)

adminVar = tk.IntVar(controlSection)
adminChk = tk.Checkbutton(controlSection, text="admin", variable=adminVar)
loginBtn = tk.Button(controlSection, text="Login", bg="black", fg="white", command=loginHandler, highlightbackground="black")
cancelBtn = tk.Button(controlSection, text="Cancel", bg="black", fg="white", command=cancel, highlightbackground="black")

controlSection.pack(side=tk.TOP)
adminChk.pack(side=tk.LEFT)
cancelBtn.pack(side=tk.RIGHT)
loginBtn.pack(side=tk.RIGHT)

mainWindow.mainloop()
