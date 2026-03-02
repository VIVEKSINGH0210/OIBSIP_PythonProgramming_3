🧮 Advanced BMI Calculator (Tkinter GUI)
📌 Project Description

The Advanced BMI Calculator is a Python-based graphical application built using Tkinter. It allows users to calculate their Body Mass Index (BMI), categorize their health status, store historical records in a CSV file, view previous data, and visualize BMI trends using graphs.

This project demonstrates GUI development, data storage, input validation, and data visualization using Python.

🚀 Features

✅ User-friendly GUI built with Tkinter

✅ BMI calculation using standard formula

✅ Automatic BMI category classification

✅ Input validation with error handling

✅ CSV-based data storage

✅ View saved history

✅ BMI trend graph visualization using Matplotlib

🧮 BMI Formula Used
𝐵𝑀𝐼=𝑊𝑒𝑖𝑔ℎ𝑡(𝑘𝑔)/𝐻𝑒𝑖𝑔ℎ𝑡(𝑚)^2​

📊 BMI Categories
BMI Range	Category
Less than 18.5	Underweight
18.5 – 24.9	Normal
25 – 29.9	Overweight
30 and above	Obese
🛠️ Technologies Used

Python 3.x

Tkinter (GUI)

CSV (Data Storage)

Matplotlib (Graph Visualization)

Datetime module

📂 Project Structure
Advanced-BMI-Calculator/
│
├── bmi_calculator.py
├── bmi_data.csv (auto-generated after first entry)
└── README.md
▶️ How to Run the Project
1️⃣ Install Required Libraries

Tkinter comes pre-installed with Python.

Install Matplotlib (if not installed):

pip install matplotlib
2️⃣ Run the Program
python bmi_calculator.py
🖥️ Application Interface

The application provides:

Name input field

Weight input (in kg)

Height input (in meters)

Calculate BMI button

View History button

Show BMI Trend Graph button

📊 Data Storage

All records are stored in bmi_data.csv

Data includes:

Name

Weight

Height

BMI

Date & Time

📈 BMI Trend Graph

Displays BMI values of users

Shows trend using line graph

Uses Matplotlib for visualization

⚠️ Input Validation

The application ensures:

Name cannot be empty

Height and Weight must be positive

Height must be in meters (example: 1.75)

Only numeric values are accepted

🎯 Learning Outcomes

This project helps understand:

GUI development with Tkinter

Event-driven programming

File handling in Python

CSV data storage

Data visualization

Error handling and validation

🔮 Future Improvements

User login system

Individual user history filtering

Graph by date instead of name

Export data as PDF report

BMI category color indicators

📌 Author

Vivek Kumar

📜 License

This project is open-source and free to use for educational purposes.
