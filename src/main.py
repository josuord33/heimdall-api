# src/main.py
from fastapi import FastAPI
# Attempt to load the DB client on startup (will print success/failure)
from infrastructure.persistence.client import mongo_client 
from infrastructure.api.event_router import events_router

app = FastAPI(
    title="HEIMDALL API - Handball Data Logger",
    version="0.1.0",
    description="High-performance API for real-time handball event logging."
)

# --- Include Routers ---
app.include_router(events_router)


@app.get("/", summary="Health Check")
async def root():
    return {"message": "HEIMDALL API Running"}