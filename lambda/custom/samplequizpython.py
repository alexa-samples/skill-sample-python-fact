# -*- coding: utf-8 -*-
""" USA State fact and quiz.. """
from __future__ import print_function
import math
import string
import random


MAX_QUESTION = 10

#This is the welcome message for when a user starts the skill without a specific intent.
WELCOME_MESSAGE = ("Welcome to the United States Quiz Game!  You can ask me about any of the"
                   " fifty states and their capitals, or you can ask me to start a quiz."
                   "  What would you like to do?")
#This is the message a user will hear when they start a quiz.
SKILLTITLE = "States of the USA"


#This is the message a user will hear when they start a quiz.
START_QUIZ_MESSAGE = "OK.  I will ask you 10 questions about the United States."

#This is the message a user will hear when they try to cancel or stop the skill"
#or when they finish a quiz.
EXIT_SKILL_MESSAGE = "Thank you for playing the United States Quiz Game!  Let's play again soon!"

#This is the message a user will hear after they ask (and hear) about a specific data element.
REPROMPT_SPEECH = "Which other state or capital would you like to know about?"

#This is the message a user will hear when they ask Alexa for help in your skill.
HELP_MESSAGE = ("I know lots of things about the United States.  You can ask me about a state "
                "or a capital, and I'll tell you what I know.  "
                "You can also test your knowledge by asking me to start a quiz.  "
                "What would you like to do?")

#If you don't want to use cards in your skill, set the USE_CARDS_FLAG to false.
#If you set it to true, you will need an image for each item in your data.
USE_CARDS_FLAG = True

STATE_START = "Start"
STATE_QUIZ = "Quiz"

STATE = STATE_START
COUNTER = 0
QUIZSCORE = 0


SAYAS_INTERJECT = "<say-as interpret-as='interjection'>"
SAYAS_SPELLOUT = "<say-as interpret-as='spell-out'>"
SAYAS = "</say-as>"
BREAKSTRONG = "<break strength='strong'/>"

 # --------------- speech cons -----------------

 # This is a list of positive/negative speechcons that this skill will use when a user
 # gets a correct answer. For a full list of supported speechcons, go here:
 # https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/speechcon-reference
SPEECH_CONS_CORRECT = (["Booya", "All righty", "Bam", "Bazinga", "Bingo", "Boom", "Bravo",
                        "Cha Ching", "Cheers", "Dynomite", "Hip hip hooray", "Hurrah",
                        "Hurray", "Huzzah", "Oh dear.  Just kidding.  Hurray", "Kaboom",
                        "Kaching", "Oh snap", "Phew", "Righto", "Way to go", "Well done",
                        "Whee", "Woo hoo", "Yay", "Wowza", "Yowsa"])

SPEECH_CONS_WRONG = (["Argh", "Aw man", "Blarg", "Blast", "Boo", "Bummer", "Darn", "D'oh",
                      "Dun dun dun", "Eek", "Honk", "Le sigh", "Mamma mia", "Oh boy",
                      "Oh dear", "Oof", "Ouch", "Ruh roh", "Shucks", "Uh oh", "Wah wah",
                      "Whoops a daisy", "Yikes"])

# --------------- a class to contain states and their details -----------------
class Item:
    """ Item class """
    def __init__(self, state, abbreviation, capital, statehoodyear, statehoodorder):
        self.statename = state
        self.abbreviation = abbreviation
        self.capital = capital
        self.statehoodyear = statehoodyear
        self.statehoodorder = statehoodorder

    @staticmethod
    def get_random_property():
        """ get property name  """
        val = ["Abbreviation", "Capital", "Statehood Year",
               "Statehood Order"]
        return  random.choice(val)

    @staticmethod
    def properties():
        """ get property name  """
        val = ["Abbreviation", "Capital", "Statehood Year",
               "Statehood Order", "State Name"]
        return val

    @staticmethod
    def properties_to_upper(prop):
        """ get property value  """
        if prop == "abbreviation":
            return "Abbreviation"
        elif prop == "capital":
            return "Capital"
        elif prop == "statehoodyear" or prop == "statehood year":
            return "Statehood Year"
        elif prop == "statehoodorder" or prop == "statehood order":
            return "Statehood Order"
        elif prop == "statename" or prop == "state name":
            return "State"
        return ""

    def property_value(self, prop):
        """ get property value  """
        if prop == "abbreviation":
            return self.abbreviation
        elif prop == "capital":
            return self.capital
        elif prop == "statehoodyear" or prop == "statehood year":
            return self.statehoodyear
        elif prop == "statehoodorder" or prop == "statehood order":
            return self.statehoodorder
        elif prop == "statename" or prop == "state name":
            return self.statename
        return ""

    def get_text_description(self):
        """ get text details for card display """

        text = "State Name: " + self.statename + "\n"
        text += "State Captial: " +self.capital + "\n"
        text += "Statehood Year: " +self.statehoodyear + "\n"
        text += "Statehood Order: " +self.statehoodorder + "\n"
        text += "Abbreviation: " +self.abbreviation + "\n"
        return text

# --------------- our list of states -----------------
ITEMS = []
ITEMS.append(Item("Alabama", "AL", "Montgomery", "1819", "22"))
ITEMS.append(Item("Alaska", "AK", "Juneau", "1959", "49"))
ITEMS.append(Item("Arizona", "AZ", "Phoenix", "1912", "48"))
ITEMS.append(Item("Arkansas", "AR", "Little Rock", "1836", "25"))
ITEMS.append(Item("California", "CA", "Sacramento", "1850", "31"))
ITEMS.append(Item("Colorado", "CO", "Denver", "1876", "38"))
ITEMS.append(Item("Connecticut", "CT", "Hartford", "1788", "5"))
ITEMS.append(Item("Delaware", "DE", "Dover", "1787", "1"))
ITEMS.append(Item("Florida", "FL", "Tallahassee", "1845", "27"))
ITEMS.append(Item("Georgia", "GA", "Atlanta", "1788", "4"))
ITEMS.append(Item("Hawaii", "HI", "Honolulu", "1959", "50"))
ITEMS.append(Item("Idaho", "ID", "Boise", "1890", "43"))
ITEMS.append(Item("Illinois", "IL", "Springfield", "1818", "21"))
ITEMS.append(Item("Indiana", "IN", "Indianapolis", "1816", "19"))
ITEMS.append(Item("Iowa", "IA", "Des Moines", "1846", "29"))
ITEMS.append(Item("Kansas", "KS", "Topeka", "1861", "34"))
ITEMS.append(Item("Kentucky", "KY", "Frankfort", "1792", "15"))
ITEMS.append(Item("Louisiana", "LA", "Baton Rouge", "1812", "18"))
ITEMS.append(Item("Maine", "ME", "Augusta", "1820", "23"))
ITEMS.append(Item("Maryland", "MD", "Annapolis", "1788", "7"))
ITEMS.append(Item("Massachusetts", "MA", "Boston", "1788", "6"))
ITEMS.append(Item("Michigan", "MI", "Lansing", "1837", "26"))
ITEMS.append(Item("Minnesota", "MN", "St. Paul", "1858", "32"))
ITEMS.append(Item("Mississippi", "MS", "Jackson", "1817", "20"))
ITEMS.append(Item("Missouri", "MO", "Jefferson City", "1821", "24"))
ITEMS.append(Item("Montana", "MT", "Helena", "1889", "41"))
ITEMS.append(Item("Nebraska", "NE", "Lincoln", "1867", "37"))
ITEMS.append(Item("Nevada", "NV", "Carson City", "1864", "36"))
ITEMS.append(Item("Hampshire", "NH", "Concord", "1788", "9"))
ITEMS.append(Item("Jersey", "NJ", "Trenton", "1787", "3"))
ITEMS.append(Item("Mexico", "NM", "Santa Fe", "1912", "47"))
ITEMS.append(Item("New York", "NY", "Albany", "1788", "11"))
ITEMS.append(Item("North Carolina", "NC", "Raleigh", "1789", "12"))
ITEMS.append(Item("North Dakota", "ND", "Bismarck", "1889", "39"))
ITEMS.append(Item("Ohio", "OH", "Columbus", "1803", "17"))
ITEMS.append(Item("Oklahoma", "OK", "Oklahoma City", "1907", "46"))
ITEMS.append(Item("Oregon", "OR", "Salem", "1859", "33"))
ITEMS.append(Item("Pennsylvania", "PA", "Harrisburg", "1787", "2"))
ITEMS.append(Item("Rhode Island", "RI", "Providence", "1790", "13"))
ITEMS.append(Item("South Carolina", "SC", "Columbia", "1788", "8"))
ITEMS.append(Item("South Dakota", "SD", "Pierre", "1889", "40"))
ITEMS.append(Item("Tennessee", "TN", "Nashville", "1796", "16"))
ITEMS.append(Item("Texas", "TX", "Austin", "1845", "28"))
ITEMS.append(Item("Utah", "UT", "Salt Lake City", "1896", "45"))
ITEMS.append(Item("Vermont", "VT", "Montpelier", "1791", "14"))
ITEMS.append(Item("Virginia", "VA", "Richmond", "1788", "10"))
ITEMS.append(Item("Washington", "WA", "Olympia", "1889", "42"))
ITEMS.append(Item("West Virginia", "WV", "Charleston", "1863", "35"))
ITEMS.append(Item("Wisconsin", "WI", "Madison", "1848", "30"))
ITEMS.append(Item("Wyoming", "WY", "Cheyenne", "1890", "44"))


# --------------- entry point -----------------

def lambda_handler(event, context):
    """ App entry point  """
    
    if event['request']['type'] == "LaunchRequest":
        return on_launch()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'])


# --------------- response handlers -----------------

def on_intent(request, session):
    """ Called on receipt of an Intent  """

    intent = request['intent']
    intent_name = request['intent']['name']

    #print("on_intent " +intent_name)
    get_state(session)

    if 'dialogState' in request:
        #delegate to Alexa until dialog sequence is complete
        if request['dialogState'] == "STARTED" or request['dialogState'] == "IN_PROGRESS":
            return dialog_response("", False)

    # process the intents
    if intent_name == "QuizIntent":
        return do_quiz(request)
    elif intent_name == "AnswerIntent":
        return answer(request, intent, session)
    elif intent_name == "Quiz":
        return do_quiz(request)
    elif intent_name == "AskQuestion":
        return ask_question(request, "")
    elif intent_name == "AMAZON.HelpIntent":
        return do_help()
    elif intent_name == "AMAZON.StopIntent":
        return do_stop()
    elif intent_name == "AMAZON.CancelIntent":
        return do_stop()
    elif intent_name == "AMAZON.StartoverIntent":
        return do_quiz(request)
    else:
        print("invalid intent reply with help")
        return do_help()

def answer(request, intent, session):
    """ answer a fact or quiz question """

    global STATE

    if STATE == STATE_QUIZ:
        return answer_quiz(request, intent, session)

    return answer_facts(intent)

def answer_quiz(request, intent, session):
    """ answer a quiz question  """

    global QUIZSCORE
    global COUNTER
    global STATE
    speech_message = ""
    quizprop = ""

    if session['attributes'] and 'quizitem' in session['attributes']:
        item = session['attributes']['quizitem']
    else:
        return get_welcome_message()

    if session['attributes'] and 'quizproperty' in session['attributes']:
        quizprop = session['attributes']['quizproperty']
        quizprop = quizprop.replace(" ", "").lower()

    if session['attributes'] and session['attributes']['quizscore'] != None:
        QUIZSCORE = session['attributes']['quizscore']

    if compare_slots(intent['slots'], item[quizprop]):
        QUIZSCORE += 1
        speech_message = get_speechcon(True)
    else:
        speech_message = get_speechcon(False)

    speech_message += get_answer(quizprop, item)

    if COUNTER < MAX_QUESTION:
        speech_message += get_currentscore(QUIZSCORE, COUNTER)
        return ask_question(request, speech_message)

    speech_message += get_finalscore(QUIZSCORE, COUNTER)
    speech_message += EXIT_SKILL_MESSAGE
    STATE = STATE_START
    COUNTER = 0
    QUIZSCORE = 0

    attributes = {"quizscore":globals()['QUIZSCORE'],
                  "quizproperty":quizprop,
                  "response": speech_message,
                  "state":globals()['STATE'],
                  "counter":globals()['COUNTER'],
                  "quizitem":item
                 }
    return response(attributes, response_ssml_text(speech_message, False))


def answer_facts(intent):
    """  return a fact  """

    attributes = {"state":globals()['STATE']}

    item, propname = get_item(intent.get('slots'))
    if item is None:
        speech_message = get_badanswer(propname)
        attributes.update({"response": speech_message})
        return response(attributes, response_plain_text(speech_message, False))

    speech = get_speech_description(item)
    if USE_CARDS_FLAG:
        abbrev = item.abbreviation
        cardtext = item.get_text_description()
        return response(attributes,
                        response_ssml_cardimage_prompt(propname, speech, False,
                                                       cardtext, abbrev, REPROMPT_SPEECH))
    else:
        return response(attributes,
                        response_ssml_text_reprompt
                        (speech_message, False, REPROMPT_SPEECH))


def ask_question(request, speech_message):
    """ ask a question """

    if globals()['COUNTER'] <= 0:
        globals()['COUNTER'] = 0
        speech_message = START_QUIZ_MESSAGE + " "

    globals()['COUNTER'] += 1

    item_cls = random.choice(ITEMS)
    quizprop = item_cls.get_random_property()
    reprompt = get_question(quizprop, item_cls)
    speech_message += reprompt

    attributes = {"quizscore":globals()['QUIZSCORE'],
                  "quizproperty":quizprop,
                  "response":speech_message,
                  "state": globals()['STATE'],
                  "counter":globals()['COUNTER'],
                  "quizitem":item_cls.__dict__
                 }
    return response(attributes, response_ssml_text_and_prompt(speech_message, False, reprompt))

def do_quiz(request):
    """ clear settings and start quiz """
    global QUIZSCORE
    global COUNTER
    global STATE

    COUNTER = 0
    QUIZSCORE = 0
    STATE = STATE_QUIZ
    return ask_question(request, "")

def do_stop():
    """  stop the app """

    attributes = {"state":globals()['STATE']}
    return response(attributes, response_plain_text(EXIT_SKILL_MESSAGE, True))

def do_help():
    """ return a help response  """

    global STATE
    STATE = STATE_START
    attributes = {"state":globals()['STATE']}
    return response(attributes, response_plain_text(HELP_MESSAGE, False))

def on_launch():
    """ called on Launch reply with a welcome message """
 
    return get_welcome_message()

def on_session_ended(request):
    """ called on session end  """

    if request['reason']:
        end_reason = request['reason']
        print("on_session_ended reason: " + end_reason)
    else:
        print("on_session_ended")

def get_item(slots):
    """ return the item matching the users request, if found, or original text if not """

    properties = Item.properties()
    propertyvaluetext = ""

    for key, val in slots.items():
        if val.get('value'):
            propertyvaluetext = val['value']
            textlower = propertyvaluetext.lower()
            for prop in properties:
                proplower = prop.lower().replace(" ", "")
                for i in ITEMS:
                    if i.property_value(proplower).lower() == textlower:
                        return i, propertyvaluetext

    return (None, propertyvaluetext)

def get_state(session):
    """ get and set the current state  """

    global STATE

    if 'state' in session['attributes']:
        STATE = session['attributes']['state']
    else:
        STATE = STATE_START

def compare_slots(slots, quizproperty):
    """ compare slots to find if users answer matches """

    proplower = quizproperty.lower()
    for key, val in slots.items():
        if val.get('value'):
            lval = val['value'].lower()
            if lval == proplower:
                return True
    return False

# --------------- response string formatters -----------------
def get_welcome_message():
    """ return a welcome message """

    attributes = {"state":globals()['STATE']}
    return response(attributes, response_plain_text(WELCOME_MESSAGE, False))

def get_question(prop, item):
    """  return formatted question  """

    global COUNTER
    return ("Here is your " +str(COUNTER) + "th question. "
            "What is the " + prop + " of " + item.statename +"?")

def get_answer(prop, item):
    """  return formatted question SSML add so that Alexa spells the abbreviation out  """

    proplower = prop.replace(" ", "").lower()
    if prop == "abbreviation":
        return ("The Abbreviation of " +item['statename']
                +" is "+SAYAS_SPELLOUT +item["abbreviation"] +SAYAS +". ")

    propupper = Item.properties_to_upper(prop)
    return "The " +propupper +" of " +item['statename'] +" is " +item[proplower] +". "

def get_speech_description(item):
    """ get response to the question based on correct or incorect response"""

    stateorder = item.statehoodorder
    stateyear = item.statehoodyear
    sstate = item.statename
    sformat = BREAKSTRONG +SAYAS_SPELLOUT +item.abbreviation +SAYAS

    return (
        sstate +' is the ' +stateorder +'th state,'
        ' admitted to the Union in '+stateyear +'.'
        ' The capital of ' +sstate +' is '+item.capital +','
        ' and the abbreviation for ' +sstate +' is ' +sformat +'.'
        ' '  +sstate +' has been added to your Alexa app. '
        ' Which other state or capital would you like to know about?'
    )

def get_speechcon(correct):
    """ get response to the question based on correct or incorect response"""

    if correct:
        return SAYAS_INTERJECT + random.choice(SPEECH_CONS_CORRECT) +"! " +SAYAS +BREAKSTRONG

    return SAYAS_INTERJECT + random.choice(SPEECH_CONS_WRONG) +" " +SAYAS +BREAKSTRONG

def get_currentscore(score, counter):
    """sent after each question, reminds user of current score. """

    return "Your current score is " +str(score) + " out of " + str(counter) +". "

def get_finalscore(score, counter):
    """ sent when quiz completed and give final score """
 
    return "Your final score is " +str(score) +" out of " +str(counter) + ". "

def get_badanswer(outtext):
    """ bad answer response """

    if outtext == "":
        outtext = "This"
    return ("I'm sorry. " +outtext +" is not something I know very "
            "much about in this skill. " +HELP_MESSAGE)

def get_smallimage(name):
    """ return image url """

    return ("https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit"
            "/tutorials/quiz-game/state_flag/720x400/" +name +"._TTH_.png")


def get_largeimage(name):
    """get large version of the card image.  It should be 1200x800 pixels in dimension."""

    return ("https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit"
            "/tutorials/quiz-game/state_flag/1200x800/" +name +"._TTH_.png")

# --------------- speech response handlers -----------------
#  for details of Json format see:
#  https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference

def response_plain_text(output, endsession):
    """ create a simple json plain text response  """

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'shouldEndSession': endsession
    }


def response_ssml_text(output, endsession):
    """ create a simple json plain text response  """

    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
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


def response_ssml_cardimage_prompt(title, output, endsession, cardtext, abbreviation, reprompt):
    """ create a simple json plain text response  """

    smallimage = get_smallimage(abbreviation)
    largeimage = get_largeimage(abbreviation)
    return {
        'card': {
            'type': 'Standard',
            'title': title,
            'text': cardtext,
            'image':{
                'smallimageurl':smallimage,
                'largeimageurl':largeimage
            },
        },
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" +reprompt +"</speak>"
            }
        },
        'shouldEndSession': endsession
    }

def response_ssml_text_reprompt(output, endsession, reprompt_text):
    """  create a simple json response with a card  """

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

def response(attributes, speech_response):
    """ create a simple json response """

    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speech_response
    }
