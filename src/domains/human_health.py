import re
from src.core.data_loader import get_data, get_i18n

def get_physical_health_advice(query, language):
    """
    Provides advice on human physical health.
    Searches for diseases, symptoms, and vaccines.
    """
    i18n = get_i18n(language)
    data = get_data('human')
    lower_query = query.lower()

    # Check for specific diseases
    if 'physical_diseases' in data and not data['physical_diseases'].empty:
        for _, row in data['physical_diseases'].iterrows():
            if re.search(r'\b' + re.escape(row['disease'].lower()) + r'\b', lower_query):
                return i18n["human_physical_disease_advice"].format(
                    query=row['disease'],
                    symptoms=row['symptoms'],
                    prevention=row['prevention'],
                    treatment=row['treatment']
                )

    # Check for specific symptoms
    if 'symptoms' in data and not data['symptoms'].empty:
        for _, row in data['symptoms'].iterrows():
            if re.search(r'\b' + re.escape(row['symptom'].lower()) + r'\b', lower_query):
                return i18n["human_symptom_advice"].format(
                    query=row['symptom'],
                    causes=row['potential_causes'],
                    next_steps=row['recommended_action']
                )

    # Check for specific vaccines
    if 'vaccines' in data and not data['vaccines'].empty:
        for _, row in data['vaccines'].iterrows():
            if re.search(r'\b' + re.escape(row['vaccine_name'].lower()) + r'\b', lower_query):
                return i18n["human_vaccine_advice"].format(
                    query=row['vaccine_name'],
                    diseases_prevented=row['diseases_prevented'],
                    schedule=row['recommended_schedule']
                )

    # If no specific match is found, provide general advice
    return i18n["human_physical_unknown_response"]

def get_mental_health_advice(query, language):
    """
    Provides advice on human mental health.
    Searches for conditions and coping strategies.
    """
    i18n = get_i18n(language)
    data = get_data('human')
    lower_query = query.lower()

    # Check for specific mental conditions
    if 'mental_conditions' in data and not data['mental_conditions'].empty:
        for _, row in data['mental_conditions'].iterrows():
            if re.search(r'\b' + re.escape(row['condition'].lower()) + r'\b', lower_query):
                return i18n["human_mental_condition_advice"].format(
                    query=row['condition'],
                    symptoms=row['symptoms'],
                    professional_help=row['professional_interventions'],
                    self_care=row['self_care_strategies']
                )

    # Check for coping strategies
    if 'coping_strategies' in data and not data['coping_strategies'].empty:
        for _, row in data['coping_strategies'].iterrows():
            if re.search(r'\b' + re.escape(row['strategy'].lower()) + r'\b', lower_query):
                return i18n["human_coping_strategy_advice"].format(
                    query=row['strategy'],
                    description=row['description'],
                    benefits=row['benefits']
                )

    # If no specific match is found, provide general advice
    return i18n["human_mental_unknown_response"]
