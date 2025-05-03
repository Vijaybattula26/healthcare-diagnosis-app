from transformers import pipeline

# Load pre-trained BART model for zero-shot classification
model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Possible diseases
diseases = [
    "Flu", "Cold", "Covid-19", "Migraine", "Pneumonia", "Allergy",
    "Asthma", "Stomach Infection", "Tuberculosis"
]


def diagnose(symptoms):
    """
    Given a string of symptoms, predict the disease based on zero-shot classification.

    Arguments:
    symptoms -- a string of symptoms separated by commas.

    Returns:
    A dictionary containing the predicted diseases and their confidence scores.
    """
    result = model(symptoms, candidate_labels=diseases)

    # Return the top predicted disease and its confidence score
    return result
