import re
from src.domains import human_health, animal_health, plant_health
from src.core.data_loader import get_data, get_i18n


def get_advice(domain, query, language):
    """
    Directs the query to the correct health domain handler.
    """
    i18n = get_i18n(language)

    if domain == "human":
        # Check for specific physical vs. mental health keywords
        if any(keyword in query.lower() for keyword in i18n["mental_health_keywords"]):
            return human_health.get_mental_health_advice(query, language)
        else:
            return human_health.get_physical_health_advice(query, language)
    elif domain == "plant":
        return plant_health.get_plant_health_advice(query, language)
    elif domain == "animal":
        return animal_health.get_animal_health_advice(query, language)
    else:
        return i18n["unknown_response"]


def identify_domain(query, language):
    """
    Identifies the health domain based on keywords in the query.
    """
    i18n = get_i18n(language)

    human_keywords = i18n["human_health_keywords"]
    plant_keywords = i18n["plant_health_keywords"]
    animal_keywords = i18n["animal_health_keywords"]

    if any(re.search(r'\b' + re.escape(k) + r'\b', query.lower()) for k in human_keywords):
        return "human"
    elif any(re.search(r'\b' + re.escape(k) + r'\b', query.lower()) for k in plant_keywords):
        return "plant"
    elif any(re.search(r'\b' + re.escape(k) + r'\b', query.lower()) for k in animal_keywords):
        return "animal"
    else:
        return "unknown"
