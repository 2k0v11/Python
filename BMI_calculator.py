import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        classify_bmi(bmi)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

def classify_bmi(bmi):
    advice = ""
    if bmi < 18.5:
        category = "Underweight"
        advice = (
            "You are underweight. Here are some steps to improve your weight:\n"
            "1. Consult with a nutritionist for a personalized meal plan.\n"
            "2. Focus on nutrient-dense foods like lean proteins, whole grains, and healthy fats.\n"
            "3. Incorporate strength training exercises to build muscle mass.\n"
            "4. Stay hydrated and get adequate sleep for overall health."
        )
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        advice = (
            "Congratulations! Your weight is in the normal range. "
            "To maintain your health, consider the following:\n"
            "1. Continue with a balanced diet rich in fruits, vegetables, and whole grains.\n"
            "2. Engage in regular physical activity, such as cardio and strength training.\n"
            "3. Prioritize mental well-being with stress management techniques."
        )
    elif 25 <= bmi < 30:
        category = "Overweight"
        advice = (
            "You are overweight. Here are steps to move towards a healthier weight:\n"
            "1. Consult with a healthcare professional for personalized advice.\n"
            "2. Adopt a balanced diet with controlled portions and reduced intake of processed foods.\n"
            "3. Increase physical activity with a mix of cardio and strength training exercises.\n"
            "4. Stay consistent and make gradual, sustainable changes to your lifestyle."
        )
    else:
        category = "Obesity"
        advice = (
            "You are in the obesity category. It's essential to take significant steps to improve your health:\n"
            "1. Consult with a healthcare professional for personalized guidance and monitoring.\n"
            "2. Adopt a well-balanced, calorie-controlled diet with a focus on whole foods.\n"
            "3. Engage in regular and varied physical activities, including aerobic and strength training.\n"
            "4. Consider support from a nutritionist, fitness trainer, or a healthcare team for a comprehensive approach."
        )

    result_label.config(text=f"Your BMI is: {bmi} ({category}).")
    messagebox.showinfo("BMI Advice", advice)

def clear_entry(event):
    event.widget.delete(0, tk.END)

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("1000x500")

# Styling
root.configure(bg="#f0f0f0")
root.option_add("*TButton*highlightBackground", "#b3b3b3")

# Header
header_label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
header_label.pack(pady=20)

# Weight Entry
weight_label = tk.Label(root, text="Weight (kg):", font=("Helvetica", 14), bg="#f0f0f0")
weight_label.pack()

weight_entry = tk.Entry(root, font=("Helvetica", 14))
weight_entry.pack()
weight_entry.insert(0, "Enter weight in kg")
weight_entry.bind("<FocusIn>", clear_entry)

# Height Entry
height_label = tk.Label(root, text="Height (m):", font=("Helvetica", 14), bg="#f0f0f0")
height_label.pack()

height_entry = tk.Entry(root, font=("Helvetica", 14))
height_entry.pack()
height_entry.insert(0, "Enter height in m")
height_entry.bind("<FocusIn>", clear_entry)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 14), bg="#4CAF50", fg="white")
calculate_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="Enter your weight and height, then click 'Calculate BMI'", font=("Helvetica", 14), bg="#f0f0f0", state="disabled")
result_label.pack()

root.mainloop()
