import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_etl_process_batch():
    payload = {"batch_size": 2500, "target_sink": "ClickHouse"}
    res = client.post("/api/v1/etl/process", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "SUCCESS"
    assert data["quality_score"] == 99.8
    assert "clickhouse" in data["partition_key"]
