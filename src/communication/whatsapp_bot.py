from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from src.core.advice import get_advice

# Create a blueprint for the WhatsApp bot
whatsapp_bot_blueprint = Blueprint('whatsapp_bot', __name__)

@whatsapp_bot_blueprint.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    """
    Handles incoming WhatsApp messages and sends a reply.
    """
    try:
        # Get the incoming message from the request
        incoming_msg = request.values.get('Body', '').lower()
        user_language = 'en'  # Default to English for simplicity

        # Get advice from the core logic
        response_text = get_advice(incoming_msg, user_language)

        # Create a TwiML response
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(response_text)

        return str(resp)

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred in WhatsApp handler: {e}")
        resp = MessagingResponse()
        msg = resp.message()
        msg.body("An internal error occurred. Please try again later.")
        return str(resp)
