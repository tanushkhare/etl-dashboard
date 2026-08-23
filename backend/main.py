from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import dashboard
import uvicorn

app = FastAPI(
    title="Real-Time ETL Pipeline Microservice",
    description="High-throughput batch stream ingestion, schema normalization, and storage sink router.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "etl-dashboard"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
