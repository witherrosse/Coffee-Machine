from tkinter import *

### Convert miles to kilometers and show the result ###

def miles_to_km():

    miles = float(entry_box.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


window = Tk()

window.title("Miles to KM Converter")
window.config(padx = 20, pady = 20)

### Input box for user to type miles ###

entry_box = Entry(width=12)
entry_box.grid(column=1 , row=0)

### Label showing "Miles" next to the input box ###

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

###Label showing "equal to" before the result###

is_equal_label = Label(text="equal to")
is_equal_label.grid(column=0, row=1)

### Label where the converted result will be shown ###

result_label = Label(text="0")
result_label.grid(column=1, row=1)

###  Label showing "KM" after the result ###

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

### Button that runs the conversion when clicked ###

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1, row=2)
