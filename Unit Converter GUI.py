#56th github project --> Unit Converter GUI
print('----------Unit Converter GUI----------')
import tkinter as tk
from tkinter import ttk

LENGTH_UNITS = {
    "Meters": 1.0,
    "Kilometers": 1000.0,
    "Centimeters": 0.01,
    "Miles": 1609.344,
    "Feet": 0.3048,
    "Inches": 0.0254,
}

WEIGHT_UNITS = {
    "Kilograms": 1.0,
    "Grams": 0.001,
    "Pounds": 0.453592,
    "Ounces": 0.0283495,
}

CATEGORIES = {
    "Length": LENGTH_UNITS,
    "Weight": WEIGHT_UNITS,
}


def convert_linear(value, from_factor, to_factor):
    return value * from_factor / to_factor


def update_units(*args):
    units = list(CATEGORIES[category_var.get()].keys())
    from_unit["values"] = units
    to_unit["values"] = units
    from_unit.set(units[0])
    to_unit.set(units[1])


def convert():
    try:
        value = float(entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number.")
        return

    units = CATEGORIES[category_var.get()]
    from_name = from_unit.get()
    to_name = to_unit.get()

    if from_name not in units or to_name not in units:
        result_label.config(text="Pick valid units.")
        return

    result = convert_linear(value, units[from_name], units[to_name])
    result_label.config(text=f"{value} {from_name} = {result:.4f} {to_name}")


root = tk.Tk()
root.title("Unit Converter")

category_var = tk.StringVar(value="Length")

tk.Label(root, text="Category").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Combobox(root, textvariable=category_var,
             values=list(CATEGORIES.keys()), state="readonly",
             width=12).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="From").grid(row=1, column=0, padx=5, pady=5, sticky="w")
from_unit = ttk.Combobox(root, state="readonly", width=12)
from_unit.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="To").grid(row=2, column=0, padx=5, pady=5, sticky="w")
to_unit = ttk.Combobox(root, state="readonly", width=12)
to_unit.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Value").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry = tk.Entry(root, width=14)
entry.grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Convert", width=20, command=convert).grid(
    row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result will appear here", font=("Arial", 11))
result_label.grid(row=5, column=0, columnspan=2, pady=5)

category_var.trace_add("write", update_units)
update_units()

root.mainloop()