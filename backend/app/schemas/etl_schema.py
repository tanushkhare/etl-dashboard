from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime

class ETLProcessRequest(BaseModel):
    batch_size: int = Field(default=1000, ge=10, le=100000, description="Records to ingest and transform")
    target_sink: str = Field(default="ClickHouse", description="Destination OLAP warehouse")

class ETLProcessResponse(BaseModel):
    status: str
    records_processed: int
    throughput_rps: float
    bytes_written_kb: float
    quality_score: float
    partition_key: str
    target_sink: str
    timestamp: str
