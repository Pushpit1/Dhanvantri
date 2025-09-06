import os
import pandas as pd
import json

# Global variables to store the data in memory
HEALTH_DATA = {}
I18N_DATA = {}

def load_data():
    """
    Loads all data from CSV files into the global HEALTH_DATA dictionary.
    """
    global HEALTH_DATA
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

    # Load human health data
    human_path = os.path.join(base_path, 'human')
    HEALTH_DATA['human'] = {
        'physical_diseases': pd.read_csv(os.path.join(human_path, 'physical_diseases.csv')),
        'mental_conditions': pd.read_csv(os.path.join(human_path, 'mental_conditions.csv')),
        'coping_strategies': pd.read_csv(os.path.join(human_path, 'coping_strategies.csv')),
        'symptoms': pd.read_csv(os.path.join(human_path, 'symptoms.csv')),
        'vaccines': pd.read_csv(os.path.join(human_path, 'vaccines.csv'))
    }

    # Load animal health data
    animal_path = os.path.join(base_path, 'animal')
    HEALTH_DATA['animal'] = {
        'diseases': pd.read_csv(os.path.join(animal_path, 'diseases.csv')),
        'symptoms': pd.read_csv(os.path.join(animal_path, 'symptoms.csv')),
        'vaccines': pd.read_csv(os.path.join(animal_path, 'vaccines.csv'))
    }

    # Load plant health data
    plant_path = os.path.join(base_path, 'plant')
    HEALTH_DATA['plant'] = {
        'diseases': pd.read_csv(os.path.join(plant_path, 'diseases.csv')),
        'pests': pd.read_csv(os.path.join(plant_path, 'pests.csv')),
        'vaccines': pd.read_csv(os.path.join(plant_path, 'vaccines.csv'))
    }

    print("All health data loaded successfully.")

def load_i18n():
    """
    Loads all internationalization data from JSON files.
    """
    global I18N_DATA
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'i18n')

    for filename in os.listdir(base_path):
        if filename.endswith('.json'):
            lang_code = os.path.splitext(filename)[0]
            with open(os.path.join(base_path, filename), 'r', encoding='utf-8') as f:
                I18N_DATA[lang_code] = json.load(f)

    print("All internationalization data loaded successfully.")

def get_data(domain):
    """
    Retrieves the loaded data for a specific health domain.
    """
    return HEALTH_DATA.get(domain, {})

def get_i18n(language):
    """
    Retrieves the internationalization data for a specific language.
    """
    return I18N_DATA.get(language, I18N_DATA.get('en', {}))
