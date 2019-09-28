
from . import build_response, build_speechlet_response
from endpoints import Endpoints

def get_createaccount_response(name, session, intent):
    '''
        The user wishes to create an account
    '''
    # ensure session attributes are passed on throughout the session
    session_attributes = session['attributes']
    
    data = Endpoints.create_account(owner=name, balance=100)
    
    speech_output = f'Created an account for {name}. Your account has a balance of 100 cents.'
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = speech_output
    card_title = 'CreateAccount'
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))