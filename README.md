# 📘 StudentAPI

**StudentAPI** is a Django REST Framework-based API project designed to perform CRUD (Create, Read, Update, Delete) operations on student records. This application is ideal for learning how to build RESTful APIs using Django and DRF.

---

## 🚀 Features

- 📄 Create, Read, Update, Delete student records
- 🔍 API endpoints using Django REST Framework
- 🗃️ JSON-based responses
- ✅ Validation and error handling
- 📚 Easily extendable for use in full-stack applications

---

## 🛠️ Tech Stack

- **Framework**: Django, Django REST Framework (DRF)
- **Language**: Python 3.x
- **Database**: SQLite (default), can be switched to MySQL/PostgreSQL
- **Tools**: Git, GitHub, Postman

---

## 📦 Installation & Setup

1. **Clone the repository**  
   - git clone https://github.com/pushpalaganesh/StudentAPI.git
   - cd StudentAPI
2. **Create a virtual environment**
- python -m venv venv
- venv\Scripts\activate  # On Windows
3. **Install dependencies**
- pip install -r requirements.txt
4. **Run migrations**
- python manage.py migrate
5. **Start the development server**
- python manage.py runserver

### 🔗 API Endpoints

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| GET    | `/students/`       | Get list of students    |
| POST   | `/students/`       | Add a new student       |
| GET    | `/students/<id>/`  | Get single student detail |
| PUT    | `/students/<id>/`  | Update student info     |
| DELETE | `/students/<id>/`  | Delete a student        |

## GET Method
![Screenshot (6)](https://github.com/user-attachments/assets/cd8457e6-ebeb-43a1-80ed-d799a7d4cf84)

## POST method
![Screenshot 2025-07-04 160332](https://github.com/user-attachments/assets/1940a713-4626-4036-97d7-277ba5aef1d3)
![Screenshot (7)](https://github.com/user-attachments/assets/0e885e05-52f6-4394-bf58-c61806afb985)

## PUT method
![Screenshot 2025-07-04 160332](https://github.com/user-attachments/assets/688aa092-0f7c-432f-aa12-6c556f482fbd)

## DELETE method
![Screenshot (9)](https://github.com/user-attachments/assets/7b740183-6e4b-461d-9e33-7d495ac84a9a)


**Use Postman or curl to test the API.**
![Screenshot (10)](https://github.com/user-attachments/assets/b0f3f5ed-b302-4134-b364-50d6074acdd9)
![Screenshot (12)](https://github.com/user-attachments/assets/e69eb035-fd8d-4144-951b-c6379a1ce517)


