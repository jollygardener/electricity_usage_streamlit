import pandas as pd
import logging
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EnergyAttributes(BaseModel):
    state_class: str
    integration: str
    unit_of_measurement: str
    device_class: str
    friendly_name: str


class EnergyReading(BaseModel):
    entity_id: Optional[str] = None
    state: Optional[float] = None  # Changed to Optional[float]
    # attributes: Optional[EnergyAttributes] = None
    last_changed: datetime
    last_updated: Optional[datetime] = None

    @validator("state", pre=True)
    def parse_state(cls, v):
        if isinstance(v, (int, float)):
            return float(v)
        try:
            return float(v)
        except (ValueError, TypeError):
            return None  # Return None for invalid inputs


class EnergyData(BaseModel):
    readings: List[List[EnergyReading]]


# Example usage:
def parse_energy_data(json_data) -> pd.DataFrame:
    energy_data = EnergyData(readings=json_data)

    # Convert to DataFrame
    records = []
    skipped_count = 0

    for i, reading_group in enumerate(energy_data.readings):
        for j, reading in enumerate(reading_group):
            if reading.state is not None:
                record = {
                    "datetime": reading.last_changed,
                    "value": reading.state,
                }
                records.append(record)
            else:
                skipped_count += 1
                logger.warning(
                    f"Skipped reading at index [{i},{j}]: "
                    f"datetime={reading.last_changed}, "
                    f"entity_id={reading.entity_id}, "
                    f"invalid_value={reading.state}"
                )

    logger.info(
        f"Processed {len(records)} valid records, skipped {skipped_count} invalid records"
    )
    return pd.DataFrame(records)


# Usage example:
# with open('data.json') as f:
#     json_data = json.load(f)
# df = parse_energy_data(json_data)
# print(f"Processed {len(df)} valid records")
