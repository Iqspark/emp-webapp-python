from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Employee, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@app.post("/employees")
def create_employee(name: str, role: str, db: Session = Depends(get_db)):
    emp = Employee(name=name, role=role)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp
