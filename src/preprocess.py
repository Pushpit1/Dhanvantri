import re

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z\s]', '', text)
    return text
