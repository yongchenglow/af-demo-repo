from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Demo API", version="1.0.0")


class User(BaseModel):
    username: str
    email: str


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Demo"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/users")
def create_user(user: User):
    return {"message": "User created", "user": user}
