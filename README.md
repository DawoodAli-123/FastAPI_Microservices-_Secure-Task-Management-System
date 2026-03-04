# 🚀 FastAPI Microservices – Secure Task Management System

A production-ready microservices architecture built using **FastAPI**, **Oracle Database**, and **Docker**, implementing JWT-based authentication, Role-Based Access Control (RBAC), and API Gateway routing.

This project simulates an enterprise-grade backend system with scalable architecture and database flexibility.

---

# 🏗 Architecture Overview

```
                   ┌──────────────────┐
                   │   API Gateway    │
                   │   (FastAPI)      │
                   └─────────┬────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
┌───────────────┐                        ┌────────────────┐
│  Auth Service │                        │  Task Service   │
│  (FastAPI)    │                        │  (FastAPI)      │
└──────┬────────┘                        └───────┬────────┘
       │                                               │
       └────────────── Oracle Database ────────────────┘
```

---

# 🧩 Microservices

## 1️⃣ API Gateway

* Entry point for all client requests
* Proxies traffic to respective services
* Centralized routing
* Easily extendable for rate limiting or monitoring

## 2️⃣ Auth Service

* User Registration
* Secure Login with JWT
* Role-Based Access Control (RBAC)
* Token validation endpoint
* Secure password hashing (bcrypt)

## 3️⃣ Task Service

* Task CRUD operations
* Owner-based task access
* JWT validation via Auth Service
* Scalable service structure

---

# 🛠 Tech Stack

* **FastAPI**
* **Oracle XE (Dockerized)**
* **SQLAlchemy ORM**
* **JWT (python-jose)**
* **Passlib (bcrypt)**
* **HTTPX (Service-to-Service Communication)**
* **Docker & Docker Compose**
* **OpenAPI (Swagger UI)**

---

# 📁 Project Structure

```
task-microservices/
│
├── docker-compose.yml
├── .env
│
├── auth-service/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── task-service/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
└── api-gateway/
    ├── app/
    ├── Dockerfile
    └── requirements.txt
```

---

# ⚙️ Environment Configuration

Create a `.env` file in the root directory:

```
DATABASE_URL=oracle+oracledb://system:oracle@oracle-db:1521/XEPDB1
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 🐳 Running the Project

Make sure Docker is installed.

### 🔹 Build & Start Services

```
docker compose up --build
```

---

# 🌐 Service Endpoints

| Service         | URL                        |
| --------------- | -------------------------- |
| API Gateway     | http://localhost:8000/docs |
| Auth Service    | http://localhost:8001/docs |
| Task Service    | http://localhost:8002/docs |
| Oracle Database | localhost:1521             |

---

# 🔐 Authentication Flow

1️⃣ Register User
`POST /auth/register`

2️⃣ Login
`POST /auth/login`

3️⃣ Receive JWT Token

4️⃣ Use Token in Header:

```
Authorization: Bearer <your_token>
```

5️⃣ Access Task APIs via Gateway

---

# 📌 Key Features

* Clean Microservices Architecture
* JWT Authentication with Role Claims
* Oracle Database Integration
* Secure Password Hashing
* Service-to-Service Communication
* Dockerized Deployment
* OpenAPI Auto Documentation
* Production-Ready Structure
* Database-Agnostic Design

---

# 🔄 Database Flexibility (Oracle → PostgreSQL)

This project is built using SQLAlchemy ORM, making it database-agnostic.

Although Oracle XE is used by default, the system can easily switch to PostgreSQL.

## 🔁 Steps to Switch to PostgreSQL

### 1️⃣ Update requirements.txt

Replace:

```
oracledb
```

With:

```
psycopg2-binary
```

### 2️⃣ Update `.env`

```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@postgres-db:5432/taskdb
```

### 3️⃣ Update docker-compose.yml

Add:

```yaml
postgres-db:
  image: postgres:15
  environment:
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres
    POSTGRES_DB: taskdb
  ports:
    - "5432:5432"
```

No changes required in:

* Business logic
* Authentication
* Service layers
* API Gateway

This demonstrates architectural abstraction and portability.

---

# 📈 Design & Performance Highlights

* Stateless JWT authentication
* Microservices separation of concerns
* Docker network-based service discovery
* ORM abstraction for database flexibility
* Enterprise-ready scalable structure
* Clean separation (Gateway → Auth → Task)

---

# 🚀 Future Enhancements

* Async SQLAlchemy 2.0
* Alembic Migrations
* Redis for token caching
* Centralized Logging (ELK stack)
* Rate Limiting
* Circuit Breaker Pattern
* Kubernetes Deployment
* CI/CD Pipeline
* Distributed Tracing (OpenTelemetry)

---

# 👨‍💻 Author

**Dawood Ali Shaik**
Software Engineer | Python Backend Developer
FastAPI • Microservices • Docker • Oracle • PostgreSQL

---

# ⭐ Why This Project?

This project demonstrates:

* Real-world microservices architecture
* Secure authentication mechanisms
* Oracle database integration
* Containerized deployment
* Backend scalability design
* Enterprise-level backend structuring

---

# 📄 License

This project is built for learning, demonstration, and portfolio purposes.
