import os
import pickle


def load_model():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    model_path = os.path.join(BASE_DIR, "models", "symptom_disease_model.pkl")
    with open(model_path, "rb") as f:
        vectorizer, model = pickle.load(f)
    return vectorizer, model

def predict_top_diseases(text, vectorizer, model, top_n=3):
    X_vec = vectorizer.transform([text])
    probs = model.predict_proba(X_vec)[0]
    classes = model.classes_
    top_indices = probs.argsort()[-top_n:][::-1]
    return [classes[i] for i in top_indices]
