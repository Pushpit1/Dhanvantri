from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from src.core.advice import get_advice

# Create a blueprint for the SMS handler
sms_handler_blueprint = Blueprint('sms_handler', __name__)

@sms_handler_blueprint.route("/sms", methods=['POST'])
def sms_reply():
    """
    Handles incoming SMS messages and sends a reply.
    """
    try:
        # Get the incoming message from the request
        incoming_msg = request.values.get('Body', '').lower()
        user_language = 'en'  # Default to English for simplicity

        # Get advice from the core logic
        response_text = get_advice(incoming_msg, user_language)

        # Create a TwiML response
        resp = MessagingResponse()
        resp.message(response_text)

        return str(resp)

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred in SMS handler: {e}")
        resp = MessagingResponse()
        resp.message("An internal error occurred. Please try again later.")
        return str(resp)
