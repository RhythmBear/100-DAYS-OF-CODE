from tkinter import *
KM_TEXT = 0
FONT = ("Courier", 12)

my_window = Tk()
my_window.title("Mile to Kilo Converter")
my_window.minsize(width=300, height=150)
my_window.config(padx=25, pady=25)


def mile_converter():
    mile_value = mile_entry.get()
    if mile_value != 0:
        km = round(float(mile_value) * 1.609, 4)
        label_km_value.config(text=km, font=FONT)


# Create buttons
my_button = Button(text="Calculate", command=mile_converter, font=FONT)
my_button.grid(row=2, column=1)


# Create the Entry
mile_entry = Entry(width=10, justify="center", font=FONT)
mile_entry.grid(row=0, column=1)

# Create the Labels
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)

label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)

label_equals = Label(text="Is equal to ", font=FONT)
label_equals.grid(column=0, row=1)

label_km_value = Label(text=KM_TEXT, font=FONT)
label_km_value.grid(row=1, column=1)


my_window.mainloop()
