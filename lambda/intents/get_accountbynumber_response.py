
from . import build_response, build_speechlet_response, pos_to_int
from endpoints import Endpoints

def get_accountbynumber_response(name, session, intent):
    """ This response is built when the accountbynumber intent is triggered.
        The user will request ('tell me about my first account') and this is
        the response.
    """
    # ensure session attributes are passed on throughout the session
    session_attributes = session['attributes']
    
    
    # the account the user wishes to access
    # if user wants to access the first account = accounts[0]
    input_number = intent['slots']['number']['value']
    
    number = pos_to_int(input_number)
    
    # load accounts by owner. if the function fails to find the owner name,
    # it will return with 'Error'
    
    data = Endpoints.accounts_by_owner(owner=name)
    if data != 'Error':
        accounts = data['accounts']
        num_accounts=len(accounts)
        
    
    if number == -1:
        speech_output = f'Account number out of bounds'
    elif data in ['Error']:
        speech_output = f'User {name} not found.'
    elif number<=num_accounts:
        balance = accounts[number]['balance']
        speech_output = f'The balance in your {input_number} account is {balance} cents'
    else:
        speech_output = f'{number} account not found.'
    
    card_title = "PosAccount"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))