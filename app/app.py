from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import pymysql, os

app = FastAPI()

db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="devops_app"
)

@app.get("/users")
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

@app.post("/login")
def login(email: str, password: str):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s",(email,password))
    return {"status":"success" if cursor.fetchone() else "fail"}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
