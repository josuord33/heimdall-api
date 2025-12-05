# src/core/services/event_service.py
from typing import Optional, Dict, Any
from core.domain.event import EventCreate
# Dependency Inversion Principle: The Core calls the repository adapter
from infrastructure.persistence.repositories import event_repository

class EventService:
    """
    Service layer for all Event-related business logic.
    It orchestrates the data flow between the API and the persistence layer.
    """
    
    def record_new_event(self, event_data: EventCreate, operator_ip: str) -> Optional[str]:
        """
        Receives the validated event data, prepares it for storage, and calls 
        the persistence adapter.
        """
        
        # 1. Convert the Pydantic model to a dictionary for PyMongo
        event_dict = event_data.model_dump()
        
        # 2. Add server-side metadata (this is business logic/preparation)
        event_dict["operator_ip"] = operator_ip
        # Note: The 'timestamp_record' is added by the EventDB model default factory
        
        # 3. Call the Persistence Adapter (the Port)
        inserted_id = event_repository.insert_event(event_dict)
        
        # 4. Return the result ID or None
        return inserted_id

# Instantiated service to be used in the FastAPI router (Infrastructure)
event_service = EventService()