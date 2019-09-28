
from . import build_response, build_speechlet_response

def get_thankyou_response(user_name):
    """ Response for when the user wants to end the session
    """
    session_attributes = {}
    card_title = "ThankYou"
    speech_output = f"Thank you {user_name} for using our application!"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))