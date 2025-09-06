from flask import Blueprint, request, jsonify

# Import the core advice logic
from src.core.advice import get_advice

# Create a blueprint for the web application routes
web_app_blueprint = Blueprint('web_app', __name__)

@web_app_blueprint.route('/ask', methods=['POST'])
def ask_advice():
    """
    Handles POST requests from the web front-end.
    Expects a JSON payload with 'query' and 'language'.
    """
    try:
        data = request.get_json()
        user_query = data.get('query')
        user_language = data.get('language', 'en')

        if not user_query:
            return jsonify({"error": "No query provided."}), 400

        # Get advice from the core logic
        response = get_advice(user_query, user_language)

        return jsonify({"response": response})

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500
