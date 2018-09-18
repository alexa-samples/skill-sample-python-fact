# Build an Alexa Fact Skill in ASK Python SDK
<img src="https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/quiz-game/header._TTH_.png" />


[![Voice User Interface](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/navigation/1-locked._TTH_.png)](./1-voice-user-interface.md)[![Lambda Function](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/navigation/2-locked._TTH_.png)](./2-lambda-function.md)[![Connect VUI to Code](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/navigation/3-locked._TTH_.png)](./3-connect-vui-to-code.md)[![Testing](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/navigation/4-locked._TTH_.png)](./4-testing.md)[![Customization](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/navigation/5-on._TTH_.png)](./5-customization.md)[![Publication](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/navigation/6-off._TTH_.png)](./6-publication.md)


## Customize the Skill to be Yours

At this point, you should have a working copy of our Fact skill.  In order to make it your own, you will need to customize it with data and responses that you create. The data and responses can be found in the [lambda_function.py](../lambda/py/lambda_function.py) file. Here are the things you will need to change:

1.  **New data.** You will need to provide a set of facts for your topic.  We recommend a minimum of 25, but a total closer to 100 offers a better experience.

    1.  **Open a copy of lambda_function.py.** If you haven't already downloaded the code for this project, [you can find a copy of lambda_function.py here](../lambda/py/lambda_function.py).  You can use a simple, lightweight code editor like [Atom](http://atom.io), [Sublime Text](http://sublimetext.com), or [VSCode](http://code.visualstudio.com).

    2.  **Search for the comment "TODO: Replace this data with your own."**  This is the data for our skill.  You can see that it is a simple list of facts.

2.  **New sentences to respond to your users.** There are several sentences and responses that you will want to customize for your skill.

    1.  **Go back to your copy of [lambda_function.py](../lambda/py/lambda_function.py).**

    2.  **Look for the comment "TODO: The items below this comment need your attention."** This is the beginning of the section where you need to customize several text strings for your skill.

    3.  **Continue through lambda_function.py until you reach the bottom of the section.**  This will ensure that you cover each of the values that you need to update.

3.  **New language.** If you are creating this skill for another language other than English, you will need to make sure Alexa's responses are also in that language.

    *  For example, if you are creating your skill in German, every single response that Alexa makes has to be in German.  You can't use English responses or your skill will fail certification.
    
5.  **When you have replaced the data in `lambda_function.py`, you need to upload the latest data into Lambda.**  Copy the updated contents into the ``skill_env`` folder, zip the contents of the ``skill_env`` folder and upload it to AWS Lambda as discussed in the "**Finish configuring your function**" step in [Lambda setup documentation](./2-lambda-function.md). Test your skill through the Alexa Simulator on the developer portal, with the updated changes.    

6.  **Once you have made the updates listed on this page, you can click "Launch" in the top navigation to move on to Publishing and Certification of your skill.**

    <!--![Dev Portal Next](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/general/3-7-next-button._TTH_.png) -->


[![Next](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/general/buttons/button_next_publication._TTH_.png)](6-publication.md)
    
   
