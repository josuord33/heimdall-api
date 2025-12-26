from unittest.mock import patch, MagicMock
from core.services.event_service import EventService
from core.domain.event import EventCreate

def test_record_new_event():
    # Mock data
    event_data = EventCreate(
        match_id="507f1f77bcf86cd799439011",
        player_number=10,
        game_minute=15,
        action_type="GOAL",
        action_subtype="Zone 1"
    )
    operator_ip = "127.0.0.1"
    
    # Mock repository
    with patch("core.services.event_service.event_repository") as mock_repo:
        mock_repo.insert_event.return_value = "new_event_id"
        
        service = EventService()
        result = service.record_new_event(event_data, operator_ip)
        
        assert result == "new_event_id"
        mock_repo.insert_event.assert_called_once()
        
        # Check that operator_ip was added
        call_args = mock_repo.insert_event.call_args[0][0]
        assert call_args["operator_ip"] == operator_ip
        assert call_args["action_type"] == "GOAL"
