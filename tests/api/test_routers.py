from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_create_event_success():
    payload = {
        "match_id": "507f1f77bcf86cd799439011",
        "player_dorsal": 10,
        "game_minute": 15,
        "action_type": "GOAL",
        "action_subtype": "Zone 1"
    }
    
    with patch("infrastructure.api.event_router.event_service") as mock_service:
        mock_service.record_new_event.return_value = "new_event_id"
        
        response = client.post("/events/", json=payload)
        
        assert response.status_code == 201
        assert response.json()["event_id"] == "new_event_id"

def test_create_event_invalid_data():
    payload = {
        "match_id": "507f1f77bcf86cd799439011",
        "player_dorsal": 10,
        "game_minute": 15,
        "action_type": "INVALID_TYPE", # Invalid
        "action_subtype": "Zone 1"
    }
    
    response = client.post("/events/", json=payload)
    
    assert response.status_code == 422
