def explain_risk(rule, risk):
    """
    Explain the detected risk based on the IoT rule description.
    """
    explanations = {
        "Data Leakage": "This rule may send sensitive information (e.g., location) to untrusted services.",
        "Physical Vulnerability": "This rule grants access to physical devices that may not be secured properly.",
        "Cybersecurity Threat": "This rule involves external services that could be vulnerable to attacks."
    }
    return explanations.get(risk, "Unknown risk")

