
from . import build_response, build_speechlet_response

def get_welcome_response():
    """ Response for when the user starts the sesssion
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the account management application!"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))