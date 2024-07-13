from tkinter import *


def button_clicked():
    my_label.config(text=my_input.get())
    print("I got clicked")


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button1
button_1 = Button(text="Click Me", command=button_clicked)
button_1.grid(column=1, row=1)

# Button2
button_2 = Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()
