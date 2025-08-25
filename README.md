
# Task Management API

A backend project built with **Django REST Framework** that allows users to manage their daily tasks efficiently.  
This API supports user authentication, task categorization, and task collaboration via comments.

---

## 🚀 Features
- User authentication (register & login)
- CRUD operations for tasks
- Categorize tasks
- Add comments to tasks
- Token-based authentication

---

## 🛠️ Tech Stack
- **Python 3**
- **Django**
- **Django REST Framework**
- **SQLite** (for development)
  

---

## 📂 Project Structure
```

task-management-api/
│
├── README.md
├── manage.py
├── task\_management\_api/        # main project folder
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/                      # app for task management
├── models.py
├── serializers.py
├── views.py
├── urls.py
└── tests.py

````

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/task-management-api.git
   cd task-management-api
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

---

## 📌 API Endpoints (Planned)

| Method | Endpoint                  | Description                  |
| ------ | ------------------------- | ---------------------------- |
| POST   | `/api/register`           | Register a new user          |
| POST   | `/api/login`              | User login & token retrieval |
| GET    | `/api/tasks`              | Get all tasks                |
| POST   | `/api/tasks`              | Create a task                |
| GET    | `/api/tasks/{id}`         | Get task details             |
| PUT    | `/api/tasks/{id}`         | Update a task                |
| DELETE | `/api/tasks/{id}`         | Delete a task                |
| GET    | `/api/categories`         | Get all categories           |
| POST   | `/api/categories`         | Create a category            |
| GET    | `/api/comments/{task_id}` | Get comments for a task      |
| POST   | `/api/comments/{task_id}` | Add a comment to a task      |

---

## 👤 Author

**Beka Addisu**
ALX Backend Engineering Student






