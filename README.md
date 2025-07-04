# 🎓 Student Database Management System 🗃️

**Full-Stack Student Record Management Web Application using Flask, SQLite, and HTML/CSS**

![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)  
![Frontend](https://img.shields.io/badge/frontend-HTML%20%7C%20CSS-blue.svg)  
![Status](https://img.shields.io/badge/status-Completed-brightgreen.svg)

---

## 🧠 Project Overview

This project is a **Student Database Management System** that allows admin and student users to perform operations like:

- Adding student records
- Viewing dashboards
- Editing student data
- Login-based access for students and admins

Built using **Python Flask**, this system interacts with an **SQLite database** to manage student information. A clean frontend built with **HTML & CSS** provides an intuitive user experience.

---

## ⚙️ Technologies Used

### 🖥️ Backend

- Python 3.8+
- Flask (Web Framework)
- SQLite3 (Relational Database)
- Jinja2 (Templating Engine)

### 🎨 Frontend

- HTML5
- CSS3
- Basic JavaScript (if needed)

---

## 📦 Key Features

✅ Add, Edit, and Delete student records  
✅ Admin login with dashboard  
✅ Student login with profile view  
✅ SQLite-backed data persistence  
✅ Simple, mobile-responsive HTML/CSS UI  
✅ Secure password column added via schema update

---

## 📁 Project Structure

```

Student-DB-Management/
├── app.py                         # Main application entry point
├── requirements.txt               # Required Python packages
├── README.md                      # Project documentation

├── db/
│   ├── init\_db.py                 # DB schema setup
│   ├── add\_password\_column.py     # Script to add password field
│   └── student\_db.sqlite3         # SQLite database file

├── static/
│   ├── images/                    # UI image assets (if any)
│   └── style.css                  # Styling

├── templates/
│   ├── index.html
│   ├── admin\_login.html
│   ├── admin\_dashboard.html
│   ├── student\_login.html
│   ├── student\_dashboard.html
│   ├── add\_student.html
│   └── edit\_student.html

└── venv/                          # Virtual environment

````

---

## 🖼️ Screenshots

| ![Index Page](https://github.com/user-attachments/assets/aa8b5b61-f0c5-472b-8cbb-b790d25b7b02) | ![Student Login](https://github.com/user-attachments/assets/674ffb32-4288-44ca-b9b6-3d96ada623bb) | ![Admin Login](https://github.com/user-attachments/assets/45a1bb63-ca87-46f9-a37f-bda760e15779) | ![Add Student](https://github.com/user-attachments/assets/84dd17a4-085c-415d-bcb9-d2839055563b) | ![Admin Dashboard](https://github.com/user-attachments/assets/0387174c-efe5-4308-aa8a-229d17262e29) | ![Student Dashboard](https://github.com/user-attachments/assets/1257fa41-4b45-432a-a515-2e3cbb6ad554)

---


## 🚀 How to Run the Project![2]()


### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Student-DB-Management.git
cd Student-DB-Management
````

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize the Database

```bash
python db/init_db.py
python db/add_password_column.py  # Only if needed
```

### 5️⃣ Start the Application

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🔍 Future Enhancements

* Password hashing for better security
* Pagination and search in dashboards
* Export records to CSV or PDF
* Add admin user registration
* Add email-based password reset flow

---

## 📬 Contact

**Sai Sruthi Karnatakapu**
📧 [k.saisruthi913@gmail.com](mailto:k.saisruthi913@gmail.com)
🔗 [LinkedIn Profile](https://www.linkedin.com/in/saisruthi-karnatakapu/)

```

