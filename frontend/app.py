import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #090d16;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        .sidebar .stSidebar {
            background-color: #0f172a;
            border-right: 1px solid #1e293b;
        }
        h1, h2, h3 {
            color: #f8fafc;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        .stButton>button {
            background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
            color: #090d16;
            font-weight: 600;
            border: none;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Real-Time ETL Dashboard", layout="wide")

st.title("⚡ Real-Time ETL Pipeline & Stream Monitoring")
st.markdown("High-velocity data ingestion, schema validation telemetry, and OLAP sink execution metrics.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Pipeline Dispatch Parameters")
    batch_size = st.slider("Batch Record Size", 500, 50000, 5000, step=500)
    target_sink = st.selectbox("Target Storage Sink", ["ClickHouse", "PostgreSQL", "Apache Iceberg", "Amazon S3"])
    
    if st.button("Trigger Ingestion Batch", type="primary"):
        with st.spinner("Executing pipeline ETL extraction & normalization..."):
            try:
                res = requests.post("http://localhost:8000/api/v1/etl/process", json={"batch_size": batch_size, "target_sink": target_sink}, timeout=5)
                if res.status_code == 200:
                    st.session_state["p04b_result"] = res.json()
                    st.success("Batch successfully ingested!")
                else:
                    st.error(f"ETL API Error: {res.text}")
            except Exception:
                st.warning("Backend API offline. Executing client-side simulated ETL stream.")
                st.session_state["p04b_result"] = {
                    "status": "SUCCESS",
                    "records_processed": batch_size,
                    "throughput_rps": round(batch_size / 0.045, 2),
                    "bytes_written_kb": round((batch_size * 128) / 1024, 2),
                    "quality_score": 99.8,
                    "partition_key": f"{target_sink.lower()}_partition_sim_01",
                    "target_sink": target_sink,
                    "timestamp": "2026-08-28T07:00:00Z"
                }

with col2:
    if "p04b_result" in st.session_state:
        res = st.session_state["p04b_result"]
        st.subheader("Telemetry & Execution Metrics")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Records Ingested", f"{res['records_processed']:,}")
        m2.metric("Throughput (RPS)", f"{res['throughput_rps']:,.1f}")
        m3.metric("Data Quality Score", f"{res['quality_score']}%")
        
        st.markdown(f"**Target Sink:** `{res['target_sink']}` | **Partition Key:** `{res['partition_key']}`")
        
        # Telemetry chart
        df = pd.DataFrame({
            "Stage": ["Extraction", "Transformation", "Validation", "Sink Load"],
            "Duration (ms)": [12, 18, 5, 9]
        })
        fig = px.bar(df, x="Stage", y="Duration (ms)", title="Pipeline Stage Latency Breakdown (ms)", color="Stage")
        st.plotly_chart(fig, use_container_width=True)

