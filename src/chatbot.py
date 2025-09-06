# dummy example for testing
user_state = {}


def chatbot_response(user_id):
    if user_id not in user_state:
        user_state[user_id] = {"questions_asked": 0}

    state = user_state[user_id]

    # Max 3 follow-up questions
    if state["questions_asked"] < 3:
        state["questions_asked"] += 1
        return f"Question {state['questions_asked']}: Do you have fever?"
    else:
        # Final diagnosis
        user_state[user_id] = {}  # reset
        return "✅ Based on your answers, you may have a mild cold. Take rest and stay hydrated."
