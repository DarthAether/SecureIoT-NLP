from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder='D:/3_2_AD/NLPAD/templates')

def detect_risks():
    # Example data to simulate detected risks
    risks_data = [
        {"Rule": "Rule 1", "Description": "User data sent unencrypted", "Risk": "Data Leakage", "Confidence": 0.85},
        {"Rule": "Rule 2", "Description": "Open port on device", "Risk": "Physical Vulnerability", "Confidence": 0.65},
        {"Rule": "Rule 3", "Description": "Unpatched software", "Risk": "Cybersecurity Threat", "Confidence": 0.90}
    ]
    
    # Create DataFrame
    detected_risks = pd.DataFrame(risks_data)
    
    return detected_risks

@app.route('/')
def dashboard():
    # Call the risk detection function
    detected_risks = detect_risks()

    # Convert the DataFrame to a list of dictionaries and pass to the template
    risks_list = detected_risks.to_dict(orient='records')

    return render_template('dashboard.html', risks=risks_list)

if __name__ == '__main__':
    app.run(debug=True)
