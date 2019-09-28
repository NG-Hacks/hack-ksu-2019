
from . import build_response, build_speechlet_response, pos_to_int
from endpoints import Endpoints

def get_sendmoney_response(name, session, intent):
    '''
        This is the response when the user wants to send money
    '''
    # ensure session attributes are passed on throughout the session
    session_attributes = session['attributes']
    
    # load intent values
    try:
        dest = intent['slots']['dest']['value']
        amount = intent['slots']['amount']['value']
        input_number = intent['slots']['number']['value']
        if type(input_number) == str:
            number = pos_to_int(input_number)
            
        speech_output = f"Sending {dest} {amount} cents from the {input_number} account"
    except:
        speech_output = "There was an error."
    
    res = Endpoints.transaction_between_users(
            sourceOwner=name,
            destinationOwner=dest,
            sourceAccountNumber=number,
            amount=amount)
    print(res)
    if res == 'Error':
        raise ValueError
        
    card_title = "SendMoney"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))