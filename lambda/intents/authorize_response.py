
from . import build_response, build_speechlet_response

def authorize_response(intent):
    """ 
        This intent triggers once the user has authorized by announcing their
        names.
    """
    # load the name from the intent slots
    name = intent['slots']['name']['value']
    
    # put the name in the session attributes. this will allow us to pass it on
    # to other functions
    session_attributes = {'name': name}
    
    # build response
    card_title = "Authorization"
    speech_output = f'Thank you {name}. What would you like to do?'
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))