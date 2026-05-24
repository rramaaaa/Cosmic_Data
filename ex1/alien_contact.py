from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validator_Checker(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("The Contact ID should start with AC")

        elif self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                    "The Signal Strength more than 7.0 "
                    "or missing received message"
                    )

        elif self.contact_type == ContactType.TELEPATHIC and\
                self.witness_count < 3:
            raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                    )

        elif self.contact_type == ContactType.PHYSICAL\
                and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        else:
            return self


valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        contact_type="radio",
        location="Area 51, Nevada",
        signal_strength=8.0,
        duration_minutes=45,
        witness_count=5,
        message_received="’Greetings from Zeta Reticuli’"
        )

print("Alien Contact Log Validation")
print("======================================")
print("Valid contact report:")
print(f"ID: {valid_contact.contact_id}")
print(f"Location: {valid_contact.location}")
print(f"Signal: {valid_contact.signal_strength}/10")
print(f"Duration: {valid_contact.duration_minutes} minutes")
print(f"Witnesses: {valid_contact.witness_count}")
print(f"Message: {valid_contact.message_received}")
print()

try:
    AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        contact_type="telepathic",
        location="Area 51, Nevada",
        signal_strength=8.0,
        duration_minutes=45,
        witness_count=2,
        message_received="’Greetings from Zeta Reticuli’"
        )

except ValidationError as error:
    print("======================================")
    print("Expected validation error:")
    for err in error.errors():
        print(err["msg"])
