# src/infrastructure/api/event_router.py
from fastapi import APIRouter, status, HTTPException, Request
from core.domain.event import EventCreate
from core.services.event_service import event_service

# Note: Security logic (JWT) will be added here later.
events_router = APIRouter(prefix="/events", tags=["Events"])

@events_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Record a new match event (GOAL, MISS, etc.)",
)
async def record_event(event: EventCreate, request: Request):
    """
    Receives an event payload from the tablet, validates it via Pydantic, 
    and sends it to the Core Service for processing and persistence.
    """
    
    # Extract IP address from the request
    operator_ip = request.client.host if request.client else "Unknown IP"
    
    # Call the Core Service layer (Dependency Inversion)
    inserted_id = event_service.record_new_event(event, operator_ip)
    
    if inserted_id:
        return {
            "message": "Event recorded successfully.",
            "event_id": inserted_id
        }
    else:
        # The service layer failed to persist the data (likely a MongoDB error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to record event due to a database error."
        )