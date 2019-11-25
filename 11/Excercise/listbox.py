import tkinter as tk

window = tk.Tk()

def select():
    for index in lst.curselection():
        print(index, lst.get(index))
    
lst = tk.Listbox(window, height=3, selectmode=tk.MULTIPLE)

color = ['red', 'green', 'blue']

for item in color:
    lst.insert(tk.END, item)

lst.pack()

btn = tk.Button(window, text="Click Me", command=select)
btn.pack()

window.mainloop()
