
from . import build_response, build_speechlet_response
from endpoints import Endpoints

def get_recenttransactions_response(name, session, intent):
    '''
        This response is build on the recenttransactions intent. Alexa will
        tell the user details about their most recent transaction.
    '''
    # ensure session attributes are passed on throughout the session
    session_attributes = session['attributes']
    
    transactions = Endpoints.list_transactions_by_owner(owner=name)

    recent_transaction = transactions[0]
    party = recent_transaction['counterParty']
    amount = recent_transaction['amount']
    type = recent_transaction['type']
    desc = recent_transaction['description']
    card_title = "RecentTransaction"
    
    line_1 = f"The party that hosted your transaction was {party}. "
    line_2 = f'The amount was {amount} cents. '
    line_3 = f'The transaction type was {type}. '
    line_4 = f'The description for the transaction is: {desc}. '
    
    speech_output = line_1 + line_2 + line_3 + line_4
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))