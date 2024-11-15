import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import random
import numpy as np
from sympy import symbols, Eq, solve, integrate, diff
from sympy.matrices import Matrix
from scipy.fft import fft
import base64
import matplotlib.pyplot as plt

class UltimateCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Ultimate Calculator")
        self.geometry("600x1000")
        self.resizable(0, 0)

        self.expression = ""
        self.result_var = tk.StringVar()
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Display
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=8, width=20, justify='right')
        entry.grid(row=0, column=0, columnspan=5, pady=10)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 'Solve',
            '4', '5', '6', '*', 'Matrix',
            '1', '2', '3', '-', 'Prime',
            '0', '.', '=', '+', 'FFT',
            'C', 'Stats', 'Integrate', 'Differentiate', 'Geometry',
            'Rand Int', 'Rand Float', 'Bin->Dec', 'Dec->Bin', 'Unit Conv',
            'Roman->Int', 'Int->Roman', 'Base64 Encode', 'Base64 Decode', 'Physics',
            'Graph', 'Multi-Equation', 'Clear History', 'History', 'Quit'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(
                self, text=button, padx=20, pady=20, font=("Arial", 12),
                command=lambda b=button: self.on_button_click(b)
            ).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            self.calculate_result()
        elif char == 'C':
            self.clear_display()
        elif char == 'Solve':
            self.solve_equation()
        elif char == 'Matrix':
            self.matrix_operations()
        elif char == 'Stats':
            self.statistical_tools()
        elif char == 'Prime':
            self.prime_tools()
        elif char == 'Rand Int':
            self.random_integer()
        elif char == 'Rand Float':
            self.random_float()
        elif char == 'Integrate':
            self.integrate_function()
        elif char == 'Differentiate':
            self.differentiate_function()
        elif char == 'Bin->Dec':
            self.binary_to_decimal()
        elif char == 'Dec->Bin':
            self.decimal_to_binary()
        elif char == 'Roman->Int':
            self.roman_to_integer()
        elif char == 'Int->Roman':
            self.integer_to_roman()
        elif char == 'Base64 Encode':
            self.base64_encode()
        elif char == 'Base64 Decode':
            self.base64_decode()
        elif char == 'FFT':
            self.fourier_transform()
        elif char == 'Graph':
            self.plot_graph()
        elif char == 'Multi-Equation':
            self.multi_equation_solver()
        elif char == 'Unit Conv':
            self.unit_conversion()
        elif char == 'Geometry':
            self.geometry_tools()
        elif char == 'Physics':
            self.physics_calculator()
        elif char == 'History':
            self.show_history()
        elif char == 'Clear History':
            self.clear_history()
        elif char == 'Quit':
            self.quit()
        else:
            self.add_to_expression(char)

    # Additional advanced features implemented below
    def fourier_transform(self):
        data = simpledialog.askstring("FFT", "Enter data points separated by commas:")
        try:
            data_points = list(map(float, data.split(',')))
            result = fft(data_points)
            messagebox.showinfo("FFT Result", f"Transformed Data: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input! {e}")

    def base64_encode(self):
        text = simpledialog.askstring("Base64 Encode", "Enter text to encode:")
        try:
            encoded = base64.b64encode(text.encode()).decode()
            messagebox.showinfo("Base64 Encode", f"Encoded: {encoded}")
        except Exception:
            messagebox.showerror("Error", "Invalid input!")

    def base64_decode(self):
        encoded_text = simpledialog.askstring("Base64 Decode", "Enter Base64 encoded text:")
        try:
            decoded = base64.b64decode(encoded_text.encode()).decode()
            messagebox.showinfo("Base64 Decode", f"Decoded: {decoded}")
        except Exception:
            messagebox.showerror("Error", "Invalid input!")

    def roman_to_integer(self):
        roman = simpledialog.askstring("Roman to Integer", "Enter Roman numeral:")
        try:
            roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            integer = 0
            prev_value = 0
            for char in reversed(roman.upper()):
                value = roman_map[char]
                if value < prev_value:
                    integer -= value
                else:
                    integer += value
                prev_value = value
            messagebox.showinfo("Roman to Integer", f"Integer: {integer}")
        except Exception:
            messagebox.showerror("Error", "Invalid Roman numeral!")

    def integer_to_roman(self):
        number = simpledialog.askinteger("Integer to Roman", "Enter an integer:")
        try:
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4, 1
            ]
            syms = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"
            ]
            roman = ''
            i = 0
            while number > 0:
                for _ in range(number // val[i]):
                    roman += syms[i]
                    number -= val[i]
                i += 1
            messagebox.showinfo("Integer to Roman", f"Roman: {roman}")
        except Exception:
            messagebox.showerror("Error", "Invalid number!")

    def unit_conversion(self):
        try:
            unit = simpledialog.askstring("Unit Conversion", "Enter conversion (e.g., 'km to miles'):") 
            value = simpledialog.askfloat("Unit Conversion", "Enter value:")
            conversions = {
                'km to miles': 0.621371,
                'miles to km': 1.60934,
                'kg to lbs': 2.20462,
                'lbs to kg': 0.453592,
                'c to f': lambda x: x * 9/5 + 32,
                'f to c': lambda x: (x - 32) * 5/9
            }
            if unit in conversions:
                result = conversions[unit](value) if callable(conversions[unit]) else value * conversions[unit]
                messagebox.showinfo("Unit Conversion", f"Converted Value: {result}")
        except Exception:
            messagebox.showerror("Error", "Invalid input!")

    def plot_graph(self):
        try:
            # Prompt user to input the function and range
            func = simpledialog.askstring("Plot Graph", "Enter a function of x (e.g., x**2 + 2*x + 1):")
            x_start = simpledialog.askfloat("Plot Graph", "Enter the start value of x:")
            x_end = simpledialog.askfloat("Plot Graph", "Enter the end value of x:")

            if not func or x_start is None or x_end is None:
                messagebox.showwarning("Warning", "All inputs are required!")
                return

            # Generate x values and evaluate the function
            x = np.linspace(x_start, x_end, 500)
            y = [eval(func, {'x': val, 'np': np, 'math': math}) for val in x]

            # Plot the graph
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, label=f"y = {func}")
            plt.title("Graph of the Function")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)
            plt.legend()
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
if __name__ == "__main__":
    app = UltimateCalculator()
    app.mainloop()
