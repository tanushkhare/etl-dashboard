from fastapi import APIRouter, HTTPException
from backend.app.schemas.dashboard import ETLRequest, ETLResponse
from backend.app.services.dashboard_service import etl_engine

router = APIRouter(prefix="/api/v1/etl", tags=["ETL Pipeline"])

@router.post("/process", response_model=ETLResponse)
async def process_etl_batch(payload: ETLRequest):
    try:
        result = etl_engine.process_batch(payload.batch_size, payload.target_sink)
        return ETLResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
