import re
from src.core.data_loader import get_data, get_i18n

def get_animal_health_advice(query, language):
    """
    Provides advice on animal health based on the user's query.
    Searches through diseases, symptoms, and vaccines data.
    """
    i18n = get_i18n(language)
    data = get_data('animal')
    lower_query = query.lower()

    # Check if the query is for a specific disease
    if 'diseases' in data and not data['diseases'].empty:
        for index, row in data['diseases'].iterrows():
            if re.search(r'\b' + re.escape(row['disease'].lower()) + r'\b', lower_query):
                return i18n["animal_disease_advice"].format(
                    query=row['disease'],
                    animals_affected=row['affected_animals'],
                    symptoms=row['symptoms'],
                    prevention=row['prevention']
                )

    # Check if the query is for a specific symptom
    if 'symptoms' in data and not data['symptoms'].empty:
        for index, row in data['symptoms'].iterrows():
            if re.search(r'\b' + re.escape(row['symptom'].lower()) + r'\b', lower_query):
                return i18n["animal_symptom_advice"].format(
                    query=row['symptom'],
                    causes=row['potential_causes'],
                    next_steps=row['recommended_action']
                )

    # Check if the query is for vaccines
    if 'vaccines' in data and not data['vaccines'].empty:
        for index, row in data['vaccines'].iterrows():
            if re.search(r'\b' + re.escape(row['vaccine_name'].lower()) + r'\b', lower_query):
                return i18n["animal_vaccine_advice"].format(
                    query=row['vaccine_name'],
                    diseases_prevented=row['diseases_prevented'],
                    schedule=row['recommended_schedule']
                )

    # If no specific match is found, provide general advice
    return i18n["animal_unknown_response"]
