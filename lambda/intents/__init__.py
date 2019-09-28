# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
    
# --------------- Other helpers ----------------------
def pos_to_int(input_number:str):
    # turn positional data to integer. yes i know this is ugly
    if input_number in ['1st', 'first']:
        number = 0
    elif input_number in ['2nd', 'second']:
        number = 1
    elif input_number in ['3rd', 'third']:
        number = 2
    elif input_number in ['4th', 'fourth']:
        number = 3
    elif input_number in ['5th', 'fifth']:
        number = 4
    elif input_number in ['6th', 'sixth']:
        number = 5
    elif input_number in ['7th', 'seventh']:
        number = 6
    elif input_number in ['8th', 'eighth']:
        number = 7
    elif input_number in ['9th', 'ninth']:
        number = 8
    elif input_number in ['10th', 'tenth']:
        number = 9
    else:
        number = -1
        
    return number