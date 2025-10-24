#experiment 9 

# Knowledge base: rules for diagnosis
rules = [
    {"if": {"fever", "cough", "fatigue"}, "then": "Flu"},
    {"if": {"fever", "cough", "shortness of breath"}, "then": "COVID-19"},
    {"if": {"headache", "nausea", "sensitivity to light"}, "then": "Migraine"},
    {"if": {"sore throat", "runny nose", "sneezing"}, "then": "Common Cold"},
    {"if": {"chest pain", "shortness of breath", "dizziness"}, "then": "Heart Attack"},
]

# Inference engine: checks which rules match the user's symptoms
def diagnose(symptoms):
    matched_diseases = []
    symptoms_set = set(symptoms)

    for rule in rules:
        if rule["if"].issubset(symptoms_set):
            matched_diseases.append(rule["then"])

    return matched_diseases


# User interface: terminal input/output
def main():
    print("🤖 Welcome to the Medical Expert System")
    print("Enter your symptoms separated by commas (e.g., fever, cough):")

    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_input.split(",")]

    diagnoses = diagnose(symptoms)

    if diagnoses:
        print("\n✅ Possible diagnosis(es):")
        for disease in diagnoses:
            print(f"- {disease}")
    else:
        print("\n⚠ No matching diagnosis found. Please consult a doctor.")


# Run the program
if _name_ == "_main_":
    main()