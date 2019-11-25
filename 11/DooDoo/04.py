import tkinter as tk

window = tk.Tk()
window.geometry("300x300+100+100")

window.title = "ANG?"

def btn1Callback():
    print("ANG?")
    label1['text'] = "ANG!!"

btn1 = tk.Button(window, text='ANG?', fg="black", command=btn1Callback)
btn1.pack(fill=tk.BOTH)

label1 = tk.Label(window, text="HUH", font=('Halvetica', 30))
label1.pack()

window.mainloop()