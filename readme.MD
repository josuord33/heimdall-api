# 🚀 HEIMDALL API
### High-Performance Handball Event Logger

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to the **HEIMDALL API** backend repository. This service is designed to log real-time handball events (goals, misses, recoveries, etc.) with high performance, serving data to the client Tablet UI and the centralized Dashboard.

The API is built using **FastAPI** and adheres to the **Hexagonal Architecture (Ports and Adapters)** principle for maximum maintainability and testability.

---

## 🏗️ Architecture Overview

The project is structured into three main layers to separate Business Logic (Core) from Infrastructure (Technology):

- **Core (Domain & Services)**: Contains the pure business logic and Pydantic data models. It knows nothing about FastAPI or MongoDB.
- **Infrastructure (Persistence & API)**: Contains the technical implementations.
    - **API**: Handles HTTP requests, authentication, and calls the Core Service.
    - **Persistence**: Handles the connection to MongoDB Atlas and implements the repository methods.

### Project Structure
```
src/
├── core/               # Business Logic
│   ├── domain/         # Pydantic Models (Entities)
│   └── services/       # Use Cases / Business Rules
├── infrastructure/     # Technical Implementation
│   ├── api/            # FastAPI Routers (Controllers)
│   ├── persistence/    # MongoDB Client & Repositories
│   └── security/       # JWT Auth & Hashing
└── main.py             # Application Entrypoint
```

---

## ⚙️ Setup and Installation

### 1. Prerequisites
You must have **Python 3.13+** and `pip` installed. We highly recommend using a version manager like `pyenv`.

### 2. Clone the Repository and Create Environment

```bash
# Clone the repository
git clone https://github.com/josuord33/heimdall-api.git
cd heimdall-api

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
Install all required Python libraries from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configuration (.env)
The API relies on sensitive environment variables defined in the `.env` file located in the project root. **THIS FILE MUST NOT BE COMMITTED TO GIT.**

Create a `.env` file with the following variables:

| Variable | Description | Example |
| :--- | :--- | :--- |
| `MONGO_URI` | Connection string to MongoDB Atlas. | `mongodb+srv://user:pass@cluster.mongodb.net/...` |
| `DB_NAME` | Name of the MongoDB database. | `HEIMDALL_DB` |
| `SECRET_KEY` | Key for JWT signing (min 32 chars). | `my_super_secret_key_...` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime (minutes). | `1440` |
| `OWN_TEAM_ID` | ObjectId of your team in the DB. | `655a6d8c97e10a6a43e4f71a` |

---

## 🚀 Running the API

Use `uvicorn` to start the server. **Crucially**, you must run the command from the project root and point to the app instance correctly.

### Start the Server (Development)

```bash
# Make sure your virtual environment is activated
uvicorn main:app --reload --app-dir src
```

### Access
- **API Documentation (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health Check**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎯 Key Endpoints

| Endpoint | Method | Security | Description |
| :--- | :--- | :--- | :--- |
| `/token` | `POST` | Open | Operator Login. Returns a 24-hour JWT. |
| `/events/` | `POST` | JWT | **CRITICAL**: Registers real-time event data. |
| `/match` | `POST` | JWT | Creates a new match entry. |
| `/team/{id}` | `GET` | JWT | Fetches the team roster. |

---

## 🧪 Testing

We use `pytest` to write unit tests for the Core Services layer, ensuring business logic integrity.

```bash
# Run tests
pytest
```