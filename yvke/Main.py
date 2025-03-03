# Χρειάζονται βελτιώσεις, για παραδειγμα θα χρειαστεί
# διαφορετικός αλγόριθμος για νεο περιστατικό και
# διαφορετικός για περισταικό που εχει έρθει (βαση δεδομένων)
# θα χρειαστεί να αλλαξει δόση
# διαφορετικό για καποιον που παιρνει αγωγή
# θα χρειαστεί να αλλαξει δόση
# θα χρειαστεί layer AI agent

import logging
from iModels import PatientInfo
from rEngine import DoseCalculator
from aiAgent import AIAgent  # Import AI agent

logging.basicConfig(level=logging.INFO)


def main():
    calculator = DoseCalculator()
    ai_agent = AIAgent()  # Initialize AI agent instance

    # Example patient data
    patient = PatientInfo(
        tsh=2.6,
        gestational_week=20,
        weight=70,
        age=30,
        is_new=False,  # New patient flag
        on_medication=False  # Medication flag
    )

    # Use AI agent to adjust patient data if necessaryd
    patient = ai_agent.adjust_patient_data(patient)

    # Different algorithms based on patient status
    # ενοχρηστρώντας τον αλγόριθμο που χρειάζεται σε κάθε περίπτωση
    if patient.is_new:
        recommendation = calculator.recommend_dose_new_patient(patient)
    elif patient.on_medication:
        recommendation = calculator.recommend_dose_on_medication(patient)
    #elif not patient.is_new:
       # recommendation = calculator.recommend_dose_existing_patient(patient)
    else:  # Default recommendation
        recommendation = calculator.recommend_dose(patient)

    print(recommendation)


if __name__ == "__main__":
    main()
