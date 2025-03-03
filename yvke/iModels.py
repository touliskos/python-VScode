from dataclasses import dataclass
from enum import Enum
from typing import Optional

class WeightCategory(Enum):
    UNDER_50 = "<50"
    BETWEEN_50_65 = "50-65"
    BETWEEN_65_75 = "65-75"
    ABOVE_75 = ">75"

@dataclass
class PatientInfo:
    tsh: float
    gestational_week: int
    weight: float
    on_treatment: bool = False
    ivf: bool = False
    twin: bool = False
    thyroidectomy: bool = False
    age: int = 30
    previous_dose: Optional[float] = None
    fT4: Optional[float] = None
    TAI: Optional[float] = None
    is_new: bool = True  # Added field to support new patients
    on_medication: bool = False         # Added field to support patients on medication
    