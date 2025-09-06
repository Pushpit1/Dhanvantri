"""
Communication package initializer.
Provides a common interface to integrate multiple channels like
web, SMS, and WhatsApp for the health chatbot.
"""
from .web_app import create_web_app
from .sms_handler import handle_sms
from .whatsapp_bot import handle_whatsapp
