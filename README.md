<div align="center">

# ✅ TaskFlow

### A Modern Full-Stack Task Management Application

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React_19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vite.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br />

**TaskFlow** is a secure, full-stack task management app built with **FastAPI** and **React**. It features JWT authentication, per-user task isolation, and a clean card-based UI — designed to learn and demonstrate modern web development practices.

[Getting Started](#-getting-started) •
[Features](#-features) •
[API Reference](#-api-reference) •
[Architecture](#-architecture) •
[Contributing](#-contributing)

---

</div>

<br />

## ⚡ Features

<table>
<tr>
<td width="50%">

### 🔐 Authentication & Security
- User registration with **Argon2** password hashing
- **JWT (JSON Web Token)** based authentication
- OAuth2 password flow with Bearer tokens
- Protected routes on both frontend & backend
- Auto-redirect on token expiry

</td>
<td width="50%">

### 📋 Task Management
- **Create**, **Read**, **Update**, **Delete** tasks (full CRUD)
- Per-user task isolation — users only see their own tasks
- Mark tasks as complete / incomplete with one click
- Inline editing with save functionality
- Real-time toast notifications on every action

</td>
</tr>
<tr>
<td width="50%">

### 🎨 Frontend
- **React 19** with functional components & hooks
- **React Router v7** with protected route guards
- **Axios** interceptors for auto token attachment
- **Lucide React** icons for a clean UI
- Card-based responsive layout

</td>
<td width="50%">

### 🛠️ Backend
- **FastAPI** with automatic OpenAPI/Swagger docs
- **SQLAlchemy ORM** with declarative models
- **Pydantic v2** schemas for request validation
- **PostgreSQL** database with foreign key relations
- **CORS middleware** configured for cross-origin requests

</td>
</tr>
</table>

<br />

## 🏗️ Architecture

```mermaid
graph LR
    subgraph Frontend["🖥️ Frontend (React + Vite)"]
        A[Login Page] -->|POST /users/login| B[Auth Token]
        B --> C[Task Dashboard]
        C -->|Axios + Bearer Token| D[API Calls]
    end

    subgraph Backend["⚙️ Backend (FastAPI)"]
        D -->|REST API| E[Routers]
        E --> F[User Router]
        E --> G[Task Router]
        F --> H[Auth Module]
        G --> H
        H -->|Argon2 + JWT| I[Security Layer]
    end

    subgraph Database["🗄️ Database"]
        F --> J[(PostgreSQL)]
        G --> J
    end

    style Frontend fill:#1a1a2e,stroke:#e94560,color:#eee
    style Backend fill:#16213e,stroke:#0f3460,color:#eee
    style Database fill:#0f3460,stroke:#533483,color:#eee
```

<br />

## 📁 Project Structure

```
Task-Management_FastAPI/
│
├── 📂 backend/
│   ├── 📂 src/
│   │   ├── 📂 models/          # SQLAlchemy ORM models
│   │   │   ├── user.py         # User model (id, username, password)
│   │   │   └── task.py         # Task model (id, title, description, completed, user_id)
│   │   ├── 📂 schemas/         # Pydantic validation schemas
│   │   │   ├── user.py         # UserCreate schema
│   │   │   └── task.py         # TaskCreate schema
│   │   ├── 📂 routers/         # API route handlers
│   │   │   ├── user.py         # /users/register, /users/login
│   │   │   └── task.py         # /tasks/create, /tasks/get, etc.
│   │   ├── 📂 security/        # Authentication & config
│   │   │   ├── auth.py         # Argon2 hashing, JWT encode/decode, OAuth2
│   │   │   └── config.py       # Pydantic Settings (.env loader)
│   │   ├── database.py         # SQLAlchemy engine & session
│   │   └── main.py             # FastAPI app entry point
│   ├── .env.example            # Environment variables template
│   └── requirements.txt        # Python dependencies
│
├── 📂 frontend/
│   ├── 📂 src/
│   │   ├── 📂 components/
│   │   │   ├── Login.jsx       # Login form with auth flow
│   │   │   ├── Task.jsx        # Task CRUD dashboard
│   │   │   ├── Navbar.jsx      # Navigation bar with logout
│   │   │   └── api.jsx         # Axios instance & API endpoints
│   │   ├── App.jsx             # Routes & protected route wrapper
│   │   ├── App.css             # Global styles
│   │   └── main.jsx            # React DOM entry point
│   ├── package.json            # Node dependencies
│   └── vite.config.js          # Vite configuration
│
├── .gitignore
└── README.md
```

<br />

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

| Tool | Version | Download |
|------|---------|----------|
| **Python** | 3.10+ | [python.org](https://www.python.org/downloads/) |
| **Node.js** | 18+ | [nodejs.org](https://nodejs.org/) |
| **PostgreSQL** | 14+ | [postgresql.org](https://www.postgresql.org/download/) |
| **Git** | Latest | [git-scm.com](https://git-scm.com/) |

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/preyas-patel26/Task-Management_FastAPI.git
cd Task-Management_FastAPI
```

### 2️⃣ Setup the Backend

```bash
# Navigate to backend
cd backend

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env         # macOS/Linux
copy .env.example .env       # Windows
```

Edit `backend/.env` with your PostgreSQL credentials:

```env
POSTGRES_URI=postgresql://postgres:your_password@localhost:5432/taskdb
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRY_MINUTES=30
```

> [!IMPORTANT]
> Create the PostgreSQL database first:
> ```sql
> CREATE DATABASE taskdb;
> ```

### 4️⃣ Start the Backend Server

```bash
# From the backend directory
uvicorn src.main:app --reload
```

The API will be available at **http://127.0.0.1:8000**

> [!TIP]
> Visit **http://127.0.0.1:8000/docs** for the interactive Swagger UI documentation.

### 5️⃣ Setup & Start the Frontend

```bash
# Open a new terminal, navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at **http://localhost:5173**

<br />

## 📡 API Reference

### 🔑 Authentication

<details>
<summary><code>POST</code> <code>/users/register</code> — Register a new user</summary>

#### Request Body

```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```

#### Response `200 OK`

```json
{
  "id": 1,
  "username": "john_doe"
}
```

</details>

<details>
<summary><code>POST</code> <code>/users/login</code> — Login & get access token</summary>

#### Request Body (`application/x-www-form-urlencoded`)

| Field | Type | Description |
|-------|------|-------------|
| `username` | `string` | Your username |
| `password` | `string` | Your password |

#### Response `200 OK`

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

</details>

---

### 📋 Tasks (🔒 Requires Authentication)

> All task endpoints require the `Authorization: Bearer <token>` header.

<details>
<summary><code>POST</code> <code>/tasks/create-task</code> — Create a new task</summary>

#### Request Body

```json
{
  "title": "Learn FastAPI",
  "description": "Complete the official tutorial",
  "completed": false
}
```

#### Response `200 OK`

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete the official tutorial",
  "completed": false,
  "user_id": 1
}
```

</details>

<details>
<summary><code>GET</code> <code>/tasks/get-tasks</code> — Get all tasks for current user</summary>

#### Response `200 OK`

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the official tutorial",
    "completed": false,
    "user_id": 1
  }
]
```

</details>

<details>
<summary><code>GET</code> <code>/tasks/get-task/{id}</code> — Get a specific task by ID</summary>

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | `int` | Task ID |

#### Response `200 OK`

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete the official tutorial",
  "completed": false,
  "user_id": 1
}
```

#### Error Responses

| Status | Description |
|--------|-------------|
| `403` | Not authorized to access this task |
| `404` | Task not found |

</details>

<details>
<summary><code>PUT</code> <code>/tasks/update-task?id={id}</code> — Update a task</summary>

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | `int` | Task ID to update |

#### Request Body

```json
{
  "title": "Learn FastAPI (Updated)",
  "description": "Completed!",
  "completed": true
}
```

</details>

<details>
<summary><code>DELETE</code> <code>/tasks/delete-task?id={id}</code> — Delete a task</summary>

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | `int` | Task ID to delete |

#### Response `200 OK`

```json
{
  "message": "Task is deleted"
}
```

</details>

<br />

## 🗄️ Database Schema

```mermaid
erDiagram
    USERS {
        int id PK "Auto-increment"
        string username UK "Unique, Not Null"
        string password "Argon2 Hashed, Not Null"
    }
    TASKS {
        int id PK "Auto-increment"
        string title "Not Null"
        string description "Nullable"
        boolean completed "Default: false"
        int user_id FK "References users.id"
    }
    USERS ||--o{ TASKS : "owns"
```

<br />

## 🔒 Authentication Flow

```mermaid
sequenceDiagram
    actor User
    participant Frontend as React Frontend
    participant Backend as FastAPI Backend
    participant DB as PostgreSQL

    User->>Frontend: Enter credentials
    Frontend->>Backend: POST /users/login (form data)
    Backend->>DB: Query user by username
    DB-->>Backend: User record
    Backend->>Backend: Verify password (Argon2)
    Backend->>Backend: Generate JWT token
    Backend-->>Frontend: { access_token, token_type }
    Frontend->>Frontend: Store token in localStorage

    Note over Frontend,Backend: Subsequent Requests

    Frontend->>Backend: GET /tasks/get-tasks<br/>Authorization: Bearer <token>
    Backend->>Backend: Decode & verify JWT
    Backend->>DB: Query tasks WHERE user_id = current_user.id
    DB-->>Backend: User's tasks
    Backend-->>Frontend: Task list JSON
    Frontend->>User: Render task cards
```

<br />

## 🛠️ Built With

<div align="center">

| Layer | Technology | Purpose |
|:-----:|:----------:|:-------:|
| **Frontend** | ![React](https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black) | UI Components |
| **Bundler** | ![Vite](https://img.shields.io/badge/Vite_8-646CFF?style=flat-square&logo=vite&logoColor=white) | Dev Server & Build |
| **Routing** | ![React Router](https://img.shields.io/badge/React_Router_7-CA4245?style=flat-square&logo=reactrouter&logoColor=white) | Client-side Routing |
| **HTTP Client** | ![Axios](https://img.shields.io/badge/Axios-5A29E4?style=flat-square&logo=axios&logoColor=white) | API Requests |
| **Icons** | ![Lucide](https://img.shields.io/badge/Lucide_React-F56565?style=flat-square&logoColor=white) | UI Icons |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | REST API |
| **ORM** | ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logoColor=white) | Database ORM |
| **Validation** | ![Pydantic](https://img.shields.io/badge/Pydantic_v2-E92063?style=flat-square&logo=pydantic&logoColor=white) | Schema Validation |
| **Auth** | ![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white) | Token Authentication |
| **Hashing** | ![Argon2](https://img.shields.io/badge/Argon2-6C3483?style=flat-square&logoColor=white) | Password Hashing |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) | Relational Database |

</div>

<br />

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

<br />

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br />

---

<div align="center">

**Built with ❤️ by [Preyas Patel](https://github.com/preyas-patel26)**

⭐ Star this repo if you found it helpful!

</div>
