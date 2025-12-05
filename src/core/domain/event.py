
# src/core/domain/event.py
from pydantic import BaseModel, Field, conint, ConfigDict
from typing import Optional
from datetime import datetime

# --- Pydantic Model for incoming HTTP data ---
class EventCreate(BaseModel):
    match_id: str = Field(..., description="Unique ID of the current match (ObjectId string).")
    player_dorsal: conint(ge=1, le=99) = Field(..., description="Dorsal of the player involved in the action.")
    game_minute: conint(ge=0) = Field(..., description="Minute in the match clock.")
    
    action_type: str = Field(..., strict=True, pattern=r"^(GOAL|MISS|RECOVERY|LOSS|RIVAL_GOAL|TIMEOUT|CARD)$", description="Primary action type.")
    action_subtype: str = Field(..., description="Context of the action, such as shot zone or cause of turnover.")
    
    xg_value: Optional[float] = Field(None, description="Expected Goals value, if applicable.")
    
# --- Model used for data storage in MongoDB (DB Model) ---
class EventDB(EventCreate):
    id: str = Field(..., alias="_id", description="MongoDB's unique document ID.")
    timestamp_record: datetime = Field(default_factory=datetime.utcnow, description="Server-side timestamp of when the event was recorded.")
    operator_ip: Optional[str] = Field(None, description="IP address of the client that submitted the event.")
    team: str = Field("Muskiz EB", description="Team performing the action (default: Muskiz EB).")
    
    model_config = ConfigDict(populate_by_name=True)