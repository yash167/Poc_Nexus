
from fastapi import FastAPI
from prometheus_client import make_asgi_app
from starlette.middleware.wsgi import WSGIMiddleware

app = FastAPI(title="PoCForge FINAL")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/risk/{asset_id}")
def risk(asset_id: str):
    return {
        "asset_id": asset_id,
        "risk_score": 82.5,
        "sla_days": 7,
        "zero_day_probability": 0.42
    }

@app.get("/executive-summary/{asset_id}")
def executive(asset_id: str):
    return {
        "executive_summary": f"Asset {asset_id} shows elevated risk posture."
    }

metrics_app = make_asgi_app()
app.mount("/metrics", WSGIMiddleware(metrics_app))
