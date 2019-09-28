
from . import build_response, build_speechlet_response
from endpoints import Endpoints

def get_accountlist_response(name, session):
    """ This is the response for the account list response. Alexa will tell you
        how many accounts you have.
    """
    # ensure session attributes are passed on throughout the session
    session_attributes = session['attributes']
    
    # attempt to load accounts with the owner name. If the owner name does not
    # have any accounts, the function will return with "Error"
    data = Endpoints.accounts_by_owner(owner=name)

    if data != 'Error':
        accounts = data['accounts']
        speech_output = f'You have {len(accounts)} accounts.'
    else:
        speech_output = f'User {name} not found.'
    
    card_title = "NumAccounts"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))