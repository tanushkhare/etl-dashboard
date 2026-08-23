from pydantic import BaseModel, Field

class ETLRequest(BaseModel):
    batch_size: int = Field(..., ge=100, le=100000, description="Batch record count")
    target_sink: str = Field(..., description="Target database sink: ClickHouse, PostgreSQL, or S3")

class ETLResponse(BaseModel):
    status: str
    throughput_rps: int
    quality_score: float
    dropped_records: int
    latency_ms: float
    partition_key: str
    bytes_written_kb: float
