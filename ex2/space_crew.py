from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime

class Rank(str, Enum):
    CADET="cadet"
    OFFICER="officer"
    LIEUTENANT="lieutenant"
    CAPTAIN="captain"
    COMMANDER="commander"


class CrewMember_Model(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=10)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission_Model(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember_Model] = Field(ge=1, le=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def Mission_validator(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("The Mission ID should starts with M")

        is_have = 0
        for i in crew:
            if i.rank.lower() == "commader" or i.rank.lower() == "captain":
                is_have += 1
        if is_have == 0:
            raise ValueError("Must have at least one Commander or Captain")

        if duration_days > 365:
            num = 0
            for i in crew:
                if i.years_experience < 5:
                    num += 1

            if num >= len(self.crew) / 2:
                raise ValueError("you need 50% experienced crew (5+ years)")

        for i in crew:
            if not i.is_active:
                raise ValueError("All crew members must be active")

        return self

first_member = CrewMember_Model(
        member_id="saher123",
        name="SarahConnor",
        rank="commander",
        age=20,
        specialization="Mission Command",
        years_experience=7
        )

sec_member = CrewMember_Model(
        member_id="john123",
        name="John Smith",
        rank="lieutenant",
        age=22,
        specialization="Navigation",
        years_experience=20
        )

thir_member = CrewMember(
        member_id="alice123",
        name="AliceJohnso",
        rank="officer",
        age=21,
        specialization="Engineering",
        years_experience=40
        )

valid_mission = SpaceMission_Model(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[first_member, sec_member, thir_member]
        )

print("Space Mission Crew Validation")
print("=========================================")
print("Valid mission created:")
print(f"Mission: {valid_mission.mission_name}")
print(f"ID: {valid_mission.mission_id}")
print(f"Destination: {valid_mission.destination}")
print(f"Duration: {valid_mission.duration} days")
print(f"Budget: {valid_mission.budget_millions}")
print(f"Crew size: {len(crew)}")
print("Crew members:")
for i in range(len(crew)):
    print(f"- {i.name} ({i.rank}) - {i.specialization}")
print()

try:
    CrewMember_Model(
        member_id="saher123",
        name="Sarah Connor",
        rank="commander",
        age=20,
        specialization="Mission Command",
        years_experience=7
        )

except ValidationError as error:
    print("=========================================")
    print("Expected validation error:")
    for err in error.errors():
        print(err["msg"])
