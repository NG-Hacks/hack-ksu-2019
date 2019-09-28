"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function

import json

# internal
#from utility import conn
from endpoints.transactions.transaction_between_users import transaction_between_users
from endpoints import Endpoints

Endpoints.initialize()

# --------------- Functions that control the skill's behavior ------------------
from intents.authorize_response import authorize_response
from intents.get_accountbynumber_response import get_accountbynumber_response
from intents.get_accountlist_response import get_accountlist_response
from intents.get_authorization_response import get_authorization_response
from intents.get_recenttransactions_response import get_recenttransactions_response
from intents.get_sendmoney_response import get_sendmoney_response
from intents.get_thankyou_response import get_thankyou_response
from intents.get_welcome_response import get_welcome_response
from intents.handle_session_end_request import handle_session_end_request
from intents.get_myname_response import get_myname_response
from intents.get_createaccount_response import get_createaccount_response
from intents.get_makedeposit_response import get_makedeposit_response
        

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    pass

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    
    # try to load the user name
    try:
        user_name = session['attributes']['name']
    # if it throws an error, likely the key doesn't exist, set user_name
    # to none because it is uninitialized
    except:
        user_name = None
    
    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    if intent_name == 'ownername':
        return authorize_response(intent)
    
    # user must have given name to pass this point
    if user_name == None:
        return get_authorization_response()
    
    # user wants to know about their accounts.
    if intent_name == "accountlist":
        return get_accountlist_response(user_name, session)
    if intent_name == 'accountbynumber':
        return get_accountbynumber_response(user_name, session, intent)
    if intent_name == 'recenttransactions':
        return get_recenttransactions_response(user_name, session, intent)
    if intent_name == 'sendmoney':
        return get_sendmoney_response(user_name, session, intent)
    if intent_name == 'myname':
        return get_myname_response(user_name, session, intent)
    if intent_name == 'createaccount':
        return get_createaccount_response(user_name, session, intent)
    if intent_name == 'makedeposit':
        return get_makedeposit_response(user_name, session, intent)
    
    if intent_name == 'thankyou':
        return get_thankyou_response(user_name)
    if intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
        
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.ask.skill.a98f4df5-7ab4-41d0-9f87-549851109ff5"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])