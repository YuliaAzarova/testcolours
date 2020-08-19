from random import *
from tkinter import *
from time import *

window = Tk()
window.geometry('270x300')
window.config(bg = 'hot pink')
window.title('Тест цвета')

listbox = Listbox(width = 13, height = 8,
                  selectbackground = 'olive',bg = 'sea green',
                  font = 'Times 18')
listbox.grid(row = 0, column = 0)

for colors in 'lime', 'medium blue', 'bisque', 'coral':
    listbox.insert(END, colors)

label = Label(bg = 'old lace', width = 13, height = 11)
label.grid(row = 0, column = 1, columnspan = 2)

def Click(event):
    x = listbox.curselection()
    label['bg'] = listbox.get(x)

button = Button(text = 'Жми!', font = 'Times 18')
button.grid(row = 1, column = 0)
button.bind('<Button-1>', Click)

entry = Entry(bg = 'cyan', width = 10)
entry.grid(row = 1, column = 1)

def OnClick(event):
    listbox.insert(END, entry.get())

but = Button(text = 'Add', font = 'Times 18')
but.grid(row = 1, column = 2)
but.bind('<Button-1>', OnClick)

window.mainloop()
