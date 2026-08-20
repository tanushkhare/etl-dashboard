from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import dashboard

app = FastAPI(
    title="ETL Pipeline & Dashboard API",
    version="1.0.0",
    description="API for ingesting, transforming, and serving analytical metrics."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)

@app.get("/")
def read_root():
    return {"message": "ETL Pipeline & Dashboard Backend is running successfully!"}