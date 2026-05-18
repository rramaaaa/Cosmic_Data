from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    station_id: str = Field(gt=3, lt=11)
    name: str = Field(gt=0, lt=52)
    crew_size: int = Field(gt=0, lt=21)
    power_level: float = Field(gt=0.0, lt=100.0)
    oxygen_level: float = Field(gt=0.0, lt=100.0)
    last_maintenance: datetime
    is_operational: bool : Field(defaults=True)
    notes: str | None = Field(le=200)


def main() -> None:
    data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "is_operational": True
            }

    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print("Valied: ")
