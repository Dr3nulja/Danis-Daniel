#02.05.2023
#graphic design for project
#Danis Nizamov, Daniel Stikkel JPTV22

#02.05.2023
#graphic design for project
#Danis Nizamov JPTV22

import tkinter as tk
window = tk.Tk()
window.geometry("1280x960")
window.title("Word maker game")


label = tk.Label(text="Word maker game", width=15, height=5, font=("Arial", 17))
label.pack()


label = tk.Label(text="_"*1000)
label.pack()


label = tk.Label(text="Letters: ", font=("Arial", 15))
label.pack(anchor="w")


label = tk.Label(text="_"*1000)
label.pack()

entry = tk.Entry(width=17, font=("Arial", 24))
entry.pack(padx=6, pady=6)


def myClick():
    word = entry.get()
    listbox.insert(0, word)


listbox = tk.Listbox(height = 15,
                  width = 33,
                  bg = "grey",
                  activestyle = 'dotbox',
                  font = "Arial",
                  fg = "white")
scrollbar = tk.Scrollbar()
scrollbar.pack(side = "right", fill= "both")
for values in range(0):
    listbox.insert("end", values)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack() 


button = tk.Button(text="Add Word to Listbox", command=myClick, font=("Arial", 12))
button.pack(anchor="n")


button = tk.Button(text="Save", font=("Arial", 15))
button.place(x="25", y="15")
button.pack(anchor="se")


def myQuit():
    window.destroy()
    window.quit()


button = tk.Button(text="Quit", font=("Arial", 15), command=myQuit)
button.place(x="25", y="35")
button.pack(anchor="se")

input()
