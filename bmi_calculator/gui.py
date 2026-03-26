import tkinter as tk
from tkinter import messagebox
from .core import calculate_bmi, get_bmi_category

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        title_label = tk.Label(self.root, text="BMI Calculator", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Height (cm):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.height_var = tk.StringVar()
        height_entry = tk.Entry(input_frame, textvariable=self.height_var, width=15)
        height_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.weight_var = tk.StringVar()
        weight_entry = tk.Entry(input_frame, textvariable=self.weight_var, width=15)
        weight_entry.grid(row=1, column=1, padx=5, pady=5)

        calc_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate)
        calc_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=5)

    def calculate(self):
        try:
            height = float(self.height_var.get())
            weight = float(self.weight_var.get())

            if height <= 0 or weight <= 0:
                messagebox.showerror("Error", "Height and Weight must be positive values.")
                return

            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)

            self.result_label.config(text=f"BMI: {bmi} ({category})")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

def run_gui():
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
