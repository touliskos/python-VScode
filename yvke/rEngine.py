import os
import json
import logging
from typing import List
from iModels import PatientInfo, WeightCategory

logger = logging.getLogger(__name__)

# Load adjustment factors from config.json
# rEngine.py

# Build absolute path relative to this file's directory
config_path = os.path.join(os.path.dirname(__file__), 'config.json')

with open(config_path, 'r') as f:
    config = json.load(f)
    ADJUSTMENT_FACTORS = config["adjustment_factors"]


class TSHRange:
    def __init__(self, lower: float, upper: float, dose: float):
        self.lower = lower
        self.upper = upper
        self.dose = dose

    def contains(self, tsh: float) -> bool:
        """Check if the TSH value falls within this range."""
        return self.lower <= tsh < self.upper

    def adjust_for_factors(self, weight: float, age: int, thyroidectomy: bool, twin: bool, ivf: bool) -> float:
        """Adjust the base dose based on patient-specific factors. this part is yet to be done """
        base_dose = self.adjust_for_weight(weight)

        # Apply adjustments based on conditions, further adjustments to be be added here, possibly
        adjustments = {
            "elderly": age > 45,
            "thyroidectomy": thyroidectomy,
            "twin": twin,
            "ivf": ivf
        }

        for factor, condition in adjustments.items():
            if condition:
                base_dose *= ADJUSTMENT_FACTORS[factor]
                logger.info(
                    f"Applied {factor} adjustment: {ADJUSTMENT_FACTORS[factor]}")

        return base_dose

    def get_weight_category(self, weight: float) -> WeightCategory:
        """Determine the weight category based on the patient's weight."""
        if weight < 50:
            return WeightCategory.UNDER_50
        elif weight <= 65:
            return WeightCategory.BETWEEN_50_65
        elif weight <= 75:
            return WeightCategory.BETWEEN_65_75
        else:
            return WeightCategory.ABOVE_75

    def adjust_for_weight(self, weight: float) -> float:
        """Adjust the base dose based on the patient's weight category."""
        weight_category = self.get_weight_category(weight)
        if weight_category == WeightCategory.UNDER_50:
            return self.dose - 12.5
        elif weight_category == WeightCategory.ABOVE_75:
            return self.dose + 12.5
        return self.dose


class DoseCalculator:
    def __init__(self):
        self.tsh_dose: List[TSHRange] = [
            TSHRange(i["lower"], i["upper"], i["dose"])
            for i in config["tsh_dose"]
        ]

    def recommend_dose(self, patient: PatientInfo) -> str:
        """Recommend a dose based on the patient's TSH value and other factors."""
        try:
            from Helper import validate_patient_info
            validate_patient_info(patient)
            print()
            logger.info(
                f"\nΕκτίμηση δόσης λεβοθυροξίνης για έγκυο ασθενή με \n\033[96mτιμή TSH: {patient.tsh}, βάρους: {patient.weight} kg\033[0m")
            print()
            print()

            for i in self.tsh_dose:
                if i.contains(patient.tsh):
                    final_dose = i.adjust_for_factors(
                        patient.weight, patient.age, patient.thyroidectomy, patient.twin, patient.ivf
                    )
                    logger.info(f"\nFinal dose calculated: {final_dose} mcg")
                    print("="*50)
                    return f"\033[33mΠροτεινόμενη δοσολογία: {final_dose} mcg\033[0m"
                    print()

            return "TSH out of range. Ειδικός Ιατρός θα επικοινωνήσει στα στοιχεία που έχουμε καταχωρημένα."
        except ValueError as e:
            logger.error(f"Validation failed: {e}")
            return str(e)

    def recommend_dose_new_patient(self, patient):
        # Algorithm for new patient
        # ...implementation...
        pass

    def recommend_dose_existing_patient(self, patient):
        # Algorithm for existing patient
        # ...implementation...
        pass

    def recommend_dose_on_medication(self, patient):
        # Algorithm for patient on medication
        # ...implementation...
        pass
