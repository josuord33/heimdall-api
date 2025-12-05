🚀 HEIMDALL API
High-Performance Handball Event Logger (FastAPI + MongoDB)
Welcome to the HEIMDALL API backend repository. This service is designed to log real-time handball events (goals, misses, recoveries, etc.) with high performance, serving data to the client Tablet UI and the centralized Dashboard.

The API is built using FastAPI and adheres to the Hexagonal Architecture (Ports and Adapters) principle for maximum maintainability and testability.

Shutterstock

🏗️ Architecture Overview
The project is structured into three main layers to separate Business Logic (Core) from Infrastructure (Technology):

Core (Domain & Services): Contains the pure business logic and Pydantic data models. It knows nothing about FastAPI or MongoDB.

Infrastructure (Persistence & API): Contains the technical implementations.

API: Handles HTTP requests, authentication, and calls the Core Service.

Persistence: Handles the connection to MongoDB Atlas and implements the repository methods.

⚙️ Setup and Installation
1. Prerequisites

You must have Python 3.10+ and pip installed. We highly recommend using a version manager like pyenv.

2. Clone the Repository and Create Environment

Bash
# Clone the repository (if not already done)
git clone <your-repo-url> heimdall-api
cd heimdall-api

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies

Install all required Python libraries from the requirements.txt file:

Bash
pip install -r requirements.txt
🔑 Configuration (.env)
The API relies on sensitive environment variables defined in the .env file located in the project root. THIS FILE MUST NOT BE COMMITTED TO GIT.

Configuration Details:

Variable	Description	Example
MONGO_URI	Connection string to the MongoDB Atlas cluster.	mongodb+srv://user:...@Cluster.net/...
DB_NAME	Name of the MongoDB database (HEIMDALL_DB).	HEIMDALL_DB
SECRET_KEY	Cryptographic key for JWT signing (minimum 32 chars).	my_super_secret_key_12345
ACCESS_TOKEN_EXPIRE_MINUTES	Token lifetime (set to 1440 for 24 hours).	1440
OWN_TEAM_ID	ObjectId of the Muskiz EB roster in the teams collection.	655a6d8c97e10a6a43e4f71a
🚀 Running the API
Use Uvicorn to start the server. Crucially, the --app-dir src flag is required to correctly resolve Python package imports in the Hexagonal structure.

Activate Environment:

Bash
source venv/bin/activate
Start the Server (Development):

Bash
uvicorn src.main:app --reload --app-dir src
Access

API Documentation (Swagger UI): http://127.0.0.1:8000/docs

Health Check: http://127.0.0.1:8000/

🎯 Key Endpoints (Tablet Focus)
Endpoint	Method	Security	Description
/token	POST	Open	Operator Login. Returns a 24-hour JWT.
/events/	POST	JWT Required	CRITICAL: Registers real-time event data (Goal, Miss, etc.).
/match	POST	JWT Required	Creates a new match entry, returning the match_id.
/team/{id}	GET	JWT Required	Fetches the team roster (using OWN_TEAM_ID).
🧪 Testing
(To be implemented: We will use pytest to write unit tests for the Core Services layer, ensuring business logic integrity without connecting to MongoDB.)

Python
# Run tests
pytest