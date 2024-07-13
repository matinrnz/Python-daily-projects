from tkinter import *


def calculate():
    miles = float(input_miles.get())
    kilometers = round(miles * 1.609)
    result_label.config(text=kilometers)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=("Ariel", 18))
miles_label.grid(column=2, row=0)

eq_label = Label(text="is equal to", font=("Ariel", 18))
eq_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Ariel", 18))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Ariel", 18))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
