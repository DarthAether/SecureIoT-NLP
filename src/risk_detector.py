import pandas as pd
from nlp_model import classify_risk

def detect_risks(rule_data):
    """
    Detect risks from a list of IoT rule descriptions.
    """
    detected_risks = []
    for rule in rule_data:
        risk, score = classify_risk(rule['description'])
        detected_risks.append({
            'rule': rule['description'],
            'detected_risk': risk,
            'confidence': score
        })
    return pd.DataFrame(detected_risks)

