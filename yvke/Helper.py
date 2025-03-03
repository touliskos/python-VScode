from iModels import PatientInfo

def validate_patient_info(patient: PatientInfo) -> None:
    """Validate patient information to ensure all values are within reasonable ranges."""
    if patient.tsh < 0:
        raise ValueError("TSH must be a positive number.")
    if patient.weight <= 0:
        raise ValueError("Weight must be a positive number.")
    if patient.age <= 0:
        raise ValueError("Age must be a positive number.")
    if not (0 <= patient.gestational_week <= 40):
        raise ValueError("Gestational week must be between 0 and 40.")