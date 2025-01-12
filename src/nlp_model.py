from transformers import pipeline

def classify_risk(rule_description):
    """
    Classify the risk level of a given IoT rule description using a pre-trained NLP model.
    """
    model = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
    categories = ["Data Leakage", "Physical Vulnerability", "Cybersecurity Threat"]
    result = model(rule_description, candidate_labels=categories)
    return result['labels'][0], result['scores'][0]

