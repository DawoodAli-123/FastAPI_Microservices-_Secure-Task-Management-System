from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine, Base
from app.models import User
from app.schemas import UserCreate, Token
from app.security import hash_password, verify_password, create_access_token, decode_token

app = FastAPI(title="Auth Service")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email,
                   hashed_password=hash_password(user.password),
                   role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created"}

@app.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(db_user.id, db_user.role)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/validate")
def validate(token: str):
    return decode_token(token)
