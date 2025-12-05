# src/infrastructure/persistence/repositories.py
import logging
from typing import Dict, Any, Optional
from pymongo.results import InsertOneResult
from pymongo.errors import PyMongoError
from infrastructure.persistence.client import events_collection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EventRepository:
    """
    Adapter for the 'events' collection. Implements the persistence methods 
    required by the Core Service.
    """

    def insert_event(self, event_data: Dict[str, Any]) -> Optional[str]:
        """
        Inserts a single event document into the MongoDB 'events' collection.
        Handles database errors and logging.
        """
        try:
            result: InsertOneResult = events_collection.insert_one(event_data)
            
            inserted_id = str(result.inserted_id)
            logger.info(f"Event successfully recorded with ID: {inserted_id}")
            
            return inserted_id
        
        except PyMongoError as e:
            logger.error(f"MongoDB Error during event insertion: {e}. Data: {event_data}")
            return None
        
        except Exception as e:
            logger.critical(f"Unexpected error during event insertion: {e}")
            return None

# Instantiated repository to be used in the Core Service layer
event_repository = EventRepository()