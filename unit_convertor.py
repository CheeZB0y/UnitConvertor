import tkinter as tk
from unit_converter.converter import converts

class unitConvertor:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Universal Unit Convertor")
        self.root.geometry("350x450")

        self.label = tk.Label(self.root, text="Universal Unit Convertor", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.distance_options = ["Meters", "Kilometers", "Feet", "Miles"]

        self.distance_label = tk.Label(self.root, text="Distance", font=("Arial", 14))
        self.distance_label.pack(padx=10, pady=20, anchor='w')

        self.dist_dropdown_frame = tk.Frame(self.root)
        self.dist_dropdown_frame.pack(padx=10, pady=1, fill="x")

        # First Distance Dropdown

        self.distance_value1 = tk.StringVar()
        self.distance_value1.set(self.distance_options[0])
        self.distance_dropdown1 = tk.OptionMenu(self.dist_dropdown_frame, self.distance_value1, *self.distance_options)
        self.distance_dropdown1.grid(row=0, column=0, padx=10, pady=5)

        # Distance To Text

        self.dist_to_text = tk.Label(self.dist_dropdown_frame, text="TO")
        self.dist_to_text.grid(row=0, column=1, padx=5, pady=5)

        # Second Distance Dropdown

        self.distance_value2 = tk.StringVar()
        self.distance_value2.set(self.distance_options[2])

        self.distance_dropdown2 = tk.OptionMenu(self.dist_dropdown_frame, self.distance_value2, *self.distance_options)
        self.distance_dropdown2.grid(row=0, column=2, padx=10, pady=5)

        self.root.mainloop()

unitConvertor()