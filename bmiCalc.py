import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
FILE_NAME="bmi_data.csv"
def calculate_bmi():
    try:
        name=name_entry.get().strip()
        weight=float(weight_entry.get())
        height=float(height_entry.get())
        if not name:
            messagebox.showerror("Error","Name cannot be empty")
            return
        if weight<=0 or height<=0:
            messagebox.showerror("Error","Height and Weight must be positive")
            return
        if height>3:
            messagebox.showerror("Error","Height should be in meters(e.g.,1.75)")
            return
        bmi=weight/(height**2)
        category=get_category(bmi)
        result_label.config(text=f"BMI:{bmi:.2f}({category})")
        save_data(name,weight,height,bmi)
    except ValueError:
        messagebox.showerror("Error","Please enter valid numbers")
def get_category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi<25:
        return "Normal"
    elif 25<=bmi<30:
        return "Overweight"
    else:
        return "Obese"
def save_data(name,weight,height,bmi):
    file_exists=os.path.isfile(FILE_NAME)
    with open(FILE_NAME,"a",newline="") as file:
        writer=csv.writer(file)
        if not file_exists:
            writer.writerow(["Name","Weight","Height","BMI","Date"])
        writer.writerow([name,weight,height,bmi,datetime.now()])
def view_history():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo("Info","No data found")
        return
    history_window=tk.Toplevel(root)
    history_window.title("BMI History")
    text=tk.Text(history_window,width=80,height=20)
    text.pack()
    with open(FILE_NAME,"r") as file:
        text.insert(tk.END,file.read())
def show_graph():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo("Info","No data found")
        return
    names=[]
    bmis=[]
    with open(FILE_NAME, "r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            names.append(row["Name"])
            bmis.append(float(row["BMI"]))
    plt.figure()
    plt.plot(names,bmis,marker="o")
    plt.title("BMI Trend")
    plt.xlabel("User")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
root=tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x400")
tk.Label(root,text="Name").pack()
name_entry=tk.Entry(root)
name_entry.pack()
tk.Label(root,text="Weight(kg)").pack()
weight_entry=tk.Entry(root)
weight_entry.pack()
tk.Label(root,text="Height(m)").pack()
height_entry=tk.Entry(root)
height_entry.pack()
tk.Button(root,text="Calculate BMI",command=calculate_bmi).pack(pady=5)
tk.Button(root,text="View History",command=view_history).pack(pady=5)
tk.Button(root,text="Show BMI Trend Graph",command=show_graph).pack(pady=5)
result_label=tk.Label(root,text="",font=("Arial",12,"bold"))
result_label.pack(pady=10)
root.mainloop()