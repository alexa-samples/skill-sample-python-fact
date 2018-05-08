# -*- coding: utf-8 -*-
""" simple fact sample app """

from __future__ import print_function

import random

Language_Support = {
    "en-US": {
        "translation": {
            "FACTS": [
                "A year on Mercury is just 88 days long.",
                ("Despite being farther from the Sun, Venus experiences higher "
                 "temperatures than Mercury."),
                ("Venus rotates counter-clockwise, possibly because of a collision"
                 " in the past with an asteroid."),
                "On Mars, the Sun appears about half the size as it does on Earth.",
                "Earth is the only planet not named after a god.",
                "Jupiter has the shortest day of all the planets.",
                ("The Milky Way galaxy will collide with the Andromeda Galaxy in about"
                 " 5 billion years."),
                "The Sun contains 99.86% of the mass in the Solar System.",
                "The Sun is an almost perfect sphere.",
                ("A total solar eclipse can happen once every 1 to 2 years."
                 " This makes them a rare event."),
                ("Saturn radiates two and a half times more energy into space"
                 " than it receives from the sun."),
                "The temperature inside the Sun can reach 15 million degrees Celsius.",
                "The Moon is moving approximately 3.8 cm away from our planet every year."
            ],
            "PLANETS": {
                "mercury":{
                    "PrintName": "Mercury",
                    "DistanceFromSun": 36, # millions of miles
                    "Weather": "high of 840 and low of minus 275 fahrenheit. Nothing but sun."
                },
                "venus":{
                    "PrintName": "Venus",
                    "DistanceFromSun": 67.2, # millions of miles
                    "Weather": "high and low of 870 fahrenheit. Expect thick cloud cover <break time=\"1s\"/> forever."
                },
                "earth":{
                    "PrintName": "Earth",
                    "DistanceFromSun": 93, # millions of miles
                    "Weather": "high of 136 and low of minus 129 fahrenheit. Anything can happen on this planet."
                },
                "mars":{
                    "PrintName": "Mars",
                    "DistanceFromSun": 141.6, # millions of miles
                    "Weather": "high of 70 and low of minus 195 fahrenheit. Sunny with a chance of sandstorms later in the day."
                },
                "jupiter":{
                    "PrintName": "Jupiter",
                    "DistanceFromSun": 483.6, # millions of miles
                    "Weather": "high of minus 148 and low of minus 234 fahrenheit. Storms are highly likely, bringing heavy rain and high winds."
                },
                "saturn":{
                    "PrintName": "Saturn",
                    "DistanceFromSun": 886.7, # millions of miles
                    "Weather": "high of 134 and low of minus 288 fahrenheit. Cloudy with a chance of super storm."},
                "uranus":{
                    "PrintName": "Uranus",
                    "DistanceFromSun": 1784, # millions of miles
                    "Weather":"high and low of minus 357 fahrenheit. Cloudy with a chance of storms."
                },
                "neptune":{
                    "PrintName": "Neptune",
                    "DistanceFromSun": 2794.4, # millions of miles
                    "Weather":"high of minus 328 and low of minus 360 fahrenheit. Extreme wind and a change of storms."
                },
                "pluto":{
                    "PrintName": "Pluto",
                    "DistanceFromSun": 3674.5, # millions of miles
                    "Weather":"high of minus 387 and low of minus 396 fahrenheit. Snow is expected."
                }
            },
            "VEHICLES": {
                "car": {"speed": 65, "string":"in a car"},
                "jet": {"speed": 500, "string":"in a jetliner"},
                "concorde": {"speed": 1350, "string":"in a Concorde"},
                "rocket": {"speed": 11250, "string":"by rocket"},
                "light": {"speed": 670616629, "string":"at the speed of light"}
            },
            "JOKES": [ # jokes from http://www.funology.com/outer-space-jokes/
                "What is a spaceman’s favorite chocolate? <break time=\"1s\"/>A marsbar!",
                "What kind of music do planets sing? <break time=\"1s\"/>Neptunes!",
                "What do aliens on the metric system say? <break time=\"1s\"/>Take me to your liter.",
                "Why did the people not like the restaurant on the moon? <break time=\"1s\"/>Because there was no atmosphere.",
                "I’m reading a book about anti-gravity. <break time=\"1s\"/>It’s impossible to put down!",
                "How many ears does Captain Kirk have? <break time=\"1s\"/>Three. A left ear, a right ear, and a final frontier!",
                "What did Mars say to Saturn? <break time=\"1s\"/>Give me a ring sometime!"
            ],
            "SKILL_NAME":"Spacey",
            "GET_FACT_MESSAGE": "Here's an interesting one: ",
            "HELP_MESSAGE" : ("You can say tell me a space fact, ask me for the travel time between two planets,"
            " the weather on a planet, or ask me to tell a joke, or, you can say exit... What can I help you with?"),
            "HELP_REPROMPT" : "What can I help you with?",
            "STOP_MESSAGE" : "Goodbye!",
            "LAUNCH_MESSAGE": ("Welcome to Spacey. I know facts about space, how long it takes to travel between two planets, "
            "the weather when you get there, and I even know a joke. what would you like to know?"),
            "LAUNCH_MESSAGE_REPROMPT": "Try asking me to tell you something about space.",
            "ASK_MESSAGE": " what else would you like to know"
        }
    },
    "en-GB": {
        "translation": {
            "FACTS": [
                "A year on Mercury is just 88 days long.",
                ("Despite being farther from the Sun, Venus experiences higher"
                 " temperatures than Mercury."),
                ("Venus rotates anti-clockwise, possibly because of a collision"
                 " in the past with an asteroid."),
                "On Mars, the Sun appears about half the size as it does on Earth.",
                "Earth is the only planet not named after a god.",
                "Jupiter has the shortest day of all the planets.",
                ("The Milky Way galaxy will collide with the Andromeda Galaxy"
                 " in about 5 billion years."),
                "The Sun contains 99.86% of the mass in the Solar System.",
                "The Sun is an almost perfect sphere.",
                ("A total solar eclipse can happen once every 1 to 2 years."
                 " This makes them a rare event."),
                ("Saturn radiates two and a half times more energy into space than"
                 " it receives from the sun."),
                "The temperature inside the Sun can reach 15 million degrees Celsius.",
                "The Moon is moving approximately 3.8 cm away from our planet every year."
            ],
            "JOKES": [ # jokes from http://www.funology.com/outer-space-jokes/
                "What is a spaceman’s favorite chocolate? <break time=\"1s\"/>A marsbar!",
                "What kind of music do planets sing? <break time=\"1s\"/>Neptunes!",
                "What do aliens on the metric system say? <break time=\"1s\"/>Take me to your liter.",
                "Why did the people not like the restaurant on the moon? <break time=\"1s\"/>Because there was no atmosphere.",
                "I’m reading a book about anti-gravity. <break time=\"1s\"/>It’s impossible to put down!",
                "How many ears does Captain Kirk have? <break time=\"1s\"/>Three. A left ear, a right ear, and a final frontier!",
                "What did Mars say to Saturn? <break time=\"1s\"/>Give me a ring sometime!"
            ],
            "SKILL_NAME": "Spacey",
            "GET_FACT_MESSAGE": "Here's an interesting one: ",
            "HELP_MESSAGE" : ("You can say tell me a space fact, ask me for the travel time between two planets,"
            " the weather on a planet, or ask me to tell a joke, or, you can say exit... What can I help you with?"),
            "HELP_REPROMPT" : "What can I help you with?",
            "STOP_MESSAGE" : "Goodbye!",
            "LAUNCH_MESSAGE": ("Welcome to Spacey. I know facts about space, how long it takes to travel between two planets, "
            "the weather when you get there, and I even know a joke. what would you like to know?"),
            "LAUNCH_MESSAGE_REPROMPT": "Try asking me to tell you something about space.",
            "ASK_MESSAGE": " what else would you like to know"
        }
    }
}

# --------------- App entry point -----------------

def lambda_handler(event, context):
    """  App entry point  """

    #print(event)

    if event['session']['new']:
        on_session_started()

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended()

# --------------- Response handlers -----------------

def on_intent(request, session):
    """ called on receipt of an Intent  """

    intent_name = request['intent']['name']
    #print("on_intent " +intent_name)
    #print(request)

    locale = request['locale']
    if locale == "":
        locale = getlocale(session)

    if locale == "":
        locale = "en-US"

    if 'dialogState' in request:
        #delegate to Alexa until dialog sequence is complete
        if request['dialogState'] == "STARTED" or request['dialogState'] == "IN_PROGRESS":
            attributes = {"locale":locale}
            return dialog_response(attributes, False)

    # process the intents
    if intent_name == "GetNewFactIntent":
        return get_fact_response(locale)
    elif intent_name == "GetTravelTime":
        return get_travel_time_response(locale, request)
    elif intent_name == "GetWeather":
        return get_weather_response(locale, request)
    elif intent_name == "GetJoke":
        return get_joke_response(locale)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response(locale)
    elif intent_name == "AMAZON.StopIntent":
        return get_stop_response(locale)
    elif intent_name == "AMAZON.CancelIntent":
        return get_stop_response(locale)
    else:
        print("invalid Intent reply with help")
        return get_help_response(locale)

def get_fact_response(locale):
    """ get and return a random fact for the current locale """

    resdata = resource_handler(locale)
    factmessage = resdata["GET_FACT_MESSAGE"]
    cardcontent = random.choice(resdata["FACTS"])
    speech_message = factmessage + cardcontent + resdata["ASK_MESSAGE"]
    attributes = {"locale":locale}
    skillname = resdata["SKILL_NAME"]
    return response(attributes, speech_response_with_card(skillname, speech_message,
                                                          cardcontent, False))

def get_travel_time_response(locale, request):
    """ get and return a travel time between Planets for the current locale """

    resdata = resource_handler(locale)
    intent = request['intent']

    if 'slots' in intent:
        slots = intent['slots']
        for key, val in slots.items():
            if key == "DepartingPlanet":
                if val.get('value'):
                    planet_from = val['value'].lower()
                    if planet_from in resdata["PLANETS"]:
                        departing_planet = resdata['PLANETS'][planet_from]
                    else:
                        speech_output = ("There is no planet by name " + planet_from +
                                         ", would you please provide a valid planet name? "+
                                         "to try again say calculate travel time.")
                        return response("", speech_response_prompt(speech_output,
                                                                   speech_output, False))
            elif key == "ArrivingPlanet":
                if val.get('value'):
                    planet_to = val['value'].lower()
                    if planet_to in resdata["PLANETS"]:
                        arrival_planet = resdata['PLANETS'][planet_to]
                    else:
                        speech_output = ("There is no planet by name " + planet_to +
                                         ", would you please provide a valid planet name? "
                                         "to try again say calculate travel time.")
                        return response("", speech_response_prompt(speech_output,
                                                                   speech_output, False))

        vehicle = "rocket"
        distance = abs(departing_planet['DistanceFromSun'] - arrival_planet['DistanceFromSun'])
        speed_of_travel = resdata['VEHICLES'][vehicle]['speed']

        speech_output = "It would take about "

        travel_time_hours = (distance*1000000)/speed_of_travel
        if travel_time_hours < 24:
            travel_time_minutes = str(round(travel_time_hours * 60))
            speech_output += travel_time_minutes+" minutes"
        elif travel_time_hours > 8760:
            travel_time_years = str(round((travel_time_hours / 8760), 1))
            speech_output += travel_time_years+" years"
        elif travel_time_hours > 730:
            travel_time_months = str(round((travel_time_hours / 730), 1))
            speech_output += travel_time_months+" months"
        elif travel_time_hours > 24:
            travel_time_days = str(round((travel_time_hours / 24), 1))
            speech_output += travel_time_days+" days"
        else:
            speech_output += travel_time_hours+" hours"

        speech_output += (" to travel from " + departing_planet['PrintName']+ " to " +
                          arrival_planet['PrintName'] + " " +
                          resdata['VEHICLES'][vehicle]['string'] + "." +
                          resdata['ASK_MESSAGE'])

        return  response("", speech_response_with_card(resdata["SKILL_NAME"], speech_output,
                                                       speech_output, False))

def get_weather_response(locale, request):
    """ get and return a weather of Planets for the current locale """

    resdata = resource_handler(locale)
    intent = request['intent']

    if 'slots' in intent:
        slots = intent['slots']
        for key, val in slots.items():
            if val.get('value'):
                planet_name = val['value'].lower()
                if planet_name in resdata["PLANETS"]:
                    info = resdata['PLANETS'][planet_name]
                    speech_output = ("The forecast for "+info['PrintName']+" is "+info['Weather']
                                     + resdata["ASK_MESSAGE"])
                    reprompt_text = resdata["ASK_MESSAGE"]
                    return response("", response_ssml_text_and_prompt(speech_output,
                                                                      False, reprompt_text))
                else:
                    speech_output = ("There is no planet by name " + planet_name +
                                     ", would you please provide a valid planet name? "
                                     "to try again say tell me weather.")
                    return response("", speech_response_prompt(speech_output,
                                                               speech_output, False))
    return get_help_response(locale)


def get_joke_response(locale):
    """ get and return a random joke for the current locale """

    resdata = resource_handler(locale)
    cardcontent = random.choice(resdata["JOKES"])
    speech_message = cardcontent + " <break time=\"1s\"/>" + resdata["ASK_MESSAGE"]
    attributes = {"locale":locale}
    return response(attributes, response_ssml_text_and_prompt
                    (speech_message, False, speech_message))

def get_help_response(locale):
    """ get and return the help string for the current locale  """

    resdata = resource_handler(locale)
    speech_message = resdata["HELP_MESSAGE"]
    attributes = {"locale":locale}
    return response(attributes, speech_response_prompt(speech_message,
                                                       speech_message, False))
def get_launch_response(locale):
    """ get and return the help string for the current locale  """

    resdata = resource_handler(locale)
    speech_message = resdata["LAUNCH_MESSAGE"]
    prompt_message = resdata["LAUNCH_MESSAGE_REPROMPT"]
    attributes = {"locale":locale}
    return response(attributes, response_ssml_text_and_prompt(speech_message,
                                                              False, prompt_message))

def get_stop_response(locale):
    """ end the session, user wants to quit the game """

    resdata = resource_handler(locale)
    attributes = {"locale":locale}
    speech_output = resdata["STOP_MESSAGE"]
    return response(attributes, speech_response(speech_output, True))

def on_session_started():
    """" called when the session starts  """
    #print("on_session_started")

def on_session_ended():
    """ called on session ends """
    #print("on_session_ended")

def on_launch(request):
    """ called on Launch, we reply with a launch message  """

    return get_launch_response(request['locale'])

def resource_handler(locale):
    """  Get resourse data for specified locale """

    return Language_Support[locale]["translation"]

def getlocale(session):
    """ get the locale string from attribute array """

    attributes = session['attributes']
    return  attributes['locale']


# --------------- Speech response handlers -----------------

def speech_response(output, endsession):
    """  create a simple json response  """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'shouldEndSession': endsession
    }

def dialog_response(attributes, endsession):
    """  create a simple json response with card """

    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response':{
            'directives': [
                {
                    'type': 'Dialog.Delegate'
                }
            ],
            'shouldEndSession': endsession
        }
    }

def speech_response_with_card(title, output, cardcontent, endsession):
    """  create a simple json response with card """

    return {
        'card': {
            'type': 'Simple',
            'title': title,
            'content': cardcontent
        },
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'shouldEndSession': endsession
    }

def response_ssml_text_and_prompt(output, endsession, reprompt_text):
    """ create a Ssml response with prompt  """

    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" +reprompt_text +"</speak>"
            }
        },
        'shouldEndSession': endsession
    }

def speech_response_prompt(output, reprompt_text, endsession):
    """ create a simple json response with a prompt """

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': endsession
    }

def response(attributes, speech_message):
    """ create a simple json response  """

    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speech_message
    }
   
