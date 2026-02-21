# Employee Backend API

A FastAPI-based backend application for managing employee data.

## Features

- RESTful API for employee management
- SQLAlchemy ORM for database operations
- PostgreSQL support (with SQLite fallback for development)
- CORS enabled for frontend integration
- Unit tests with pytest

## Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd employeee-backend
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables (optional):
Create a `.env` file with:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

If `DATABASE_URL` is not set, the application will use SQLite (`sql_app.db`).

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### GET /employees
Retrieve all employees.

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "role": "Developer"
  }
]
```

### POST /employees
Create a new employee.

**Parameters:**
- `name` (string): Employee name
- `role` (string): Employee role

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "role": "Developer"
}
```

## Running Tests

Run the test suite:
```bash
pytest
```

## Project Structure

```
employeee-backend/
├── app/              # Application source code
│   ├── __init__.py
│   ├── main.py       # FastAPI application and routes
│   ├── models.py     # SQLAlchemy models
│   └── database.py   # Database configuration
├── tests/            # Test files
│   ├── __init__.py
│   └── test_main.py  # Unit tests
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Technologies

- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **PostgreSQL/SQLite**: Database
- **Pytest**: Testing framework
- **Uvicorn**: ASGI server

## License

[Add your license here]
