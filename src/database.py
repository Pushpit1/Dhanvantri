# src/database.py
import pandas as pd
import os

# Paths to CSVs
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))

SYMPTOMS_FILE = os.path.join(BASE_DIR, "symptoms.csv")
DISEASES_FILE = os.path.join(BASE_DIR, "diseases.csv")
VACCINES_FILE = os.path.join(BASE_DIR, "vaccines.csv")

# Load CSVs once
symptom_data = pd.read_csv(SYMPTOMS_FILE)
disease_data = pd.read_csv(DISEASES_FILE)
vaccine_data = pd.read_csv(VACCINES_FILE)

def get_vaccine_info(disease_name):
    """Returns vaccine info for a disease if available"""
    row = vaccine_data[vaccine_data['disease'].str.lower() == disease_name.lower()]
    if not row.empty:
        return row['vaccine_info'].values[0]
    return None

def get_outbreak_alert(disease_name):
    """Returns outbreak alert info if available"""
    row = disease_data[disease_data['disease'].str.lower() == disease_name.lower()]
    if not row.empty and 'outbreak_alert' in row.columns:
        alert = row['outbreak_alert'].values[0]
        return alert if pd.notnull(alert) else None
    return None
