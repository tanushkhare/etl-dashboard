from pydantic import BaseModel, Field
from typing import Optional

class ETLRequest(BaseModel):
    batch_size: int = Field(..., ge=10, le=100000, description="Number of stream records in batch")
    target_sink: str = Field(..., description="Target database/lake sink (ClickHouse, PostgreSQL, S3)")

class ETLResponse(BaseModel):
    status: str
    throughput_rps: int
    quality_score: float
    dropped_records: int
    latency_ms: float
    partition_key: str
    bytes_written_kb: float
