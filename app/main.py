from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Simple Task Tracker!"}

# Include API routes
app.include_router(api_router, prefix="/api")