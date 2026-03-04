# 🚀 FastAPI Microservices – Secure Task Management System (Oracle-Based)

A production-ready microservices architecture built using **FastAPI**, **Oracle Database**, and **Docker**, implementing JWT-based authentication, Role-Based Access Control (RBAC), and API Gateway routing.

---

## 🏗 Architecture Overview

This project follows a real-world microservices architecture:

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

## 🧩 Microservices

### 1️⃣ API Gateway

* Entry point for all client requests
* Proxies requests to respective services
* Centralized routing

### 2️⃣ Auth Service

* User Registration
* Login with JWT generation
* Role-Based Access Control (RBAC)
* Token validation endpoint

### 3️⃣ Task Service

* Task CRUD operations
* Token validation via Auth Service
* Owner-based task management

---

## 🛠 Tech Stack

* **FastAPI**
* **Oracle XE (Docker)**
* **SQLAlchemy (Oracle Dialect)**
* **JWT (python-jose)**
* **Passlib (bcrypt hashing)**
* **HTTPX (service-to-service calls)**
* **Docker & Docker Compose**

---

## 📁 Project Structure

```
task-microservices/
│
├── docker-compose.yml
├── .env
│
├── auth-service/
├── task-service/
└── api-gateway/
```

---

## ⚙️ Environment Configuration

Create a `.env` file:

```
DATABASE_URL=oracle+oracledb://system:oracle@oracle-db:1521/XEPDB1
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🐳 Running the Project

Make sure Docker is installed.

### 🔹 Build & Start Services

```bash
docker compose up --build
```

---

## 🌐 Service URLs

| Service      | URL                        |
| ------------ | -------------------------- |
| API Gateway  | http://localhost:8000/docs |
| Auth Service | http://localhost:8001/docs |
| Task Service | http://localhost:8002/docs |
| Oracle DB    | localhost:1521             |

---

## 🔐 Authentication Flow

1. Register a user via `/auth/register`
2. Login via `/auth/login`
3. Receive JWT token
4. Use token in header:

```
Authorization: Bearer <your_token>
```

5. Access task endpoints via API Gateway

---

## 📌 Key Features

* Clean Microservices Architecture
* JWT Authentication with Role Claims
* Oracle Database Integration
* Service-to-Service Validation using HTTPX
* Dockerized Multi-Service Deployment
* OpenAPI Documentation (Swagger UI)
* Secure Password Hashing (bcrypt)
* Production-like Structure

---

## 📈 Performance & Design Highlights

* Stateless JWT-based authentication
* Decoupled services with independent deployment
* Database-driven architecture using Oracle XE
* Service discovery via Docker networking
* Scalable architecture ready for Kubernetes

---

## 🚀 Future Enhancements

* Async SQLAlchemy 2.0
* Alembic Migrations
* Redis for Token Caching
* Centralized Logging (ELK)
* Rate Limiting
* Kubernetes Deployment
* CI/CD Pipeline Integration
* OpenTelemetry Distributed Tracing

---

## 👨‍💻 Author

**Dawood Ali Shaik**
Software Engineer | Python Backend Developer
FastAPI • Microservices • Docker • Oracle

---

## ⭐ Why This Project?

This project simulates an enterprise-grade backend system and demonstrates:

* Microservices architecture design
* Secure authentication mechanisms
* Real-world Oracle DB integration
* Containerized production deployment
* Backend scalability principles

---

## 📄 License

This project is for learning and demonstration purposes.
