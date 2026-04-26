# 📚 Library Management System (CLI - Python)

A simple Command Line Interface (CLI) based Library Management System built using Python. This project allows users to manage books, issue and return them, and automatically calculates fines for late returns.

---

## 🚀 Features

- 📖 Add new books to the library
- 📚 View all available books
- 📥 Issue books to students
- 📤 Return books
- 🧾 Automatic fine calculation (₹5 per day after 7 days)
- 🧑 Track student name, roll number, and issue date

---

## 🛠️ Tech Stack

- Language: Python
- Interface: Command Line Interface (CLI)
- Data Storage: In-memory (using dictionaries)

---

## 📂 Project Structure

library-management-system/
│
├── main.py
├── README.md

---

## ▶️ How to Run

1. Clone the repository:

git clone https://github.com/thelatika-22/library-management-system.git

2. Go to the project folder:

cd library-management-system

3. Run the program:

python main.py

---

## 💡How It Works

- Books are stored in a dictionary: books
- Issued books are tracked in: issued_books
- Student details are stored at the time of issuing

## 🔁 Workflow:

1. Add books to the system
2. View available books
3. Issue a book (removes from available list)
4. Return a book (adds back to available list)
5. Fine is calculated if returned after 7 days

---

## 📸 Sample Menu

MENU
1. ADD BOOKS
2. AVAILABLE BOOKS
3. ISSUE BOOK
4. RETURN BOOK
5. EXIT

---

## 📌 Future Improvements

- 💾 Store data using files or database (SQLite/MySQL)
- 🔐 Add login system for admin/users
- 🌐 Convert into web app
- 📊 Add full transaction history tracking

---

## 🙌 Contributing

Feel free to fork this repository and improve it. Pull requests are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ✨ Author

Latika Sharma

---

⭐ If you like this project, give it a star on GitHub!
