from pydantic import ValidationError
import pytest
from core.domain.event import EventCreate

def test_event_create_valid():
    event = EventCreate(
        match_id="507f1f77bcf86cd799439011",
        player_dorsal=10,
        game_minute=15,
        action_type="GOAL",
        action_subtype="Zone 1"
    )
    assert event.player_dorsal == 10
    assert event.action_type == "GOAL"

def test_event_create_invalid_action_type():
    with pytest.raises(ValidationError):
        EventCreate(
            match_id="507f1f77bcf86cd799439011",
            player_dorsal=10,
            game_minute=15,
            action_type="INVALID",
            action_subtype="Zone 1"
        )

def test_event_create_invalid_dorsal():
    with pytest.raises(ValidationError):
        EventCreate(
            match_id="507f1f77bcf86cd799439011",
            player_dorsal=100, # Max is 99
            game_minute=15,
            action_type="GOAL",
            action_subtype="Zone 1"
        )
