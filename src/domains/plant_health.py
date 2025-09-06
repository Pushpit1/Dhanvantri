import re
from src.core.data_loader import get_data, get_i18n

def get_plant_health_advice(query, language):
    """
    Provides advice on plant health based on the user's query.
    Searches through diseases and pests data.
    """
    i18n = get_i18n(language)
    data = get_data('plant')
    lower_query = query.lower()

    # Check for specific diseases
    if 'diseases' in data and not data['diseases'].empty:
        for _, row in data['diseases'].iterrows():
            if re.search(r'\b' + re.escape(row['disease'].lower()) + r'\b', lower_query):
                return i18n["plant_disease_advice"].format(
                    query=row['disease'],
                    symptoms=row['symptoms'],
                    causes=row['causes'],
                    treatment=row['treatment']
                )

    # Check for specific pests
    if 'pests' in data and not data['pests'].empty:
        for _, row in data['pests'].iterrows():
            if re.search(r'\b' + re.escape(row['pest'].lower()) + r'\b', lower_query):
                return i18n["plant_pest_advice"].format(
                    query=row['pest'],
                    affected_plants=row['affected_plants'],
                    signs=row['signs_of_infestation'],
                    treatment=row['treatment_options']
                )

    # If no specific match is found, provide general advice
    return i18n["plant_unknown_response"]
