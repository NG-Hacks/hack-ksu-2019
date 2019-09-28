
from . import build_response, build_speechlet_response

def get_authorization_response():
    """ The user has not yet been authorized. Request authorization.
    """
    session_attributes = {}
    card_title = "AuthorizationRequest"
    speech_output = f'Please authorize by telling me your name.'
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))