from fastapi import APIRouter
from app.schemas.dashboard import MetricsIngestRequest, MetricsResponse
from app.services.dashboard_service import process_etl_pipeline

router = APIRouter(prefix="/api", tags=["Dashboard & ETL"])

@router.post("/metrics", response_model=MetricsResponse)
def ingest_metrics(payload: MetricsIngestRequest):
    return process_etl_pipeline(payload.metric_name, payload.value, payload.source)