import sqlite3
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Hardcoded credentials - SECURITY ISSUE!
API_KEY = "sk_live_51HxYzKJdfjkls93jfd"
DATABASE_PASSWORD = "admin123"


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/api/auth/login")
def login(request: LoginRequest):
    # SQL Injection vulnerability - CRITICAL!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{request.username}' AND password = '{request.password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return {"token": "jwt_token_here", "api_key": API_KEY}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/api/users/{user_id}")
def get_user(user_id: str):
    # Another SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()
