import tkinter as tk
from unit_converter.converter import converts

class unitConvertor:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Universal Unit Convertor")
        self.root.geometry("350x450")

        self.label = tk.Label(self.root, text="Universal Unit Convertor", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.distance_label = tk.Label(self.root, text="Distance")
        self.distance_label.pack(padx=20, pady=20)

        self.root.mainloop()

unitConvertor()