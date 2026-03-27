# SecureIoT-NLP

NLP-based security and privacy risk detection for IoT automation rules.

## Problem

Smart home automation rules (e.g., "If door unlocks, turn off camera") can introduce security vulnerabilities and privacy leaks. Existing IoT platforms don't analyze rules for risk before deployment.

## Approach

- Parse IoT automation rules from trigger-action datasets
- Extract semantic features using NLP preprocessing
- Classify rules by risk category (security, privacy, safety, benign)
- Flag dangerous rule combinations before they're deployed

## Tech Stack

`Python` `NLP` `scikit-learn` `pandas`

## Project Structure

```
SecureIoT-NLP/
├── src/
│   ├── data_exploration.py    # Dataset analysis
│   └── data_preprocessing.py  # Feature extraction pipeline
├── data/                      # IoT rule datasets
├── models/                    # Trained classifiers
├── docs/                      # Documentation
└── script.py                  # Entry point
```

## Usage

```bash
pip install -r requirements.txt
python script.py
```

## License

MIT
