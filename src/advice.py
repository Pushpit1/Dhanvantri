def get_advice(disease):
    advice_map = {
        "covid": "Isolate yourself, consult a doctor, monitor oxygen levels.",
        "flu": "Rest, stay hydrated, take antipyretics.",
        "malaria": "See a doctor urgently, avoid dehydration.",
        "fever": "Monitor temperature, stay hydrated, see doctor if persistent."
    }
    return advice_map.get(disease.lower(), "Consult a healthcare professional.")
