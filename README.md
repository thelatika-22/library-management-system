# 📚 Library Management System (CLI - Python)

A Command Line Interface (CLI) based Library Management System built using Python and Object-Oriented Programming (OOP). The system allows librarians to add, search, issue, and return books while maintaining student records and calculating fines for late returns.

---

## 🚀 Features

* 📖 Add new books to the library
* 🔍 Search books by name
* 📚 View all available books
* 🎫 Issue books to students
* 🔄 Return issued books
* 💰 Automatic fine calculation for late returns
* 👨‍🎓 Store student details (Name & Roll Number)
* 🔤 Find books starting with a specific letter
* 📋 Display students who have issued books
* 📊 Generate Book → Roll Number dictionary
* ⚠️ Input validation and exception handling
* 🏗️ Object-Oriented Programming based design

---

## 🛠️ Tech Stack

* Language: Python
* Interface: Command Line Interface (CLI)

### Concepts Used

* Classes & Objects
* Constructors (`__init__`)
* Dictionaries
* List Comprehensions
* Lambda Functions
* Filter Function
* Loops
* Exception Handling
* Menu-Driven Programming
* OOP Principles

---

## 📂 Project Structure

```text
library-management-system/

│

├── main.py

└── README.md
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/thelatika-22/library-management-system.git
```

### 2. Navigate to the Project Folder

```bash
cd library-management-system
```

### 3. Run the Program

```bash
python main.py
```

---

## 💡 How It Works

1. Add books to the library.
2. View available books.
3. Search books using keywords.
4. Issue books to students.
5. Store student details and issue date.
6. Return books and calculate fines.
7. View issued students and roll number records.
8. Exit the system when finished.

---

## 📸 Sample Output

```text
========== LIBRARY MENU ==========

1. ADD BOOK
2. AVAILABLE BOOKS
3. SEARCH BOOK
4. ISSUE BOOK
5. RETURN BOOK
6. STUDENT NAMES
7. BOOKS STARTING WITH LETTER
8. ROLL NUMBERS DICTIONARY
9. EXIT

Enter Your Choice: 1

Enter Book Name: Python Basics

Python Basics added successfully.
```

### Book Return Example

```text
Enter the book you want to return: Python Basics

Enter Return Day: 12

Book Returned Successfully

Student: Latika Sharma

Roll Number: 101

Days Kept: 10

Fine: Rs 15
```

---

## 📌 Key Functionalities

### 📖 Book Management

* Add Books
* Search Books
* Display Available Books

### 👨‍🎓 Student Management

* Store Student Name
* Store Roll Number
* Track Issued Books

### 💰 Fine Management

* First 7 Days → No Fine
* After 7 Days → ₹5 per extra day

### 📊 Reports

* Student Names List
* Books by Starting Letter
* Book → Roll Number Dictionary

---

## 🔮 Future Improvements

* 💾 Store data permanently using files
* 🗄️ Database integration (MySQL/SQLite)
* 📅 Use actual dates instead of day numbers
* 🔐 Admin Login System
* 📈 Library Statistics Dashboard
* 🖥️ GUI Version using Tkinter
* 🌐 Web-Based Library System

---

## 🙌 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

---

## 📜 License

This project is licensed under the MIT License.

---

## ✨ Author

**Latika Sharma**

B.Tech CSE Student

⭐ If you like this project, give it a star on GitHub!
