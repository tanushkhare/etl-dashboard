# ⚡ Real-Time ETL Dashboard

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://etl-dashboard-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://etl-dashboard-web.vercel.app](https://etl-dashboard-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
High-throughput stream extraction, transformation, and validation pipeline streaming telemetry records into columnar storage with dead-letter queue (DLQ) quarantining.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, AsyncIO, Docker, Columnar Storage (ClickHouse/PostgreSQL)
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Non-blocking Event Loop:** Replaced blocking sleep calls with asynchronous task handling.
* **Dead-Letter Quarantine:** Automatically catches and isolates malformed records without halting the stream.
* **Containerized Config:** Dockerfile and requirements pinned for reliable builds.

---

## 🚀 API Contracts
```http
POST /api/v1/etl/process
Request:
{
  "batch_size": 2500,
  "target_sink": "ClickHouse"
}

Response (200 OK):
{
  "status": "SUCCESS",
  "throughput_rps": 13888,
  "quality_score": 99.8,
  "dropped_records": 2,
  "latency_ms": 14.2,
  "partition_key": "part_2026_clickhouse_01"
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v