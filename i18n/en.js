const en = {
  locale: "en",
  meta: {
    language_name: "English",
    version: "1.0",
    last_updated: "2025-09-06"
  },
  intents: {
    greeting: {
      examples: ["hello", "hi", "hey", "good morning", "good evening"],
      responses: [
        "Hi! I'm HealthBot — I can help with symptoms, prevention tips, vaccine schedules and nearby health centres. How can I help you today?",
        "Hello! I can answer health questions, check symptoms, or help book an appointment. What would you like to do?"
      ]
    },
    thanks: {
      examples: ["thanks", "thank you", "thx"],
      responses: [
        "You're welcome! If you need anything else, I'm here.",
        "Glad to help — stay safe!"
      ]
    }
  },
  quick_replies: {
    main_menu: ["Check symptoms", "Prevention tips", "Vaccine schedule", "Book appointment", "Nearest center", "Emergency"]
  }
};
