from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine, Base
from app.models import Task
import httpx

app = FastAPI(title="Task Service")

Base.metadata.create_all(bind=engine)

AUTH_URL = "http://auth-service:8001/validate"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def verify_token(auth: str = Header(...)):
    token = auth.split(" ")[1]
    async with httpx.AsyncClient() as client:
        res = await client.post(AUTH_URL, params={"token": token})
        data = res.json()
        if "error" in data:
            raise HTTPException(status_code=401, detail="Invalid token")
        return data

@app.post("/tasks")
async def create_task(title: str, description: str,
                      user=Depends(verify_token),
                      db: Session = Depends(get_db)):

    task = Task(title=title,
                description=description,
                owner_id=int(user["sub"]))
    db.add(task)
    db.commit()
    return {"message": "Task created"}
