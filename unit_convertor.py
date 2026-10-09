import tkinter as tk
from unit_converter.converter import converts

class unitConvertor:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Universal Unit Convertor")
        self.root.geometry("340x350")

        self.label = tk.Label(self.root, text="Universal Unit Convertor", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.options = ["Meters", "Kilometers", "Feet", "Miles", "Celsius", "Fahrenheit"]

        self.dropdown_frame = tk.Frame(self.root)
        self.dropdown_frame.pack(padx=10, pady=1)

        # First Dropdown

        self.value1 = tk.StringVar()
        self.value1.set(self.options[0])
        self.dropdown1 = tk.OptionMenu(self.dropdown_frame, self.value1, *self.options)
        self.dropdown1.grid(row=0, column=0, padx=10, pady=5)

        # To Text

        self.to_text = tk.Label(self.dropdown_frame, text="TO")
        self.to_text.grid(row=0, column=1, padx=5, pady=5)

        # Second Dropdown

        self.value2 = tk.StringVar()
        self.value2.set(self.options[2])

        self.dropdown2 = tk.OptionMenu(self.dropdown_frame, self.value2, *self.options)
        self.dropdown2.grid(row=0, column=2, padx=10, pady=5)

        # Value Input

        self.entry = tk.Entry(self.dropdown_frame, width=10)
        self.entry.grid(row=1, column=0, padx=20, pady=10)

        # Convert Button

        self.button = tk.Button(self.dropdown_frame, text="Convert", command=self.calculate_input)
        self.button.grid(row=1, column=1, padx=10, pady=10)

        # Output Label

        self.output_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.output_label.pack(padx=10, pady=10)

        self.root.mainloop()

    def calculate_input(self):
            self.number_value = self.entry.get()
            self.from_unit = self.value1.get()
            self.to_unit = self.value2.get()
            self.from_simple = ""
            self.to_simple = ""

            if self.from_unit == "Meters":
                 self.from_simple = "m"
            elif self.from_unit == "Kilometers":
                 self.from_simple = "km"
            elif self.from_unit == "Feet":
                self.from_simple = "foot"
            elif self.from_unit == "Miles":
                self.from_simple = "mile"
            elif self.from_unit == "Celsius":
                self.from_simple = "°C"
            elif self.from_unit == "Fahrenheit":
                self.from_simple = "°F"

            if self.to_unit == "Meters":
                 self.to_simple = "m"
            elif self.to_unit == "Kilometers":
                 self.to_simple = "km"
            elif self.to_unit == "Feet":
                self.to_simple = "foot"
            elif self.to_unit == "Miles":
                self.to_simple = "mile"
            elif self.to_unit == "Celsius":
                self.to_simple = "°C"
            elif self.to_unit == "Fahrenheit":
                self.to_simple = "°F"

            if not self.number_value:
                 self.output_label.config(text="Please enter a value", fg="red")
                 return

            try:
                self.input_str = f"{self.number_value} {self.from_simple}"
                self.target_str = str(self.to_simple)
                self.output = converts(self.input_str, self.target_str)
                if '.' in self.output:
                    self.output = f"{float(self.output):.4f}"
                self.output_label.config(text=f"{self.output} {self.to_simple}", fg="black")

            except Exception:
                 self.output_label.config(text="Incompatible unit conversion!", fg="red")



unitConvertor()