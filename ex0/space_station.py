from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200)


def main() -> None:
    data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-05-18T14:30:00",
            "is_operational": True,
            "notes": None
            }

    station = SpaceStation(**data)
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not Operational")

    print()
    try:
        SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=30,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance="2026-05-18T14:30:00",
                is_operational=True,
                notes=None
                )
    except ValidationError as error:
        print("========================================")
        print("Expected validation error:")
        for err in error.errors():
            print(err["msg"])


main()
