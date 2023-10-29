import tkinter as tk
import pandas as pd
import numpy as np
# from tkinter import filedialog
import os

import tkinter as tk

import tkinter as tk
from tkinter import filedialog

# Model
class Calculator:
    def add(self, a, b):
        return a + b

# View
class CalculatorView:
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        master.title("Magic Accounting")
        
        # Entry boxes for numbers
        self.entry_a = tk.Entry(master)
        self.entry_a.pack()
        
        self.entry_b = tk.Entry(master)
        self.entry_b.pack()

        # Button to perform addition
        self.add_button = tk.Button(master, text="Add", command=self.add)
        self.add_button.pack()
        
        # Button to select file paths
        self.path_button = tk.Button(master, text="Select Files", command=self.select_files)
        self.path_button.pack()

        # Label to display the result of addition
        self.result_label = tk.Label(master, text="Result: ")
        self.result_label.pack()

        # Label to display selected paths
        self.paths_label = tk.Label(master, text="Selected Paths: None")
        self.paths_label.pack()
        
        # Variable to store selected file paths
        self.selected_paths = []

    def add(self):
        """Perform addition using the model and update the result label."""
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        result = self.controller.add(a, b)
        self.result_label.config(text=f"Result: {result}")

    def select_files(self):
        """Open file dialog to select multiple files and update the paths label."""
        self.selected_paths = filedialog.askopenfilenames()
        self.paths_label.config(text=f"Selected Paths: {', '.join(self.selected_paths)}")

# Controller
class CalculatorController:
    def __init__(self):
        self.model = Calculator()
        self.root = tk.Tk()
        self.view = CalculatorView(self.root, self)
        
    def add(self, a, b):
        return self.model.add(a, b)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CalculatorController()
    app.run()

