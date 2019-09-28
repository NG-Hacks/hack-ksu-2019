
from . import build_response, build_speechlet_response

def get_makedeposit_response(name, session, intent):
    """ 
        Response for when the use wants to make a deposit
    """
    session_attributes = session['attributes']
    card_title = "MakeDeposit"
    speech_output = "Okay, I just need your social security number. Just kidding. Go to an ATM."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))