# ai-threat-detection-dashboard
# 🛡️ AI-Powered Network Threat Detection Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![ML](https://img.shields.io/badge/ML-Random%20Forest-green)
![Dataset](https://img.shields.io/badge/Dataset-CICIDS%202017-orange)

## 🔴 Live Demo
👉 **[subhavi-ai-threat-detection.streamlit.app](https://subhavi-ai-threat-detection.streamlit.app)**

## Overview
A real-time cybersecurity dashboard that uses Machine Learning to automatically detect and classify network-based cyberattacks. Built on the industry-standard CICIDS 2017 dataset used by real cybersecurity researchers.

The system detects 3 types of attacks with up to 98% precision:
- **DDoS** (Distributed Denial of Service)
- **Botnet** traffic
- **Port Scanning**

## Features
- Real-time threat detection simulation
- Interactive visualizations (pie chart, bar chart)
- Live metrics dashboard
- Random Forest classifier trained on 516,000+ real network traffic records
- 98% precision on DDoS detection

## Tech Stack
- **Python** — core language
- **Scikit-learn** — Random Forest ML model
- **Streamlit** — interactive dashboard
- **Plotly** — data visualizations
- **Pandas / NumPy** — data processing
- **CICIDS 2017** — real-world network intrusion dataset

## Dataset
The [CICIDS 2017 dataset](https://www.unb.ca/cic/datasets/ids-2017.html) was created by the Canadian Institute for Cybersecurity. It contains real network traffic captured during simulated cyberattacks, with 79 features per traffic flow including packet size, flow duration, and byte transfer rates.

## Model Performance
| Attack Type | Precision | Recall | F1-Score |
|-------------|-----------|--------|----------|
| DDoS        | 0.98      | 0.77   | 0.86     |
| Botnet      | 0.55      | 0.90   | 0.68     |
| Portscan    | 0.56      | 0.27   | 0.36     |
| **Overall** | **0.74**  | **0.70**| **0.68**|

## How to Run Locally
```bash
git clone https://github.com/SubhaviSomesula/ai-threat-detection-dashboard.git
cd ai-threat-detection-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/dashboard.py
```

## Project Structure
ai-threat-detection-dashboard/
├── data/                          # CICIDS 2017 dataset files
├── notebooks/
│   └── 01_data_exploration.ipynb  # EDA and model training
├── src/
│   └── dashboard.py               # Streamlit dashboard
├── requirements.txt
└── README.md

## Author
**Subhavi Somesula**
- LinkedIn: [linkedin.com/in/subhavisomesula](https://linkedin.com/in/subhavisomesula)
- Email: subhavisomesula@gmail.com