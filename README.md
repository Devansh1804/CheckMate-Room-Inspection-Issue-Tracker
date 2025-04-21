# 🛠️ CheckMate – Room Inspection & Issue Tracker

CheckMate is a web-based platform designed to streamline hostel room inspections and issue reporting. Built with **Flask**, **MongoDB**, and **HTML/CSS**, this application allows students to log room issues and wardens/admins to track and update their status efficiently.

---

## 🚀 Features

- 👨‍🎓 **Student Panel**  
  - Secure login system  
  - Submit issues with photo, description, and location  
  - View issue submission confirmation  

- 🛡️ **Admin Panel**  
  - Secure admin login  
  - View all issues submitted by students  
  - Update status (Pending, In Progress, Resolved)

- 🗂️ **MongoDB Database**  
  - Stores all users, issues, and images  
  - Efficiently manages inspection records  

- 📷 **File Upload Support**  
  - Upload room issue images directly from the browser  
  - Secure and validated upload mechanism  

---

## 🏗️ Tech Stack

| Technology | Purpose                     |
|------------|-----------------------------|
| Flask      | Backend web framework       |
| MongoDB    | NoSQL database              |
| HTML/CSS   | Frontend interface          |
| PyMongo    | Flask-MongoDB integration   |
| Werkzeug   | Secure file uploads         |

---

## 🧾 Setup Instructions

### 🔧 Prerequisites

- Python 3.8+ installed
- MongoDB installed and running locally
- VS Code (or any code editor)

### 📦 Install Dependencies

```bash
pip install flask flask_pymongo werkzeug


## ⚙️ How to Run
1. Start MongoDB
Make sure MongoDB is running locally (mongodb://localhost:27017)

2. Insert Sample Admin (MongoDB Compass)
Go to checkmate → users collection and insert:

{
  "email": "admin@admin.com",
  "password": "admin",
  "role": "admin",
  "username": "Admin"
}

3. Run Flask App
python app.py

4. Open in Browser
http://127.0.0.1:5000
