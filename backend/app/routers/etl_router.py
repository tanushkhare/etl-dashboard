from fastapi import APIRouter, HTTPException
from backend.app.schemas.etl_schema import ETLProcessRequest, ETLProcessResponse
from backend.app.services.etl_service import etl_engine

router = APIRouter(prefix="/api/v1/etl", tags=["Real-Time ETL Engine"])

@router.post("/process", response_model=ETProcessResponse if "ETProcessResponse" in locals() else ETLProcessResponse)
async def trigger_etl_pipeline(payload: ETLProcessRequest):
    try:
        metrics = await etl_engine.process_batch(payload.batch_size, payload.target_sink)
        return ETLProcessResponse(**metrics)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
