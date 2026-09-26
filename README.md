# student-managment-system-
A console-based Student Management System built with Python to manage student records, marks, averages, rankings, and pass/fail results using dictionaries, functions, loops, and conditional statements.
# 🎓 Student Management System

A simple **console-based Student Management System built using Python**.
This project allows users to manage student records, marks, averages, and results through an interactive menu-driven interface.

## 📌 Features

* ➕ **Add Student** – Add a new student with roll number, name, and marks for 3 subjects.
* 📋 **View Students** – Display all registered students and their marks.
* 🔍 **Search Student** – Find a student using their roll number.
* ✏️ **Update Marks** – Update the marks of an existing student.
* 🗑️ **Delete Student** – Remove a student record.
* 📊 **Calculate Average** – Calculate the average marks of a student.
* 🏆 **Highest Scorer** – Find the student with the highest average.
* 📉 **Lowest Scorer** – Find the student with the lowest average.
* ✅ **Pass/Fail Check** – Determine whether a student passes or fails based on their average.
* 🚪 **Exit** – Safely exit the application.

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Lists
* Functions
* Loops
* Conditional Statements
* User Input
* Basic Data Processing

## 📂 Data Structure

Student records are stored in a Python dictionary:

```python
students = {
    "101": {
        "name": "Rahul",
        "marks": [85, 78, 92]
    }
}
```

The **roll number** is used as the unique key for each student.

## ⚙️ How It Works

When the program starts, it displays a menu:

```text
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Delete Student
6. Calculate Average
7. Highest Scorer
8. Lowest Scorer
9. Pass/Fail
10. Exit
```

The user selects an option, and the corresponding function is executed.

## 🧮 Pass/Fail Criteria

The program calculates the average of the three subject marks.

```text
Average >= 40 → PASS
Average < 40  → FAIL
```

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your system.

Check using:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/student-management-system.git
```

### 3. Open the Project

```bash
cd student-management-system
```

### 4. Run the Program

```bash
python student_management.py
```

## 💡 Concepts Practiced

This project was created to practice fundamental Python programming concepts:

* Variables
* Dictionaries
* Lists
* `if`, `elif`, and `else`
* `for` and `while` loops
* Functions
* `input()` and `print()`
* Dictionary operations
* List operations
* `sum()` and `len()`
* Searching
* Updating records
* Deleting records
* Basic problem-solving and logic building

## 🔮 Future Improvements

Possible improvements for future versions:

* 💾 Store student data permanently using **files**
* 🗄️ Add **SQLite/MySQL database** support
* 🔐 Add user login/authentication
* 📈 Generate student performance reports
* 📊 Add grades and rankings
* 🖥️ Create a graphical user interface using **Tkinter**
* 🌐 Convert it into a web application using **Flask/Django**
* 📄 Export student reports to CSV/PDF
* 🔎 Add validation for marks and roll numbers

## 🎯 Project Purpose

The main purpose of this project is to strengthen **Python fundamentals and problem-solving skills** by building a practical CRUD-style application.

## 👨‍💻 Author

**Your Name**

Sabbisetty Veera Venkata Naga Viswas Gupta

⭐ If you found this project useful, consider giving the repository a star!
