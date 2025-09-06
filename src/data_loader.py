# Simulate real-time outbreak & vaccine info
def get_outbreak_alert(disease):
    alerts = {
        "covid": "High alert in your area. Wear mask & sanitize.",
        "malaria": "Increase in cases in nearby villages."
    }
    return alerts.get(disease.lower(), "")

def get_vaccine_info(disease):
    vaccines = {
        "covid": "Vaccines available: Covaxin, Covishield.",
        "flu": "Flu shot recommended annually."
    }
    return vaccines.get(disease.lower(), "")
