from pydantic import BaseModel

class MetricsIngestRequest(BaseModel):
    metric_name: str
    value: float
    source: str

class MetricsResponse(BaseModel):
    status: str
    message: str
    processed_value: float