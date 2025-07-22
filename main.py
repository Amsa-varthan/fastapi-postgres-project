# main.py
from fastapi import FastAPI
from api.routers import auth

app = FastAPI(
    title="Job Portal API",
    description="API documentation for the Job Portal user authentication system."
)

# Include the authentication router
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Portal API"}

